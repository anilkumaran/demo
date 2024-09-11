pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
                sh '''
                echo $(pwd)
                ls
                whoami
                python hello.py
                '''
            }
        }
        stage('GetCode') {
            steps {
                echo 'Getting Code'
            }
        }
        stage('Install Software') {
            steps {
                echo 'Installing python'
            }
        }
        stage('Build') {
            steps {
                echo 'Building app...'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing App...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying App...'
            }
        }
    }

}
