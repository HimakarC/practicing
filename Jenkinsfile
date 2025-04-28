pipeline {
    agent any
    stages {
        stage('SSH to Remote Server') {
            steps {
                sshagent(['ubuntu']) {
                    sh 'ssh -o StrictHostKeyChecking=no ubuntu@18.224.62.192'
                }
            }
        }
    }
}
