#include <iostream>
#include <fstream>
#include <queue>
#include <vector>

using namespace std;

long long solutie(int n, int p) {
    vector<int> cifre = {2, 3, 5, 7};
    vector<bool> viz(5000005, false); // Inițializăm un array boolean pentru a ține evidența resturilor vizitate
    queue<long long> q;
    q.push(0);

    while (!q.empty()) {
        long long a = q.front();
        q.pop();

        if (!viz[a % p]) {
            if (a % p == n) {
                return a;
            }

            viz[a % p] = true;
            for (int cifra : cifre) {
                q.push(10 * a + cifra);
            }
        }
    }

    return -1;
}

int main() {
    ifstream in("cifre4.in");
    ofstream out("cifre4.out");
    int t, n, p;
    in >> t;

    while (t--) {
        in >> n >> p;
        long long result = solutie(n, p);
        out << result << endl;
    }

    in.close();
    out.close();
    return 0;
}
