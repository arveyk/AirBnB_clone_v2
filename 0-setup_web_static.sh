#!/usr/bin/env bash
# Script for preping web server
mkdir -p /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html
echo "<html>\n<head></head>\n<body>\
	</body></html>" >> /data/web_static/releases/test/index.html

ln -s  /data/web_static/releases/test/index.html  /data/web_static/releases/test/
chown -hR ubuntu:ubuntu /data/
