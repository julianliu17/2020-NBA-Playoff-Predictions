![NBA Logo](https://github.com/julianliu17/2020-NBA-Playoff-Predictions/blob/master/Pictures/NBAlogo.png "NBA Logo")
# 2020 NBA Playoffs Prediction 
**2020 NBA Playoffs winner and teams prediction based on regular season stats**

Playoff winner is decided based on number of playoff games won

1. Scraped 16 years of regular season stats and historic playoff wins from basketball-reference.com using python and beautifulsoup4
2. Performed Data Cleaning and Feature Engineering from scraped data
3. Exploratory Data Analysis
4. Executed Classification models (Logistic Regression, K-NN, Random Forest, SVC, Neural Network) to predict __*playoff teams*__ with highest accuracy = 100%
5. Executed Linear Regression models (Linear Regression, Lasso Regression, Neural Network) to predict __*playoff winner*__ with lowest RMSE = 4.26 games

This was my first ever data science project, and I wanted to do it on a topic I am enthusiastic about to keep me motivated. 2020 has been a crazy year, when the NBA returned at the bubble I was over the moon. The goal of this project was to predict the winner of the 2020 NBA Playoffs using regular season stats, but I quickly realised I could also build a model to predict which 16 teams would make the playoffs based on regular season stats. I scraped all of the data used in this project, feel free to download, edit and run *NBAScraper.py* on your terminal to scrape the stats you want to make your own predictions.

## File Descriptions
NBAPredictions.ipynb - *Jupyter Notebook with data cleaning, feature engineering, EDA as well as classification and linear regression models.*

NBAScraper.py - *Python file that can be run on your terminal with `C:\path> python NBAScraper.py`, saves nba_data.csv and playoffs_data.csv to desktop.*

nba_data.csv - *16 years of regular season stats for all 30 NBA teams.*

playoffs_data.csv - *Historic playoff wins from seasons 2004-05 to 2018-19 for playoff teams from each season.* 

my_dl_model.h5 - *Deep Learning model for predicting playoff winner.*

my_dlc_model.h5 - *Deep Learning model for predicting playoff teams.*

IMPORTANT: Change path code in *NBAScraper.py* for saving to your own computer and desired path.

## Resources Used
__Python Version__: 3.8

__Packages__: pandas, numpy, matplotlib, seaborn, beautifulsoup, tensorflow

__Data Source__: https://www.basketball-reference.com/
## Web Scraping and Features Definition
These are the features that were scraped and their definitions:
  * __Season__ - *NBA Season denoted "yyyy-yy", eg. "2008-09"*
  * __Team__ - *Full team name, eg. "Golden State Warriors"*
  * __Tm__ - *Team name abbreviation, eg. "GSW"*
  * __W__ - *Total number of wins in a season*
  * __L__ - *Total number of losses in a season*
  * __W/L%__ - *Win-Loss percentage, calculated by wins/total games played in a season*
  * __Finish__ - *Regular season finish by division*
  * __SRS__ - *Simple Rating System, a rating system that takes into account average point differential and strength of schedule. SRS = 0 = average*
  * __Pace__ - *Estimate of possesions per 48 mins*
  * __Rel Pace__ - *Team's possessions per 48 mins relative to the league*
  * __ORtg__ - *Offensive rating, estimate of points scored per 48 mins*
  * __Rel ORtg__ - *Team's offensive rating relative to the league*
  * __DRtg__ - *Defensive rating, estimate of points allowed per 48 mins*
  * __Rel DRtg__ - *Team's defensive rating relative to the league*
  * __Playoffs__ - *Description of playoff status, eg. "Lost W. Div. Semis" or "Won Finals"*
  * __Coaches__ - *Name of coach/coaches*
  * __Top WS__ - *Highest win share generator during the regular season, eg. "K. Bryant (8.1)"*
  * __Age__ - *Average player age*
  * __Ht.__ - *Average player height*
  * __Wt.__ - *Average player weight*
  * __G__ - *Games played in a season*
  * __MP__ - *Minutes played in a season*
  * __FG__ - *Field goals made in a season*
  * __FGA__ - *Field goal attempts in a season*
  * __FG%__ - *Field goal percentage in a season*
  * __3P__ - *3 points made in a season*
  * __3PA__ - *3 point attempts in a season*
  * __3P%__ - *3 point percentage in a season*
  * __2P__ - *2 points made in a season*
  * __2PA__ - *2 point attempts in a season*
  * __2P%__ - *2 point percentage in a season*
  * __FT__ - *Free throws made in a season*
  * __FTA__ - *Free throw attempts in a season*
  * __FT%__ - *Free throw percentage in a season*
  * __ORB__ - *Total offensive rebounds in a season*
  * __DRB__ - *Total defensive rebounds in a season*
  * __TRB__ - *Total rebounds in a season*
  * __AST__ - *Total assists in a season*
  * __STL__ - *Total steals in a season*
  * __BLK__ - *Total blocks in a season*
  * __TOV__ - *Total turnovers in a season*
  * __PF__ - *Total personal fouls in a season*
  * __PTS__ - *Total points scored in a season*
  * __Playoff Wins__ - *Number of playoff wins, 16 is the maximum and implies the team won the playoffs

To get the csv file for these features simply change the code `df.to_csv(r'C:\YOUR PATH\nba_data.csv',index=False, header=True)` and `df3.to_csv(r'C:\YOUR PATH\playoffs_data.csv',index=False, header=True)` in the NBAScraper.py file. When you run `python NBAScraper.py` you should get something like this.

![Scraping Demo](https://github.com/julianliu17/2020-NBA-Playoff-Predictions/blob/master/Pictures/ScrapingDemo.JPG "Scraping Demo")

## Data Cleaning and Feature Engineering

## EDA

## Model Building

## Model Performance
For the classification problem, the neural network 17/8/1 model had a perfect 100% accuracy on test set (2019-20 season), closely followed by the random forest model with 97% accuracy.

  * Neural Network 17/8/1 accuracy = 100%
  * Random Forest accuracy = 97%
  * SVC accuracy = 93%
  * Logistic Regression accuracy = 93%
  * K-NN (n=8) accuracy = 90%

For the linear regression problem, all the models had very similar RMSE, but the neural network 18/18/18/1 model had the lowest RMSE.

  * Neural Network 18/18/18/1 RMSE = 4.26
  * Linear Regression RMSE = 4.32
  * Lasso Regression RMSE = 4.34

## Project Evaluation
For our linear regression problem, I would say that such a small improvement in RMSE cannot justify the need for using a deep learning model. There was also a problem with training size for this problem, since there are only 16 teams who makes the playoffs every season, our initial 16 years worth of data was basically cut in half.

