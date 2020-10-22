from datetime import datetime
import re
from gen_funcs import print_game, get_user_game_info


def game_datetime(hid, aid, teams, games):
    # inserts a datetime into a game, given ids, games, teams

    # gets date input, checks for errors
    date = input("   Date (MM/DD/YYYY): ").split("/")
    while len(date) != 3 or len(date[0]) > 2 \
            or len(date[1]) > 2 or len(date[2]) != 4:
        date = [item for item in input("Try again. Make sure to follow " +
                                       "the format 'MM/DD/YYYY':" +
                                       " ").split("/")]
    mo, day, yr = [int(item) for item in date]

    # gets time input, checks for errors
    time = re.split(":| ", input("   Time (HH:MM [AM/PM]): "))
    while len(time) != 3 or len(time[0]) > 2 or len(time[1]) != 2:
        time = re.split(":| ", input("Try again. Make sure to follow "
                                     + "the format 'HH:MM [AM/PM]': "))
    hr, min, ampm = int(time[0]), int(time[1]), time[2]

    # corrects for 24-hour time, checks for errors
    while(1):
        if ampm == 'AM' or ampm == 'am':
            if hr == 12:
                hr = 0
            break
        elif ampm == 'PM' or ampm == 'pm':
            if hr != 12:
                hr += 12
            break
        ampm = input("Is this time AM or PM? ")

    # inserts completed datetime into the given game
    games[hid][aid].date = datetime(yr, mo, day, hr, min)
    print("\nGame scheduled:")
    print_game(games[hid][aid], teams, games)


def schedule_games(teams, teams_dict, games):
    # inputs game datetime into game specified by user,
    # given teams, teams_dict, games, user input

    while(1):
        hid, aid = get_user_game_info(teams_dict)

        # if game is not scheduled, enter datetime info
        if games[hid][aid].date is None:
            game_datetime(hid, aid, teams, games)
        # if game is scheduled, reschedule if requested
        else:
            print("\nThis game is already scheduled:")
            print_game(games[hid][aid], teams, games)
            if input('Would you like reschedule? (y/n) ') == 'y':
                game_datetime(hid, aid, teams, games)
        if input('\nSchedule another game? (y/n) ') == 'n':
            break
