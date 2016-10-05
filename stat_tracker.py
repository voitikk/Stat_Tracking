import csv
import requests
import sys
import webbrowser
from bs4 import BeautifulSoup
from array import array

print("Wait until finished...")
print("Ignore the following error\n\n\n")
with open('HC_Summer_Stats.csv', 'w') as csvfile:
    fieldnames = ['First', 'Last', 'Team', 'Pos', 'Avg', 'G', 'AB', 'R', 'H', '2B', '3B', 'HR', 'RBI', 'BB', 'HBP', 'SO']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    
    #Travis Cloney
    url = 'http://pgcbl.bbstats.pointstreak.com/team_stats.html?teamid=90390&seasonid=30255'
    response = requests.get(url)
    html = response.content
    bs = BeautifulSoup(html)
    possible_links = bs.findAll('a')
    for link in possible_links:
        if link.get('href') == 'player.html?playerid=993044&seasonid=30255':
            nex = link.findNext('td')
            position = nex.text
            nex = nex.findNext('td')
            average = nex.text
            nex = nex.findNext('td')
            games = nex.text
            nex = nex.findNext('td')
            atbats = nex.text
            nex = nex.findNext('td')
            runs = nex.text
            nex = nex.findNext('td')
            hits = nex.text
            nex = nex.findNext('td')
            doubles = nex.text
            nex = nex.findNext('td')
            triples = nex.text
            nex = nex.findNext('td')
            homeruns = nex.text
            nex = nex.findNext('td')
            rbis = nex.text
            nex = nex.findNext('td')
            walks = nex.text
            nex = nex.findNext('td')
            hbp = nex.text
            nex = nex.findNext('td')
            strikeouts = nex.text
            writer.writerow({'First': 'Travis', 'Last': 'Cloney', 'Team': 'Newark Pilots', 'Pos': position, 'Avg': average, 'G': games, 'AB': atbats, 'R': runs, 'H': hits, '2B': doubles, '3B': triples, 'HR': homeruns, 'RBI': rbis, 'BB': walks, 'HBP': hbp, 'SO': strikeouts})  
    
    #Devin McGrath 
    url = 'http://sunsbb.bbstats.pointstreak.com/team_stats.html?teamid=69161'
    response = requests.get(url)
    html = response.content
    bs = BeautifulSoup(html)
    possible_links = bs.findAll('a')
    for link in possible_links:
        if link.get('href') == 'player.html?playerid=975963&seasonid=30012':
            nex = link.findNext('td')
            position = nex.text
            nex = nex.findNext('td')
            average = nex.text
            nex = nex.findNext('td')
            games = nex.text
            nex = nex.findNext('td')
            atbats = nex.text
            nex = nex.findNext('td')
            runs = nex.text
            nex = nex.findNext('td')
            hits = nex.text
            nex = nex.findNext('td')
            doubles = nex.text
            nex = nex.findNext('td')
            triples = nex.text
            nex = nex.findNext('td')
            homeruns = nex.text
            nex = nex.findNext('td')
            rbis = nex.text
            nex = nex.findNext('td')
            walks = nex.text
            nex = nex.findNext('td')
            hbp = nex.text
            nex = nex.findNext('td')
            strikeouts = nex.text
            writer.writerow({'First': 'Devin', 'Last': 'McGrath', 'Team': 'Pittsfield Suns','Pos': position, 'Avg': average, 'G': games, 'AB': atbats, 'R': runs, 'H': hits, '2B': doubles, '3B': triples, 'HR': homeruns, 'RBI': rbis, 'BB': walks, 'HBP': hbp, 'SO': strikeouts})  

    #Josh Hassell
    url = 'http://www.400hitter.com/team.asp?TmID=564&SeID=270&CtID=0&pt=b'
    response = requests.get(url)
    html = response.content
    bs = BeautifulSoup(html)
    possible_links = bs.findAll('a')
    for link in possible_links:
        if link.get('href') == 'player.asp?PlID=27610&SeID=270&TmID=564&CtID=0&pt=b':
            nex = link.findNext('td')
            games = nex.text
            nex = nex.findNext('td')
            atbats = nex.text
            nex = nex.findNext('td')
            runs = nex.text
            nex = nex.findNext('td')
            hits = nex.text
            nex = nex.findNext('td')
            doubles = nex.text
            nex = nex.findNext('td')
            triples = nex.text
            nex = nex.findNext('td')
            homeruns = nex.text
            nex = nex.findNext('td')
            rbis = nex.text
            nex = nex.findNext('td')
            walks = nex.text
            nex = nex.findNext('td')
            strikeouts = nex.text
            nex = nex.findNext('td')
            nex = nex.findNext('td')
            nex = nex.findNext('td')
            average = nex.text
            nex = nex.findNext('td')
            nex = nex.findNext('td')
            hbp = nex.text
            writer.writerow({'First': 'Josh', 'Last': 'Hassell', 'Team': 'Lexington Blue Sox','Pos': position, 'Avg': average, 'G': games, 'AB': atbats, 'R': runs, 'H': hits, '2B': doubles, '3B': triples, 'HR': homeruns, 'RBI': rbis, 'BB': walks, 'HBP': hbp, 'SO': strikeouts})  

    
    #Alex Gionis
    url = 'http://pgcbl.bbstats.pointstreak.com/team_stats.html?teamid=112015&seasonid=30255'
    response = requests.get(url)
    html = response.content
    bs = BeautifulSoup(html)
    possible_links = bs.findAll('a')
    for link in possible_links:
        if link.get('href') == 'player.html?playerid=995693&seasonid=30255':
            nex = link.findNext('td')
            position = nex.text
            nex = nex.findNext('td')
            average = nex.text
            nex = nex.findNext('td')
            games = nex.text
            nex = nex.findNext('td')
            atbats = nex.text
            nex = nex.findNext('td')
            runs = nex.text
            nex = nex.findNext('td')
            hits = nex.text
            nex = nex.findNext('td')
            doubles = nex.text
            nex = nex.findNext('td')
            triples = nex.text
            nex = nex.findNext('td')
            homeruns = nex.text
            nex = nex.findNext('td')
            rbis = nex.text
            nex = nex.findNext('td')
            walks = nex.text
            nex = nex.findNext('td')
            hbp = nex.text
            nex = nex.findNext('td')
            strikeouts = nex.text
            writer.writerow({'First': 'Alex', 'Last': 'Gionis', 'Team': 'Geneva Red Wings','Pos': position, 'Avg': average, 'G': games, 'AB': atbats, 'R': runs, 'H': hits, '2B': doubles, '3B': triples, 'HR': homeruns, 'RBI': rbis, 'BB': walks, 'HBP': hbp, 'SO': strikeouts})

    #Bill Schlich
    url = 'http://hcbl.bbstats.pointstreak.com/team_stats.html?teamid=109121&seasonid=29816'
    response = requests.get(url)
    html = response.content
    bs = BeautifulSoup(html)
    possible_links = bs.findAll('a')
    for link in possible_links:
        if link.get('href') == 'player.html?playerid=973409&seasonid=29816':
            nex = link.findNext('td')
            position = nex.text
            nex = nex.findNext('td')
            average = nex.text
            nex = nex.findNext('td')
            games = nex.text
            nex = nex.findNext('td')
            atbats = nex.text
            nex = nex.findNext('td')
            runs = nex.text
            nex = nex.findNext('td')
            hits = nex.text
            nex = nex.findNext('td')
            doubles = nex.text
            nex = nex.findNext('td')
            triples = nex.text
            nex = nex.findNext('td')
            homeruns = nex.text
            nex = nex.findNext('td')
            rbis = nex.text
            nex = nex.findNext('td')
            walks = nex.text
            nex = nex.findNext('td')
            hbp = nex.text
            nex = nex.findNext('td')
            strikeouts = nex.text
            writer.writerow({'First': 'Bill', 'Last': 'Schlich', 'Team': 'Southampton Breakers','Pos': position, 'Avg': average, 'G': games, 'AB': atbats, 'R': runs, 'H': hits, '2B': doubles, '3B': triples, 'HR': homeruns, 'RBI': rbis, 'BB': walks, 'HBP': hbp, 'SO': strikeouts})  

    #Thomas Russo
    url = 'http://www.400hitter.com/team.asp?TmID=564&SeID=270&CtID=0&pt=b'
    response = requests.get(url)
    html = response.content
    bs = BeautifulSoup(html)
    possible_links = bs.findAll('a')
    for link in possible_links:
        if link.get('href') == 'player.asp?PlID=27608&SeID=270&TmID=564&CtID=0&pt=b':
            nex = link.findNext('td')
            games = nex.text
            nex = nex.findNext('td')
            atbats = nex.text
            nex = nex.findNext('td')
            runs = nex.text
            nex = nex.findNext('td')
            hits = nex.text
            nex = nex.findNext('td')
            doubles = nex.text
            nex = nex.findNext('td')
            triples = nex.text
            nex = nex.findNext('td')
            homeruns = nex.text
            nex = nex.findNext('td')
            rbis = nex.text
            nex = nex.findNext('td')
            walks = nex.text
            nex = nex.findNext('td')
            strikeouts = nex.text
            nex = nex.findNext('td')
            nex = nex.findNext('td')
            nex = nex.findNext('td')
            average = nex.text
            nex = nex.findNext('td')
            nex = nex.findNext('td')
            hbp = nex.text
            writer.writerow({'First': 'Thomas', 'Last': 'Russo', 'Team': 'Lexington Blue Sox','Pos': position, 'Avg': average, 'G': games, 'AB': atbats, 'R': runs, 'H': hits, '2B': doubles, '3B': triples, 'HR': homeruns, 'RBI': rbis, 'BB': walks, 'HBP': hbp, 'SO': strikeouts})  

    #Spencer Tinkel
    url = 'http://sunsbb.bbstats.pointstreak.com/team_stats.html?teamid=69161'
    response = requests.get(url)
    html = response.content
    bs = BeautifulSoup(html)
    possible_links = bs.findAll('a')
    for link in possible_links:
        if link.get('href') == 'player.html?playerid=975934&seasonid=30012':
            nex = link.findNext('td')
            position = nex.text
            nex = nex.findNext('td')
            average = nex.text
            nex = nex.findNext('td')
            games = nex.text
            nex = nex.findNext('td')
            atbats = nex.text
            nex = nex.findNext('td')
            runs = nex.text
            nex = nex.findNext('td')
            hits = nex.text
            nex = nex.findNext('td')
            doubles = nex.text
            nex = nex.findNext('td')
            triples = nex.text
            nex = nex.findNext('td')
            homeruns = nex.text
            nex = nex.findNext('td')
            rbis = nex.text
            nex = nex.findNext('td')
            walks = nex.text
            nex = nex.findNext('td')
            hbp = nex.text
            nex = nex.findNext('td')
            strikeouts = nex.text
            writer.writerow({'First': 'Spencer', 'Last': 'Tinkel', 'Team': 'Pittsfied Suns','Pos': position, 'Avg': average, 'G': games, 'AB': atbats, 'R': runs, 'H': hits, '2B': doubles, '3B': triples, 'HR': homeruns, 'RBI': rbis, 'BB': walks, 'HBP': hbp, 'SO': strikeouts})  

    #Alex Voitik
    url = 'http://www.400hitter.com/team.asp?TmID=564&SeID=270&CtID=0&pt=b'
    response = requests.get(url)
    html = response.content
    bs = BeautifulSoup(html)
    possible_links = bs.findAll('a')
    for link in possible_links:
        if link.get('href') == 'player.asp?PlID=25701&SeID=270&TmID=564&CtID=0&pt=b':
            nex = link.findNext('td')
            games = nex.text
            nex = nex.findNext('td')
            atbats = nex.text
            nex = nex.findNext('td')
            runs = nex.text
            nex = nex.findNext('td')
            hits = nex.text
            nex = nex.findNext('td')
            doubles = nex.text
            nex = nex.findNext('td')
            triples = nex.text
            nex = nex.findNext('td')
            homeruns = nex.text
            nex = nex.findNext('td')
            rbis = nex.text
            nex = nex.findNext('td')
            walks = nex.text
            nex = nex.findNext('td')
            strikeouts = nex.text
            nex = nex.findNext('td')
            nex = nex.findNext('td')
            nex = nex.findNext('td')
            average = nex.text
            nex = nex.findNext('td')
            nex = nex.findNext('td')
            hbp = nex.text
            writer.writerow({'First': 'Alex', 'Last': 'Voitik', 'Team': 'Lexington Blue Sox','Pos': position, 'Avg': average, 'G': games, 'AB': atbats, 'R': runs, 'H': hits, '2B': doubles, '3B': triples, 'HR': homeruns, 'RBI': rbis, 'BB': walks, 'HBP': hbp, 'SO': strikeouts})  

    #Kellen McCormick
    url = 'http://pgcbl.bbstats.pointstreak.com/team_stats.html?teamid=90390&seasonid=30255'
    response = requests.get(url)
    html = response.content
    bs = BeautifulSoup(html)
    possible_links = bs.findAll('a')
    for link in possible_links:
        if link.get('href') == 'player.html?playerid=993033&seasonid=30255':
            nex = link.findNext('td')
            position = nex.text
            nex = nex.findNext('td')
            average = nex.text
            nex = nex.findNext('td')
            games = nex.text
            nex = nex.findNext('td')
            atbats = nex.text
            nex = nex.findNext('td')
            runs = nex.text
            nex = nex.findNext('td')
            hits = nex.text
            nex = nex.findNext('td')
            doubles = nex.text
            nex = nex.findNext('td')
            triples = nex.text
            nex = nex.findNext('td')
            homeruns = nex.text
            nex = nex.findNext('td')
            rbis = nex.text
            nex = nex.findNext('td')
            walks = nex.text
            nex = nex.findNext('td')
            hbp = nex.text
            nex = nex.findNext('td')
            strikeouts = nex.text
            writer.writerow({'First': 'Kellen', 'Last': 'McCormick', 'Team': 'Newark Pilots','Pos': position, 'Avg': average, 'G': games, 'AB': atbats, 'R': runs, 'H': hits, '2B': doubles, '3B': triples, 'HR': homeruns, 'RBI': rbis, 'BB': walks, 'HBP': hbp, 'SO': strikeouts})
    
    #Dan Vucovitch
    url = 'http://pgcbl.bbstats.pointstreak.com/team_stats.html?teamid=90390&seasonid=30255'
    response = requests.get(url)
    html = response.content
    bs = BeautifulSoup(html)
    possible_links = bs.findAll('a')
    for link in possible_links:
        if link.get('href') == 'player.html?playerid=993025&seasonid=30255':
            nex = link.findNext('td')
            position = nex.text
            nex = nex.findNext('td')
            average = nex.text
            nex = nex.findNext('td')
            games = nex.text
            nex = nex.findNext('td')
            atbats = nex.text
            nex = nex.findNext('td')
            runs = nex.text
            nex = nex.findNext('td')
            hits = nex.text
            nex = nex.findNext('td')
            doubles = nex.text
            nex = nex.findNext('td')
            triples = nex.text
            nex = nex.findNext('td')
            homeruns = nex.text
            nex = nex.findNext('td')
            rbis = nex.text
            nex = nex.findNext('td')
            walks = nex.text
            nex = nex.findNext('td')
            hbp = nex.text
            nex = nex.findNext('td')
            strikeouts = nex.text
            writer.writerow({'First': 'Dan', 'Last': 'Vucovich', 'Team': 'Newark Pilots','Pos': position, 'Avg': average, 'G': games, 'AB': atbats, 'R': runs, 'H': hits, '2B': doubles, '3B': triples, 'HR': homeruns, 'RBI': rbis, 'BB': walks, 'HBP': hbp, 'SO': strikeouts})

    #Cam O'Neill
    url = 'http://necbl_bluesox.bbstats.pointstreak.com/team_stats.html?teamid=6403'
    response = requests.get(url)
    html = response.content
    bs = BeautifulSoup(html)
    possible_links = bs.findAll('a')
    for link in possible_links:
        if link.get('href') == 'player.html?playerid=990546&seasonid=29799':
            nex = link.findNext('td')
            position = nex.text
            nex = nex.findNext('td')
            average = nex.text
            nex = nex.findNext('td')
            games = nex.text
            nex = nex.findNext('td')
            atbats = nex.text
            nex = nex.findNext('td')
            runs = nex.text
            nex = nex.findNext('td')
            hits = nex.text
            nex = nex.findNext('td')
            doubles = nex.text
            nex = nex.findNext('td')
            triples = nex.text
            nex = nex.findNext('td')
            homeruns = nex.text
            nex = nex.findNext('td')
            rbis = nex.text
            nex = nex.findNext('td')
            walks = nex.text
            nex = nex.findNext('td')
            hbp = nex.text
            nex = nex.findNext('td')
            strikeouts = nex.text
            writer.writerow({'First': 'Cam', 'Last': 'O\'Neill', 'Team': 'Valley Blue Sox','Pos': position, 'Avg': average, 'G': games, 'AB': atbats, 'R': runs, 'H': hits, '2B': doubles, '3B': triples, 'HR': homeruns, 'RBI': rbis, 'BB': walks, 'HBP': hbp, 'SO': strikeouts})
    
    #Awari Muoneke
    #CANNOT FIND
    
    #Anthony Critelli
    url = 'http://www.pointstreak.com/baseball/team_stats.html?teamid=3431&seasonid=29795'
    response = requests.get(url)
    html = response.content
    bs = BeautifulSoup(html)
    possible_links = bs.findAll('a')
    for link in possible_links:
        if link.get('href') == 'player.html?playerid=986462&seasonid=29795':
            nex = link.findNext('td')
            position = nex.text
            nex = nex.findNext('td')
            average = nex.text
            nex = nex.findNext('td')
            games = nex.text
            nex = nex.findNext('td')
            atbats = nex.text
            nex = nex.findNext('td')
            runs = nex.text
            nex = nex.findNext('td')
            hits = nex.text
            nex = nex.findNext('td')
            doubles = nex.text
            nex = nex.findNext('td')
            triples = nex.text
            nex = nex.findNext('td')
            homeruns = nex.text
            nex = nex.findNext('td')
            rbis = nex.text
            nex = nex.findNext('td')
            walks = nex.text
            nex = nex.findNext('td')
            hbp = nex.text
            nex = nex.findNext('td')
            strikeouts = nex.text
            writer.writerow({'First': 'Anthony', 'Last': 'Critelli', 'Team': 'Harwich Mariners','Pos': position, 'Avg': average, 'G': games, 'AB': atbats, 'R': runs, 'H': hits, '2B': doubles, '3B': triples, 'HR': homeruns, 'RBI': rbis, 'BB': walks, 'HBP': hbp, 'SO': strikeouts})
    
    fieldnames = ['First', 'Last', 'Team', 'Pos', 'G', 'GS', 'CG', 'IP', 'H', 'R', 'ER', 'BB', 'SO', 'W', 'L', 'SV', '2B', '3B', 'ERA']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    
    #Pitchers
    
    #Pat McGowan
    url = 'http://worcesterbaseball.bbstats.pointstreak.com/team_stats.html?teamid=69160&seasonid=30012&view=pitching'
    response = requests.get(url)
    html = response.content
    bs = BeautifulSoup(html)
    possible_links = bs.findAll('a')
    for link in possible_links:
        if link.get('href') == 'player.html?playerid=970256&seasonid=30012':
            nex = link.findNext('td')
            g = nex.text
            nex = nex.findNext('td')
            gs = nex.text
            nex = nex.findNext('td')
            cg = nex.text
            nex = nex.findNext('td')
            ip = nex.text
            nex = nex.findNext('td')
            h = nex.text
            nex = nex.findNext('td')
            r = nex.text
            nex = nex.findNext('td')
            er = nex.text
            nex = nex.findNext('td')
            bb = nex.text
            nex = nex.findNext('td')
            so = nex.text
            nex = nex.findNext('td')
            w = nex.text
            nex = nex.findNext('td')
            l = nex.text
            nex = nex.findNext('td')
            sv = nex.text
            nex = nex.findNext('td')
            dub = nex.text
            nex = nex.findNext('td')
            tri = nex.text
            nex = nex.findNext('td')
            era = nex.text
            writer.writerow({'First': 'Pat', 'Last': 'McGowan', 'Team': 'Worcester Bravehearts', 'Pos':'RHP', 'G':g, 'GS':gs, 'CG':cg, 'IP':ip, 'H':h, 'R':r, 'ER':er, 'SO':so, 'BB':bb, 'W':w, 'L':l, 'SV':sv, '2B':dub, '3B':tri, 'ERA':era})
    
    #Brendan King
    url = 'http://www.pointstreak.com/baseball/team_stats.html?teamid=3435&seasonid=29795&view=pitching'
    response = requests.get(url)
    html = response.content
    bs = BeautifulSoup(html)
    possible_links = bs.findAll('a')
    for link in possible_links:
        if link.get('href') == 'player.html?playerid=899441&seasonid=29795':
            nex = link.findNext('td')
            g = nex.text
            nex = nex.findNext('td')
            gs = nex.text
            nex = nex.findNext('td')
            cg = nex.text
            nex = nex.findNext('td')
            ip = nex.text
            nex = nex.findNext('td')
            h = nex.text
            nex = nex.findNext('td')
            r = nex.text
            nex = nex.findNext('td')
            er = nex.text
            nex = nex.findNext('td')
            bb = nex.text
            nex = nex.findNext('td')
            so = nex.text
            nex = nex.findNext('td')
            w = nex.text
            nex = nex.findNext('td')
            l = nex.text
            nex = nex.findNext('td')
            sv = nex.text
            nex = nex.findNext('td')
            dub = nex.text
            nex = nex.findNext('td')
            tri = nex.text
            nex = nex.findNext('td')
            era = nex.text
            writer.writerow({'First': 'Brendan', 'Last': 'King', 'Team': 'Falmouth Commodores', 'Pos':'RHP', 'G':g, 'GS':gs, 'CG':cg, 'IP':ip, 'H':h, 'R':r, 'ER':er, 'SO':so, 'BB':bb, 'W':w, 'L':l, 'SV':sv, '2B':dub, '3B':tri, 'ERA':era})
    
    #Danny Barlok
    url = 'http://worcester_fcbl.bbstats.pointstreak.com/team_stats.html?teamid=69160&seasonid=30012&view=pitching'
    response = requests.get(url)
    html = response.content
    bs = BeautifulSoup(html)
    possible_links = bs.findAll('a')
    for link in possible_links:
        if link.get('href') == 'player.html?playerid=970199&seasonid=30012':
            nex = link.findNext('td')
            g = nex.text
            nex = nex.findNext('td')
            gs = nex.text
            nex = nex.findNext('td')
            cg = nex.text
            nex = nex.findNext('td')
            ip = nex.text
            nex = nex.findNext('td')
            h = nex.text
            nex = nex.findNext('td')
            r = nex.text
            nex = nex.findNext('td')
            er = nex.text
            nex = nex.findNext('td')
            bb = nex.text
            nex = nex.findNext('td')
            so = nex.text
            nex = nex.findNext('td')
            w = nex.text
            nex = nex.findNext('td')
            l = nex.text
            nex = nex.findNext('td')
            sv = nex.text
            nex = nex.findNext('td')
            dub = nex.text
            nex = nex.findNext('td')
            tri = nex.text
            nex = nex.findNext('td')
            era = nex.text
            writer.writerow({'First': 'Danny', 'Last': 'Barlok', 'Team': 'Worcester Bravehearts', 'Pos':'RHP', 'G':g, 'GS':gs, 'CG':cg, 'IP':ip, 'H':h, 'R':r, 'ER':er, 'SO':so, 'BB':bb, 'W':w, 'L':l, 'SV':sv, '2B':dub, '3B':tri, 'ERA':era})

    #Phil Reese 
    url = 'http://www.pointstreak.com/baseball/team_stats.html?teamid=3432&seasonid=29795&view=pitching'
    response = requests.get(url)
    html = response.content
    bs = BeautifulSoup(html)
    possible_links = bs.findAll('a')
    for link in possible_links:
        if link.get('href') == 'player.html?playerid=999684&seasonid=29795':
            nex = link.findNext('td')
            g = nex.text
            nex = nex.findNext('td')
            gs = nex.text
            nex = nex.findNext('td')
            cg = nex.text
            nex = nex.findNext('td')
            ip = nex.text
            nex = nex.findNext('td')
            h = nex.text
            nex = nex.findNext('td')
            r = nex.text
            nex = nex.findNext('td')
            er = nex.text
            nex = nex.findNext('td')
            bb = nex.text
            nex = nex.findNext('td')
            so = nex.text
            nex = nex.findNext('td')
            w = nex.text
            nex = nex.findNext('td')
            l = nex.text
            nex = nex.findNext('td')
            sv = nex.text
            nex = nex.findNext('td')
            dub = nex.text
            nex = nex.findNext('td')
            tri = nex.text
            nex = nex.findNext('td')
            era = nex.text
            writer.writerow({'First': 'Phil', 'Last': 'Reese', 'Team': 'Wareham Gatemen', 'Pos':'RHP', 'G':g, 'GS':gs, 'CG':cg, 'IP':ip, 'H':h, 'R':r, 'ER':er, 'SO':so, 'BB':bb, 'W':w, 'L':l, 'SV':sv, '2B':dub, '3B':tri, 'ERA':era})
   
    #George Capen
    url = 'http://necbl.bbstats.pointstreak.com/team_stats.html?teamid=51489&seasonid=29799&view=pitching'
    response = requests.get(url)
    html = response.content
    bs = BeautifulSoup(html)
    possible_links = bs.findAll('a')
    for link in possible_links:
        if link.get('href') == 'player.html?playerid=898679&seasonid=29799':
            nex = link.findNext('td')
            g = nex.text
            nex = nex.findNext('td')
            gs = nex.text
            nex = nex.findNext('td')
            cg = nex.text
            nex = nex.findNext('td')
            ip = nex.text
            nex = nex.findNext('td')
            h = nex.text
            nex = nex.findNext('td')
            r = nex.text
            nex = nex.findNext('td')
            er = nex.text
            nex = nex.findNext('td')
            bb = nex.text
            nex = nex.findNext('td')
            so = nex.text
            nex = nex.findNext('td')
            w = nex.text
            nex = nex.findNext('td')
            l = nex.text
            nex = nex.findNext('td')
            sv = nex.text
            nex = nex.findNext('td')
            dub = nex.text
            nex = nex.findNext('td')
            tri = nex.text
            nex = nex.findNext('td')
            era = nex.text
            writer.writerow({'First': 'George', 'Last': 'Capen', 'Team': 'Ocean State Waves', 'Pos':'RHP', 'G':g, 'GS':gs, 'CG':cg, 'IP':ip, 'H':h, 'R':r, 'ER':er, 'SO':so, 'BB':bb, 'W':w, 'L':l, 'SV':sv, '2B':dub, '3B':tri, 'ERA':era})
    
    #Declan Cronin
    url = 'http://sunsbb.bbstats.pointstreak.com/team_stats.html?teamid=69161&seasonid=30012&view=pitching'
    response = requests.get(url)
    html = response.content
    bs = BeautifulSoup(html)
    possible_links = bs.findAll('a')
    for link in possible_links:
        if link.get('href') == 'player.html?playerid=975906&seasonid=30012':
            nex = link.findNext('td')
            g = nex.text
            nex = nex.findNext('td')
            gs = nex.text
            nex = nex.findNext('td')
            cg = nex.text
            nex = nex.findNext('td')
            ip = nex.text
            nex = nex.findNext('td')
            h = nex.text
            nex = nex.findNext('td')
            r = nex.text
            nex = nex.findNext('td')
            er = nex.text
            nex = nex.findNext('td')
            bb = nex.text
            nex = nex.findNext('td')
            so = nex.text
            nex = nex.findNext('td')
            w = nex.text
            nex = nex.findNext('td')
            l = nex.text
            nex = nex.findNext('td')
            sv = nex.text
            nex = nex.findNext('td')
            dub = nex.text
            nex = nex.findNext('td')
            tri = nex.text
            nex = nex.findNext('td')
            era = nex.text
            writer.writerow({'First': 'Declan', 'Last': 'Cronin', 'Team': 'Pittsfield Suns', 'Pos':'RHP', 'G':g, 'GS':gs, 'CG':cg, 'IP':ip, 'H':h, 'R':r, 'ER':er, 'SO':so, 'BB':bb, 'W':w, 'L':l, 'SV':sv, '2B':dub, '3B':tri, 'ERA':era})
  
print("Done!")
