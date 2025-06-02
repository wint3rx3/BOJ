#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>

using namespace std;

int main() {
    int N, M;
    cin >> N >> M;
    vector<string> sequences(N);
    for (int i = 0; i < N; i++) {
        cin >> sequences[i];
    }
    string result = "";
    int distance_sum = 0;

    for (int i = 0; i < M; i++) {
        unordered_map<char, int> count;
        for (const auto& seq : sequences) {
            count[seq[i]]++;
        }
        char max_nucleotide = 'A';
        for (const auto& pair : count) {
            if (pair.second > count[max_nucleotide] || (pair.second == count[max_nucleotide] && pair.first < max_nucleotide)) {
                max_nucleotide = pair.first;
            }
        }
        result += max_nucleotide;
        distance_sum += N - count[max_nucleotide];
    }

    cout << result << endl;
    cout << distance_sum << endl;
    return 0;
}