pipeline {
    agent any
    parameters {
        choice(name: 'VERSION', choices: ['v1.0', 'v2.0', 'v3.0'], description: 'Build versions of Jenkins Build')
    }
    environment {
        VARIABLE = 'HELLO JENKINS'
        SERVER_CREDENTIALS = credentials('git_token_credentials')
    }
    stages {
        stage('Build') {
            steps {
                echo 'You are in Build stage...'
                echo "Build Version ${VERSION}"
                echo "My credential username ${SERVER_CREDENTIALS_USR}"
                echo "My credentials password ${SERVER_CREDENTIALS_PSW}"
                sh 'python --version'
                sh 'python Hello_World.py'
            }
        }
        stage('Test') {
            
            steps{
                echo 'You are in test stage...'
                echo "Testing if variable works for ${VARIABLE}"
            }
        }
        stage('Deploy') {
            steps{
                echo 'You are in deploy stage...'
            }
        }
    }
    post{
        always {
            echo 'You have successfully run a build in jenkins'
        }
        success{
            echo 'Your build is successfull congratulations'
        }
        failure{
            echo 'Sorry for fail build'
        }
    }
}
