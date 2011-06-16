#! /usr/bin/env python
import csv

def main():
	with open('test.csv', 'r') as f:
		test_reader = csv.reader(f)
		for row in test_reader:
			print row

	with open('test.csv', 'a') as f:
		test_writer = csv.writer(f)
		test_writer.writerow(['adam','89','mauve'])

if __name__ == "__main__":
	main()
