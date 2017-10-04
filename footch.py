import random
WIN_SCR = 3
DRAW_SCR = 1
LOOSE_SCR = 0
n = int(input())
team=[]
for i in range(n):
    team.append({'name': str(input()), 'goal' : 0, 'miss' : 0, 'score' : 0, 'games' : []})
for i in range(len(team)):
    for j  in range(i+1,len(team)):
        res_i = random.randint(0,10)
        res_j = random.randint(0,10)
        team[i]['goal'] += res_i 
        team[i]['miss'] += res_j
        team[j]['goal'] += res_j
        team[j]['miss'] += res_i
        team[i]['games'].append({'aponent' : team[j]['name'], 'miss':res_j, 'goal' : res_i})
        team[j]['games'].append({'aponent' : team[i]['name'], 'miss':res_i, 'goal' : res_j})
        if res_i > res_j:
            team[i]['score'] += WIN_SCR
            team[j]['score'] += LOOSE_SCR
        elif res_i < res_j:
            team[j]['score'] += WIN_SCR
            team[i]['score'] += LOOSE_SCR
        elif res_i == res_j:
            team[j]['score'] += DRAW_SCR
            team[i]['score'] += DRAW_SCR      
print(team)

