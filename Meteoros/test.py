# 2 4 5 1
x1, y1, x2, y2 = 2, 4, 5, 1

x, y = 1, 2


def FindPoint(x1, y1, x2, y2, x, y):
    # bottom left is x1, y1 and top right is x2, y2
    # check if x1, y1 is bottom left and x2, y2 is top right if not swap
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1

    if (x > x1 and x < x2 and
            y > y1 and y < y2):
        return True
    else:
        return False


print(FindPoint(x1, y1, x2, y2, x, y))

# cpp code in multiline string
cpp_code = """
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
    else
    {
        return false;
    }
}

int main()
{
    int x1, y1, x2, y2, x, y;
    cin >> x1 >> y1 >> x2 >> y2 >> x >> y;
    cout << findPoint(x1, y1, x2, y2, x, y);
    return 0;
}
"""