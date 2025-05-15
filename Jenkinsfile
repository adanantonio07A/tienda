pipeline {
    agent any

    environment {
        VENV_PATH = 'venv'
    }

    stages {
        stage('Clonar repositorio') {
            steps {
                git branch: 'main', url: 'https://github.com/adanantonio07A/tienda.git'
            }
        }
        stage('Preparar entorno') {
            agent {
                docker {
                    image 'python:3.10'
                }
            }
            steps {
                echo 'Creando entorno virtual e instalando dependencias...'
                sh '''
                    python -m venv $VENV_PATH
                    . $VENV_PATH/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Ejecutar pruebas') {
            agent {
                docker {
                    image 'python:3.10'
                }
            }
            steps {
                echo 'Ejecutando pruebas...'
                sh '''
                    . $VENV_PATH/bin/activate
                    pytest
                '''
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
        success {
            echo '¡Todo correcto! ✔️'
        }
    }
}
