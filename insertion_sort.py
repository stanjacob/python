
import random

def insertion_sort(list_nums):
	i = 1
	while i < len(list_nums):
		current_num = list_nums[i]
		j = i - 1
		while j >= 0 and list_nums[j] > current_num:
			list_nums[j + 1] = list_nums[j]
			j -= 1
		list_nums[j+1] = current_num
		i += 1

def main():
	rand_numbers = []
	for i in range(10):
		temp = random.randint(1, 100)
		rand_numbers.append(temp)
	print rand_numbers
	insertion_sort(rand_numbers)
	print rand_numbers

main()

