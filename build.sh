#!/bin/bash

IMAGE_NAME=$1

if [ -z $CI ]
then
    exit 1
fi

echo ---------------------------------------
echo Building image
echo ---------------------------------------

docker build -t $CI_REGISTRY_USER/$IMAGE_NAME:$TRAVIS_TAG ./azure-vote || exit 1

echo ---------------------------------------
echo Login to Dockerhub
echo ---------------------------------------

echo -n "$CI_REGISTRY_PASSWORD" | docker login --username $CI_REGISTRY_USER --password-stdin

echo ---------------------------------------
echo Pushing image to Dockerhub
echo ---------------------------------------

docker push $CI_REGISTRY_USER/$IMAGE_NAME:$TRAVIS_TAG || exit 1