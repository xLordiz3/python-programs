from random import choice

players = ["A", "B", "C", "D"]
Team1 = []
Team2 = []

while (len(players) > 0):
    playerA = choice(players)
    Team1.append(playerA)
    players.remove(playerA)

    playerB = choice(players)
    Team2.append(playerB)
    players.remove(playerB)

print(Team1)
print(Team2)
