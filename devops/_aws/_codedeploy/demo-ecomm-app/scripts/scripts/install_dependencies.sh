#!/bin/bash
sudo yum update -y
sudo yum install python3 -y
sudo pip3 install -r /home/ec2-user/app/requirements.txt
