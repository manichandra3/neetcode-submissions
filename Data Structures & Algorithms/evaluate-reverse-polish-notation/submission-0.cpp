class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        std::stack<int> stack;
        for(const auto& token : tokens) {
            if (std::isdigit(token.back())) {
                stack.push(std::stoi(token));
            } else {
                int b = stack.top();
                stack.pop();
                int a = stack.top();
                stack.pop();
                
                if (token == "+") {
                    stack.push(a + b);
                } else if (token == "-") {
                    stack.push(a - b);
                } else if (token == "*") {
                    stack.push(a * b);
                } else if (token == "/") {
                    stack.push(a / b);
                } else {
                    throw std::invalid_argument("Unknown operator");
                }
            }
        }
        return stack.top();
    }
};
