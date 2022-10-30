#!/usr/bin/bash

# VARABLES #
machine=$1
SECRET_KEY="/home/ec2-user/.ssh/id_rsa" 
JENKINS_PROJECT_FOLDER = /var/lib/jenkins/workspace/dev-Automation
echo "deploying to $machine"
echo "createing projenct directory"
ssh -i "${SECRET_KEY}" ${machine} "mkdir -p /home/ec2-user/final-project"
echo "yes"
echo "copying..."
scp -i "$(SECRET_KEY)" "${JENKINS_PROJECT_FOLDER}" "${machine}:/home/ec2-user/final-project"
echo "yes"
