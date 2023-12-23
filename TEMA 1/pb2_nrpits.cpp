#include <iostream>
#include <fstream>
#include <vector>
#include <stack>

void solve(const std::vector<int>& sir) {
    const int max = 1000001;
    int count_pits = 0;
    std::stack<int> stack;
    stack.push(max);

    for (int a : sir) {
        while (a > stack.top()) {
            stack.pop();
            if (stack.size() > 1) {
                count_pits++;
            }
        }
        stack.push(a);
    }

    std::ofstream outfile("nrpits.out");
    outfile << count_pits;
    outfile.close();
}

int main() {
    std::ifstream infile("nrpits.in");
    int n;
    infile >> n;

    std::vector<int> sir(n);
    for (int i = 0; i < n; ++i) {
        infile >> sir[i];
    }

    infile.close();
    solve(sir);

    return 0;
}
