![NBA Logo](https://github.com/julianliu17/2020-NBA-Playoff-Predictions/blob/master/Pictures/NBAlogo.png "NBA Logo")
# 2020 NBA Playoffs Prediction 
**2020 NBA Playoffs winner and teams prediction based on regular season stats**

*Note: Playoff winner is decided based on number of playoff games won*

1. Scraped 16 years of regular season stats and historic playoff wins from basketball-reference.com using python and beautifulsoup4
2. Performed Data Cleaning and Feature Engineering from scraped data
3. Exploratory Data Analysis
4. Executed Classification models (Logistic Regression, K-NN, Random Forest, SVC, Neural Network) to predict __*playoff teams*__ with highest accuracy = 100%
5. Executed Linear Regression models (Linear Regression, Lasso Regression, Neural Network) to predict __*playoff winner*__ with lowest RMSE = 4.26 games

This was my first ever data science project, and I wanted to do it on a topic I am enthusiastic about. 2020 has been a crazy year, when the NBA returned at the bubble I was over the moon. The goal of this project was to predict the winner of the 2020 NBA Playoffs using regular season stats, but I quickly realised I could also build a model to predict which 16 teams would make the playoffs based on regular season stats. I scraped all of the data used in this project, feel free to download, edit and run *NBAScraper.py* on your terminal to scrape the stats you want to make your own predictions.

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
After scraping the data, I ended up with 2 csv files which I needed to merge and clean so that it was usable for our models. I made the following changes and created the following varaibles:
  * Removed asteriks from some Team names on nba_data dataframe, then merged the 2 tables on columns Season and Team
  * Renamed Wins to Playoff Wins to avoid confusion with regular season wins
  * Dropped unnecessary (in my opinion) columns such as MP, Finish, Coaches, Tm and repeated columns on both dataframes
  * Converted Playoff columns to Make Playoffs which returned 0s and 1s instead of a description of playoff status, teams that did not make the playoffs did not have a description in the Playoff column
  * Converted na values in Playoff Wins to 0
  * Converted average player heights from foot inches to cm, eg. '6-6' to 198.12
  * Dropped 2PA, 3PA, FGA and FTA since they could be calculated backwards using 2P and 2P% for example
  * Dropped ORtg, DRtg and Pace since on its own they don't mean anything unless compared with the rest of the league, which we already have in the dataframe as Rel ORtg, Rel DRtg and Rel Pace
  * Dropped W and L, since W/L% is calculated using W so both W and L will be strongly correlated to W/L% and to each other
  * Converted stats to per game stats, because the number of games played each season is different (games were cut short in 2020 because of COVID, but I found that in other seasons there also have been cases where not all 82 games were played), eg. 2P is now converted to 2P/gm
  * Dropped G column after using number of games to convert stats to per game stats
  * After plotting heatmap of correlations, dropped features SRS and PTS/gm as SRS was strongly correlated to W/L% and PTS/gm to FG/gm
  * Dropped weakly correlated features to both Make Playoffs __and__ Playoff Wins, FT/gm, 2P/gm, FT%, Wt., Ht., Rel Pace
  * I also split my dataframe into 2019-20 season (target_season) and the remaining seasons (df)
  * Dropped columns Season and Team as they are of no use anymore after splitting dataframe into 2
  * Before bulding models and after EDA, I decided to remove W/L% when building my classification models, becuase this project is trying to predict whether a team makes the playoffs based on regular season stats, but W/L% will too easily pick out the top teams

*EDA and model building was performed on df, target_season was used as a test set to predict our final results. The tables and their info() is shown below.*

![df info](https://github.com/julianliu17/2020-NBA-Playoff-Predictions/blob/master/Pictures/Cleaned_df.JPG "df info")
![df target season](https://github.com/julianliu17/2020-NBA-Playoff-Predictions/blob/master/Pictures/Cleaned_target.JPG "df target season")

![df pt1](https://github.com/julianliu17/2020-NBA-Playoff-Predictions/blob/master/Pictures/Cleaned_df_table_pt1.JPG "df pt1")![df pt2](https://github.com/julianliu17/2020-NBA-Playoff-Predictions/blob/master/Pictures/Cleaned_df_table_pt2.JPG "df pt2")
## EDA
I looked at the heatmap and distributions of the data for all of the variables. 

Below are the visualizations I plotted for all features against playoff wins.

![heatmap](https://github.com/julianliu17/2020-NBA-Playoff-Predictions/blob/master/Pictures/Heatmap.JPG "heatmap")

![dist pt1](https://github.com/julianliu17/2020-NBA-Playoff-Predictions/blob/master/Pictures/Dist_pt1.JPG "dist pt1")

![dist pt2](https://github.com/julianliu17/2020-NBA-Playoff-Predictions/blob/master/Pictures/Dist_pt2.JPG "dist pt2")

![dist pt3](https://github.com/julianliu17/2020-NBA-Playoff-Predictions/blob/master/Pictures/Dist_pt3.JPG "dist pt3")

![W/L](https://github.com/julianliu17/2020-NBA-Playoff-Predictions/blob/master/Pictures/W_L.JPG "W/L")

![fairly correlated](https://github.com/julianliu17/2020-NBA-Playoff-Predictions/blob/master/Pictures/Fairly_correlated.JPG "fairly correlated")

![fairly correlated pt2](https://github.com/julianliu17/2020-NBA-Playoff-Predictions/blob/master/Pictures/Fairly_correlated_pt2.JPG "fairly correlated pt2")

![weakly correlated](https://github.com/julianliu17/2020-NBA-Playoff-Predictions/blob/master/Pictures/Weakly_correlated.JPG "weakly correlated")
## Model Building
### Predicting which teams will make the 2020 Playoffs
This was a classification problem and I decided to adopt the following models: Logistic Regression, K-NN, Random Forest, SVC and ANN. As mentioned before, I decided to drop the W/L% column for this problem. First, I split the data into train and validation sets with a test size of 30%. I scaled my X_train values with MinMaxScaler and fitted the scaler on X_test and target_X values. I also tried using a StandardScaler but the models predicted all ones (make playoffs).

I evaluated my models with classification report and confusion matrix, before using the models on the test set of the 2019-20 season, the final test set predictions were also evaluated with classification report and confusion matrix, since there is already data on which teams made the playoffs this season. 

__Logistic Regression__ - Started off with max_iter = 300 and increased it to 1000, but found no improvement

__K-NN__ - I used the elbow method to search for the k value that returned the minimum error rate, as shown in the plot below. I chose 8 becuase it gave the same error rates as 9,10 or 12 and to speed up the model.
![elbow method](https://github.com/julianliu17/2020-NBA-Playoff-Predictions/blob/master/Pictures/K-NN.JPG "elbow method")

__Random Forest__ - Started off with n_estimators = 200 and increased it to 1000, accuracy improved from 83% to 84%, wasn't enough to justify slowing the model down so I decided to stick with 200

__SVC__ - Performed GridSearchCV to find best parameters

__Neural Network__ - Systematically tested out different layers and nodes, found the best combination was 17/8/1 with a dropout layer (0.5) in between each layer. Implemented early stopping to prevent overfitting.
![dlccode](https://github.com/julianliu17/2020-NBA-Playoff-Predictions/blob/master/Pictures/dlc_code.JPG "dlc code")![dlcloss](https://github.com/julianliu17/2020-NBA-Playoff-Predictions/blob/master/Pictures/dlc_loss.JPG "dlc loss")
### Predicting the winner of the 2020 Playoffs
This was a linear regression problem and I decided to adopt the following models: Linear Regression (OLS), Lasso Regression and ANN. This time the features included W/L%. Again, I first split the data into train and validation sets with a test size of 30%. I did not scale my X values because I found that it was not needed and doing so caused an error.

__Ordinary Least Squares (OLS)__ - When I started off with the OLS linear regression model, I realised that I should remove all the data which didn't make the playoffs, as including it gave me a large MAE at playoff wins = 0. The resulting plot still wasn't a straight a line I'd hoped for. I tried removing weakly correlated features but that did not help so I decided to keep those in the model.

__Lasso Regression__ - The Lasso Regression performed marginally better than the OLS model, RMSE = 4.34 compared to RMSE = 4.36

__Neural Network__ - Systematically tested out different layers and nodes, found the best combination was 18/18/18/1 with a dropout layer (0.5) before the output layer. Implemented early stopping to prevent overfitting. The ANN model was the only model that predicted positive playoff wins for all teams that actually made the 2020 playoffs.
![dlcode](https://github.com/julianliu17/2020-NBA-Playoff-Predictions/blob/master/Pictures/dl_code.JPG "dl code")![dlloss](https://github.com/julianliu17/2020-NBA-Playoff-Predictions/blob/master/Pictures/dl_loss.JPG "dl loss")

When a team wins the playoffs they have to win 16 games, but none of our models predicted 16 games. So I decided to use the playoff wins predicted by the models to calculate the win probability by dividing playoff wins by 16 (there's probably a better way to do this, but this is what I chose to go with). There were also negative playoff wins predicted by the models so I set them all to 0. 

Our final predictions for the 2020 NBA Playoffs by the ANN model is shown below:

![final predictions](https://github.com/julianliu17/2020-NBA-Playoff-Predictions/blob/master/Pictures/final_predictions.JPG "final predictions")

All the models have predicted the same top 5 teams most likely to win the playoffs:
1. Milwaukee Bucks
2. Los Angeles Lakers
3. Toronto Raptors
4. Los Angeles Clippers
5. Utah Jazz

Well, only the Lakers remain in this top 5 predicted by the models. Maybe teams don't take the regular season all that seriously after all...
## Model Performance
For the classification problem, the neural network 17/8/1 model had a perfect 100% accuracy on test set (2019-20 season), closely followed by the random forest model with 97% accuracy.

  * __Neural Network 17/8/1__ accuracy = 100%
  * __Random Forest__ accuracy = 97%
  * __SVC__ accuracy = 93%
  * __Logistic Regression__ accuracy = 93%
  * __K-NN__ accuracy = 90%

For the linear regression problem, all the models had very similar RMSE, but the neural network 18/18/18/1 model had the lowest RMSE and the only model that predicted positive playoff wins for all teams that made the playoffs.

  * __Neural Network 18/18/18/1__ RMSE = 4.26
  * __Lasso Regression__ RMSE = 4.34
  * __Linear Regression__ RMSE = 4.36
## Project Evaluation
For our linear regression problem, I would say that such a small improvement in RMSE alone cannot justify the need for using a deep learning model but because it was the only model that predicted positive number of playoff wins for all teams that actually made the 2020 playoffs, the best model for our linear regression problem was the ANN model. There was also a problem with training size for this problem, since there are only 16 teams who makes the playoffs every season, our initial 16 years worth of data was basically cut in half. Another problem is that our features did not have a very strong correlation with the number of playoff wins, which also hurt our models' performance. If I were to do this project again I would definitely look for features more strongly correlated to the number of playoff wins. I definitely could also adopt other models such as random forest regression and ridge regression.

Nevertheless, our classification models performed reasonably well with our ANN model performing with an accuracy of 100% on our test set.

The goal of this project was met, which was to predict the winner of the 2020 playoffs. Although the models all predicted for the Bucks to win this year while they surprisingly already got knocked out by the Miami Heat, our runner-up prediction of the Lakers are still in the playoffs with a 2-1 lead on the Nuggets. 

Will the Lakers really win it this year? 

I hope not. Go Nuggets!

