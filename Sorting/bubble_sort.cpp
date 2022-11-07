#include <iostream>
using namespace std;

void bubbleSort(int *arr, int n){



	for (int i=0; i<n; i++){
		bool swaped = false;
		for(int j =0; j < n-i; j++){
			if (arr[j] > arr[j+1]){
				swap(arr[j], arr[j+1]);
				swaped=true;
			}
		}

		if (swaped){
			break;
		}
	}
}


void printArray(int *arr,int n){
	for (int i=0; i<n; i++){
		cout << arr[i] << " ";
	}
}

int main(){
	
	int n;
	cin >> n;
	int a[n];

	for (int i = 0; i < n; ++i)
	{
		cin >> a[i];
	}

	bubbleSort(a,n);
	printArray(a,n);
	

	return 0;
}


