import urllib
from bs4 import BeautifulSoup
import json

fp = open('news_sports.html','r')
soup = BeautifulSoup(fp, 'html.parser')

match_dates = soup.findAll("div", {"class":"team_head_date"})
match_names = soup.findAll("div", {"class":"match-name"})
match_details = soup.findAll("div", {"class":"team_head_vs"})
match_venues = soup.findAll("div", {"class":"match-venue1"})
match_results = soup.findAll("span", {"class":"progess"})

data = {}
data['match_results'] = []

for i in range(0,len(match_dates)):
    data['match_results'].append({
        'match_date': match_dates[i].find('span').text,
        'match_name': match_names[i].find('span').text,
        'match_detail': match_details[i].find('span').text,
        'match_venue': match_venues[i].find('span').text,
        'match_result': match_results[i].find('span').text,
    })
    

with open('match_results.json', 'w') as outfile:  
    json.dump(data, outfile, indent=4)

with open('match_results.json', 'r') as infile:  
    data = json.load(infile)
    for p in data['match_results']:
        print('Match Date: ' + p['match_date'])
        print('Tour: ' + p['match_name'])
        print('Match name: ' + p['match_detail'])
        print('Venue: ' + p['match_venue'])
        print('Result: ' + p['match_result'])
        print('')