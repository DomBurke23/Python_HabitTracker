<div align="center">
    <p align="center">
    Dominiques Habit tracker.
    </p>
</div>

<!-- Table of Contents -->
<details>
    <summary>Table of Contents</summary>
    <ol>
        <li>
            <a href="#about-the-project">About the Project</a>
            <ul>
                <li>
                    <a href="#built-with">Built With</a>
                </li>
            </ul>
        </li>
        <li>
            <a href="#getting-started">Getting Started</a>
            <ul>
                <li>
                    <a href="#running-application">Running the application</a>
                </li>
            </ul>
        </li>
        <li>
            <a href="#requirements">Requirements</a>
        </li>
        <li>
            <a href="#designs">Designs</a>
        </li>
        <li>
            <a href="#issues-faced">Issues faced</a>
        </li>
        <li>
            <a href="#improvements-made">Improvements Made</a>
        </li>
    </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About the project
...

### Built with
The backend language used in this project is Python, with the Flask framework. The frontend uses HTML and CSS.

<!-- GETTING STARTED -->
## Getting Started 
...

### Running Application 
To run this program in the terminal run 
python3 app.py 

<!-- Requirements -->
## Requirements
1. I want a page which asks the user to input daily habits, then show them habits on the page. 
I chose to make a python app as this is a language I am not familiar with, html and css is what I am using with my client which I wanted to work on more. 

2. Split the pages so that we have a calendar view, which lists the habits against the days of the month. So, we can tick green or cross with a red x if not done , include todays date on the page, 
do not allow the user to mark off habits for future days of the month.  

3. Add a Login page using an sql database schema. If successful, redirect to the homepage, if unsuccessful, show error message. 

<!-- Designs -->
## Designs
...

<!-- Issues Faced -->
## Issues Faced / Improvments made 
1. With requirement 2, when adding a 2nd habit, the 2nd habit would appear in cell 1 under habit 1 so that we could not see any data(tick/cross icons) in habit 2 column. The fix was commenting out the .habit-cell in the css 

<!-- Improvements Made -->
## Improvements Made
2. While working on requirement 2, I wanted to include a navigation bar to swap between pages, I decided I wanted the navigation to be on everypage and instead of duplicating code I made a base file which can be imported on each page required. 