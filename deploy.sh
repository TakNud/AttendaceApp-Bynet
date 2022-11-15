#!/usr/bin/bash

# VARABLES #
machine=$1
JENKINS_PROJECT_FOLDER="/var/lib/jenkins/workspace/dev-Automation/docker-compose.yml"
echo "deploying to $machine"
echo "createing directory and copy"
scp -o StrictHostKeyChecking=no -r $JENKINS_PROJECT_FOLDER ec2-user@$machine:/home/ec2-user/final
scp -o StrictHostKeyChecking=no -r ~/.docker/config.json ec2-user@$machine:~/.docker/config.json
echo "COPIED to $machine"
ssh ec2-user@$machine "docker login"
ssh ec2-user@$machine "docker pull almogso/attenapp:latest"
ssh ec2-user@$machine "docker-compose -f /home/ec2-user/final/docker-compose.yml up -d"
if [ $machine == "test" ];
then
    sleep 20
    echo 'Run Curl testing...'
    if curl -I test 2>&1 | grep -w "200\|301" ; then
        echo 'Test success'
    else
        echo 'Test not success'
    fi
    
    ssh ec2-user@$machine "docker-compose -f /home/ec2-user/final/docker-compose.yml down"
    echo 'Test Docker Finished !' 
fi
    
