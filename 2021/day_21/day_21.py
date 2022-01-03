player_pos = { #test data
    "p1": 3,#4,
    "p2": 7 #8 
}

player_pos = {
    "p1": 3,#4,
    "p2": 4 #5 
}

player_points = {
    "p1" : 0,
    "p2": 0
}

dice = 1
dice_rolls = 0
found_1000 = False
while not found_1000:
    for player in player_pos:
        for _ in range(3):
            player_pos[player] += dice
            dice += 1
            dice_rolls += 1
            player_pos[player] %= 10
            if dice > 100:
                dice = 1 
        player_points[player] += player_pos[player] + 1
        
        if player_points[player] >= 1000:
            found_1000 = True
            break

print("Part 1: " + str(min(player_points.values()) * dice_rolls))
