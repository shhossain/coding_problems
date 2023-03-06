#include <iostream>
using namespace std;

int main(){
	int t;
	cin >> t;
	while(t--){
		int n;
		cin >> n;
		int arr[n];
		for (int i = 0; i < n;i++){
			cin >> arr[i];
		}

		int x = -1;
		for (int i = 0; i < n;i++)
			if (arr[i] < x || x == -1){
				x = arr[i];
			}
		
		// cout << x << endl;

		long long total = 0;
		for (int i = 0; i < n;i++){
			total += (arr[i] - x);
		}

		cout << total << endl;

	}
	
	

	return 0;
}