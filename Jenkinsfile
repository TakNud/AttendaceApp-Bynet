pipeline {
    environment {
        registry = 'jenk_deneme/ml_model'
        dockerImage = ''
    }
    agent any
    stages {
        stage('Build Docker Image') {
            agent any
            steps {
                script {
                    dockerImage = docker.build registry + ":$BUILD_NUMBER"
                }
            }
        }
        stage('Run Image'){
            steps {
                sh 'docker compose up -d --no-color --wait'
            }
        }
    }
}
post {
    always {
        sh 'docker compose down --remove-orphans -v'
    }
}
