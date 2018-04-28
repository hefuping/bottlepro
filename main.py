#!/usr/bin/env python
#coding=utf-8

from bottle import route,run
from bottle import template,static_file,FileUpload,request

download_path='./download'
@route('/download/<filename:path>')
def download(filename):
    return static_file(filename, root=download_path, download=filename)

save_path='./upload'
@route('/upload',method='POST')
def upload():
    uploadfile = request.files.get('filedata')
    uploadfile.save(save_path,overwrite=True)

@route('/')
def index():
    return template('index')

run(host='0.0.0.0',port=8088,debug=True)
