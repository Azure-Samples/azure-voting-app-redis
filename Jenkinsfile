
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
                  docker.withRegistry('https://index.docker.io/v1/', 'DockerHub') {
                  def image = docker.build('schaugule/jenkins-course:latest')
                  image.push()
                  }
              }
             }

             }


        }
        stage('Parallel demo') {
        parallel {
        stage('Dummy step i'){
            steps{
                script {
                    traditional_int_for_loop()
                }
            }
        }

         stage('Dummy step j'){
            steps{
                script {
                     traditional_int_for_loop()
                }
            }
        }
        }
    }

    stage('Deploy to QA'){
       environment {
           ENVIRONMENT = 'QA'
       }
       steps {
           echo "Deploying to $ENVIRONMENT"
       }


    }

    stage ('Approve'){
        when {
            branch 'master'
        }
        options {
            timeout(time:1, unit: 'HOURS')

        }
        steps {
            input message: "Deploy?"
        }
    }

      stage('Deploy to PROD'){
       environment {
           ENVIRONMENT = 'PROD'
       }
       steps {
           echo "Deploying to $ENVIRONMENT"
       }


    }
    
       
    }
}

def traditional_int_for_loop() {
    for (int i = 0; i < 100; i++) {
        sleep(1)
        echo "Hello ${i}"
    }
}
