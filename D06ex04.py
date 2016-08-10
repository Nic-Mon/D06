
def read_e_and_write(filename):
	fin = open(filename, 'r')
	lines = fin.readlines()
	e_names = []
	count = 0

	for line in lines:
		if 'e' in line.split()[0] or 'E' in line.split()[0]:
			count += 1
			e_names.append(line.split()[0])

	fout = open("Names with e.txt", 'w')
	fout.write("Number of Names that contain e: " + str(count) + '\n')
	for name in e_names:
		fout.write(name + '\n')

	fin.close()
	fout.close()

def main():
	
	read_e_and_write("roster.txt")

if __name__ == '__main__':
	main()