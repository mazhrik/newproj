pipeline {
    agent {
        node{
        label "Jenkins-slave-1"
        }
    }
    environment {
        CONTAINER_NAME = 'hospital_app_container_1'
    }
    stages {
        stage('Pull and Run Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker_credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh "docker login -u $DOCKER_USER -p $DOCKER_PASS"
                    sh "docker pull malikmuneeb98900/hospital:latest"
                    sh "docker run -d -p  8001:8080 --name $CONTAINER_NAME malikmuneeb98900/hospital:latest"
                    timeout(time: 3, unit: 'MINUTES') {
                        sh "docker stop $CONTAINER_NAME"
                        sh "docker rm $CONTAINER_NAME"
                    }
                    
                }
            }
        }
    }
}