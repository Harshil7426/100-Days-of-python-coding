from flask import Flask, redirect, session, request
from replit import db
import os

app = Flask(__name__, static_url_path="/static")
app.secret_key = os.environ['secretKey']

adminUserId = "123456" #Change this to your ID

def getBlogs():
  entry = ""
  f = open("entry.html", "r")
  entry = f.read()
  f.close()
  keys = db.keys()
  keys = list(keys)
  content = ""
  for key in reversed(keys):
    thisEntry = entry
    if key != "user":
      thisEntry = thisEntry.replace("{title}", db[key]["title"])
      thisEntry = thisEntry.replace("{date}", db[key]["date"])
      thisEntry = thisEntry.replace("{body}", db[key]["body"])
      content += thisEntry
  return content
      

@app.route('/')
def index():
  userid = request.headers['X-Replit-User-Id']
  print(userid)
  if userid == adminUserId:
    return redirect("/edit")
  elif userid:
    return redirect("/naughty")
  page = ""
  f = open("blog.html", "r")
  page = f.read()
  f.close()
  page = page.replace("{content}", getBlogs())
  return page

@app.route("/edit")
def edit():
  userid = request.headers['X-Replit-User-Id']
  if userid != adminUserId:
    return redirect("/")
  page = ""
  f = open("edit.html", "r")
  page = f.read()
  page = page.replace("{content}", getBlogs())
  f.close()
  return page

@app.route("/add", methods=["POST"])
def add():
  userid = request.headers['X-Replit-User-Id']
  if userid != adminUserId:
    return redirect("/")
  form = request.form
  entry = {"title": form["title"], "date" : form["date"], "body": form["body"]}
  db[form["date"]] = entry
  return redirect("/edit")

@app.route("/naughty")
def naughty():
  return "You're not alllowed! 🤪"

app.run(host='0.0.0.0', port=81)
