#include <iostream>
#include <fstream>
#include <sstream>

const int MAX_ROWS = 10;
const int MAX_COLS = 10;

bool isPrime(int number) {
    if (number <= 1) {
        return true;
    }
    for (int i = 2; i * i <= number; ++i) {
        if (number % i == 0) {
            return false;
        }
    }
    return true;
}

int sumOfPrimesInMatrix(int matrix[MAX_ROWS][MAX_COLS], int numRows, int numCols) {
    int sum = 0;
    for (int i = 0; i < numRows; ++i) {
        for (int j = 0; j < numCols; ++j) {
            if (isPrime(matrix[i][j])) {
                sum += matrix[i][j];
            }
        }
    }
    return sum;
}

void readMatrixFromFile(const std::string& filePath, int matrix[MAX_ROWS][MAX_COLS], int& numRows, int& numCols) {
    std::ifstream file(filePath);

    numRows = 0;
    std::string line;
    while (std::getline(file, line) && numRows < MAX_ROWS) {
        std::istringstream iss(line);
        numCols = 0;
        int value;
        while (iss >> value && numCols < MAX_COLS) {
            matrix[numRows][numCols] = value;
            ++numCols;
        }
        ++numRows;
    }

    file.close();
}

void writeSumOfPrimesToFile(const std::string& filePath, int sum) {
    std::ofstream output_file(filePath);
    output_file << "Sum of prime numbers in the matrix: " << sum << std::endl;
    output_file.close();
}

int main() {
    int matrix[MAX_ROWS][MAX_COLS] = {};
    int numRows, numCols;

    std::string filePath = "test.txt";
    readMatrixFromFile(filePath, matrix, numRows, numCols);
    for (int i = 0; i < numRows; ++i) {
        for (int j = 0; j < numCols; ++j) {
            std::cout << matrix[i][j] << " ";
        }
        std::cout << std::endl;
    }

    int sumOfPrimes = sumOfPrimesInMatrix(matrix, numRows, numCols);

    writeSumOfPrimesToFile("output.txt", sumOfPrimes);

    return 0;
}
