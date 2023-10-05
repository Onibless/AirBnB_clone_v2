#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static
content="<!DOCTYPE html>
<html>
<head>
    <title>Nginx</title>
</head>
<body>
    Nginx is running
</body>
</html>"
sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get purge nginx -y
sudo apt-get autoremove -y
sudo apt-get install nginx -y
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/ && echo "$content" > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
# sed -i 's/old_string/new_string/g' filename
sed -i '51 i \\n\tlocation /hbnb_static {\n\talias /data/web_static/current;\n\t}' /etc/nginx/sites-available/default
sudo service nginx restart
