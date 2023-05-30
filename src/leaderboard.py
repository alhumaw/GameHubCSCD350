

def set_score(score, game):
    with open(game+".txt", "a") as f:
        f.write(score)
        sort(game+".txt")

def read_score(file):
    with open(file, "r") as f:
        f.read(file)

def sort(file):
    walk = open(file)
    nums = []
    for line in walk:
        temp = line.split()
        for i in temp:
            nums.append(i)
    walk.close()
    nums.sort(reverse=True)

    with open(file, "w") as f:
        for i in nums:
            f.write(i)



