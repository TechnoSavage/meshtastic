# Meshtastic projects
Scripts to use with Meshtastic radios

## Background

Requirements (Global)

- Python 3.8+
- pipenv - https://pypi.org/project/pipenv/
- meshtastic 2.2.17+

## Meshtastic API Docs

- Using the API - 
- Swagger Docs -

## Configuration Explained

- There is a sample environment variables file called .env_sample under the root folder of this project
- You will clone this file and create one called .env where you input your secrets and other configuration variables (API Keys, location information)
- Parameters - explanations of what you see in .env_sample

`OWM_KEY` - openweathermap.org API key for scripts that pull forecast infomation \
`LATITUDE` - 
`LONGITUDE` - 
`SERIAL_PORT` - 

## Getting Started

- Clone this repository

```
git clone https://github.com/TechnoSavage/foobar.git
```

- Clone .env_sample to .env under the same directory

```
cp .env_sample .env
```

- Update the necessary variables in the `.env` based on the script you'd like to run (NOTE: you need to rerun pipenv shell anytime you update these values to reload them)

- Install dependancies

```
pipenv install -r requirements.txt
```

- Enter pipenv

```
pipenv shell
```
