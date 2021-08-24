class Team():
    def __init__(self, name):
        self.name = name
        self.matches_played = 0
        self.wins = 0
        self.draws = 0
        self.losses = 0
        self.points = 0

    def update_points(self):
        self.points = self.wins * 3 + self.draws

    def add_match(self, result):
        self.matches_played += 1

        if result == 'win':
            self.wins += 1
        elif result == 'draw':
            self.draws += 1
        elif result == 'loss':
            self.losses += 1
        else:
            raise ValueError("Unknown match result: " + result)
        self.update_points()

    def __repr__(self):
        return " | ".join((self.name.ljust(30), str(self.matches_played).rjust(2), 
        str(self.wins).rjust(2), str(self.draws).rjust(2), str(self.losses).rjust(2), 
        str(self.points).rjust(2)))

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        if self.points == other.points:
            return self.name > other.name
        return self.points < other.points

def tally(rows):
    teams = []

    for row in rows:
        team_one, team_two, result = row.split(';')
        
        if Team(team_one) not in teams:
            teams.append(Team(team_one))
        team_one = teams.index(Team(team_one))

        if Team(team_two) not in teams:
            teams.append(Team(team_two))
        team_two = teams.index(Team(team_two))

        if result == 'win':
            teams[team_one].add_match('win')
            teams[team_two].add_match('loss')
        elif result == 'loss':
            teams[team_one].add_match('loss')
            teams[team_two].add_match('win')
        elif result == 'draw':
            teams[team_one].add_match('draw')
            teams[team_two].add_match('draw')

    teams = sorted(teams, reverse=True)

    header = " | ".join(('Team'.ljust(30), 'MP', ' W', ' D', ' L', ' P'))
    return [header] + [str(team) for team in teams]
