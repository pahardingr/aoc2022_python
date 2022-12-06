with open("input.txt", "r") as aocd2:
    play_list = aocd2.read().split()

opp_play = []
my_play = []

for p in play_list:
    for i in range(len(play_list)):
        if i == 2*i-1:
            opp_play.append(p)
        else:
            my_play.append(p)
            opp_play.clear()
print(opp_play)

