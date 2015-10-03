
from gladiator.referee import run_game
import random

def schedule_game(client_list):
    clients = list(client_list)
    clientOne = random.choice(clients)
    clients.remove(clientOne)
    clientTwo = random.choice(clients)
    return run_game.delay(clientOne, clientTwo)


if __name__ == "__main__":
    clients = ['a', 'b', 'c', 'd']
    results = []
    for i in range(100):
        results.append(schedule_game(clients))

    done = False
    while not done:
        done = True
        for index, i in enumerate(list(results)):
            print index, i.status
            if i.status == 'PENDING':
                done = False
            else:
                results.remove(i)
                
