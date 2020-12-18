package api

import (
	"net/http"
)

const (
	startDesktopKey = "desktop"
)

func (a *API) start(w http.ResponseWriter, r *http.Request) {
	u := getUsr(r.Context())
	dsk := r.FormValue(startDesktopKey)

	c, err := getCookie(r)
	if err != nil {
		c = &cookie{}
	}

	id, err := a.env.Isard.DesktopStart(u, dsk, false)
	if err != nil {
		handleErr(err, w, r)
		return
	}

	c.DesktopID = id
	if err := c.update(u, w); err != nil {
		handleErr(err, w, r)
		return
	}

	w.WriteHeader(http.StatusOK)
}