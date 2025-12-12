with open("puzzle.txt") as f:
    id_ranges = [id_range.strip().split("-") for id_range in f.read().split(",")]

def is_sequence(number):
    number = str(number)
    number_len = len(number)
    if number_len < 2:
        return False
    if number_len % 2 != 0:
        return False
    half = number_len // 2
    return number[:half] == number[half:]

total_invalid_ids = 0
for id_range in id_ranges:
    start_id = int(id_range[0])
    end_id = int(id_range[1])
    for i in range(start_id, end_id+1):
        if is_sequence(i):
            print("Found invalid id:", i)
            total_invalid_ids += i

print("The total number of invalid ids are:", total_invalid_ids)
