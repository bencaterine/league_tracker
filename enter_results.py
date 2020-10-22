from gen_funcs import print_game, get_user_game_info
from schedule_games import schedule_games


def enter_results(teams, teams_dict, games):
    # enters the score of 1+ games, given teams, teams_dict, games, user input

    # gets game from user, checks for proper format
    while(1):
        hid, aid = get_user_game_info(teams_dict)
        while(1):
            hsc = input("   Home Score: ")
            if hsc.isnumeric():
                hsc = int(hsc)
                break
            else:
                print("Try again. Make sure to enter one score at a time.")
        while(1):
            asc = input("   Away Score: ")
            if asc.isnumeric():
                asc = int(asc)
                break
            else:
                print("Try again. Make sure to enter one score at a time.")

        while(1):
            # if game already has a result, check if user wants to update
            if games[hid][aid].hsc is not None \
                    and games[hid][aid].asc is not None:
                print("\nThis game already has results:")
                print_game(games[hid][aid], teams, games)
                change = input("Would you like to change the results? (y/n) ")
                if change == 'y':
                    teams[hid].remove(games[hid][aid].hsc, games[hid][aid].asc)
                    teams[aid].remove(games[hid][aid].asc, games[hid][aid].hsc)
                elif change == 'n':
                    break
            # if game is not scheduled, ask user to schedule first
            elif games[hid][aid].date is None:
                print("\nThis game is not yet scheduled. Please schedule it "
                      + "first and come back to enter results.\n")
                print("Schedule Games:\n")
                schedule_games(teams, teams_dict, games)
                return

            # if game does not have a result, enter results and update teams
            games[hid][aid].hsc = hsc
            games[hid][aid].asc = asc
            teams[hid].update(hsc, asc)
            teams[aid].update(asc, hsc)
            print("\nResult entered:")
            print_game(games[hid][aid], teams, games)
            break

        # enter more results if requested
        if input('\nEnter more results? (y/n) ') == 'n':
            break
