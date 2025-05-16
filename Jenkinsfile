pipeline {
    agent {
        docker {
            image 'python:3.10-slim' // Usa tu imagen base si ya tienes una propia
        }
    }
    environment {
        MYSQL_HOST = 'localhost'
        MYSQL_PORT = '3306'
        MYSQL_USER = 'root'
        MYSQL_PASSWORD = 'root'
        MYSQL_DB = 'tienda'
    }
    stages {
        stage('Instalar dependencias') {
            steps {
                sh '''
                    apt-get update
                    apt-get install -y default-mysql-client libmariadb-dev
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Iniciar MySQL') {
            steps {
                sh '''
                    echo "Revisando si ya existe el contenedor mysql-test..."
                    docker ps -a --format '{{.Names}}' | grep -w mysql-test && docker rm -f mysql-test || echo "No existe contenedor previo"
                    docker run -d --name mysql-test \
                      -e MYSQL_ROOT_PASSWORD=${MYSQL_PASSWORD} \
                      -e MYSQL_DATABASE=${MYSQL_DB} \
                      -p ${MYSQL_PORT}:3306 \
                      mysql:8

                    # Esperar que el puerto esté abierto (MySQL levantado)
                    for i in {1..30}; do
                        nc -z ${MYSQL_HOST} ${MYSQL_PORT} && break
                        echo "Esperando a que MySQL esté disponible..."

                        sleep 1
                    done
                '''
            }
        }

        stage('Iniciar MySQL') {
            steps {
                sh '''
                    echo "Revisando si ya existe el contenedor mysql-test..."
                    docker ps -a --format '{{.Names}}' | grep -w mysql-test && docker rm -f mysql-test || echo "No existe contenedor previo"
                    docker run -d --name mysql-test \
                      -e MYSQL_ROOT_PASSWORD=${MYSQL_PASSWORD} \
                      -e MYSQL_DATABASE=${MYSQL_DB} \
                      -p ${MYSQL_PORT}:3306 \
                      mysql:8

                    # Esperar que el puerto esté abierto (MySQL levantado)
                    for i in {1..30}; do
                        nc -z ${MYSQL_HOST} ${MYSQL_PORT} && break
                        echo "Esperando a que MySQL esté disponible..."
                        sleep 1
                    done
                '''
            }
        }
      
        stage('Correr tests') {
            steps {
                sh '''
                    # Ejecutar los tests con pytest
                    pytest
                '''
            }
        }
    }
    post {
        always {
            echo "Limpiando contenedor MySQL..."
            sh 'docker rm -f mysql-test || true'
        }
    }
}
