def binary_search(arr: list, item: int, low: int = 0, high: int = None) -> int:
    if high is None:
        high = len(arr) - 1
    mid = (low + high) // 2
    guess = arr[mid]
    if low > high:
        return None
    if guess == item:
        return mid
    if guess > item:
        high = mid - 1
        return binary_search(arr, item, low, high)
    elif guess < item:
        low = mid + 1
        return binary_search(arr, item, low, high)