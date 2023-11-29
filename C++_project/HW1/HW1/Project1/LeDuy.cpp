#include <iostream>

int main() {
    while (true) {
        long amount;
        do {
            std::cout << "Enter the amount of money (must be multiple of 10,000, enter 0 to exit): ";
            std::cin >> amount;
        } while (amount % 10000 != 0 && amount != 0);

        if (amount == 0)
        {
            break;
        }
        long initialMoney = amount;

        int denominations[] = { 500000, 200000, 100000, 50000, 20000, 10000 };
        int quantities[6] = { 0 };  

        for (int i = 0; i < 6; ++i) {
            quantities[i] = amount / denominations[i];
            amount -= quantities[i] * denominations[i];
        }

        std::cout << "Result: " << initialMoney << "vnd = ";
        for (int i = 0; i < 6; ++i) {
            std::cout << quantities[i] << " * " << denominations[i];
            if (i < 5) {
                std::cout << " + ";
            }
        }
        std::cout << std::endl;
    }

    return 0;
}