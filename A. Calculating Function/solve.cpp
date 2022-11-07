#include <iostream>
using namespace std;

int main(){
	
	long long a;
	cin >> a;
	long long v = a/2;

	long long ans;
	if (a%2==0){
		ans = -v + a;
	}
	else{
		ans = v - a;
	}

	cout << ans << endl;
	
	return 0;
}