# USD variation using Django + Celery + Nuxtjs in Docker Containers

## Introduction

This application show the variation of US Dollar in Chilean Pesos (CLP) in 2018 and 2019.

The service must get via API (https://mindicador.cl/api/dolar/dd-mm-YYYY), Dollar currency in CLP and calculate the difference between the current and previous day.

## Pre-requisites
* Docker
* Docker Compose

## Installation

For install this application, follow the next steps that are detailed below:

#### 1. Running the containers

We must write the following commands in terminal:

~~~
# cd into folder
cd dockerizing-django-celery-nuxt-app

# Create the images
docker-compose build

# Running the containers
docker-compose up -d
~~~

#### 2. Enjoy it!
Your app is ready to use!

## Usage

Django App: http://localhost:8000
Nuxtjs App: http://localhost:80
