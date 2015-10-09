
from arena.thunderdome.models import Game, Client, GameData

from gladiator.referee import run_game

import random

#def schedule_game(client_list):
#    clients = list(client_list)
#    clientOne = random.choice(clients)
#    clients.remove(clientOne)
#    clientTwo = random.choice(clients)
#    return run_game.delay(clientOne, clientTwo)


def schedule_game():
    clients = Client.objects.all()
    clientOne = random.choice(clients)
    clients.remove(clientOne)
    clientTwo = random.choice(clients)
    t = [clientOne, clientTwo]
    random.shuffle(t)
    return sked(t[0], t[1])

def sked(clientOne, clientTwo):
    game = Game.objects.create()
    c1 = Client.objects.get(name=clientOne)
    c2 = Client.objects.get(name=clientTwo)
    
    for guy in (c1, c2):
        GameData(game=game, client=guy).save()

    
    game.save()
    return (game, run_game.delay(c1.name, c2.name))


def setup_test_clients():
    for i in Client.objects.all():
        i.delete()

    Client(name='a').save()
    Client(name='b').save()
    Client(name='c').save()
    Client(name='d').save()
    
    for g in Game.objects.all():
        g.delete()

    for dg in GameData.objects.all():
        dg.delete()

def maintain_gamedata():
    pass

if __name__ == "__main__":
    setup_test_clients()

    game_queue = []

    for i in range(10):
        game_queue.append(schedule_game())
       

    done = False
    while not done:
        done = True
        for index, i in enumerate(list(results)):
            print index, i.status
            if i.status == 'PENDING':
                done = False
            else:
                results.remove(i)
                
