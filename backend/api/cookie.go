package api

import (
	"encoding/base64"
	"encoding/json"
	"fmt"
	"net/http"
	"time"

	"github.com/isard-vdi/isard/backend/model"
)

type cookie struct {
	Name         string            `json:"name"`
	DesktopID    string            `json:"desktop_id"`
}

const cookieName = "isard"

func (c *cookie) save(w http.ResponseWriter) error {
	b, err := json.Marshal(c)
	if err != nil {
		return fmt.Errorf("save cookie: encode json: %v", err)
	}

	http.SetCookie(w, &http.Cookie{
		Name:     cookieName,
		Value:    base64.StdEncoding.EncodeToString(b),
		SameSite: http.SameSiteStrictMode,
		Path:     "/",
		Expires:  time.Now().AddDate(0, 0, 1),
	})

	return nil
}

func (c *cookie) update(u *model.User, w http.ResponseWriter) error {
	c.Name = u.Name

	if err := c.save(w); err != nil {
		return err
	}

	return nil
}

func getCookie(r *http.Request) (*cookie, error) {
	c, err := r.Cookie(cookieName)
	if err != nil {
		return &cookie{}, nil
	}

	val, err := base64.StdEncoding.DecodeString(c.Value)
	if err != nil {
		return nil, fmt.Errorf("get cookie: decode base64: %v", err)
	}

	var v cookie
	if err := json.Unmarshal(val, &v); err != nil {
		return nil, fmt.Errorf("get cookie: decode json: %v", err)
	}

	return &v, nil
}

func delCookie(w http.ResponseWriter, r *http.Request) {
	c, err := r.Cookie(cookieName)
	if err == nil {
		c.Value = ""
		c.Path = "/"
		c.MaxAge = -1
		c.Expires = time.Unix(1, 0)

		http.SetCookie(w, c)
	}
}
