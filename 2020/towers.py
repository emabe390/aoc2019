from math import sqrt
from random import randint

class Node():
	def __init__(self, id, x, y):
		self.id = id
		self.x = x
		self.y = y

	def distance(self, x, y):
		return sqrt((self.x - x) ** 2 + (self.y - y) ** 2)

def make_towers(x_max, y_max, n):
	towers = []
	k = 0
	n_sqrt = sqrt(n)
	dx = x_max/n_sqrt
	dy = y_max/n_sqrt
	
	for x in range(x_max):
		for y in range(y_max):
			if k >= n:
				break
			towers.append(Node(k, x, y))
			k += 1

	return towers


def find_freq(x_max, y_max, towers):
	freq = {t: 0 for t in towers}
	for x in range(x_max):
		for y in range(y_max):
			min_distance = None
			best_tower = None
			for t in towers:
				d = t.distance(x,y)
				if min_distance is None or d < min_distance:
					min_distance = d
					best_tower = t
			freq[best_tower] += 1
	return freq

def move_tower(x_max, y_max, tower):
	if randint(0, 1) == 0:
		tower.x = (tower.x + 1) % x_max
	else:
		tower.y = (tower.y + 1) % y_max


def calc_freq(x_max, y_max, tolerance, freq):
	lowest_freq = x_max*y_max
	highest_freq = 0
	highest_freq_tower = None
	for t, f in freq.items():
		if highest_freq < f:
			highest_freq_tower = t
			highest_freq = f
		if lowest_freq > f:
			lowest_freq = f
	if highest_freq - lowest_freq <= tolerance:
		return True, None, None
	return False, highest_freq_tower, highest_freq


def main():
	x = 100
	y = 100
	k = 50
	tolerance = 5
	towers = make_towers(x, y, k)
	while True:
		freq = find_freq(x, y, towers)
		done, worst, pre_score = calc_freq(x, y, tolerance, freq)
		if done:
			return towers
		
		pre_x = worst.x
		pre_y = worst.y
		best_score = x*y
		best_x = None
		best_y = None
		best_freq = None
		
		for dx in range(-1, 2):
			for dy in range(-1, 2):
				worst.x = (worst.x + dx) % x
				worst.y = (worst.y + dy) % y
				freq = find_freq(x, y, towers)
				done , __, score = calc_freq(x, y, tolerance, freq)
				if done is True:
					return towers
				if score < best_score:
					best_freq = freq
					best_x = worst.x
					best_y = worst.y
					best_score = score
				worst.x = pre_x
				worst.y = pre_y
		if pre_score == best_score:
			tolerance += 1
			print("Increasing tolerance to", tolerance)
			print("Score", best_score)
			for t, f in best_freq.items():
				print(t.id, f)
		worst.x = best_x
		worst.y = best_y
			
good_towers = main()

for t in good_towers:
	print(t.id, t.x, t.y)