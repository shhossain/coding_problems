#include <bits/stdc++.h>
using namespace std;

void display(int a[], int n)
{
    for (int i = 0; i < n; i++)
    {
        cout << a[i] << " ";
    }
    cout << endl;
}

// Function to find the permutations
void findPermutations(int a[], int n)
{

    // Sort the given array
    sort(a, a + n);

    // Find all possible permutations
    cout << "Possible permutations are:\n";
    do
    {
        display(a, n);
    } while (next_permutation(a, a + n));
}

// function to print the divisors
void printDivisors(int n)
{
    int arr[n];
    for (int i = 1; i <= n; i++)
        if (n % i == 0)
            arr[i] = i;
    
    
    
    findPermutations(arr, n);
}

/* Driver program to test above function */
int main()
{
    printDivisors(14);
    return 0;
}