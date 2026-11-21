pipeline {
    agent any

    stages {

        stage('Clonar Proyecto') {
            steps {
                echo 'Repositorio obtenido desde GitHub'
            }
        }

        stage('Verificar Archivos') {
            steps {
                bat 'dir'
            }
        }

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