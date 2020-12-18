package api

import (
	"net/http"
	"encoding/json"
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
