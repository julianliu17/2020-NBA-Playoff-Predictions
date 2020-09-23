# 2020 NBA Playoffs Prediction
**2020 NBA Playoffs winner and teams prediction based on regular season stats**

Playoff winner is decided based on number of playoff games won

1. Scraped 16 years of regular season stats and historic playoff wins from basketball-reference.com using python and beautifulsoup4
2. Performed Data Cleaning and Feature Engineering from scraped data
3. Exploratory Data Analysis
4. Executed Classification models (Logistic Regression, K-NN, Random Forest, SVC, Neural Network) to predict __*playoff teams*__ with highest accuracy = 100%
5. Executed Linear Regression models (Linear Regression, Lasso Regression, Neural Network) to predict __*playoff winner*__ with lowest RMSE = 4.26 games

This was my first ever data science project, and I wanted to do it on a topic I am enthusiastic about to keep me motivated. 2020 has been a crazy year, when the NBA returned from the bubble I was over the moon. This goal of this project was to predict the winner of the 2020 NBA Playoffs using regular season stats, but I quickly realised I could also build a model to predict which 16 teams would make the playoffs based on regular season stats. I scraped all of the data used in this project, feel free to download, edit and run *NBAScraper.py* on your terminal to scrape the stats you want to make your own predictions.

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

__Data__: https://www.basketball-reference.com/


## Web Scraping and Features Definition



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


