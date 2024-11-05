# Openspace classifier challenge

## Remarks

This repository contains the final version of the first project I worked on during my AI and Data science bootcamp training at BeCode (Brussels, Belgium). While I am aware the code may not be optimal, keep in mind that the assignment for this project was due after only one and a half weeks of training and introduction to Python and Git/GitHub.

My contributions to this project are:
  - table.py : collaboration and contributions with Stef
  - openspace.py : full authorship
  - main.py : full authorship

The repository contains 2 branches
  - main : functional, but limited. (The program does not accept excel files containing more than 24 names)
  - Nice-to-haves : same as main, with added functionality. (More than 24 names, user interaction, ...)

This repository is a copy of the [original](https://github.com/StefVandekerckhove1/Project) I contributed to on Stef's profile.

## 1. Description

  Welcome to our openspace classifier!

  To get to know each other we developed a program that re-assigns everyday new seats to each colleague in an openspace of 6 tables with each 4 seats.

  The program contains the folder 'utils' with following files:

  - main.py:
    Main script which displays the final seat distribution in the openspace office.
  
  - openspace.py:
    Containing class object Openspace which randomly assigns colleagues to a free seat on a table and returns a plot with the seat distribution.
  
  - table.py:
    Containing class objects Table and Seat which give the number of free and occupied seats.
  
## 2. Installation

This program requires the installation of following packages:

- shapely v2.0.6
- geopandas v1.0.1
- pandas v2.2.3
- matplotlib v3.9.2

## 3. Usage

  How does the program work?
  
  The default setup of the open space is 6 tables of 4 seats (so 24 seats in total).
  
  - The program can take a filepath with an excel file as argument to load the list of colleagues.
    
  - The program distributes randomly the people on the existing tables and displays how much seats are left.
    
  - If the list of colleagues is longer than 24 participants, the program will ask if you want to add another table.

  - The program exports an excel file containing the seating plan.

  - After initial setup the program allows taking into account extra departures or arrivals.
    
  
## 4. Visuals

   ![The Office](https://imgix.bustle.com/uploads/image/2017/12/19/1b3f939e-752b-4d8b-80ba-b2384790f8ad-michael-scott-office.jpg?w=1020&h=574&fit=crop&crop=faces&auto=format&q=70)
  

## 5. Contributors
   
  - Kevin Potter
  - Stef Vandekerckhove

## 6. Timeline

| Thursday 24/10                                    | Friday 25/10                                             |
| ------------------------------------------------- | -------------------------------------------------------- |
| Preparation of repository                         | openspace.py (Openspace)                                 |
| table.py (Seat, Table)                            | README.md                                                |
| openspace.py (Openspace)                          |                                                          |

