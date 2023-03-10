pipeline {
    agent any
    stages {
        stage('Pull and Run Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker_credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh "docker login -u $DOCKER_USER -p $DOCKER_PASS"
                    sh "docker pull malikmuneeb98900/hospital:latest"
                    sh "docker run -p 8000:8080 malikmuneeb98900/hospital:latest"
                    

                }
            }
        }
    }
}