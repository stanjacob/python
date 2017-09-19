def get_kth_elem():


def median(list_nums):

	if len(list_nums) == 1:
		return list_nums[0]

	if len(list_nums) < 6:
		list_nums = merge_sort(list_nums)
		mid_index = len(list_nums) / 2
		if len(list_nums) % 2 != 0:
			return list_nums[mid_index]
		else:
			return (list_nums[mid_index] + list_nums[mid_index - 1]) / 2

	# Group list into subset of 5
	broken_lists = []
	break_len = 5
	curr_size = len(list_nums)
	i = 0
	while True:
		if curr_size == 0:
			break
		elif curr_size < break_len:
			broken_lists.append(list_nums[i:(i+curr_size)])
			break
		else:
			broken_lists.append(list_nums[i:(i+break_len)])
		curr_size -= break_len
		i += break_len
	
	new_list = []
	for i in range(len(broken_lists)):
		curr_med = median(broken_lists[i])
		new_list.append(curr_med)

	pivot = median(new_list)
	reordered_list = []
	num_inserts = 0

	for i in range(curr_size):
		if list_nums[i] < pivot:
			reordered_list.insert(0, list_nums[i])
			num_inserts += 1
		else:
			reordered_list.append(list_nums[i])

	ind = num_inserts + 1;
	if ind == k:
		return list_nums[ind]
	elif ind < k:
		return median(list_nums[1:k-1], ind)
	elif ind > k:
		return median(list_nums[k+1:ind], ind-k)
