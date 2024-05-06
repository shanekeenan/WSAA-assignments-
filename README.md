# Web services and applications (WSAA) coursework
Assignments and lab python code for Web services and applications (WSAA) module with lecturer Andrew Beatty 

Semester 2, Higher Diploma in Science in Data Analytics at ATU, Galway, 2023/24. 

Author: Shane Keenan 


## About 

This repository contains assignments  - 

1. assignments - contains code for weekly assignments 
    - currentweather.py   (Week 2 - Topic02 Representing Data)
    - assignment03-cso.py (Week 4 - Topic 04 Reading apis in the wild)
    - assignment04-github.py    (Week 5 - Topic 05 Authentication) 


## Running the code 

steps to create:  

1. Install Anaconda 
2. Install visual studio code 
3. create a github account 
4. create public repository "WSAA-coursework" with README.md and .gitignore file
5. Sign into github using VScode 
6. Clone repository to PC 
7. Create necesary folders and files
8. Commit all and push to repo 

## Required python packages

``import requests``
``import json``
``from github import Github``


### fine-grained token to access repo /shanekeenan/aprivate stored in config.py file.  
``from config import apikeys as cfg``


# Topic02 Representing Data

Assignment
Using the URL below
https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=temperature_2m
Write a python program called currentweather.py that will print out the current temperature on the console (and only the temperature)
I have set the lat/long to my location, you may use that or a different location.
Last few marks:
Look at the documentation (below) and print out the current wind direction (10m) as well.
🌤️ Free Open-Source Weather API | Open-Meteo.com

Status: complete 
Date: 17/02/2024


# Topic03 Data Transfer

Assignment 
Quiz - HTTP and URLs 
Status: complete - 100 % yeah !  
Date: 23/02/2024


# Assignment 3 from Topic 04 Reading apis in the wild

Write a program that retrieves the dataset for the "exchequer account (historical series)" from the CSO, and stores it into a file called "cso.json".
Upload this program to the same repository you used for the XML assignment
Save this assignment as "assignment03-cso.py"
This program should not be a long one
I don't need you to reformat or analyse the data in any way
It should be about 10ish lines long (I have not counted)
You will need to find the dataset in CSO.ie, try economic and then finance, then finance indicators. yes it is difficult to find, that is part of the task, actually the easiest way to find it is search for it.

Status: complete 
Date: 18/03/2024


# Assignment 04 from Topic 05 Authentication

Write a program in python that will read a file from a repository, 
The program should then replace all the instances of the text "Andrew" with your name. 
The program should then commit those changes and push the file back to the repository (You will need authorisation to do this).
I do not need to see your keys (see lab2, to follow)
Handup: Push the program as assignment04-github.py to assignments repository.
Marks: Marks will be given for the functionality and layout of the code; I do expect minimal comments to indicate you know what the program is doing.

Status: complete 
Date: 03/05/2024


# TOPIC 06 Creating your own API with FLASK

Assignment 
Quiz - Virtual environments and FLask
Dtatus: complete - 8.67/10   
Date: 06/05/2024


