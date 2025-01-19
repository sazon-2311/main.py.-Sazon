import math

__team_1 = 'Мастера кода'
__team_2 = 'Волшебники данных'
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score_2 + score_1
time_avg = round(((team1_time + team2_time) / (score_1 + score_2)), 1)
team_vin = ''

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    team_vin = __team_1
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    team_vin = __team_2
else:
    team_vin = 'Ничья'

team1 = "В команде %s участников: %s ! " % (__team_1, team1_num)
team2 = "В команде %s участников: %s ! " % (__team_2, team2_num)
team1_2 = "Итого сегодня в командах участников: %s и %s!" % (team1_num, team2_num)
_score_1 = "Команда {} решила задач: {} !".format(__team_1, score_1)
_score_2 = "Команда {} решила задач: {} !".format(__team_2, score_2)
time_team1 = "{} решили задачи за {} с !".format(__team_1, int(team1_time))
time_team2 = "{} решили задачи за {} с !".format(__team_2, int(team2_time))
score1_2 = f"Команды решили {score_1} и {score_2} задач."
tasks_avg = (f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} "
             f"секунды на задачу!. \n"
             f"Команда {__team_1} в среднем на одну задачу тратила: {round(team1_time / score_1, 1)} c. \n"
             f"Команда {__team_2} в среднем на одну задачу тратила: {round(team2_time / score_2, 1)} c.")
challenge_result = f'Победа команды {team_vin}! Они решили на {score_2 - score_1} задачи больше!'

print(team1, "\n",
      team2, "\n",
      team1_2, "\n",
      _score_1, "\n",
      _score_2, "\n",
      time_team1, "\n",
      time_team2, "\n",
      score1_2, "\n",
      challenge_result, "\n",
      tasks_avg)
