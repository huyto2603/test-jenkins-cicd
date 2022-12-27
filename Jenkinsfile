pipeline {
    agent {
        docker {
            image 'python:3.8-slim-buster'
            args '-u 0:0 -v /tmp:/root/.cache'
        }
    }

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/huyto2603/test-jenkins-cicd.git']]])
            }
        }
        
        stage('Test Unit'){
            steps {
                sh 'pip3 install --upgrade pip'
                sh 'pip3 install fastapi'
                sh 'pip3 install pytest'
                sh 'pip3 install httpx'
                sh 'pytest test.py'
                echo "Check unit complete"
            }
        }
        stage('Complete') {
            steps {
                echo "test success"
            }
        }
    }
}
