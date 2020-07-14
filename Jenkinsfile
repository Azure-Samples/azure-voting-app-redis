pipeline {
    agent any

    stages {
        stage('Verify Git Branch') {
            steps {
                echo  env.GIT_BRANCH
            }
        }

        stage('Docker build') {
            steps {
                pwsh(script: 'Write-output India')
            }
        }
    
       
    }
}
