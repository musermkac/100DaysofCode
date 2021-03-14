def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while at_goal() == False:
    if wall_on_right() and front_is_clear():
        move()
    elif wall_on_right() == False:
        if front_is_clear:
            turn_right()
            if front_is_clear:
                move()
            else:
                turn_right()
                turn_right()
                turn_right()
                move()
    elif wall_on_right() and wall_in_front():
        turn_left()
    elif wall_on_right() == False and wall_in_front():
        turn_right()
    elif wall_on_right() == False and wall_in_front() == False:
        turn_right()
    else:
        move()≈
