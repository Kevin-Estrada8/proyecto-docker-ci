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
                sh 'ls -la'
            }
        }

        stage('Verificar Docker Compose') {
            steps {
                sh 'cat docker-compose.yml'
            }
        }

    }
}