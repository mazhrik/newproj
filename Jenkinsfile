pipeline {
    agent any
    stages {
        stage('Pull Docker image') {
            steps {
                script {
                    docker.pull('image-name:tag')
                }
            }
        }
        stage('Run Docker container') {
            steps {
                script {
                    docker.run('image-name:tag')
                }
            }
        }
    }
}