#Predict 2020 NBA playoff winner
#Webscrape data from basketball reference
#Source code: https://towardsdatascience.com/web-scraping-nba-stats-4b4f8c525994
#Resource: https://www.basketball-reference.com/teams/

#Scraper
from bs4 import BeautifulSoup,Comment
import requests
import time
from itertools import repeat

years_to_scrape = 16	#Scrape 16 years because Hornets' last continuous data breaks at 2004

#Will first scrape ATL data, then use a for loop for the other 29 teams
teams = ['BOS','NJN','CHA','CHI','CLE','DAL','DEN','DET','GSW',
'HOU','IND','LAC','LAL','MEM','MIA','MIL','MIN','NOH','NYK','OKC','ORL',
'PHI','PHO','POR','SAC','SAS','TOR','UTA','WAS']

url1 = "https://www.basketball-reference.com/teams/ATL/"	#Franchise index
url2 = "https://www.basketball-reference.com/teams/ATL/stats_basic_totals.html"	#Year by year basic stats, 3pt% etc.

print("Scraping franchise data for ATL...(1 of 30)")
request1 = requests.get(url1)
time.sleep(2)
print("Scraping basic stats for ATL...(1 of 30)")
request2 = requests.get(url2)

soup1 = BeautifulSoup(request1.text,features='lxml')
soup2 = BeautifulSoup(request2.text,features='lxml')

features1 = [th.getText() for th in soup1.findAll('tr', limit=2)[0].findAll('th')]
features2 = [th.getText() for th in soup2.findAll('tr', limit=2)[0].findAll('th')]

rows1 = soup1.findAll('tr')[1:years_to_scrape+1]
rows2 = soup2.findAll('tr')[1:years_to_scrape+1]

stats1 = [[td.getText() for td in rows1[i].findAll('td')] for i in range(len(rows1))]
stats2 = [[td.getText() for td in rows2[i].findAll('td')] for i in range(len(rows2))]

seasons = [[th.getText() for th in rows2[i].findAll('th')] for i in range(len(rows2))]	#Should be the same for both stat page

for i in range(0,len(seasons)):	#Insert season column into first stat table
	season = seasons[i][0]
	stats1[i].insert(0,season)
	stats2[i].insert(0,season)

import pandas as pd
df1 = pd.DataFrame(stats1,columns=features1)
df2 = pd.DataFrame(stats2,columns=features2)

df1 = df1.drop('Lg',axis=1)
df2 = df2.drop('Lg',axis=1)

df = pd.merge(df1,df2,on='Season')

team_number = 2
for team in teams:
    url1 = f"https://www.basketball-reference.com/teams/{team}/"	#Franchise index
    url2 = f"https://www.basketball-reference.com/teams/{team}/stats_basic_totals.html"	#Year by year basic stats, 3pt% etc.

    print(f"Scraping franchise data for {team}...({team_number} of 30)")
    request1 = requests.get(url1)
    time.sleep(2)
    print(f"Scraping basic stats for {team}...({team_number} of 30)")
    request2 = requests.get(url2)
    team_number += 1

    soup1 = BeautifulSoup(request1.text,features='lxml')
    soup2 = BeautifulSoup(request2.text,features='lxml')

    features1 = [th.getText() for th in soup1.findAll('tr', limit=2)[0].findAll('th')]
    features2 = [th.getText() for th in soup2.findAll('tr', limit=2)[0].findAll('th')]

    rows1 = soup1.findAll('tr')[1:years_to_scrape+1]
    rows2 = soup2.findAll('tr')[1:years_to_scrape+1]

    stats1 = [[td.getText() for td in rows1[i].findAll('td')] for i in range(len(rows1))]
    stats2 = [[td.getText() for td in rows2[i].findAll('td')] for i in range(len(rows2))]

    seasons = [[th.getText() for th in rows2[i].findAll('th')] for i in range(len(rows2))]	#Should be the same for both stat page

    for i in range(0,len(seasons)):	#Insert season column into first stat table
    	season = seasons[i][0]
    	stats1[i].insert(0,season)
    	stats2[i].insert(0,season)
        
    df1_team = pd.DataFrame(stats1,columns=features1)
    df2_team = pd.DataFrame(stats2,columns=features2)
    df1_team = df1_team.drop('Lg',axis=1)
    df2_team = df2_team.drop('Lg',axis=1)
    df_team = pd.merge(df1_team,df2_team,on='Season')
    df = pd.concat([df,df_team],ignore_index=True)

print(df)
df.to_csv(r'C:\Users\Julian\Desktop\nba_data.csv',index=False, header=True)

#Scraping Playoffs Data
end_year = 2020
year_to_start_scrape = 2005
years = range(year_to_start_scrape,end_year)

team = []
wins = []
season = []
playoff_wins_data = {'Season':season,'Team':team,'Wins':wins}
df3 = pd.DataFrame(data=playoff_wins_data)
i=1
for year in years:
	url3 = f'https://www.basketball-reference.com/playoffs/NBA_{year}.html'
	print(f"Scraping playoffs data for {year}...({i} of {years_to_scrape-1})")
	i+=1
	request3 = requests.get(url3)
	time.sleep(2)
	soup3 = BeautifulSoup(request3.text,features='lxml')
	comments = soup3.findAll(id='all_misc')[0].findAll(string=lambda text: isinstance(text,Comment))[0]
	newsoup = BeautifulSoup(comments,'lxml')
	features3 = [th.getText() for th in newsoup.findAll('tr')[1].findAll('th')]
	featuresx = []
	featuresx.append(features3[0:4])

	playoff_win_features = featuresx[0]
	playoff_win_features.remove('G')
	playoff_win_features.remove('Rk')

	rows3 = newsoup.findAll('tr')[2:18]

	team = [rows3[i].findAll('td')[0].getText() for i in range(0,16)]
	wins = [rows3[i].findAll('td')[2].getText() for i in range(0,16)]
	
	season = []
	seasonstr = str(year-1)+'-'+str(year)[2:]
	season.extend([seasonstr for i in range(len(team))])

	playoff_wins_data = {'Season':season,'Team':team,'Wins':wins}

	df_year = pd.DataFrame(data=playoff_wins_data)
	df3 = pd.concat([df3,df_year],ignore_index=True)

print(df3)
df3.to_csv(r'C:\Users\Julian\Desktop\playoffs_data.csv',index=False, header=True)