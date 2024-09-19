pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
        stage('ManageEC2') {
            parallel {
                stage('GetLaptopDetail') {
                    steps {
                        echo 'python3 get_laptop_details.py'
                    }
                }
                stage('Stop EC2') {
                    steps {
                        echo 'python3 stop_ec2.py'
                    }
                }
            }
        }
        //     steps {
        //         withAWS(region: 'us-east-1'){
        //             withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'PROD_AWS_ACCESS_KEY_ID', accessKeyVariable: 'AWS_ACCESS_KEY_ID', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY']]) {
        //                 sh'''
        //                 python3 stop_ec2_instances.py
        //                 '''
        //             }
        //         }
        //     }
        // }
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
