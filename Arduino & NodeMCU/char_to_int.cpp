#include<iostream>
#include <string>

using namespace std;

float getValue(string str, int i, char endChar) {
    float n = 0;
    int pnt = 0, temp = 10, x;
    while (str[i] != endChar){
        cout << "(" << str[i] << "): ";
        x = str[i] - '0';
        if (str[i] == '.' && pnt == 0){
            pnt = 1;
            i++;
            continue;
        }
        
        if (pnt == 0) {
            n = n*10 + x;
        }
        else {
            n = n + ((float)x/(float)temp);
            temp = temp*10;
        }
        cout << "-->> " << n << "\n";
        i++;
    }
    return n;
}

int main()
{
    cout << "Hello World!\n";
    float speed, turn;
    string s = "mov(0.785, 0.955)";
    
    speed = getValue(s, 4, ',');
    cout << speed << "\n";
    
    int i=0;
    while(s[i] != ',')
        i++;
    i += 2;
    cout <<"\n [comma found at " << i << "]\n";
    turn = getValue(s, i, ')');
    cout << turn << endl;
    
    return 0;
}