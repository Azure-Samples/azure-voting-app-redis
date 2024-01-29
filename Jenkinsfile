pipeline{
    agent any

    stages{
        stage('Verify Branch'){
            steps{
                echo "$GIT_BRANCH"
            }
        }
        stage('Docker Build'){
            steps{
                sh(script: 'docker componse build')
            }
        }
        stage('Start App'){
            steps{
                sh(script: 'docker compose up -d')
            }
        }
        stage('Run Tests'){
            steps{
                sh(script: 'pytest ./tests/test_sample.py')
            }
            post{
                success{
                    echo 'Test Passed!'
                }
                failure{
                    echo 'Test Failed!'
                }
            }
        }
    }
    post{
            always{
                sh(script: 'docker compose down')
            }
        }
}
