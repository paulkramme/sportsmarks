#!/usr/bin/env python3


def mark(hits, distance):
	standard_multiplier = 3 #std distance = 4 Meter
	points = hits * 3
	return points


def exists():
	try:
		f = open("marklist.csv", "r")
		f.close()
	except FileNotFoundError:
		f = open("marklist.csv", "w")
		f.write("name,hits,note_in_punkten\n")


def main():
	finalmark = 0
	hits = 0
	throw_count = 5
	i = 1
	while True:
		name = input("Name? ")
		if name != '':
			break
		else:
			pass
	while i <= throw_count:
		hit = input("Getroffen? (y/n) ")
		if hit == "y" or hits == "ja":
			distance = int(input("Entfernung zum Korb? "))
			hits = hits + 1
			finalmark = mark(hits, distance)
			i = i + 1
		elif hit == "n" or hits == "nein":
			i = i + 1
		else:
			print("Please state 'y' or 'n' or 'ja' or 'nein'.")
		print(hits)
	exists()
	with open("marklist.csv", "a") as f:
		f.write(name + "," + str(hits) + "," + str(finalmark) + '\n')
	print("End program.")


if __name__ == __name__:
	main()
