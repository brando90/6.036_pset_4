import math

class Boosting:
	# data_points = [..., (x_1,...x_d), ... ]
	def __init__(self, data_points):
		self.data = data_points
		self.n = len(seld.data)

	def initialWeight(self):
		self.weights = []
		init_weight = 1.0/float(self.n)
		for i in range(self.n):
			self.weights.append(init_weight)

	def AdaBoost(self, rounds_of_boosting):
		self.initialWeight();
		self.rounds_of_boosting = rounds_of_boosting
		for m in range(rounds_of_boosting):
			(theta_m, e_m) = self.findCurrentBestStump()

	def findCurrentBestStump(self):

		return (theta_m, e_m)

	def setVoteForCurrentStump(self, e_m):
		return 0.5 * Math.log((1.0 - e_m) / e_m)
