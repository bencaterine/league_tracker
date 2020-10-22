class Team:
    # a Team includes a team's id (given by the program), name, and performance
    # information, such as wins, for, and points
    def __init__(self, name, id):
        self.name, self.id = name, id
        self.pld = self.win = self.draw = self.loss \
            = self.fo = self.ag = self.diff = self.pts = 0
        self.form = ''

    def update(self, fo, ag):
        # updates all of the Team information after a game
        self.pld += 1
        self.fo += fo
        self.ag += ag
        self.diff = self.fo - self.ag
        if fo > ag:
            self.win += 1
            self.pts += 3
        elif fo == ag:
            self.draw += 1
            self.pts += 1
        else:
            self.loss += 1

    def remove(self, fo, ag):
        # removes the Team information from the given game (if user changes)
        self.pld -= 1
        self.fo -= fo
        self.ag -= ag
        self.diff = self.fo - self.ag
        if fo > ag:
            self.win -= 1
            self.pts -= 3
        elif fo == ag:
            self.draw -= 1
            self.pts -= 1
        else:
            self.loss -= 1


class Game:
    # a Game includes 2 team ids for the participants, a datetime, and a score
    def __init__(self, hid, aid):
        self.hid, self.aid = hid, aid
        self.date = self.hsc = self.asc = None
