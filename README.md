# iris-streamlit-heroku web app
This repository contains the code for a web app that uses a machine learning model to predict the species of an iris flower based on its sepal and petal measurements. The web app is built using [Streamlit](https://www.streamlit.io/) and is deployed on [Heroku](https://www.heroku.com/).

The web app can be accessed at: https://iris-streamlit-heroku-085ce6246a15.herokuapp.com/

## Requirements
requirements.yml file contains the list of all the packages required to run the code in this repository. requirements.yml is generated using the following command:

```
conda env export --no-builds | grep -v "prefix" > requirements.yml
```
To create a conda environment using the requirements.yml file, run the following command:

```
conda env create -f requirements.yml
```