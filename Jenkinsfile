pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
                sh '''
                python3 create_db_backup
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
