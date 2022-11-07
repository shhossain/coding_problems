#include <iostream>
using namespace std;

int main(){
	
	int n,a;
	cin >> n;
	while(n--){
		cin >> a;
		string s;
		cin >> s;

		int q=0;
		int a=0;

		for (char c: s){
			if (c == 'Q'){
				q++;
			}
			else{
				if (q > 0){
					q--;
				}
			}
		}

		if (q){
			cout << "No" << endl;
		}
		else{
			cout << "Yes" << endl;
		}


	}
	
		

	return 0;
}