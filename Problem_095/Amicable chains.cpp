#include<iostream>
#include<ctime>
#include<cmath>
#include<map>
#include<vector>
#include<cstdio>
#include<algorithm>

using namespace std;

int is_prime(int n)
{	
	if(n<2)
		return 0;
	else if(n<4)
		return 1;
	else if(n%2==0 || n%3==0)
		return 0;
	int i = 5;
	while(i*i <=n)
	{
		if(n%i==0 || n%(i+2)==0)
			return 0;
		i += 6;
	}
	return 1;
}

int divisor_sum(int n)
{
	int sum = 1;
	for(int div=2; div<int(sqrt(n))+1; div++)
	{
		if (n % div == 0)
		{
			sum += div;
			if (div*div != n)
				sum += int(n/div);
		}
	}	
	return sum;
}



void prime_factors(vector<vector<int> >& x, vector<vector<int> >& y, vector<int> primes, vector<int>& nonprimes, int number)
{	
	nonprimes.push_back(number);
	int flag, count, prev_index, prime_index, prime, ii;
	flag = 0;
	vector<int> pf, mult;
	vector<int>::iterator prev_check;
	for(ii=0; ii<primes.size(); ii++)
	{
		count = 0;
		prime = primes[ii];
		while(number % prime == 0)
		{
			number /= prime;
			count ++;
			prev_check = find(nonprimes.begin(), nonprimes.end(), number);
			if (prev_check != nonprimes.end())
			{
				flag = 1;
				prev_index = distance(nonprimes.begin(), prev_check);
				if(find(x[prev_index].begin(), x[prev_index].end(), prime) != x[prev_index].end())
				{
					prime_index = distance(x[prev_index].begin(), find(x[prev_index].begin(), x[prev_index].end(), prime));
					count += y[prev_index][prime_index];
					pf = x[prev_index];
					mult = y[prev_index];
					mult[prime_index] = count;
				}
				else
				{
					pf = x[prev_index];
					pf.push_back(prime);
					mult = y[prev_index];
					mult.push_back(count);
				}
				break;
			}
		}
		if(count && flag == 0)
		{
			pf.push_back(prime);
			mult.push_back(count);
		}
		if(number == 1 || flag == 1)
		{
			x.push_back(pf);
			y.push_back(mult);
			return;
		}
	}	
}




int main()
{
	clock_t start;
    	double duration;
   	start = std::clock();	

	int i, j, next, flag;
	map<int, int> divisor_dict;
	vector<int> chain, longest_chain;
	for(i=4; i<1*pow(10, 6); i++)
	{
		if(!is_prime(i))	
			divisor_dict[i] = divisor_sum(i);
	}
	cout<<"first phase is done in "<<(clock() - start ) / (double) CLOCKS_PER_SEC<<" seconds"<<"\n";


//ALTERNATIVE METHOD WITH PRIME FACTORS
//	vector<int> primes, nonprimes, dummy;
//	vector<vector<int> > pfactors, multiplicity;	
//	for(i=2; i<pow(10,6); i++)
//	{
//		if(is_prime(i))
//			primes.push_back(i);
//		else
//		{
//			prime_factors(pfactors, multiplicity, primes, nonprimes, i);
//		}
//DISPLAY
//		cout<<"i: "<<i<<"\n"<<"primes: ";
//		for(int m = 0; m<primes.size(); m++)
//			cout<<primes[m]<<" ";
//		cout<<"\n"<<"nonprimes: ";
//		for(int m = 0; m<nonprimes.size(); m++)
//			cout<<nonprimes[m]<<" ";
//		cout<<"\n"<<"prime factors \t&\t multiplicities:"<<"\n";
//		for(int m = 0; m<pfactors.size(); m++)
//		{
//			cout<<nonprimes[m]<<": [";
//			for(int n = 0; n<pfactors[m].size(); n++)
//				cout<<pfactors[m][n]<<" ";
//			cout<<"\b]"<<"\t\t"<<"[";
//			for(int n = 0; n<multiplicity[m].size(); n++)
//				cout<<multiplicity[m][n]<<" ";
//			cout<<"\b]"<<"\n";
//		}
//	}



	for(int i=4; i<pow(10, 7); i++)
	{
		if(!is_prime(i))	
			{	
				//cout<<"i: "<<i<<"\n";
				flag = 0;
				j = i;
				while(1)
				{
					next = divisor_dict[j];
					if(next < i || next > pow(10,6) || is_prime(next) || find(chain.begin(), chain.end(), next) != chain.end())
						break;
					else
					{
						chain.push_back(next);
						if(chain.back()==i)
						{	
							
							flag = 1;
							break;
						}
						j = next;					
					}
				}
				if(flag && chain.size()>longest_chain.size())
				{
					longest_chain = chain;
					//for (vector<int>::const_iterator i = chain.begin(); i != chain.end(); ++i)
    					//			cout << *i << '\t';
					//cout<<"\n";			
				}				
				chain.clear();
			}
	}
	cout<<longest_chain.back()<<"\n";

	duration = (clock() - start ) / (double) CLOCKS_PER_SEC;
  	std::cout<<"Time elapsed "<< duration <<" seconds"<<'\n';
}

