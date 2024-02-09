#!/usr/bin/env bash
# Script for preping web server
mkdir -p /data/web_static/releases/test/;
mkdir -p /data/web_static/shared;
touch /data/web_static/releases/test/index.html;

{
	echo "<html>" 
	"<head></head>"
	"<body>" 
	"</body></html>" 
} >> /data/web_static/releases/test/index.html;

ln -s  --force /data/web_static/releases/test/index.html  /data/web_static/releases/test/;

{
	echo
	"server {"
		"listen 80;"
		"location /static/ {"
			"alias /data/web_static/hbnb_static;"
		"}"
 	"}"
} >> config.txt;
< config.txt sudo tee nginx_file;
chown -hR ubuntu:ubuntu /data/;
sudo service nginx restart;
