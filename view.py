from operator import attrgetter
from gen_funcs import get_results, form, print_game


def view_schedule(teams, games):
    # prints the schedule given teams and games

    # scheduled is dated games; unscheduled is currently undated games
    scheduled = []
    unscheduled = []
    # iterate through games to store in the two lists, then sort by date/id
    for i, row in enumerate(games):
        for j, game in enumerate(games[i]):
            if game is not None and game.date is not None \
                    and game.hsc is None and game.asc is None:
                scheduled.append(game)
            elif game is not None and game.hsc is None and game.asc is None:
                unscheduled.append(game)
    scheduled.sort(key=attrgetter('date', 'hid', 'aid'))
    unscheduled.sort(key=attrgetter('hid', 'aid'))

    # mo and yr are used to determine when to print months/years in schedule
    mo = 0
    yr = 0
    # iterate through schedule, print each game, mo/yr as needed
    for game in scheduled:
        if mo != game.date.month or yr != game.date.year:
            mostr = game.date.strftime('%B').upper()
            mo = game.date.month
            if yr != game.date.year:
                yrstr = " " + game.date.strftime('%Y')
                yr = game.date.year
            else:
                yrstr = ""
            print(mostr + yrstr)
            print("   HOME            v            AWAY   DATE             "
                  + "TIME")
        print_game(game, teams, games)

    # print unscheduled header if needed, then iterate/print unscheduled games
    if len(unscheduled) > 0:
        print("GAMES NOT YET SCHEDULED")
        print("   HOME            v            AWAY   DATE             TIME")
    for game in unscheduled:
        print_game(game, teams, games)


def view_results(teams, games):
    # prints the results (completed games) given teams and games

    # stores all completed games in results, sorts by date/id
    results = get_results(games)
    results.sort(key=attrgetter('date', 'hid', 'aid'))
    mo = 0
    yr = 0

    # iterate through results, print each game, mo/yr as needed
    for game in results:
        if mo != game.date.month or yr != game.date.year:
            mostr = game.date.strftime('%B').upper()
            mo = game.date.month
            if yr != game.date.year:
                yrstr = " " + game.date.strftime('%Y')
                yr = game.date.year
            else:
                yrstr = ""
            print(mostr + yrstr)
            print("   HOME            v            AWAY   DATE             "
                  + "TIME")
        print_game(game, teams, games)


def view_standings(teams, games):
    # prints the standings given teams and games

    # standings is teams sorted by pts, diff, fo (standard soccer procedure)
    standings = sorted(teams, reverse=True,
                       key=attrgetter('pts', 'diff', 'fo'))
    # header
    print("POS CLUB           PLD  W  D  L   F   A DIFF    PTS     FORM")
    # Ex.    1 Manchester City 99 99 99 99 199 199  -99    100    WWWWW

    # iterate through standings, print each field for each team (with padding)
    for i, team in enumerate(standings):
        frm = form(team, games)
        print(str(i + 1).rjust(3, ' ') + ' ' + team.name.ljust(15, ' ')
              + str(team.pld).rjust(3, ' ') + str(team.win).rjust(3, ' ')
              + str(team.draw).rjust(3, ' ') + str(team.loss).rjust(3, ' ')
              + str(team.fo).rjust(4, ' ') + str(team.ag).rjust(4, ' ')
              + str(team.diff).rjust(5, ' ') + str(team.pts).rjust(7, ' ')
              + frm.rjust(9, ' '))
