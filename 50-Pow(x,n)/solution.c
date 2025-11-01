#include <limits.h>

double myPow(double x, int n) {
    if (x == 0.0) return 0.0;
    if (x == 1.0) return 1.0;

    long long exp = n;
    double base = x;

    if (exp < 0) {
        base = 1.0 / base;
        exp = -exp;       
    }

    double result = 1.0;
    while (exp > 0) {
        if (exp & 1) {     
            result *= base;
        }
        base *= base;      
        exp >>= 1;         
    }

    return result;
}
