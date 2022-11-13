#include <iostream>
#include <map>
using namespace std;
#define MAX  1000
  

int multiplyx(int x, int ans[], int size) 
{ 
    int carry = 0;   
    for (int i=0; i<size; i++) 
    { 
        int product = ans[i] * x + carry; 
        ans[i] = product % 10;   
        carry  = product/10;     
    } 
  
    while (carry) 
    { 
        ans[size] = carry%10; 
        carry = carry/10; 
        size++; 
    } 
    return size; 
} 
  

map<int,long long> m;
void factorial(int n) 
{ 
    int ans[MAX]; 
    ans[0] = 1; 
    int size = 1; 
    for (int x=2; x<=n; x++) 
        size = multiplyx(x, ans, size); 
    for (int i=size-1; i>=0; i--) 
        cout << ans[i]; 
} 
  	
int main() {
	
	factorial(100);
	return 0;
}