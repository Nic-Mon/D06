import random

def write_ten_rand_num(filename):
	fout = open(filename, 'w')

	for num in range(0,10):
		#writes 10 random ints from 1 to 100
		fout.write(str(random.randint(1,100)) + '\n')


def main():

	write_ten_rand_num("Ten Random Numbers.txt")


if __name__ == '__main__':
	main()