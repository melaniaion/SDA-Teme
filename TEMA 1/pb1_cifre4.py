from queue import Queue

def solutie(n, p):
    cifre = [2, 3, 5, 7]
    viz = [0 for i in range(5000005)]  # Inițializăm un array boolean pentru a ține evidența resturilor vizitate
    q = Queue()
    q.put(0)

    while not q.empty():
        a = q.get()
        
        if not viz[a % p]:
            if a % p == n:
                return a  

            viz[a % p] = 1
            for cifra in cifre:
                q.put(10 * a + cifra)

    return -1  

sol = list()
with open("cifre4.in", "r") as file:
    t = int(file.readline().strip())
    for i in range(t):
        n, p = map(int, file.readline().strip().split())
        result = solutie(n, p)
        sol.append(result)
        
with open("cifre4.out", "w") as file:
    for c in sol:
        file.write(str(c) + "\n")
