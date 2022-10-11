#include <iostream>
using namespace std;

bool findPoint(int x1, int y1, int x2, int y2, int x, int y)
{
	// bottom left is x1, y1 and top right is x2, y2
	// check if x1, y1 is bottom left and x2, y2 is top right if not swap

	if (x1 > x2)
	{
		int temp = x1;
		x1 = x2;
		x2 = temp;
	}
	if (y1 > y2)
	{
		int temp = y1;
		y1 = y2;
		y2 = temp;
	}

	if ((x > x1 && x < x2) &&
		(y > y1 && y < y2))
	{
		return true;
	}
	// if x,y in the line
	else if ((x == x1 || x == x2) && (y >= y1 && y <= y2))
	{
		return true;
	}
	else if ((y == y1 || y == y2) && (x >= x1 && x <= x2))
	{
		return true;
	}
	else
	{
		return false;
	}
}

int main()
{
	int testCases = 1;
	while (1)
	{
		int x1, y1, x2, y2;
		cin >> x1 >> y1 >> x2 >> y2;
		if (x1 == 0 && y1 == 0 && x2 == 0 && y2 == 0)
		{
			break;
		}

		int n, count = 0;
		cin >> n;
		for (int i = 0; i < n; i++)
		{
			int x, y;
			cin >> x >> y;
			if (findPoint(x1, y1, x2, y2, x, y))
			{
				count++;
			}
		}
		// Teste 1

		cout << "Teste " << testCases << endl;
		cout << count;
		testCases++;
	}
}