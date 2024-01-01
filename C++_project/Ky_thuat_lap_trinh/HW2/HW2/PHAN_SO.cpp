//#include <iostream>
//
//struct Fraction {
//    int numerator;
//    int denominator;
//
//    Fraction() {
//
//    }
//
//    Fraction(int num, int denom) : numerator(num), denominator(denom) {
//        if (denominator == 0) {
//            exit(1);
//        }
//    }
//};
//
//int getGCD(int a, int b) {
//    while (b != 0) {
//        int temp = b;
//        b = a % b;
//        a = temp;
//    }
//    return a;
//}
//
//Fraction simplify(const Fraction& frac) {
//    Fraction result = frac;
//    int gcd = getGCD(result.numerator, result.denominator);
//    result.numerator /= gcd;
//    result.denominator /= gcd;
//    return result;
//}
//
//
//Fraction operator+(const Fraction& a, const Fraction& b) {
//    return simplify(Fraction(a.numerator * b.denominator + b.numerator * a.denominator, a.denominator * b.denominator));
//}
//
//Fraction operator-(const Fraction& a, const Fraction& b) {
//    return simplify(Fraction(a.numerator * b.denominator - b.numerator * a.denominator, a.denominator * b.denominator));
//}
//
//Fraction operator*(const Fraction& a, const Fraction& b) {
//    return simplify(Fraction(a.numerator * b.numerator, a.denominator * b.denominator));
//}
//
//Fraction operator/(const Fraction& a, const Fraction& b) {
//    return simplify(Fraction(a.numerator * b.denominator, a.denominator * b.numerator));
//}
//
//bool operator==(const Fraction& a, const Fraction& b) {
//    return (a.numerator * b.denominator == b.numerator * a.denominator);
//}
//
//bool operator!=(const Fraction& a, const Fraction& b) {
//    return !(a == b);
//}
//
//bool operator>(const Fraction& a, const Fraction& b) {
//    return (a.numerator * b.denominator > b.numerator * a.denominator);
//}
//
//bool operator<(const Fraction& a, const Fraction& b) {
//    return (a.numerator * b.denominator < b.numerator * a.denominator);
//}
//
//bool operator>=(const Fraction& a, const Fraction& b) {
//    return !(a < b);
//}
//
//bool operator<=(const Fraction& a, const Fraction& b) {
//    return !(a > b);
//}
//
//Fraction& operator+=(Fraction& a, const Fraction& b) {
//    a = a + b;
//    return a;
//}
//
//Fraction& operator-=(Fraction& a, const Fraction& b) {
//    a = a - b;
//    return a;
//}
//
//Fraction inputFraction() {
//    int num, denom;
//    std::cout << "Enter the numerator: ";
//    std::cin >> num;
//    std::cout << "Enter the denominator: ";
//    std::cin >> denom;
//    return Fraction(num, denom);
//}
//
//void outputFraction(const Fraction& output) {
//    std::cout << output.numerator << "/" << output.denominator;
//    std::cout << std::endl;
//}
//
//void inputFractionArray(Fraction fractionArray[], int size) {
//    for (int i = 0; i < size; ++i) {
//        Fraction temp = inputFraction();
//        fractionArray[i] = simplify(temp);
//    }
//}
//
//void outputFractionArray(const Fraction fractionArray[], int size) {
//    for (int i = 0; i < size; ++i) {
//        outputFraction(fractionArray[i]);
//    }
//}
//
//Fraction findLargestElement(const Fraction fractionArray[], int size) {
//    Fraction largest = fractionArray[0];
//
//    for (int i = 1; i < size; ++i) {
//        if (fractionArray[i] > largest) {
//            largest = fractionArray[i];
//        }
//    }
//    return largest;
//}
//
//Fraction calculateSum(const Fraction fractionArray[], int size) {
//    Fraction sum(0, 1);
//
//    for (int i = 0; i < size; ++i) {
//        sum += fractionArray[i];
//        sum = simplify(sum);
//    }
//    return sum;
//}
//
//void arrangeAscendingOrder(Fraction fractionArray[], int size) {
//    for (int i = 0; i < size - 1; ++i) {
//        for (int j = 0; j < size - i - 1; ++j) {
//            if (fractionArray[j] > fractionArray[j + 1]) {
//                Fraction temp = fractionArray[j];
//                fractionArray[j] = fractionArray[j + 1];
//                fractionArray[j + 1] = temp;
//            }
//        }
//    }
//}
//
//int main() {
//    Fraction a = inputFraction();
//    outputFraction(a);
//    Fraction b = inputFraction();
//    outputFraction(b);
//
//    Fraction sum = a + b;
//    Fraction difference = a - b;
//    Fraction product = a * b;
//    Fraction quotient = a / b;
//
//    std::cout << "Sum: ";
//    outputFraction(sum);
//    std::cout << "Sub: ";
//    outputFraction(difference);
//    std::cout << "Multiply: ";
//    outputFraction(product);
//    std::cout << "Division: ";
//    outputFraction(quotient);
//
//    std::cout << "Comparison ==: " << (a == b) << std::endl;
//    std::cout << "Comparison !=: " << (a != b) << std::endl;
//    std::cout << "Comparison >: " << (a > b) << std::endl;
//    std::cout << "Comparison <: " << (a < b) << std::endl;
//    std::cout << "Comparison >=: " << (a >= b) << std::endl;
//    std::cout << "Comparison <=: " << (a <= b) << std::endl;
//
//    a += b;
//    std::cout << "After a += b: ";
//    outputFraction(a);
//
//    a -= b;
//    std::cout << "After a -= b: ";
//    outputFraction(a);
//
//    int size;
//    std::cout << "Enter the size of the array: ";
//    std::cin >> size;
//
//    Fraction* fractionArray = new Fraction[size];
//
//    inputFractionArray(fractionArray, size);
//
//    std::cout << "\nLargest element:";
//    outputFraction(findLargestElement(fractionArray, size));
//
//    std::cout << "\Sum of elements:";
//    outputFraction(calculateSum(fractionArray, size));
//
//    arrangeAscendingOrder(fractionArray, size);
//    std::cout << "\Arrange ascending order:\n";
//    outputFractionArray(fractionArray, size);
//
//    return 0;
//}
