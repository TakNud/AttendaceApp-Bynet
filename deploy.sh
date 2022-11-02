#!/usr/bin/bash

# VARABLES #
machine=$1
SECRET_KEY="/var/lib/jenkins/.ssh/id_rsa" 
JENKINS_PROJECT_FOLDER="/var/lib/jenkins/workspace/dev-Automation"
echo "deploying to $machine"
echo "createing directory and copy"
#ssh -i $SECRET_KEY -o StrictHostKeyChecking=no $machine "mkdir -p /home/ec2-user/final"
scp -r -i $SECRET_KEY -o StrictHostKeyChecking=no $JENKINS_PROJECT_FOLDER ec2-user@$machine:/home/ec2-user/final
#scp -rp -i $SECRET_KEY -o StrictHostKeyChecking=no $JENKINS_PROJECT_FOLDER ec2-user@$machine:/home/ec2-user/final
#scp -i $SECRET_KEY $JENKINS_PROJECT_FOLDER ec2-user@$machine:~
