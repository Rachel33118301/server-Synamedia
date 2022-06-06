pipeline {
    environment {
        imagename="udp-derver"
    }
    // agent {
    //     docker {
    //         // maven:3.8.1-adoptopenjdk
    //         image 'cdrachel/cdnode'
    //         args '-v /root/.m2:/root/.m2'

            
    //     }
    // }
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t $imagename .'
            }
        }
        stage('Test') { 
            steps {
                sh 'docker run --rm $imagename -m pytest --ignore=cs_utils --suppress-no-test-exit-code'
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