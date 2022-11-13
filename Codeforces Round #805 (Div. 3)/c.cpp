#include <iostream>
#include <map>
#include <vector>
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


// Loops
#define loop(n) for(int i = 0; i < n; i++)
#define range(a,b) for(int i = a; i < n; i++)
#define rangestep(a,b,step) for(int i = a; i <b; i+=step)

// Functions





main(){
	
	int t;
	cin>>t;
	while (t--){
		map<int,vector<int>> m;
		int n,q,x,a,b;
		cin >> n >> q;
		loop(n){
			cin >> x;
			m[x].push_back(i);
		}


		loop(q){
			i2(a,b);

			if (m[a].size() == 0 or m[b].size() == 0){
				NO;
				continue;
			}

			if (a==b){
				YES;
				continue;
			}

			if (m[b].back() > m[a].front()){
				YES;
			}
			else{
				NO;
			}


		}

	}
	return 0;
}