with open("puzzle.txt") as f:
    id_ranges = [id_range.strip().split("-") for id_range in f.read().split(",")]

def is_sequence(number):
    number = str(number)
    number_len = len(number)
    if number_len < 2:
        return False
    for sub_len in range(1, number_len // 2 + 1):
        if number_len % sub_len != 0:
            continue
        substring = number[:sub_len]
        repeats = number_len // sub_len
        if substring * repeats == number:
            return True
    return False

total_invalid_ids = 0
for id_range in id_ranges:
    start_id = int(id_range[0])
    end_id = int(id_range[1])
    for i in range(start_id, end_id+1):
        if is_sequence(i):
            print("Found invalid id:", i)
            total_invalid_ids += i

print("The total number of invalid ids are:", total_invalid_ids)
