import matplotlib.pyplot as plt

from random_walk import RandomWalk

# keep making new plots as long as program is active
while True: 
	# make a random walk, and plot the points
	rw = RandomWalk()
	rw.fill_walk()

	# set size of plotting window
	# plt.figure(figsize=(10, 6))

	point_numbers = list(range(rw.num_points))
	plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=15)
		
	# Emphasize first and last points
	plt.scatter(0, 0, c='green', edgecolors='none', s=100)
	plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

	# remove the axes
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)

	plt.show()

	keep_running = input("Make another walk? (y/n): ")
	if keep_running == 'n':
		break