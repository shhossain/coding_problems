#include <iostream>
#include <vector>
using namespace std;

int main(){
	
	int n;
	cin >> n;

	vector<int> a(n,0);

	int x;
	cin >> x;
	for (int i = 0; i < x; ++i)
	{
		int v;
		cin >> v;
		a[v-1] = 1;
	}

	int y;
	cin >> y;
	for (int i = 0; i < y; ++i)
	{
		int v;
		cin >> v;
		a[v-1] = 1;
	}


	bool win = true;
	for (int i = 0; i < n; ++i)
	{
		if (a[i] != 1){
			win = false;
			break;
		}
	}

	if (win){
		cout << "I become the guy." << endl;
	}
	else{
		cout << "Oh, my keyboard!" << endl;
	}
	
	

	return 0;
}