pipeline {
    environment {
        registry = 'jenk_deneme/ml_model'
        DOCKERHUB_CREDENTIALS=credentials('Docker-Cred')
        dockerImage = ''
    }
    agent any
    stages {
        stage('Build Docker Image') {
            agent any
            steps {
                script {
                    
                    sh 'docker build -t almogso/attenapp:latest .'
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
                sh 'docker stop $(docker ps -q) || docker rm $(docker ps -a -q) || docker rmi $(docker images -q -f dangling=true)'
                echo 'docker image removed from local'
            }
        }
    }
}

