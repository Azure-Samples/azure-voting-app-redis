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


        stage('Start an App'){
            steps {
                pwsh(script: """
                 echo $env.STAGE_NAME
                """)
            }
            post {
                success{
                    echo "Scuccess"
                }

                failure {
                    echo "Failuer"
                }
            }
        }

        stage('Run tests'){
            steps {
                echo "Workspace is $WORKSPACE"
                pwsh(script: """
                echo ${Get-Location}
                //python ./tests/test_plan.py
                """)
            }

        }

        stage('Stop test app'){
            steps {
                pwsh(script: """
               echo $env.STAGE_NAME
                """)
            }

        }

        stage('Push container'){
             steps{

             echo "Workspace is $WORKSPACE"
             dir("$WORKSPACE/azure-vote"){
              script {
                  docker.withRegistry('https://index.docker.io/v1/', 'DockerHub')
                  def image = docker.build('schaugule/jenkins-course:latest')
                  image.push()
              }
             }

             }


        }
    
       
    }
}
