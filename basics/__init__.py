def counter():
    count = 0

    def increment():
        nonlocal count
        count = count + 1
        return count

    return increment

increment = counter()
print(increment())
print(increment())
print(increment())

def player():

    players = [100, 200, 300, 400, 0, 0, 0, 0]

    print(players)
    stack_0 : list = [play for play in players if play == 0]
    print(stack_0)

    for play in players:
        for p in stack_0:
            if play == p:
                players.remove(p)
    print(players)
player()



