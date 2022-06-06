pipeline {
    agent any
    environment {
        imagename="udp-derver"
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
               withCredentials([usernamePassword(credentialsId: '9c9b3ac6-bc43-49ee-9bbb-6de9f7d42482', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                sh '''
                    echo $PASSWORD | docker login -u $USERNAME --password-stdin ghcr.io
                    docker tag $imagename ghcr.io/Rachel33118301/$imagename
                    docker push ghcr.io/Rachel33118301/$imagename
                '''
              }
            }
        }
    }
}