def get_score(game_stamps, offset):
    total_score = 0
    for elem in game_stamps:    
        time, score = elem        #The first value of a list in a tuple is time, the second one is the score at that time
        if time <= offset:
            total_score = score
    
    return total_score

