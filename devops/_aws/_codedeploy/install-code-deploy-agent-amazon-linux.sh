#!/bin/bash
export AWS_REGION='us-east-1'

sudo yum update -y
sudo yum install -y ruby
sudo yum install -y wget

# (Optional) To clean the AMI of any previous agent caching information, run the following script:
CODEDEPLOY_BIN="/opt/codedeploy-agent/bin/codedeploy-agent"
$CODEDEPLOY_BIN stop
yum erase codedeploy-agent -y

cd /home/ec2-user

wget https://aws-codedeploy-${AWS_REGION}.s3.${AWS_REGION}.amazonaws.com/latest/install
chmod +x ./install
sudo ./install auto
sudo service codedeploy-agent start
sudo systemctl status codedeploy-agent