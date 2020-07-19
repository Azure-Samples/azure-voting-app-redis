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
                pwsh(script: """
                echo $pwd
                python ./tests/test_plan.py
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
    
       
    }
}
