#include <iostream>
using namespace std;

int main(){

	int t;
	cin >> t;
	while (t--){
		int n;
		cin >> n;
		int arr[n]={0};
		

		for(int i = 0; i < n; i++){
			int x;
			cin >> x;
			if (arr[x] == 0){
				cout << x << " ";
				arr[x]++;
			}
		}
		cout << endl;
	}

}