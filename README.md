# bottlepro
本项目是一个基于bottle web框架开发的应用软件，支持文件上传、下载
##下载文件
>curl -o test.png http://192.168.4.122:8088/download/test.png
##上传文件
>curl http://192.168.4.122:8088/upload -F "filedata=@./test.png"
