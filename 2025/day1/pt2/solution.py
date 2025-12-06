def interpret_rotation(rotation):
    if rotation[0] == "L":
        rotation = int(rotation[1:]) * -1
    else:
        rotation = int(rotation[1:])
    return rotation

with open("puzzle.txt") as f:
    rotations = [interpret_rotation(rotation.strip()) for rotation in f.readlines()]

dial = 50
password = 0
print(dial)
for rotation in rotations:
    direction = -1 if rotation < 0 else 1
    for step in range(abs(rotation)):
        dial = (dial + direction) % 100
        if dial == 0:
            password += 1
    print(dial)

print("The password is", password)
