#include <iostream>
using namespace std;


void swap(int& a, int& b) {
	int temp = a;	
	a = b;
	b = temp;
}


void selectionSort(int *arr,int n){
	for (int i=0; i<n-1; i++){
		int minIndex = i;

		for(int j = i+1; j<n; j++){
			if (arr[j] < arr[minIndex]){
				minIndex = j;
			}
		}

		swap(arr[minIndex],arr[i]);
	}
}


void bubbleSort(int *arr, int n){
	for (int i=0; i<n; i++){

		for(int j =0; j < n-i; j++){
			if (arr[j] > arr[j+1]){
				swap(arr[j], arr[j+1]);
			}
		}
	}
}




int main() {

	int n;
	cin >> n;
	int a[n];
	for (int i = 0; i < n; i++){
		cin >> a[i];
	}
	selectionSort(a,n);
	for (int i=0;i<n;i++){
		cout << a[i] << " ";
	}

	// bubbleSort(a,n);
	// for (int i=0;i<n;i++){
	// 	cout << a[i] << " ";
	// }


}