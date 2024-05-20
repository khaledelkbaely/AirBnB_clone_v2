#!/usr/bin/env bash
# set up web server for the deployment of web_static

# Install nginx if not already installed
sudo apt-get update -y && sudo apt-get install nginx -y

# create the folder /data/ if not exist
[ ! -d /data/ ] && sudo mkdir /data/

# create the folder /data/web_static/ if not exist
[ ! -d /data/web_static/ ] && sudo mkdir /data/web_static/

# create the folder /data/web_static/releases/ if not exist
[ ! -d /data/web_static/releases/ ] && sudo mkdir /data/web_static/releases/

# create the folder /data/web_static/shared/ if not exist
[ ! -d /data/web_static/shared/ ] && sudo mkdir /data/web_static/shared/

# create the folder /data/web_static/releases/test/ if not exist
[ ! -d /data/web_static/releases/test/ ] && sudo mkdir /data/web_static/releases/test/

# create the folder /data/web_static/releases/test/index.html if not exist
[ ! -e /data/web_static/releases/test/index.html ] && echo "Hello this test for web_static" | sudo tee /data/web_static/releases/test/index.html &> /dev/null
# create symbolic link /data/web_static/current linked to /data/web_static/releases/test/
# if the symbolic link exists delete then recreat it
if [ ! -e /data/web_static/current/ ]; then
	sudo ln -s /data/web_static/releases/test/ /data/web_static/current
else
	sudo rm -rf /data/web_static/current
	sudo ln -s /data/web_static/releases/test/ /data/web_static/current
fi
# give ownership of the /data/ to the ubuntu user and group with the recursive option
sudo chown -R /data/ ubuntu:ubuntu
# update the nginx configuration to serve the /data/web_static/curent/ to hbnb_static (use alias)
sudo sed -i "/server_name _;/a location \/hbnb_static {\n\t\talias \/data\/web_static\/current\/;\n\t}" /etc/nginx/sites-available/default
# restart nginx
sudo service nginx restart 
