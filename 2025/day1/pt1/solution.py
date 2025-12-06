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
    dial = (dial + rotation) % 100
    print(dial)
    if dial == 0:
        password += 1

print("The password is", password)
