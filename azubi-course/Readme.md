# 1. Containerisierung

## Basics 
- was ist ein container? 
- wie erstellt man einen Container? 

- downloade dieses docker image <insert ubuntu> here 
- starte den container und execute in den container  'docker exec -it <name> /bin/bash' 

## Dockerfile
- erstelle selber ein dockerimage 

1. nimm das ubuntu image als base image im dockerfile 
2. installiere python 
4. build das image 

## Container 
starte das erzeugte image mit "docker run" 

was kann man zum start einen container für variablen mitgeben?
- volumes 
- env_vars
- ports

versuche lokal in deiner IDE ein neues projekt aufzusetzen und ein python hello world programm zu schreiben.
jetzt dieses directory beim start des container in den container mounten (volume)
und das python script im container ausführen. 

## Docker Image erweitern 
wenn das geklappt hat, erweite das dockerfile mit 
- ansible
- ssh (openssh-server) 

try to run das dockerfile auf diesen branch, wenn der bosch proxy einen auf gandalf you shall not pass macht
pull das image hier <ubuntu-ansible-image>


# 2. Ansible 

## Basics 
- was ist Ansible, wofür wird es gebraucht und wie verwendet man es 

todo 

## Ansible im Container 
run den ansible container von dem wir das image erstellt haben und mounte per volume wieder dein lokales directory 

führe den befehl "ansible-playbook" im container aus. 
wenn das klappt lese dich in ansible tasks ein und erstelle ein file oder directory per ansible in dem selben container. 

## Ansible Playbooks 
stop den ansible container 

1. erstelle ein docker network 
2. starte controller container
   - network 
   - volume - dein lokales dir 
   - name: controller 
3. target container
   - network 
   - name: target 

wie funktioniert ein docker network? 
finde die ip adressen der beiden container raus? 

versuche dich per ssh vom controller auf den target container zu verbinden 
ssh root password ist: password 
wenn das klappt versuche per ansible ein directory vom controller auf den target container zu erstellen. 

### ssh connection 
on controller 
bin/bash# ssh-keygen -t rsa -b 2048 -f ~/.ssh/id_rsa -N ""
bin/bash# ssh-copy-id -i ~/.ssh/id_rsa.pub root@<target-name>  
// password ist: password 
bin/bash# service ssh start 

on target 
bin/bash# service ssh start 

was passiert hier? 

now connect per ssh vom controller auf target
bin/bash# ssh root@<target-name> 

### ansible 
anstatt die ansible task auf localhost auszuführen
erstelle ein inventory directory in deinem ansible projekt in deiner ide 
was ist ein inventory?

erstelle ein test directory in deinem inventory und trage deinen target host ein,

jetzt versuche deine task zum erstellen eines directorys auf den target container auszuführen. 
// der aufbau ist in /ansible-automation ordner zur hilfe abgelegt. 

teste die inventorys aus und geniere unterschiedliche inventories und erstelle noch mehr target container 
vielleicht erweitere das ansible das es noch mehr macht als nur ein directory zu erstellen 
notiere deine ergebnisse 

weiter gehts auf dem branch 03-api 

# API Project
was ist eine API?

aufgabe programmiere eine simple REST API in einer beliebigen progammiersprache
und dockerisiere die application 

in /simple-api ist ein ganz einfaches Flask Beispiel 
aufpassen beim dockerisieren den port mit frei zu geben, 

# Observerbilty 
applicationen monitoren wir in der mfe mit dem LGTM (loki,grafana,tempo,mimir) stack 

## Prometheus 
was ist eine Metric?
was macht Prometheus? 

### hands on 
1. baue in die api einen Prometheus endpunkt mit ein um deine app zu monitoren 
2. starte prometheus als container und guck dir deine metriken im prometheus an 

## Grafana 
grafana ist die visualisierungs application für unterschiedliche data sourcen wie auch
prometheus 

### hands on 
1. pull und starte grafana als container 
2. verbinde die prometheus datasource mit grafana 
3. baue ein dashboard um die metriken der api anzeigen zu lassen 

## more 
logi - logs 
tempo - traces
können mit in diesem setup erweitert werden 


