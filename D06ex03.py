
def read_e(filename):
	fin = open(filename, 'r')
	lines = fin.readlines()
	e_names = []
	count = 0

	for line in lines:
		if 'e' in line.split()[0] or 'E' in line.split()[0]:
			count += 1
			e_names.append(line.split()[0])

	print("Number of Names that contain e: " + str(count))
	print(e_names)

def main():
	
	read_e("roster.txt")

if __name__ == '__main__':
	main()