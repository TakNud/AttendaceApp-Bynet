#!/usr/bin/bash

# VARABLES #
machine=$1
SECRET_KEY="/var/lib/jenkins/.ssh/id_rsa" 
JENKINS_PROJECT_FOLDER="/var/lib/jenkins/workspace/dev-Automation/docker-compose.yml"
echo "deploying to $machine"
echo "createing directory and copy"
scp -o StrictHostKeyChecking=no -r $JENKINS_PROJECT_FOLDER ec2-user@$machine:/home/ec2-user/final
echo "COPIED to $machine"
docker login
docker pull almogso/attenapp:tagname
docker-compose -f /home/ec2-user/final/dev-Automation/docker-compose.yml up -d
if [$machine == "test"];
then
    echo 'Run Curl testing...'
    if [curl test > HTML_Output];
        then echo "Request was successful"
        else echo "CURL Failed"
    fi 
    docker-compose -f /home/ec2-user/final/dev-Automation/docker-compose.yml down
    echo 'Test Docker Stopped !' 
fi
    
