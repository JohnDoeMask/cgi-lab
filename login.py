#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()
import os

from templates import login_page, secret_page, after_login_incorrect
import secret
from http.cookies import SimpleCookie

print("Content-Type: text/html")

# login.py
# Q4
# print(login_page())

s = cgi.FieldStorage()
username = s.getfirst("username")
password = s.getfirst("password")


# Q5
form_ok = username == secret.username and password == secret.password
c = SimpleCookie(os.environ["HTTP_COOKIE"])
c_username = None
c_password = None
if c.get("username"):
    c_username = c.get("username").value
if c.get("password"):
    c_password = c.get("password").value

cookie_ok = c_username == secret.username and c_password == secret.password

if cookie_ok:
    username = c_username
    password = c_password

if form_ok:
    print("Set-Cookie: username= ", username)
    print("Set-Cookie: password= ", password)

# Q6
if not username and not password:
    print(login_page())
elif username == secret.username and password == secret.password:
    print(secret_page(username, password))
else:
    print(after_login_incorrect())

print()


# hello.py
# print("Content-Type: text/html\n")
# print()
# print("<!doctype html><title>Hello</title><h2>Hello World</h2>")
#
# # Q1
# # print(os.environ)
#
# # Q2
# # print(os.environ["QUERY_STRING"])
#
# # Q3
# print(os.environ["HTTP_USER_AGENT"])
