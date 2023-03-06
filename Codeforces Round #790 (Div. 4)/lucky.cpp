#include <iostream>
#include <string>
using namespace std;


int main(){
	int t;
	cin>>t;
	while(t--){
		string s;
		cin >> s;
		int x = 0;
		bool plus = true;
		for (int i = 0; i < 6; i++){
			if (plus){
				x+=int(s[i]);
			}
			else{
				x-=int(s[i]);

			}
			if (i==2){
				plus = false;
			}
		}
		if (x==0){
			cout << "YES";
		}
		else{
			cout << "NO";
		}
		cout << endl;
	}

}