package api

import (
	"encoding/json"
	"net/http"

	"github.com/gorilla/mux"
)

func (a *API) desktops(w http.ResponseWriter, r *http.Request) {
	u := getUsr(r.Context())
	/*
		json.Marshal returns null if desktops are an empty array
		See also:
		https://github.com/golang/go/issues/27589
		https://github.com/golang/go/issues/37711
	*/
	var err error
	b := []byte("[]")
	if u.Desktops != nil {
		b, err = json.Marshal(u.Desktops)
		if err != nil {
			http.Error(w, "cannot encode desktops", http.StatusBadRequest)
			return
		}
	}

	w.Header().Set("Content-Type", "application/json")
	w.Write(b)
}

func (a *API) desktopStart(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	d, ok := vars["desktop"]
	if !ok {
		http.Error(w, "unknown desktop", http.StatusBadRequest)
		return
	}

	if err := a.env.Isard.DesktopStart(d); err != nil {
		handleErr(err, w, r)
		return
	}

	c, err := getCookie(r)
	if err != nil {
		handleErr(err, w, r)
		return
	}

	c.DesktopID = d
	if err := c.save(w); err != nil {
		handleErr(err, w, r)
		return
	}

	u := getUsr(r.Context())
	a.env.Sugar.Infow("desktop start",
		"desktop", d,
		"usr", u.ID(),
	)

	w.WriteHeader(http.StatusOK)
}

func (a *API) desktopStop(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	d, ok := vars["desktop"]
	if !ok {
		http.Error(w, "unknown desktop", http.StatusBadRequest)
		return
	}

	if err := a.env.Isard.DesktopStop(d); err != nil {
		handleErr(err, w, r)
		return
	}

	c, err := getCookie(r)
	if err != nil {
		handleErr(err, w, r)
		return
	}

	c.DesktopID = d
	if err := c.save(w); err != nil {
		handleErr(err, w, r)
		return
	}

	u := getUsr(r.Context())
	a.env.Sugar.Infow("desktop stop",
		"desktop", d,
		"usr", u.ID(),
	)

	w.WriteHeader(http.StatusOK)
}
