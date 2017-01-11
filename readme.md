#Project 6 - Data Visualization with D3

##Summary
The data set is taken from prosper.com which is a peer to peer lending company. The visualization is a scatter plot with each data point representing a loan. The visualization shows 3 variables related to each loan - 1) interest rate 2) borrower credit score 3) borrower employment status. Credit score and interest rate are shown using position on the x and y axis respectively and the audience can filter the employment status by clicking the buttons on the left side of the visualization to change the colouring of the data points. 

##Design
A scatter plot was chosen to give a rich sense of the number and distribution of data points while also communicating a trend in the data. Opacity and jitter were used to show the distribution of data points more clearly. Jitter was adjusted to be wide enough to be able to clearly see the density of data points, but not too wide to make the credit score variable look continuous which would be misleading. Only 2 colours were used to keep the graphic simple, but buttons were added so the user can interact with the data and filter by employment status. The x axis (credit score) starts at 400. It is typically bad practice to start a scale at a number other than 0, however credit score is an interval measure so the 0 point doesn't have a strong meaning. This makes it acceptable to start the scale at 400 without distorting the data and this was done to keep the bulk of the data points centered in the visualization. Orange was chosen as the main data point colour because it is light enough that it is possible to overlay another colour (like blue) over it. Blue was chosen as the overlay colour.

####Additions Made After Feedback 1
User 1 indicated that they were curious if "full-time" and "part-time" were a subset of the "employed" data set. Comments were added to the Employment Status portion of the visualization to clarify that each data point is associated with 1 and only 1 employment status. 
User 1 also indicated they wanted a simple way to clear the blue overlay colour without reloading the page. A clear button was added that provides this functionality.

####Additions Made After Feedback 2 and 3
Users 2 and 3 both didn't notice the "buttons" on the left side of the visualization at first. To make the buttons appear interactive, the text was center aligned, the edges of the buttons were rounded and a shadow effect was added when the mouse hovers over a button.
User 2 commented that the y axis wasn't clear (showing percentages as values between 0 and 1). To clarify the x axis, the percentages were changed to values between 0 and 100 and a % symbol was added in brackets after the y axis title.

##Feedback
####Feedback 1
What is the difference between ‘full-time’ and ‘employed’?
‘Full-time’ should be a subset of ‘employed’ but it doesn’t appear to be?
Self-employed looks like it might be a subset of ‘employed’.
Full time people appear to fall into 2 categories, poor credit where their interest rate is variable, and good credit where their interest rate is low.
Almost all employed people have a credit score above 600.
How do I deselect so that I can change all the dots back to regular colour?
Can I select multiple colours instead of just 2?
A majority of the data points are either full-time or employed.
Colour contrast is good, blue and orange are easy to see against each other.
I like that it is interactive.

####Feedback 2
Can't tell if interest rate is 25% or 25 basis points. Credit score is obvious. 
2 common interest rates at 35%, 30%.
Employed seems to be have good credit and low interest rates. 
Not-available employment status seems to have very low credit scores.
It would be interesting to see an additional visualization that shows how many people are in each employment category.
Align the x axis ticks to multiples of 20 (every 40).
Add additional colours for the groups.

####Feedback 3
Is each data point a loan?
Why are some areas darker than the rest?
I haven't seen a visual representation like this before. My experience is with fewer participants.
I see a clear distribution that doesn't have too many outliers.
The bulk of the data points is at the center.
The higher the credit score, the lower the loan interest rate.
Fewer people were willing to loan to anyone with a low credit score.
Self-employed people have many fewer loans. Self-employed people seem to be represented across the spectrum of credit scores.
Not-available employment status seemed to have low credit scores.
People who are employed seem to report that they are employed as opposed to report "Not-available".
There are few people in part time or retired employment status.


##Resources

http://www.w3schools.com/css/css3_buttons.asp
- used to make the button stylings more obvious
- used w3schools.com for several references on css styling

http://stackoverflow.com/questions/19713333/d3js-selection-and-class
- used several stackoverflow threads like this to sort out details of how to do specefic things in d3 




