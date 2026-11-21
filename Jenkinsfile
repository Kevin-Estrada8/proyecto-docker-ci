pipeline {
    agent any

    stages {

        stage('Verificar Git') {
            steps {
                bat 'git --version'
            }
        }

        stage('Verificar Docker') {
            steps {
                bat 'docker --version'
            }
        }

        stage('Verificar Docker Compose') {
            steps {
                bat 'docker compose version'
            }
        }

    }
}