class Solution {
public:
    double Power(double base, int exponent) {
        if (exponent < 0){
            base = 1/base;
            exponent = -exponent;
        }

        double res = 1.0;
        for (int i=0;i<exponent;i++){
            res *= base;
        }
        return res;
    }
};

class Solution {
public:
    double Pow(double x, int y){
        double res = 1.0;

        while (y){
            if (y & 1)
                res *= x;
            x *= x;
            y = y >> 1;
        }

        return res;
    }

    double Power(double base, int exponent) {
        if (exponent < 0){
            base = 1/base;
            exponent = -exponent;
        }
        return Pow(base, exponent);
    }

};
