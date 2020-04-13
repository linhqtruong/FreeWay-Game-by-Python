def freeway_game(km, kph, cars):
    myTimeToExit = km / kph
    Score = 0
    for Lead, Speed in cars:
        # Caculate the distanceGap between Cars at the exit point
        distanceGap = km - (myTimeToExit - Lead/60) * Speed
        if Lead <= 0:            
            Score += distanceGap > 0
        else:
            Score -= distanceGap < 0
    return Score
