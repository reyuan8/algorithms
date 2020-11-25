def find_smallest_ind(arr: list) -> int:
	smallest = arr[0]
	smallest_ind = 0
	for i in range(len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
			smallest_ind = i
	return smallest_ind

def selection_sort(arr: list) -> list:
	new_arr = []
	for i in range(len(arr)):
		ind = find_smallest_ind(arr)
		new_arr.append(arr.pop(ind))
	return new_arr