pipeline {
    agent any

    stages {
        stage('Verify Git Branch') {
            steps {
                echo  env.GIT_BRANCH
            }
        }

        stage('Dockerbuild') {
            steps {
                pwsh(script: 'docker images -a')
                pwsh(script: """
                cd azure-vote/
                docker images -a
                docker build -t jenkins-pipeline .
                docker images -a
                cd ..
                """)
            }
        }
    
       
    }
}
