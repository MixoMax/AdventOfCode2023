//Advent of Code 2023 Day 1 Part 1

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(int argc, char *argv[]) {

    long long sum = 0;

    ifstream input_lines_file("./data.txt");
    string line;

    if (!input_lines_file.is_open()) { //check if we can open the input file
        cout << "Could not open ./data.txt" << endl;
        return 1;
    }

    while(std::getline(input_lines_file, line)) {
        string left;
        string right;
        
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
        
        string num = left + right;

        sum += atoi(num.c_str());

    }

    cout << sum << endl; // -> 54634

    input_lines_file.close();
    return sum;

}