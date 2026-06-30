#include <iostream>
#include <vector>

void printVector(int v[], int n) {
    for (int i = 0; i < n; i++) {
        std::cout << v[i] << (i == n - 1 ? "" : " ");
    }
    std::cout << std::endl;
}

void shellSort(int v[], int n) {
    for (int gap = n / 2; gap > 0; gap /= 2) {
        for (int i = gap; i < n; i += 1) {
            int temp = v[i];
            int j;
            for (j = i; j >= gap && v[j - gap] > temp; j -= gap) {
                v[j] = v[j - gap];
            }
            v[j] = temp;
        }
    }
}

int main() {
    int v[] = {49, 38, 58, 87, 34, 93, 26, 13};
    int n = sizeof(v) / sizeof(v[0]);

    std::cout << "Vetor antes da ordenação:" << std::endl;
    printVector(v, n);

    shellSort(v, n);

    std::cout << "\nVetor após a ordenação (Shell Sort):" << std::endl;
    printVector(v, n);

    return 0;
}
