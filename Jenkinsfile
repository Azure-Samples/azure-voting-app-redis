pipeline {
    agent any

    stages {

  
        stage('Verify Branch') {
            steps {
                echo '$GIT_BRANCH'
            }}




        
         stage('Clone Repo') {
            steps {
                // Get some code from a GitHub repository
                git url: 'https://github.com/anupalpatil/azure-voting-app-redis.git', branch: 'master'

               
            }}
        
        
        stage('Hello') {
            steps {
                echo 'HelloWorld'
            }}
            
             stage('GoodBye') {
            steps {
                echo 'GoodByeWorld'
            }
            
        }
    }
}
