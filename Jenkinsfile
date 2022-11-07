pipeline {
    environment {
        registry = 'jenk_deneme/ml_model'
        DOCKERHUB_CREDENTIALS=credentials('Docker-Cred')
    }
    agent any
    stages {
        stage('Build Docker Image') {
            agent any
            steps {
                script {
                    sh 'docker build -t almogso/attenapp:latest .'
                    echo 'build image succesfully'
                }
            }
        }
        stage('Login') {

            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }
        stage('docker push to hub'){
            steps {
                sh 'docker push almogso/attenapp:latest'
                echo 'image was pushed to HUB'
                //sh 'docker system prune --all'
                //echo 'y'
                //echo 'docker image removed from local'
            }
        }
        stage('Test'){
            steps{
                sshagent(['ec2-user']) {
                    sh 'bash -x deploy.sh test'
                }
            }
        }
         stage('Prod'){
            steps{
                sshagent(['ec2-user']) {
                    sh 'bash -x deploy.sh prod'
                }
            }
        }
        
    }
}

