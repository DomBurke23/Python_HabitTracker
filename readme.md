To run this program in the terminal run 
python3 app.py 

This application is using Flask. 

Requirements:
1) make a python app that has a file which all other pages use as a baseline which includes a navigation bar.
in this python file i want a page which asks the user to input daily habits.
then show them habits on the page. 

2) add a page called calendar, which lists the habits against the days of the month , 
so we can tick green or cross with a red x if not done , 
include todays date on the page, 
do not allow the user to click the cells for future days of the month.  

Issues faced here:
I1) when adding a 2nd habit, the 2nd habit would appear in cell 1 under habit 1 so that we could not see any data(tick/cross icons) in habit 2 column. 
F1) The fix was commenting out the .habit-cell in the css 

3) I want to remove a habit and replace with another one. 
