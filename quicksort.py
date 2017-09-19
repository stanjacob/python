
def quicksort(arr, lo, hi):
	if lo < hi:
		p = partition(arr, lo, hi)
		quicksort(arr, lo, p)
		quicksort(arr, p + 1, hi)

def partition(arr, lo, hi):
	pivot = arr[lo]
	i = lo - 1
	j = hi + 1
	while True:
		i += 1
		while arr[i] < pivot:
			i += 1

		j -= 1
		while arr[j] > pivot:
			j -= 1

		if i >= j:
			return j;

		swap_list(arr, i, j)

def swap_list(arr, i, j):
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp

def main():
	some_nums = [1, 43, 2, 3, 42, 343, 24234, 43, 24, 20]
	quicksort(some_nums, 0, len(some_nums)-1)
	print some_nums

main()
