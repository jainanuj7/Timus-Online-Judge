// Python3 slow for printing output, C++ solution with same logic got acccepted
// Execution Time: 0.453s
// Memory used: 5.148 KB

#include <iostream>

using namespace std;

int main()
{
   int n, q, q1, q2, k;
   cin >> n;
   int sum[n];
   sum[0] = 0;
   for(int i=0 ; i<n ; i++) {
       cin >> k;
       sum[i+1] = sum [i] + k;
       
   }
   cin >> q;
   for(int i=0 ; i<q ; i++) {
       cin >> q1 >> q2;
       cout << sum[q2] - sum[q1-1] << "\n";
   }
   
   return 0;
}
