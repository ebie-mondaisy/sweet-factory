pipeline{
    agent any
    stages{
        stage('App Testing'){
            steps{
                sh "bash test.sh"
            }
        }
        stage('Building and pushing images'){
            environment{
                DOCKERHUB_USERNAME=credentials('DOCKERHUB_USERNAME')
                DOCKERHUB_PASSWORD=credentials('DOCKERHUB_PASSWORD')
            }
            steps{
                sh "docker-compose build --parallel"
                sh "docker login -u $DOCKERHUB_USERNAME -p $DOCKERHUB_PASSWORD"
                sh "docker-compose push"
            }
        }
        stage('Deployment'){
            steps{
                sh "scp -i ~/.ssh/id_rsa docker-compose.yaml radio@swarm-manager:/home/radio/docker-compose.yaml"
                sh "scp -i ~/.ssh/id_rsa nginx.conf radio@swarm-manager:/home/radio/nginx.conf"
                sh "ansible-playbook -i ansible-config/inventory.yaml ansible-config/playbook1.yaml"
            }
        }
    }    
}