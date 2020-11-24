#include <iostream>
#include <string>

using namespace std;

int main()
{
    string a;
    int w = 0;
    cin >> a;
    for (int i = 0; i < a.length(); i++)
    {
        w+=(int(a[i])-96);
    }
    cout<<w<<endl;
    return 0;
    
}