# I want to be able to call nested_sum from main w/ various nested lists
# and I greatly desire that the function returns the sum.
# Ex. [1, 2, [3]]
# Verify you've tested w/ various nestings.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def nested_sum(nested_list):
	total = 0
	for item in nested_list:
		if isinstance(item, list):
			total += nested_sum(item)
		else:
			total += item
	return total

def main():

	list1 = [1, 2, [3, 4, 5], [6, 7]]
	list2 = [ [1.5, 2.5, 4.5, 5.5], [3, 3, 3] ]
	list3 = [1, 2, [3, 4, [5, 6, [7]]]]
	print("Nested sum of [1, 2, [3, 4, 5], [6, 7]]: ")
	print(nested_sum(list1))

	print("Nested sum of [ [1.5, 2.5, 4.5, 5.5], [3, 3, 3] ]: ")
	print(nested_sum(list2))

	print("Nested sum of [1, 2, [3, 4, [5, 6, [7]]]]: ")
	print(nested_sum(list3))


if __name__ == '__main__':
	main()