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








