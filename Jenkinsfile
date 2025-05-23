pipeline {
    agent any

    environment {
        APP = "demo"
        APP_NO_DASH = APP.replaceAll("-","")
        REGION = 'ap-south-1'
        ENV = BRANCH_NAME.replaceAll("DEMO-CICD-","").replaceAll("-","").replaceAll("\\d","").toLowerCase()
        BRANCH = BRANCH_NAME.replaceAll("USN-CICD-","").replaceAll("-","").toLowerCase()
        PORT = '5000'
    }
    stages {
        stage('Checkout') {
            steps {
                echo "Getting code"
                script {
                    sh'''
                    git clone git@github.com:surendr/testQ.git
                    
                    '''
                }
                
            }
        }
        stage('Set AWS Credentials') {
            steps {
                echo "Building ${params.EnvType} environment"
                withAWS(region: env.REGION){
                    withCredentials([[
                        $class: 'AmazonWebServicesCredentialsBinding',
                        accessKeyVariable: 'AWS_ACCESS_KEY_ID',
                        secretKeyVariable: 'AWS_SECRET_ACCESS_KEY',
                        credentialsId: 'demo-aws-account' // ID of the AWS credentials in Jenkins
                    ]]) {
                        // AWS credentials are now set in the environment
                        echo -e "pwd: ${pwd}"
                        echo "AWS credentials loaded."
                        // cfnUpdate(stack: env.APP + '-common', file:'devops/CF-' + env.APP + '-common.yaml', params:[
                        //     'Application='+ env.APP_NO_DASH,
                        //     'AccountName='+ env.ENV
                        //     ]
                        // )
                    }
                }
            }
        }
        stage('Build') {
            steps {
                echo "Building ${params.EnvType} environment"
                // CFN_TEMPLATE = 'devops/CF-' + APP + '.yaml'
                // sh 'pip install -r requirements.txt'
                // sh 'pytest tests/'  // Run tests
                // sh """
                // sudo docker build -t $DOCKER_IMAGE .
                // aws ecr get-login-password --region ${REGION} |
                // sudo docker login \
                //     --username AWS \
                //     --password-stdin \
                //     "${ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com"
                // """
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying ${params.EnvType} environment"
                // STACK_NAME = "employee-management-${params.EnvType}"

                // Run AWS CLI to create/update CloudFormation stack
                // sh """
                // aws cloudformation deploy \
                //   --template-file ${CFN_TEMPLATE} \
                //   --stack-name ${STACK_NAME} \
                //   --capabilities CAPABILITY_NAMED_IAM \
                //   --parameter-overrides EnvType=${params.EnvType} \
                //   --region ${REGION}
                // """
            }
        }
        stage("Test") {
            steps {
                script {
                    sh'''
                    ./myQAScript.sh
                    '''
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
