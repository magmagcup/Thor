# Thor: The God of Thunder  

<img width="200px" height="auto" src="static/game/icon.gif">

[![Build Status](https://travis-ci.com/magmagcup/Thor.svg?branch=develop)](https://travis-ci.com/magmagcup/Thor)
[![codecov](https://codecov.io/gh/magmagcup/thor/branch/develop/graph/badge.svg)](https://codecov.io/gh/magmagcup/thor) 

## Team members

| Name | Github
|:--|:--
|Anant Arayanant| [@MaquiaSA](https://github.com/MaquiaSA)
|Jitta Koopratoomsiri| [@jittaearn](https://github.com/jittaearn)
|Sirawich Direkwattanachai|[@magmagcup](https://github.com/magmagcup)
|Wikrom Chanthakhun|[@Champ2k](https://github.com/Champ2k)

## Project Description

Thor: The God of Thunder is an Education Game where players have to correctly answer a series of fill-in the blank questions in order to advance to the next planet(level). There are 10 planets in total and passing each planet is worth a specific amount of lighting points. There will be a time limit according to the question’s difficulty level for the player to come up with the answers. The player can view the hint of each question when place the cursor mouse in the answer box field.

## Requirements

The application requires

* Python 3.6.6 or newer
* Python add-on modules as in [requirements.txt](requirements.txt)

## Build Setup

### Step 1

Move to the directory you which to place the project folder. Then, type the following command in your Terminal shell:

git clone https://github.com/magmagcup/Thor.git

### Step 2

Go to the project directory "Thor" then type the following command:

On MacOS and Linux:

    . venv/bin/activate

    pip3 install -r requirements.txt

    python3 manage.py migrate

On Windows:

    /venv/bin/activate

    pip install -r requirements.txt

    python manage.py migrate

## How to Run

### Step 1

To run the server type the following command in the terminal.

On MacOS/Linux:

    python3 manage.py runserver --insecure

On Windows:

    python manage.py runserver --insecure

### Step 2

To enter the game site.

    http://127.0.0.1:8000/

## Developer Resources

* Iteration plans  in [project document](https://docs.google.com/document/d/1Q2PZyZD6GGjra6n8zBE4ohgaDXcAb8P__CwaxpWwbAs/edit#).  
* Task board  on [Trello](https://trello.com/b/5H0LhPUD/isp-series).
* Projects Proposal [here.](https://docs.google.com/document/d/1u56cPcZAjH7Zpv4XZvvtxiRkJ0TOCDOyWOA9pr01ESA/edit?usp=sharing)
* Code script/checklist [here.](https://docs.google.com/document/d/1rB76lxvoa3AoQ6cktqVeokeiMgrl03sMlR67-B2g_XM/edit?usp=sharing)
