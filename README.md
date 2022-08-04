# grader-dl

This repository contains a Docker image that is a modification of the [Python PrairieLearn grading image](https://github.com/PrairieLearn/PrairieLearn/tree/d4b18e0ca301eb98bd90764e5f90892cea3841a1/graders/python).

The main modifications relate to an improved set of feedback functions.

## Installation

Obtain a copy of the grader by using: 

```sh
docker pull prairielearn/prairielearn
docker pull jamesbalamuta/grader-adv-python
```

## Deployment to DockerHub 

To automate the deployment to DockerHub, the [`.github/workflows/docker-image.yml`](https://github.com/stat-prairielearn-uiuc/grader-adv-python/blob/main/.github/workflows/docker-image.yml#L25-L26) requires two secrets to be set:

```sh
DOCKERHUB_TOKEN
DOCKERHUB_USERNAME
```
