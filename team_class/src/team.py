
class Team:
	points = 0
	def __init__(self, name, players, coach):
		self.name = name
		self.players = players
		self.coach = coach
#		self.points = 0

	def add_player(self, player):
		self.players.append(player)
	
	def has_player(self, player):
		return True if player in self.players else False
	
	def play_game(self, didWin):
		if didWin:
			self.points += 3