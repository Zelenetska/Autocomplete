def binary_search(arr: list, target: str):
    start = 0
    end = len(arr) - 1

    while start <= end:
        middle = start + ((end - start) // 2)
        midpoint = arr[middle]
        if target in midpoint:
            curr_el = middle
            while target in midpoint:
                midpoint = arr[curr_el]
                curr_el -= 1
            possible_words = []
            for i in range(2, 7):
                midpoint = arr[curr_el + i]
                if target in midpoint:
                    possible_words.append(midpoint)
            return possible_words
        if midpoint > target:
            end = middle - 1
        elif midpoint < target:
            start = middle + 1
        else:
            return midpoint
    return 'Nothing found for your search'
