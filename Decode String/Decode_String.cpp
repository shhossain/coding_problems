#include <iostream>
#include <map>
using namespace std;

map<string, char> letter_map = {{"1", 'a'}, {"2", 'b'}, {"3", 'c'}, {"4", 'd'}, {"5", 'e'}, {"6", 'f'}, {"7", 'g'}, {"8", 'h'}, {"9", 'i'}, {"10", 'j'}, {"11", 'k'}, {"12", 'l'}, {"13", 'm'}, {"14", 'n'}, {"15", 'o'}, {"16", 'p'}, {"17", 'q'}, {"18", 'r'}, {"19", 's'}, {"20", 't'}, {"21", 'u'}, {"22", 'v'}, {"23", 'w'}, {"24", 'x'}, {"25", 'y'}, {"26", 'z'}};

int main()
{
	int runs;
	cin >> runs;
	for (int i = 0; i < runs; i++)
	{
		int size;
		cin >> size;
		string encoded;
		cin >> encoded;
		string decoded = "";
		int j = 0;
		while (j < size)
		{
			int lt = encoded[j] - '0';
			if (lt != 0)
			{
				decoded += letter_map[encoded.substr(j, 1)];
				j += 1;
			}
			else
			{
				int e = j + 1;
				if (e < size)
				{
					if (encoded[e] == '0')
					{
						// remove last char
						decoded = decoded.substr(0, decoded.size() - 1);
						decoded += letter_map[encoded.substr(j - 1, 2)];
						j += 2;
					}
					else
					{
						decoded = decoded.substr(0, decoded.size() - 2);
						decoded += letter_map[encoded.substr(j - 2, 2)];
						j += 1;
					}
				}
				else
				{
					decoded = decoded.substr(0, decoded.size() - 2);
					decoded += letter_map[encoded.substr(j - 2, 2)];
					j += 1;
				}
			}
		}
		cout << decoded << endl;
	}
	return 0;
}