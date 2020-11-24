#include <iostream>
#include <string>
#include <math.h>
using namespace std;
int main() {
	int k;
	string x;

	cin >> x >> k;
	int l,m;
	l = x.length();
	m = stoi(x);
	for(int i = 1; i <= k; i++){
		if(l-i > 0){
			int ad;
            int t,num;
            t = stoi(x[i-1]);
            num = 9 - t;
			ad = num * pow(10, l-i);
			m = m + ad;
            cout << t;
		}
		else break;
	}
    cout << m<< endl;
    cout << l <<endl;
    
	return 0;
}