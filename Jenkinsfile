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
                    #dockerImage = docker.build registry + ":$BUILD_NUMBER"
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
            }
        }
    }
}
post {
    always {
        sh 'docker-compose down --remove-orphans -v'
    }
}
