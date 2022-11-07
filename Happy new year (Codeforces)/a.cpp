#include <iostream>
using namespace std;

int main(){
	
	int n,k,v;
	cin>>n>>k;

	int ans = 0;
	int sum = 0;
	for (int i = 1; i <= n; ++i)
	{
		sum += 5 * i;
		if ((sum + k) < 240){
			ans++;
		}
		else if ((sum + k) == 240){
			ans++;
			break;
		}
		else{
			break;
		}
	}
	cout << ans << endl;
	

	return 0;
}