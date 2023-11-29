#include <iostream>

const unsigned long BASE_INCOME_1 = 4000000;
const unsigned long BASE_INCOME_2 = 6000000;
const unsigned long BASE_INCOME_3 = 9000000;
const unsigned long BASE_INCOME_4 = 14000000;
const unsigned long BASE_INCOME_5 = 24000000;
const unsigned long BASE_INCOME_6 = 44000000;
const unsigned long BASE_INCOME_7 = 84000000;

const double TAX_RATE_1 = 0.05;
const double TAX_RATE_2 = 0.1;
const double TAX_RATE_3 = 0.15;
const double TAX_RATE_4 = 0.2;
const double TAX_RATE_5 = 0.25;
const double TAX_RATE_6 = 0.3;
const double TAX_RATE_7 = 0.35;

unsigned long calculateTax(unsigned long income) {
    unsigned long tax = 0;

    if (income <= BASE_INCOME_1) {
        tax = 0;
    }
    else if (income <= BASE_INCOME_2) {
        tax = (income - BASE_INCOME_1) * TAX_RATE_1;
    }
    else if (income <= BASE_INCOME_3) {
        tax = (BASE_INCOME_2 - BASE_INCOME_1) * TAX_RATE_1 + (income - BASE_INCOME_2) * TAX_RATE_2;
    }
    else if (income <= BASE_INCOME_4) {
        tax = (BASE_INCOME_2 - BASE_INCOME_1) * TAX_RATE_1 + (BASE_INCOME_3 - BASE_INCOME_2) * TAX_RATE_2 + (income - BASE_INCOME_3) * TAX_RATE_3;
    }
    else if (income <= BASE_INCOME_5) {
        tax = (BASE_INCOME_2 - BASE_INCOME_1) * TAX_RATE_1 + (BASE_INCOME_3 - BASE_INCOME_2) * TAX_RATE_2 + (BASE_INCOME_4 - BASE_INCOME_3) * TAX_RATE_3 + (income - BASE_INCOME_4) * TAX_RATE_4;
    }
    else if (income <= BASE_INCOME_6) {
        tax = (BASE_INCOME_2 - BASE_INCOME_1) * TAX_RATE_1 + (BASE_INCOME_3 - BASE_INCOME_2) * TAX_RATE_2 + (BASE_INCOME_4 - BASE_INCOME_3) * TAX_RATE_3 + (BASE_INCOME_5 - BASE_INCOME_4) * TAX_RATE_4 + (income - BASE_INCOME_5) * TAX_RATE_5;
    }
    else if (income <= BASE_INCOME_7) {
        tax = (BASE_INCOME_2 - BASE_INCOME_1) * TAX_RATE_1 + (BASE_INCOME_3 - BASE_INCOME_2) * TAX_RATE_2 + (BASE_INCOME_4 - BASE_INCOME_3) * TAX_RATE_3 + (BASE_INCOME_5 - BASE_INCOME_4) * TAX_RATE_4 + (BASE_INCOME_6 - BASE_INCOME_5) * TAX_RATE_5 + (income - BASE_INCOME_6) * TAX_RATE_6;
    }
    else {
        tax = (BASE_INCOME_2 - BASE_INCOME_1) * TAX_RATE_1 + (BASE_INCOME_3 - BASE_INCOME_2) * TAX_RATE_2 + (BASE_INCOME_4 - BASE_INCOME_3) * TAX_RATE_3 + (BASE_INCOME_5 - BASE_INCOME_4) * TAX_RATE_4 + (BASE_INCOME_6 - BASE_INCOME_5) * TAX_RATE_5 + (BASE_INCOME_7 - BASE_INCOME_6) * TAX_RATE_6 + (income - BASE_INCOME_7) * TAX_RATE_7;
    }

    return tax;
}

int main() {
    while (1)
    {
        unsigned long income;

        std::cout << "Enter income in million VND: ";
        std::cin >> income;

        unsigned long tax = calculateTax(income);

        std::cout << "Tax: " << tax << " million VND\n";


    }
    return 0;
}
