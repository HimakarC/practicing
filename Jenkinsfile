pipeline {
  agent any
  stages {
    stage('SSH to Remote Server') {
      steps {
        sshagent(['ubuntu']) { //Here 'ubuntu' is the credentials that you have created in manage jenkins (Like giving slave's public key as hostname and private key of master)
          sh 'ssh -o StrictHostKeyChecking=no ubuntu@18.224.62.192'
          sh 'ansible-playbook -i inv.ini pla.yml'
        }
      }
    }
  }
}
