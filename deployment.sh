#!/bin/bash

applicationBase="edu"
containerName="${applicationBase}-container"
imageName="${applicationBase}:latest"

applicationPort=8000
dockerContainerPort=8000

docker stop $containerName || true
docker rm $containerName || true
docker rmi $imageName || true

sudo docker build -t $imageName .

sudo docker run --restart unless-stopped -p $dockerContainerPort:$applicationPort --name $containerName $imageName
