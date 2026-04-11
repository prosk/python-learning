# task from https://yandex.ru/jobs/interview/algorithms
def max_ones_sequence(arr):
    current_count = 0
    max_count = 0
    
    for num in arr:
        if num == 1:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0
    return max_count

print(max_ones_sequence([0, 1, 1, 0, 1, 1, 1, 0, 1, 1]))
print(max_ones_sequence([0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1]))
print(max_ones_sequence([0, 1]))
print(max_ones_sequence([0, 0]))