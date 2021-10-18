pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'docker build -t tomer-app .'
            }
        }
        stage('Test'){
            steps {
               sh 'docker-compose up -d'
               sh 'sleep 60'
               sh 'docker-compose down'
            }
        }
        stage('Publish'){
            steps {
               ehco "hello" 
            }
        }
        }
        
    
}
