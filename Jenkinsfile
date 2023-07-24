pipeline {
    agent any

    stages {

  
        stage('Verify Branch') {
            steps {
                echo "$GIT_BRANCH"

            }}


            stage('Docker Build') {
            steps {
            echo 'Docker Building start'
            pwsh(script: 'docker images -a' )
            pwsh(script: """ 
            cd azure-vote/
            docker images -a 
            docker build -t jenkins-pipeline .
            docker images -a 
            cd ..
            """)
            
         
            }}

        
        
    }
}
