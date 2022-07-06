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
        stage('Run Ansible'){
            steps{
                sh "ansible-playbook -i ansible-conifg/inventory.yaml ansible-config/playbook1.yaml"
            }
        }
        stage('Deployment'){
            steps{
                sh "bash deployment.sh"
            }
        }
    }    
}