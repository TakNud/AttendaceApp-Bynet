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
                sh 'docker rmi -f $(docker images -aq)'
                echo 'docker image remove from local'
            }
        }
    }
}

