#include<iostream>
#include<ctime>
#include<map>
#include<vector>

using namespace std;


int eq(int x, int y, int z, int n)
{
    return 2*(x*y + y*z + x*z) + 4 * (n-1)*(x+y+z+n-2);
}

int main()
{
    clock_t start;
    double duration;
    start = std::clock();

    int a, b, c, i, target = 1000, limit=30000;
    vector<int> values;
    map<int, int> counter;

    for(a=1; 2*a+1<limit; a++)
        for(b=1; b<=a && 2*(a*b+a+b)<limit; b++)
            for(c=1; c<=b && 2*(a*b+b*c+a*c)<limit; c++)
                for(i=1; eq(a,b,c,i)<limit; i++)
                    values.push_back(eq(a,b,c,i));

    while(!values.empty())
    {
        b = values.back();
        values.pop_back();
        if (counter.count(b))
            counter[b]++;
        else
            counter[b] = 1;
    }
    for(a = 0; a < counter.size(); a++)
        if(counter[a] == target)
            break;
    cout<<a<<'\n';

    duration = (clock() - start ) / (double) CLOCKS_PER_SEC;
    std::cout<<"Time elapsed "<< duration <<" seconds"<<'\n';
}

