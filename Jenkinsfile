pipeline {
   agent any

   stages {
      stage('Verify Branch') {
         steps {
            echo "$GIT_BRANCH" //Jenkins makes this variable for us at run time, as well as others for its own use.
         }
      }
      //Here we are building our docker image
      stage('Docker Build'){
         steps{
            sh(script: 'docker images -a')
            sh(script: """
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