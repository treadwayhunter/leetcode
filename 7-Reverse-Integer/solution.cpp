class Solution {
public:
    int reverse(int x) {
  	    bool isNeg = false;

		if (x < 0) {
			isNeg = true;
		}
		
		std::string num = std::to_string(x);
		std::string num2;
		int y = 0;

		for (int i = num.length() - 1; i >= 0; i--) {
			num2.push_back(num.at(i));
		}

		try {
			y = std::stoi(num2);
			if (isNeg) {
				y = y * -1;
			}
		}
		catch (std::exception e) {
			//std::cout << "Num2 is out of bounds\n";
		}

		return y;
    }
};