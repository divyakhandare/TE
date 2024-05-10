#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <regex>
#include <cstdlib>
using namespace std;

unordered_map<string, vector<string>> responses = {
    {"greeting", {"Welcome to our grocery store! How can we assist you today?", "Hi there! How may I help you with your grocery needs?", "Hello and welcome! What can we help you find today?"}},
    {"farewell", {"Thank you for choosing us for your grocery needs. Have a wonderful day!", "Your satisfaction is important to us. Goodbye and take care!", "If you have any more questions, feel free to ask. Have a great day!"}},
    {"help", {"Sure, I'm here to assist you. What items are you looking for?", "How can I help you with your grocery shopping today? Please let me know.", "I'm here to provide the best service for your grocery needs. What can I assist you with?"}},
    {"out_of_stock", {"I'm sorry, but it seems we're currently out of stock for that item. Is there anything else you need?", "Unfortunately, we're temporarily out of stock for that item. Can I suggest an alternative?", "We apologize, but the item you're looking for is currently unavailable. Would you like assistance finding a substitute?"}},
    {"special_offer", {"We have some exciting special offers available today! Let me tell you about them.", "Great news! We're running special promotions on select items. Would you like to know more?", "You're in luck! We have exclusive discounts on certain products today. Interested in learning more?"}},
    {"store_hours", {"Our store is open from 9am-9pm. Feel free to visit us during our operating hours.", "Our store is open seven days a week from 9am-9pm. We look forward to seeing you!", "You can visit us anytime during our operating hours, which are 9am-9pm."}},
    {"location", {"We're located at Katraj. Come visit us soon!", "Our store is conveniently located at Katraj. We hope to see you soon!", "You can find us at Katraj. We're here to serve you!"}},
    {"default", {"I apologize, but I couldn't understand your request.", "Sorry, I didn't quite catch that. Could you please provide more details?", "I'm here to assist you. Can you please clarify your inquiry?"}}
};

string respond_to_inquiry(string inquiry) {
    transform(inquiry.begin(), inquiry.end(), inquiry.begin(), ::tolower);
    if (regex_search(inquiry, regex("\\b(?:hello|hi)\\b"))) {
        return responses["greeting"][rand() % responses["greeting"].size()];
    } else if (regex_search(inquiry, regex("\\b(?:goodbye|bye)\\b"))) {
        return responses["farewell"][rand() % responses["farewell"].size()];
    } else if (regex_search(inquiry, regex("\\b(?:help|support)\\b"))) {
        return responses["help"][rand() % responses["help"].size()];
    } else if (regex_search(inquiry, regex("\\b(?:unavailable|alternative|find)\\b"))) {
        return responses["out_of_stock"][rand() % responses["out_of_stock"].size()];
    } else if (regex_search(inquiry, regex("\\b(?:discounts|offers|sale|substitute)\\b"))) {
        return responses["special_offer"][rand() % responses["special_offer"].size()];
    } else if (regex_search(inquiry, regex("\\b(?:timing|open|close|opens|closes)\\b"))) {
        return responses["store_hours"][rand() % responses["store_hours"].size()];
    } else if (regex_search(inquiry, regex("\\b(?:where|location)\\b"))) {
        return responses["location"][rand() % responses["location"].size()];
    } 
    else {
        return responses["default"][rand() % responses["default"].size()];
    }
}

int main() {
    cout << "Welcome to the Customer Interaction Chatbot!" << std::endl;
    cout << "Type 'exit' to end the conversation." << std::endl;
    while (true) {
        string user_input;
        cout << "Customer: ";
        getline(cin, user_input);
        if (user_input == "exit") {
            break;
        }
        string bot_response = respond_to_inquiry(user_input);
        cout << "Chatbot: " << bot_response <<endl;
    }
    cout << "Thank you for using the Customer Interaction Chatbot. Goodbye!" <<endl;
    return 0;
}
