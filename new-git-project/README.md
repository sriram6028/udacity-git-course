# US Bikeshare Data Explorer (CLI)

A simple command-line tool to explore US bikeshare data for Chicago, New York City, and Washington.  
Filter by **city**, **month**, and **day of week** and view useful statistics:
- Most frequent times of travel
- Most popular stations and trip combinations
- Total and average trip duration
- User demographics (user types, gender, birth years*)

\* Some datasets may not include `Gender` and `Birth Year` (e.g., Washington). The code should handle this gracefully.

---

Task	Command Used
Clone the repo:  			git clone https://github.com/sriram6028/udacity-git-course.git
Create .gitignore: 			echo "*.csv" > .gitignore
Add files:      			git add bikeshare.py .gitignore
Commit changes: 			git commit -m "Initial commit: add script and ignore data"
Create refactoring branch:	git branch refactoring
Merge branch:           	git checkout main then git merge refactoring

## Features

- Interactive prompts (no command-line flags required)
- Fast stats with `pandas`
- Clean structure that’s easy to extend


##Credits:
https://github.com/udacity/post-your-work-project

##Date created:
19-03-2026
