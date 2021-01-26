// cpp program to implement Luhn algorithm 
#include <bits/stdc++.h> 
using namespace std; 
  
// Returns true if given card number is valid 
bool checkLuhn(const string& cardNo) 
{ 
    int nDigits = cardNo.length(); 
  
    int nSum = 0, isSecond = false; 
    for (int i = nDigits - 1; i >= 0; i--) { 
  
        int d = cardNo[i] - '0'; 
  
        if (isSecond == true) 
            d = d * 2; 
  
        // We add two digits to handle 
        // cases that make two digits after 
        // doubling 
        nSum += d / 10; 
        nSum += d % 10; 
  
        isSecond = !isSecond; 
    } 
    return (nSum % 10 == 0); 
} 
  

// Driver code 
int main() 
{ 
    string cardNo = "79927398713"; 
    if (checkLuhn(cardNo)) 
        printf("This is a valid card"); 
    else
        printf("This is not a valid card"); 

    for(long long credit = 5432100000001234; credit <= 543219999991234; credit++){
        if(credit % 123457){
            cout<<credit<<" ";
        }
    }
    return 0; 
} 

