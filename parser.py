import csv

def parse():
	volunteers = []
	managers = []

	with open("responses.csv") as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		
		# burns the first title line 
		csv_reader.__next__()

		# reads the rest of the informational lines
		for line in csv_reader:
			# checks if the 5th column contains the case-sensitive word "Volunteer"
			if "Volunteer" in line[4]:
				volunteers += line
			else:
				managers += line
				
	return volunteers, managers

def main():
	parse()

if __name__ == "__main__":
	main()

