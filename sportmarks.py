#!/usr/bin/env python3


def mark(hits, distance):
	points = hits * 3
	return points


def main():
	finalmark = 0
	hits = 0
	name = input("Name? ")
	for i in range(5):
		hit = input("Getroffen? ")
		if hit == "y" or hits == "ja":
			distance = int(input("Entfernung zum Korb? "))
			finalmark = mark(hits, distance)
			hits = hits + 1
	with open("marklist.csv", "a") as f:
		f.write(name + "," + str(hits) + "," + str(finalmark) + '\n')
	print("End program.")


if __name__ == __name__:
	main()
