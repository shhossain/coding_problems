#include <stdio.h>

int main()
{
    int n, k;
    scanf("%d %d", &n, &k);
    int t = 0;
    for (int i = 0; i < n; i++)
    {
        int c;
        scanf("%d", &c);
        if ((5 - c) >= k)
        {
            t++;
        }
    }
    printf("%d \n", t / 3);
    return 0;
}