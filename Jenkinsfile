pipeline {
    agent any

    environment {
        APP = "demo"
        APP_NO_DASH = APP.replaceAll("-","")
        DOCKERFILE="devops/Dockerfile"
        REGION = 'ap-south-1'
        ENV = BRANCH_NAME.replaceAll("DEMO-CICD-","").replaceAll("-","").replaceAll("\\d","").toLowerCase()
        BRANCH = BRANCH_NAME.replaceAll("USN-CICD-","").replaceAll("-","").toLowerCase()
        PORT = '5000'
        SPACE = 'anilkumaran'
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
            steps {
                script {
                    echo "Building ${env.ENV} environment"
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
                            def stackName = "${env.APP}-${env.ENV}"
                            def filePath = "devops/CF-" + env.APP + ".yaml"
                            cfnUpdate(stack: stackName, file: filePath, params:[
                                'AppName='+ env.APP,
                                'Env='+ env.ENV
                                ]
                            )
                        }
                    }
                }
            }
        }
        stage('Build') {
            steps {
                echo "Building ${env.ENV} environment"
                CFN_TEMPLATE = 'devops/CF-' + APP + '.yaml'
                sh """
                sudo docker build -t $DOCKER_IMAGE .
                aws ecr get-login-password --region ${REGION} |
                sudo docker login \
                    --username AWS \
                    --password-stdin \
                    "${ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com"
                """
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying ${env.ENV} environment"
                sh """
                declare -A ACCOUNT_NO
                ACCOUNT_NO=(
                    ['uat']="631906900060"
                    ['prod']="631906900060"
                )

                AWS_ACCOUNT_ID="631906900060"
                aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin ${ACCOUNT_NO[$ENV]}.dkr.ecr.${REGION}.amazonaws.com
                // aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com
                // docker build --no-cache -f devops/Dockerfile -t ak .

                docker build --no-cache\
                    -f ${DOCKERFILE} \
                    --build-arg ACCOUNT_ID=${ACCOUNT_NO[$ENV]} \
                    --build-arg APP=${APP} \
                    --build-arg APPNODASH=${APP_NO_DASH} \
                    --build-arg ENV=${ENV} \
                    --build-arg BRANCH_NAME=${BRANCH} \
                    --build-arg PORT=${PORT} \
                    --build-arg REGION=${REGION} \
                    -t ${ACCOUNT_NO[$ENV]}.dkr.ecr.${REGION}.amazonaws.com/${APP_NO_DASH}:${BRANCH,,}-${BUILD_NUMBER}  \
                    -t ${ACCOUNT_NO[$ENV]}.dkr.ecr.${REGION}.amazonaws.com/${APP_NO_DASH}:latest ${WORKSPACE}

                [ $? -ne 0 ] && exit 1
                
                sudo docker push ${ACCOUNT_NO[$ENV]}.dkr.ecr.${REGION}.amazonaws.com/${APP_NO_DASH}:${BRANCH,,}-${BUILD_NUMBER}
                sudo docker push ${ACCOUNT_NO[$ENV]}.dkr.ecr.${REGION}.amazonaws.com/${APP_NO_DASH}:latest
                """
                // STACK_NAME = "employee-management-${env.ENV}"

                // Run AWS CLI to create/update CloudFormation stack
                // sh """
                // aws cloudformation deploy \
                //   --template-file ${CFN_TEMPLATE} \
                //   --stack-name ${STACK_NAME} \
                //   --capabilities CAPABILITY_NAMED_IAM \
                //   --parameter-overrides EnvType=${env.ENV} \
                //   --region ${REGION}
                // """
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
