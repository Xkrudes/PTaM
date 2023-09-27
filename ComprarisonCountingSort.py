import random


def Sort(arr):
    nop = 0
    size = len(arr)
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1 # Range of values
    
    counting_arr = [0] * range_of_elements # Array that counts the number of occurrences of elements
    output_arr = [0] * size # Result array
    
    for i in range(size):
        nop += 1
        counting_arr[arr[i] - min_val] += 1 
    
    for i in range(1, len(counting_arr)): # calculating the positions of elements in a sorted array
        nop += 1
        counting_arr[i] += counting_arr[i - 1]
    
    for i in range(size):
        nop += 1
        output_arr[counting_arr[arr[i] - min_val] - 1] = arr[i]
        counting_arr[arr[i] - min_val] -= 1

    nop += 1
    return nop


def genData(n):
    numbers = []

    for i in range(n):
        numbers.append(random.randrange(10000))
    
    return numbers


if __name__ == "__main__":
    presets = [500, 1000, 3000, 5000, 8000, 10000, 20000, 30000]
    
    for preset in presets:
        arr = genData(preset)
        nop = Sort(arr)
        print(f"N={preset} nop={nop}")