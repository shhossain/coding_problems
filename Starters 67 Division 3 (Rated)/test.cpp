#include <iostream>
#include <vector>
using namespace std;


class Solution {
  public:
    int arrayOperations(int n, vector<int> &arr) {
        int op=0;
        int c=0;
        for (auto i: arr){
            if (arr[i]==0){
                op++;
            }
            c = arr[i];
        }
        
        if (c!=0){
            op++;
        }
        
        return op;
    }
};


// { Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        
        int n;
        cin>>n;
        
        
        vector<int> arr(n);
        for(int i=0;i<n;i++){
            cin>>arr[i];
        }
        
        Solution obj;
        int res = obj.arrayOperations(n, arr);
        
        cout<<res<<endl;
        
    }
}
  // } Driver Code Ends