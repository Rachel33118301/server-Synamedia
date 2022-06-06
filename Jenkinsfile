pipeline {
    agent any
    environment {
        imagename="udp-server"
    }

    stages {
        stage('Build') {
            steps {
                sh 'docker build -t $imagename .'
            }
        }
        stage('Test') { 
            steps {
                sh 'docker run --rm --entrypoint python3 $imagename -m pytest --suppress-no-test-exit-code'
            }
        }
        stage('Publish') { 
            steps {
               withCredentials([usernamePassword(credentialsId: 'DockerHub', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                sh '''
                    echo $PASSWORD | docker login -u $USERNAME --password-stdin
                    docker tag $imagename cdrachel/$imagename
                    docker push cdrachel/$imagename
                '''
              }
            }
        }
    }
}