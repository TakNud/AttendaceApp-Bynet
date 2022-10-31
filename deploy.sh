#!/usr/bin/bash

# VARABLES #
machine=$1
SECRET_KEY="~/.ssh/id_rsa" 
JENKINS_PROJECT_FOLDER = /var/lib/jenkins/workspace/dev-Automation
echo "deploying to $machine"
echo "createing directory and copy"
scp -rp -i $SECRET_KEY -o StrictHostKeyChecking=no $JENKINS_PROJECT_FOLDER ec2-user@$machine:/home/ec2-user
