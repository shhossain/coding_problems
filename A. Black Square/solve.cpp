#include <iostream>
#include <map>
using namespace std;

// INPUTS
//  Size 1 - 3
#define i1(a) cin >> a;
#define i2(a,b) cin >> a >> b;
#define i3(a,b,c) cin >> a >> b >> c;

// Size n
#define ivec(vec,n) for(int i = 0; i < n; i++){int x;i1(x);vec.push_back(x);}
#define iarr(arr,n) for(int i = 0; i < n; i++){int x;i1(x);arr[i]=x;}


// Outputs
#define YES cout << "YES" << endl;
#define NO cout << "NO" << endl;
#define print0(a) cout << a;
#define print(a) cout << a << endl;
#define print2(a,b) cout << a << " " << b << endl;
#define printArr(arr,n) for(int i=0;i<n;i++){cout<<arr[i]<<" ";}cout<<endl;


// Loops
#define loop(n) for(int i = 0; i < n; i++)
#define range(a,b) for(int i = a; i < n; i++)
#define rangestep(a,b,step) for(int i = a; i <b; i+=step)
#define rloop(s) for(auto i: s)




int main(){
	
	map<char,int> m={{'1',0},{'2',0},{'3',0},{'4',0}};
	cin >> m['1'] >> m['2'] >> m['3'] >> m['4'];

	string s;
	cin >> s;
	int ans = 0;
	for(auto i: s){
		ans += m[i];
	}

	cout << ans << endl;

	return 0;
}