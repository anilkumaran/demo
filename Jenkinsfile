pipeline {
    agent any

    environment {
        APP = "demo"
        APP_NO_DASH = APP.replaceAll("-","")
        DOCKERFILE="devops/Dockerfile"
        REGION = 'ap-south-1'
        ENVIRONMENT = BRANCH_NAME.replaceAll("DEMO-CICD-","").replaceAll("-","").replaceAll("\\d","").toLowerCase()
        BRANCH = BRANCH_NAME.replaceAll("DEMO-CICD-","").replaceAll("-","").toLowerCase()
        PORT = '5000'
        SPACE = 'anilkumaran'
        AWS_ACCOUNT_ID="631906900060"
        ECR_REPO_NAME = "${env.APP_NO_DASH}-${env.ENVIRONMENT}"


        // Infra Details
        PROD_INSTANCE_ID = 'i-1234567890abcdef0'     // Production EC2 instance ID
        UAT_INSTANCE_ID = 'i-01838d16e7a72889d'      // UAT EC2 instance ID
        EC2_KEY_PAIR = '/var/lib/jenkins/devops/ak-instance-kp.pem'         // EC2 keypair name

        DEPLOY = 'True'
    }
    options {
        timeout(time: 1, unit: 'HOURS')
        buildDiscarder(logRotator(numToKeepStr: '20'))
        disableConcurrentBuilds()
        skipDefaultCheckout()
    }
    stages {
        stage('Checkout') {
            steps {
                echo "Getting code"
                // repo 'https://github.com/anilkumaran/demo.git'
                // git@github.com:anilkumaran/demo.git
                deleteDir()
                git credentialsId: 'jenkins-master-ssh-key', url: 'git@github.com:' + env.SPACE + '/' + env.APP + '.git', branch: env.BRANCH_NAME
            }
        }
        stage('BuildCF') {
            // To build infra required to deploy the application
            when {expression {env.DEPLOY == 'True'} }
            steps {
                script {
                    echo "Building ${env.ENVIRONMENT} environment"
                    withAWS(region: env.REGION){
                        withCredentials([[
                            $class: 'AmazonWebServicesCredentialsBinding',
                            accessKeyVariable: 'AWS_ACCESS_KEY_ID',
                            secretKeyVariable: 'AWS_SECRET_ACCESS_KEY',
                            credentialsId: 'demo-aws-account' // ID of the AWS credentials in Jenkins
                        ]]) {
                            // AWS credentials are now set in the environment
                            echo "pwd: ${pwd}"
                            echo "WORKSPACE: ${WORKSPACE}"
                            def stackName = "${env.APP}-${env.ENVIRONMENT}"
                            def filePath = "devops/CF-" + env.APP + ".yaml"
                            cfnUpdate(stack: stackName, file: filePath, params:[
                                'AppName='+ env.APP,
                                'Env='+ env.ENVIRONMENT
                                ]
                            )
                        }
                    }
                }
            }
        }
        stage('Build') {
            when {expression {env.DEPLOY == 'True'} }
            steps {
                script{
                    withAWS(region: env.REGION){
                        withCredentials([[
                            $class: 'AmazonWebServicesCredentialsBinding',
                            accessKeyVariable: 'AWS_ACCESS_KEY_ID',
                            secretKeyVariable: 'AWS_SECRET_ACCESS_KEY',
                            credentialsId: 'demo-aws-account' // ID of the AWS credentials in Jenkins
                        ]]) {

                            echo "Deploying ${env.ENVIRONMENT} environment"
                            sh """#!/bin/bash
                            whoami
                            aws ecr get-login-password --region ${REGION} | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com
                            # docker build --no-cache -f devops/Dockerfile -t ak .
                            echo "WORKSPACE: ${WORKSPACE}"
                            # -t ak ${WORKSPACE}
                            docker build --no-cache \
                                -f devops/Dockerfile \
                                --build-arg ACCOUNT_ID=${AWS_ACCOUNT_ID} \
                                --build-arg APP=${APP} \
                                --build-arg APPNODASH=${APP_NO_DASH} \
                                --build-arg ENVIRONMENT=${ENVIRONMENT} \
                                --build-arg BRANCH_NAME=${BRANCH} \
                                --build-arg PORT=${PORT} \
                                --build-arg REGION=${REGION} \
                                -t ${AWS_ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com/${ECR_REPO_NAME}:${BRANCH}-${BUILD_NUMBER} \
                                -t ${AWS_ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com/${ECR_REPO_NAME}:latest ${WORKSPACE}
                            docker push ${AWS_ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com/${ECR_REPO_NAME}:${BRANCH}-${BUILD_NUMBER}
                            docker push ${AWS_ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com/${ECR_REPO_NAME}:latest
                            """
                        }
                    }
                }

            }
        }
        stage('Deploy') {
            steps {
                script{
                    withAWS(region: env.REGION){
                        withCredentials([[
                            $class: 'AmazonWebServicesCredentialsBinding',
                            accessKeyVariable: 'AWS_ACCESS_KEY_ID',
                            secretKeyVariable: 'AWS_SECRET_ACCESS_KEY',
                            credentialsId: 'demo-aws-account' // ID of the AWS credentials in Jenkins
                        ]]) {
                            def aws_cred_file="/home/ubuntu/.aws/credentials"
                            def instanceId_pubIp_map = [
                                'uat': '13.201.35.25',
                                'prod': '1.2.3.4'
                                ]
                                
                            echo "Deploying to EC2 instance: ${instanceId_pubIp_map[ENVIRONMENT]}"
                            // def instance_ip = ${instanceId_pubIp_map[ENVIRONMENT]}
                            // echo "Deploying the Docker image to EC2 instance ${instanceId} and ip: ${instanceId_pubIp_map.}"
                            sh """#!/bin/bash
                            echo ${instanceId_pubIp_map[ENVIRONMENT]}
                            ssh -i ${EC2_KEY_PAIR} -tt ubuntu@${instanceId_pubIp_map[ENVIRONMENT]} << 'ENDSSH'
                                mkdir -p /home/ubuntu/.aws
                                touch ${aws_cred_file}
                                echo [default] > ${aws_cred_file}
                                echo aws_access_key_id = ${AWS_ACCESS_KEY_ID} >> ${aws_cred_file}
                                echo aws_secret_access_key = ${AWS_SECRET_ACCESS_KEY} >> ${aws_cred_file}
                                cat ${aws_cred_file}
                                
                                aws ecr get-login-password --region ${REGION} | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com
                                docker pull ${AWS_ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com/${ECR_REPO_NAME}:latest
                                docker stop demo || true
                                docker rm demo || true
                                docker run -d --name demo -p 5000:5000 ${AWS_ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com/${ECR_REPO_NAME}:latest
                                exit 0
                            ENDSSH
                            """
                        }
                    }
                }
            }
        }

    }
    
    post {
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Deployment failed!'
        }
    }
}
