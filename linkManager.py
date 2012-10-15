#!/usr/bin/env python2.7

from pymongo import Connection
import datetime
from bottle import route, run, request, post

@route('/')
def index():
    return '''
    <h1>Link Manager</h1>
    <form method="POST" action="/add">
        <b>Titulo del link: </b><br /><input name="title" type="text" /><br />
        <b>Url: </b><br /><input name="url" type="text" /><br />
        <b>Descripcion: </b><br />
        <textarea name="description"></textarea><br />
        <input value="agregar Link" type="submit" />
      </form>'''

@post('/add')
def add():
    conn = Connection('localhost', 27017)
    db = conn.linkManager
    dataLink = {
        "title": request.forms.get('title'),
        "url": request.forms.get('url'),
        "description": request.forms.get('description'),
        "date": datetime.datetime.utcnow()
    }
    db.links.insert(dataLink)
    return '''<b>Link Agregado</b>'''
    print dataLink

run(host='localhost', port=8080)
