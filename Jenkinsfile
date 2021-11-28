pipeline {
    agent any
    
    input {
  message 'jenkins path'
  parameters {
    string defaultValue: 'master/azure/jenkins   | dev/az/jenkins', description: 'for jenkins path', name: 'path', trim: true
    choice choices: ['dev', 'prod'], description: 'for environment', name: 'env'
  }
}


    stages {
        stage('checkout') {
            steps {
                echo 'Hello World'
            }
        }
        stage('Build'){
            steps{
                echo 'building test'
            }
        }
        stage('test'){
            steps{
                echo 'testing '
            }
        }
    }
}
