year = input()
praznici = int(input())
hweekends_Difcity = int(input())
import math
sabbat_games_Sofia = (48-hweekends_Difcity)*3/4
praznik_games = praznici*2/3
normal_games = sabbat_games_Sofia+hweekends_Difcity+praznik_games

if year == "leap":
    normal_games = normal_games*1.15

print(math.floor(normal_games))
