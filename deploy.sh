#!/usr/bin/bash

# VARABLES #
machine=$1
SECRET_KEY="/var/lib/jenkins/.ssh/id_rsa" 
JENKINS_PROJECT_FOLDER="/var/lib/jenkins/workspace/dev-Automation/docker-compose.yml"
echo "deploying to $machine"
echo "createing directory and copy"
scp -o StrictHostKeyChecking=no -r $JENKINS_PROJECT_FOLDER ec2-user@$machine:/home/ec2-user/final
echo "COPIED to $machine"
ssh ec2-user@$machine "docker login"
ssh ec2-user@$machine "docker pull almogso/attenapp:latest"
ssh ec2-user@$machine "docker-compose -f /home/ec2-user/final/dev-Automation/docker-compose.yml up -d"
if [ $machine == "test" ];
then
    echo 'Run Curl testing...'
    ANS = ssh ec2-user@$machine "curl test"
    if [ ANS > 0 ];
        then echo "Request was successful"
        else echo "CURL Failed"
    fi 
    ssh ec2-user@$machine "docker-compose -f /home/ec2-user/final/dev-Automation/docker-compose.yml down"
    echo 'Test Docker Stopped !' 
fi
    
