#include <iostream>
using namespace std;

int binary_search(int arr[], int size,int key){
	int start = 0;
	int end = size - 1;

	while (start <= end){
		int mid = (end+start)/2;
		int arr_mid = arr[mid];

		if (arr_mid == key){
			return mid;
		}
		else if (arr_mid < key){
			start = mid + 1;
		}
		else if(arr_mid > key){
			end = mid - 1 ;
		}
	}

	return -1;
}

int binary_search_desc(int arr[], int size,int key){
	int start = 0;
	int end = size - 1;

	while (start <= end){
		int mid = (end+start)/2;
		int arr_mid = arr[mid];

		if (arr_mid == key){
			return mid;
		}
		else if (arr_mid > key){
			start = mid + 1;
		}
		else if(arr_mid < key){
			end = mid - 1 ;
		}
	}

	return -1;
}


int main(){
	
	int n,f;
	cin >> n >> f;
	int a[n];
	int d[n];
	for (int i = 0; i < n; ++i)
	{
		cin >> a[i];
	}
	for (int i = 0; i < n; ++i)
	{
		cin >> d[i];
	}

	cout << binary_search(a,n,f) << endl;
	cout << binary_search_desc(d,n,f) << endl;

	return 0;
}