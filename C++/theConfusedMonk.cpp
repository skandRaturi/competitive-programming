#include <iostream>
#include <string>
using namespace std;

// class Box{
// 	private:
// 	int l,b,h;
// 	public:
// 	Box(){
// 		l=0;
// 		b=0;
// 		h=0;
// 	}
// 	Box(const Box& box){
// 		l = box.l;
// 		b = box.b;
// 		h = box.h;
// 	}
// 	Box(int a,int x,int c){
// 		l = a;
// 		b = x;
// 		h = c;
// 	}
// 	long long calculateVolume(){
// 		return (long long)l*b*h;
// 	}
// 	int getLength(){
// 		return l;
// 	}
// 	int getBreadth(){
// 		return b;
// 	}
// 	int getHeight(){
// 		return h;
// 	}
// 	friend bool operator < (Box& aBox,Box& box){
// 		if( (aBox.l < box.l) || ((aBox.b < box.b) && (aBox.l == box.l)) || ((aBox.b == box.b) && (aBox.l == box.l) && (aBox.h < box.h))){
// 			return true;
// 		}
// 		else{return false;}
// 	}
// 	friend ostream& operator <<(ostream& out,const Box& B){
// 		out << B.l <<  " " << B.b << " " << B.h;
// 		return out;
// 	}
// };
class Box{
    private:
    int l, b, h;
    public:
    Box(){
        l = 0;
        b = 0;
        h = 0;
    }
    Box(int length, int breadth, int height){
        l = length;
        b = breadth;
        h = height;
    }
    Box(const Box& B){
        l = B.l;
        b = B.b;
        h = B.h;
    }
    
    int getLenght(){
        return l;
    }
    int getBreadth(){
        return b;
    }
    int getHeight(){
        return h;
    }
    long long calculateVolume(){
        return (long long)l*b*h;
    }
    
    friend bool operator < ( Box&A,Box& B){
        if( (A.l < B.l) || ((A.b < B.b) && (A.l == B.l)) || ((A.h < B.h) && (A.l == B.l) && (A.b == B.b)) ){
            return true;
        }else{
            return false;
        }
    };
    
    friend ostream& operator<< (ostream& output, const Box& B){
        output << B.l << " " << B.b << " " << B.h;
        return output;
    }
};

int main() {
	Box b1(2,3,5);
	Box b2(b1);
	cout << b1.calculateVolume()<<endl;
	cout << b2.calculateVolume()<<endl;
	cout << b2;
	cout << b1<b2;
	return 0;
}