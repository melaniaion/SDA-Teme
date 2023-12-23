def count_pits(sir):
    max = 1000001
    nrpits = 0
    stack = [max]

    for i in range(n):
        a = sir[i]
        while a > stack[-1]:
            stack.pop()
            if len(stack) > 1:
                nrpits = nrpits + 1
        stack.append(a)

    with open("nrpits.out", "w") as file:
        file.write(str(nrpits))


with open("nrpits.in", "r") as file:
    n = int(file.readline().strip())
    sir = [int(x) for x in file.readline().strip().split()]
    count_pits(sir)
        