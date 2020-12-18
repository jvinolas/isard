package api

import (
	"net/http"
)

const (
	stopDesktopKey = "desktop"
)

func (a *API) stop(w http.ResponseWriter, r *http.Request) {
	u := getUsr(r.Context())
	dsk := r.FormValue(stopDesktopKey)

	c, err := getCookie(r)
	if err != nil {
		c = &cookie{}
	}

	err = a.env.Isard.DesktopStop(dsk)
	if err != nil {
		handleErr(err, w, r)
		return
	}

	c.DesktopID = dsk
	if err := c.update(u, w); err != nil {
		handleErr(err, w, r)
		return
	}

	w.WriteHeader(http.StatusOK)
}
