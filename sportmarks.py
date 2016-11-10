#!/usr/bin/env python3


def mark(hits, distance):
	points = hits * 3
	return points


def main():
	name = input("Name? ")
	hits = int(input("Anzahl getroffen? "))
	distance = int(input("Entfernung zum Korb? "))
	finalmark = mark(hits, distance)
	with open("marklist.csv", "a") as f:
		f.write(name + " hits=" + str(hits) + " on distance=" + str(distance) + " equals final mark " + str(finalmark) + '\n')
	print("End program.")


if __name__ == __name__:
	main()
