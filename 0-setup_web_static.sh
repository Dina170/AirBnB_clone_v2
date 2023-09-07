#!/usr/bin/env bash
# Configure Nginx server so that /redirect_me is redirecting to another page.
apt-get -y update
apt-get -y install nginx

mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared

echo "Hello World!" > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu:ubuntu /data/

echo "server {
    listen 80;
    listen [::]:80 default_server;
    root   /var/www/html;
    index  index.html;

    location /hbnb_static/ {
    	alias /data/web_static/current/;
    }
    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
    error_page 404 /404.html;
    location = /404.html {
        root /var/www/html;
        internal;
    }
}" > /etc/nginx/sites-available/default
service nginx restart