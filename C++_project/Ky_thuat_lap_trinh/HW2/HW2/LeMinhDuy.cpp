#include <iostream>

void inputArray(int*& arr, int& size) {
    std::cout << "Enter the size of the array: ";
    std::cin >> size;

    arr = new int[size];

    std::cout << "Enter " << size << " integers for the array:" << std::endl;
    for (int i = 0; i < size; ++i) {
        std::cout << "Number " << i + 1 << ": ";
        std::cin >> arr[i];
    }
}

void outputArray(const int* arr, int size) {
    std::cout << "Array elements include: ";
    for (int i = 0; i < size; ++i) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
}

int sumOfEvenElements(const int* arr, int size) {
    int sum = 0;
    for (int i = 0; i < size; ++i) {
        if (arr[i] % 2 == 0) {
            sum += arr[i];
        }
    }
    return sum;
}

int productOfOddPositionedElements(const int* arr, int size) {
    int product = 1;
    for (int i = 0; i < size; i += 2) {
        product *= arr[i];
    }
    return product;
}

int main() {
    int* myArray = nullptr;
    int size;

    inputArray(myArray, size);
    outputArray(myArray, size);

    int evenSum = sumOfEvenElements(myArray, size);
    std::cout << "Sum of even elements: " << evenSum << std::endl;

    int oddPositionedProduct = productOfOddPositionedElements(myArray, size);
    std::cout << "Product of odd-positioned elements: " << oddPositionedProduct << std::endl;

    delete[] myArray;

    return 0;
}
