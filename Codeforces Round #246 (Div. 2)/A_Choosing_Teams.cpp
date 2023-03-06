#include <iostream>
using namespace std;

int main(){
	int n,k;
	cin >> n >> k;
	int t = 0;
	for(int i = 0; i < n; i++){
		int c;
		cin >> c;
		if ((5-c) >= k){
			t++;
		}
	}
	cout << t/3 << endl;

}