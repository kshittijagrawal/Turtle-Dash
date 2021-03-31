import turtle, time, random

SCREEN_WIDTH, SCREEN_HEIGHT = 700, 600  # constants : specifying the race screen size
COLORS = ['red', 'blue', 'green', 'yellow', 'orange', 'black', 'brown', 'pink', 'purple', 'cyan']

def init_turtle():
	"""Function that creates the space track and gets it set for a race."""
	screen = turtle.Screen()
	screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
	screen.title('Turtle Dash!')


def number_of_racers():
	"""Function that accepts the user choice of number of turtles to race. If input is not an integer, user is prompted for a good input."""
	racers = 0
	while True:
		racers = input('\nEnter the number of racers.\nChoose either between 2 and 10 to race OR Q/q to quit.\nEnter here : ')
		if racers.isdigit():
			racers = int(racers)
		elif racers == "Q" or racers == "q":
			return
		else:
			print('\nInput is not a numeric. Try Again!')
			continue

		if 2 <= racers <= 10:
			return racers
		else:
			print('\nNumber not in range 2-10. Try Again!')


def create_turtles(colors):
	"""Function that creates turtles as per the user input and positions them, equally spreading through the given space track."""
	turtles = []
	spacing = SCREEN_WIDTH // (len(colors) + 1)
	for i, color in enumerate(colors):
		racer = turtle.Turtle()
		racer.color(color)
		racer.shape('turtle')
		racer.left(90)
		racer.penup()
		racer.setpos(-SCREEN_WIDTH//2 + (i + 1) * spacing, -SCREEN_HEIGHT//2 + 20)
		racer.pendown()
		turtles.append(racer)

	return turtles


def race(colors):
	"""Function that receives the colored turtles as parameters and races them."""
	turtles = create_turtles(colors)

	while True:
		for racer in turtles:
			distance = random.randrange(1, 20)
			racer.forward(distance)

			x, y = racer.pos()
			if y >= SCREEN_HEIGHT // 2 - 10:
				return colors[turtles.index(racer)]


def main():
	"""The main function."""
	racers = number_of_racers()
	if racers is None:
		quit()
	init_turtle()

	random.shuffle(COLORS)
	colors = COLORS[:racers]

	winner = race(colors)
	print("The winner is the turtle with color:", winner)
	time.sleep(5)

if __name__ == "__main__":
	"""The driver code."""
	main()