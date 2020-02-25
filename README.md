# SFIAProject-1

# Gaming shop database

## Index
[Brief](#brief)

[Architecture](#architecture)

[Deployment](#depl)

[Improvements for the Future](#improve)

[Authors](#auth)

[Acknowledgements](#ack)

<a name="brief"></a>
## The Brief

The goal of this project was to create an OOP-based web-app using flask and other tools that have been introduced during the training. There should be at least two tables with full CRUD functionality

### Solution

I have created a database for a games store to store customer information and information about games in order to ensure things are more organised

<a name="architecture"></a>
## Architecture

## Entity Relationship Diagram

### Initial Plan

![Initial ERD](/pictures/ERD_original.png)

Here is the original plan that will probably be implemented in further sprints. The database will contain two more tables with a relationship towards the Games table. However in order to achieve the MVP I decided to deliver a web-app that utilises three tables

### Delivered plan

![Delivered ERD](/pictures/ERD.png)

Here we can see the delivered ERD plan and the relationships between each tables, here its shows the one to many relationships for example many games can belong to a specific Genre.

<a name="depl"></a>
## Deployment

### Technology used

GCP - virtual environment and database

Flask - Python framework

Jenkins - Automation

Git - VCS

Trello - Project tracking

Python- Coding

<a name="improve"></a>
## Improvement for the Future

As of now the genre ID and game ID are what is being used to associate the tables with each other. Therefore to update the data like buyer ID and genre ID in the Games table. This means that the ID number of the games, genres and players must be known. I would like to change this in future sprints where the names can be used instead of IDs

I would also like to incorporate more tables into the web-app, that include a list of gaming companies and a list of platforms where the games are played and set up relationships between those tables and my currently existing tables.

A login system will be beneficial as this will increase the security of the system. It will ensure that only authorized personnel can operate the delete and update functions and helps prevent any theft of data. Along with this can be the introduction to admins and regular users that gives raise to different permissions and how each account type can interact with the app in different ways.

<a name="auth"></a>
## Authors

Philip Faboya

<a name="ack"></a>
## Acknowledgements

* QA consulting and the instructors
* My fellow colleagues in my class
