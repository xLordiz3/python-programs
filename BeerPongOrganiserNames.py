from random import choice
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--named", type=str, help="Prompts to Enter Player Names", nargs="+")
args = parser.parse_args()

def get_args():
    named = args.named[0].split(",")
    return named

def assignTeams(namedplayers):
    PP = namedplayers
    Team1 = []
    Team2 = []

    while (len(PP) > 0 and len(Team1) < 2 and len(Team2) < 2):
        PA = choice(PP)
        Team1.append(PA)
        PP.remove(PA)

        PB = choice(PP)
        Team2.append(PB)
        PP.remove(PB)

    print(Team1)
    print(Team2)

assignTeams(get_args())
