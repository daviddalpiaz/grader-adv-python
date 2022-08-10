# grader-adv-python

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

These are set under the repository's `Secret` tab.

## Development notes

### Expectation Design

When designing the new code expectation features, the focus was on improving how differences are expressed to the end user.

We took inspiration from: 

- [`cpython/Lib/unittest/case.py`](https://github.com/python/cpython/blob/54ea127923eee1672fd67cc96a4a0b10961f52ed/Lib/unittest/case.py#L677)
- [`r-lib/testthat/R/expectation.R`](https://github.com/r-lib/testthat/blob/426eb523f6772c76175d6e8d7ca04355b1ee7ad5/R/expectation.R#L38)

Moreover, we referred to [3.3. Special Method Names]([https://docs.python.org/3/reference/datamodel.html#basic-customization](https://docs.python.org/3/reference/datamodel.html#special-method-names) for guidance on customizing Python classes.

### Re-create local test environment

To experiment with the class outside of the docker container, please setup the conda environment as described in `dev-grader.yml`. In shell, type:

```bash
conda env create -f dev-grader.yml
conda activate dev-grader
```

Once done, deactivate the environment with:

```bash
conda deactivate
```
