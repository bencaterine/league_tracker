from operator import attrgetter


def get_results(games):
    # puts all finished games within 'games' in a list
    results = []
    for i, row in enumerate(games):
        for j, game in enumerate(games[i]):
            if game is not None and game.hsc is not None \
                    and game.asc is not None:
                results.append(game)
    return results


def form(team, games):
    # computes team's last 5 results given all games, returns a string
    rev_results = get_results(games)
    rev_results.sort(reverse=True, key=attrgetter('date', 'hid', 'aid'))
    last_five = []
    for game in rev_results:
        if game.hid == team.id:
            if game.hsc > game.asc:
                res = 'W'
            elif game.hsc == game.asc:
                res = 'D'
            elif game.hsc < game.asc:
                res = 'L'
            last_five.append(res)
        elif game.aid == team.id:
            if game.asc > game.hsc:
                res = 'W'
            elif game.asc == game.hsc:
                res = 'D'
            elif game.asc < game.hsc:
                res = 'L'
            last_five.append(res)
        if len(last_five) >= 5:
            break
    last_five.reverse()
    ret = ''.join(last_five)
    return ret


def print_game(game, teams, games):
    # prints upcoming game
    home = teams[game.hid].name.ljust(15, ' ')
    away = teams[game.aid].name.rjust(15, ' ')
    if game.date is None:
        date = " TBA          TBA"
    else:
        date = games[game.hid][game.aid].date.strftime('%a, %b '
                                                       + '%d'.rjust(2, ' ')
                                                       + ', %I:%M %p')
    if game.hsc is None and game.asc is None:
        print("   " + home + " v " + away + "   " + date)
    else:
        print("   " + home + str(game.hsc) + "-" + str(game.asc) + away
              + "   " + date)


def get_user_game_info(teams_dict):
    # take user team input
    home = input("Enter game information:\n   Home Team: ")
    away = input("   Away Team: ")

    # get team ids
    while(1):
        hid = teams_dict.get(home)
        if hid is not None:
            break
        home = input("Home team not found. Try again: ")
    while(1):
        aid = teams_dict.get(away)
        if aid is not None:
            break
        away = input("Away team not found. Try again: ")
    return hid, aid
