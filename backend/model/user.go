package model

import (
	"strings"
)

const userIDSFieldSeparator = "-"

// User is an user of IsardVDI
type User struct {
	UID      string
	Username string
	Provider string

	Category string
	Role     string `json:"role"`
	Group    string `json:"group"`

	Desktops []Desktop
	Templates []Template

	Name  string `json:"name"`
	Email string `json:"email"`
	Photo string `json:"photo"`
}

func (u *User) ID() string {
	return strings.Join([]string{u.Provider, u.Category, u.UID, u.Username}, userIDSFieldSeparator)
}

func (u *User) LoadFromID(id string) {
	parts := strings.Split(id, userIDSFieldSeparator)

	u.Provider = parts[0]
	u.Category = parts[1]
	u.UID = parts[2]
	u.Username = strings.Join(parts[3:], userIDSFieldSeparator)
}
