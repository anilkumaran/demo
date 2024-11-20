
sudo apt update
sudo apt install apache2 python3-pip python3.12-venv
sudo a2enmod proxy
sudo a2enmod proxy_http


mkdir demo-ecom-app
cd demo-ecom-app
python3 -m venv demo-venv
source demo-venv/bin/activate
pip3 install Flask

flask --app hello run
