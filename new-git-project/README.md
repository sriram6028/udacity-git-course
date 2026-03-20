# US Bikeshare Data Explorer (CLI)
This project uses **Python** to explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington.

# Description
A simple command-line tool to explore US bikeshare data for Chicago, New York City, and Washington.  
Filter by **city**, **month**, and **day of week** and view useful statistics:
- Most frequent times of travel
- Most popular stations and trip combinations
- Total and average trip duration
- User demographics (user types, gender, birth years*)

# Date created:
19-03-2026

# Files used
* `bikeshare.py`: The main Python script containing the logic.
* `new_york_city.csv`: Data for New York City (ignored by Git).

# Requirements
To run this project, you will need:
* Visual Studio code
* Github
* Python 3
* Pandas library
* NumPy library

# Task and Command Used
* Clone the repo:  			git clone https://github.com/sriram6028/udacity-git-course.git
* Create .gitignore: 			echo "*.csv" > .gitignore
* Add files:      			git add bikeshare.py .gitignore
* Commit changes: 			git commit -m "Initial commit: add script and ignore data"
* Create refactoring branch:	git branch refactoring
* Merge branch:           	git checkout main then git merge refactoring

# Features
* Interactive prompts (no command-line flags required)
* Fast stats with `pandas`
* Clean structure that’s easy to extend


# Credits:
https://github.com/udacity/post-your-work-project


