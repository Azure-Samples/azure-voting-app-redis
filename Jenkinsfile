pipeline {
    agent none
    stages {
        stage('Verify Branch') {
            agent { label 'docker' }
            steps {
                echo "$GIT_BRANCH"
            }
        }
        stage('Docker Build') {
            agent { label 'docker' }
            steps {
                sh 'docker compose build'
            }
        }
        stage('Deploy to QA') {
            agent { label 'built-in' }
            when {
                branch 'master'
            }
            steps {
                sh 'kubectl apply -f azure-vote-all-in-one-redis.yaml'
            }
        }
        stage('Approve Deploy to Production') {
            agent { label 'built-in' }
            when {
                branch 'master'
            }
            steps {
                input message: 'Deploy to production?'
            }
        }
        stage('Deploy to Production') {
            agent { label 'built-in' }
            when {
                branch 'master'
            }
            steps {
                echo 'Deploying to production...'
                sh 'kubectl apply -f azure-vote-all-in-one-redis.yaml'
            }
        }
    }
}
