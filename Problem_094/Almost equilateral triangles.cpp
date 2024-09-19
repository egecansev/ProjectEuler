#include<iostream>
#include<ctime>
#include<cmath>

using namespace std;


int main()
{
	std::clock_t start;
    	double duration;
   	start = std::clock();	

	int i, x;
	long long length;
	long double xp, error;
	error = pow(10,-9);
	length = 0;
	for(i=1; i<166666667; i++)
	{
		x = 2*i+1;
		xp = sqrtl(x-1)*sqrtl(3*x+1);
		if (abs(xp - round(xp)) < error)		
		{
			length += 3*x + 1;
			continue;		
		}		
		xp = sqrtl(x+1)*sqrtl(3*x-1);
		if (abs(xp - round(xp)) < error)
		{		
			length += 3*x - 1;
		}
	}
	cout<<length<<"\n";
	duration = ( std::clock() - start ) / (double) CLOCKS_PER_SEC;
  	std::cout<<"Time elapsed "<< duration <<" seconds"<<'\n';
}
