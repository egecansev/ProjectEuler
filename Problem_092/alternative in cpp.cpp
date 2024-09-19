#include <iostream>
#include <string>
#include <cmath>
#include <ctime>


int digit_square_sum(int n)
{
    int total = 0;
    while (n)
    {
        total += (n%10)*(n%10);
        n -= (n%10);
        n /= 10;
    }
    if(total == 1)
        return 0;
    else if(total == 89)
        return 1;
    else
        digit_square_sum(total);
}
int main()
{
    std::clock_t start;
    double duration;
    start = std::clock();
    
    int limit = pow(10, 7);  
    int count =0;
    for(int i=2; i<limit; i++)
        count += digit_square_sum(i);
  std::cout<<count<<"\n";
  
  duration = ( std::clock() - start ) / (double) CLOCKS_PER_SEC;
  std::cout<<"Time elapsed "<< duration <<" seconds"<<'\n';
}
