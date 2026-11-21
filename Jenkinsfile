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
                bat '"C:\\Users\\Kandres Estrada.KANDRES-ESTRADA\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" --version'
            }
        }

        stage('Verificar Docker Compose') {
            steps {
                bat '"C:\\Users\\Kandres Estrada.KANDRES-ESTRADA\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" compose version'
            }
        }

    }
}