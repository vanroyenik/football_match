import random
n = int(input())
team=[]
for i in range(len(n):
    team.append(str(input()))
count = 0
res_i = 0
res_j = 0
scr = 0
for i in range(len(n)):
    team[i] = {'goal' : 0, 'miss' : 0, 'score' : 0}
    for j in range(i+1, len(n)):
        count += 1
        team[j] = {'goal' : res_j, 'miss' : res_i, 'score' : scr}
        res_i = random.randint(0,10)
        res_j = random.randint(0,10)
        team[i]['goal'] += res_i 
        team[i]['miss'] += res_j
        team[j]['goal'] += res_j
        team[j]['miss'] += res_i
        if res_i > res_j:
            scr = 3
            team[i]['score'] += scr
            team[j]['score'] += 0
        elif res_i < res_j:
            scr = 3
            team[j]['score'] += scr
            team[i]['score'] += 0
        elif res_i == res_j:
            scr = 1
            team[j]['score'] += scr
            team[i]['score'] += scr      
        print(team)