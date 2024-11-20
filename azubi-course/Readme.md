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
wenn das klappt versuche per ansible ein directory vom controller auf den target container zu erstellen. 

- wenn du nicht weiter kommst oder fertig bist switche zu branch 02-ansible-2 

