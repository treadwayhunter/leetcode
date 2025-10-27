class Solution {
public:
    bool isPalindrome(int x) {
        string s = to_string(x);
        bool isTrue = true;

        for (int i = 0; i < s.length()/2; i++) {
            if (s.at(i) != s.at(s.length() - (i + 1)))             {
                isTrue = false;
            }
        }

        return isTrue;
    }
};