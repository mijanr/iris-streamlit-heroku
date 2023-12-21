# iris-streamlit-heroku web app
This repository contains the code for a web app that uses a machine learning model to predict the species of an iris flower based on its sepal and petal measurements. The web app is built using [Streamlit](https://www.streamlit.io/) and is deployed on [Heroku](https://www.heroku.com/).

The web app can be accessed at: https://iris-streamlit-heroku-085ce6246a15.herokuapp.com/

### Commands to run the web app locally
To run and check fastapi back-end server: 
```
uvicorn main:app --reload
```
This will run the app on:
```
http://127.0.0.1:8000/
```
To run and check streamlit:
```
streamlit run app/app.py
```
This will run the app on:
```
http://localhost:8501/
```
FastAPI endpoints:
```
http://127.0.0.1:8000/docs
```
This will show the swagger UI for the API.

## Requirements
requirements.yml file contains the list of all the packages required to run the code in this repository. requirements.yml is generated using the following command:

```
conda env export --no-builds | grep -v "prefix" > requirements.yml
```
To create a conda environment using the requirements.yml file, run the following command:

```
conda env create -f requirements.yml
```