#!/usr/bin/env bash
#deply web_static to servers

sudo apt -y update
sudo apt install -y nginx
# creates the folder if it doesn't exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# create a fake HTML file /data/web_static/releases/test/index.html
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

#create a symbolic link
sudo rm /data/web_static/current
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/

# update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
hbnb_static="        location /hbnb_static {
                alias /data/web_static/current/;
}"
sudo sed -i '54r /dev/stdin'  /etc/nginx/sites-enabled/default <<< "$hbnb_static"

sudo service nginx restart