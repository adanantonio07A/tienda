pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Clonar repositorio') {
            steps {
                git branch: 'main', url: 'https://github.com/adanantonio07A/tienda.git'
            }
        }

        stage('Preparar entorno') {
            steps {
                sh 'python -m venv $VENV_DIR'
                sh './$VENV_DIR/Scripts/activate && pip install -r requirements.txt'
            }
        }

        stage('Ejecutar pruebas') {
            steps {
                sh './$VENV_DIR/Scripts/activate && pytest'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finalizado.'
        }
        failure {
            echo 'Algo falló. Revisa el log.'
        }
    }
}
