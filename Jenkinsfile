pipeline {
    agent any

    stages {
        stage('Verify Git Branch') {
            steps {
                echo  '${GIT_BRANCH}'
            }
        }

        stage('Docker build') {
            steps {
                pwsh(script: 'docker images -a')
                pwsh(script: """
                cd azure-vote
                docker images -a
                docker build -t jenkins-pipeline .
                docker images -a
                cd ..
                """)
            }
        }
    
       
    }
}
