//Advent of Code 2023 Day 1 Part 1

#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>

//using namespace std;


std::string replace(std::string input_str, std::string old_str, std::string new_str) {
    size_t pos = 0;
    while ((pos = input_str.find(old_str, pos)) != std::string::npos) {
         input_str.replace(pos, old_str.length(), new_str);
         pos += new_str.length();
    }
    return input_str;
}


int main(int argc, char *argv[]) {

    std::map<std::string, std::string> number_dict = {
        {"oneight", "18"},
        {"twone", "21"},
        {"threeight", "38"},
        {"fiveight", "58"},
        {"sevenine", "79"},
        {"eightwo", "82"},
        {"eighthree", "83"},
        {"nineight", "98"},
        {"one", "1"},
        {"two", "2"},
        {"three", "3"},
        {"four", "4"},
        {"five", "5"},
        {"six", "6"},
        {"seven", "7"},
        {"eight", "8"},
        {"nine", "9"}
    };

    long long sum = 0;

    std::ifstream input_lines_file("./data.txt");
    std::string line;

    if (!input_lines_file.is_open()) { //check if we can open the input file
        std::cout << "Could not open ./data.txt" << std::endl;
        return 1;
    }

    while(std::getline(input_lines_file, line)) {

        for (auto& item: number_dict) {
            line = replace(line, item.first, item.second);
        }


        std::string left;
        std::string right;
        
        //loop through string line from left to right and assign the first char that is in nums to left
        for (int i = 0; i < line.size(); i++){
            if (isdigit(line[i])) {
                left = line[i];
                break;
            }
        }

        //do the same from right to left
        for (int i = line.size(); i >= 0; i--) {
            if (isdigit(line[i])) {
                right = line[i];
                break;
            }
        }
        
        std::string num = left + right;

        sum += atoi(num.c_str());

    }

    std::cout << sum << std::endl; // -> 54634 WRONG, it should be lower

    input_lines_file.close();
    return sum;

}