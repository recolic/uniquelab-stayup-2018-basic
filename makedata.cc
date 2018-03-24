#include<cstdlib>
#include<rlib/stdio.hpp>
#include<rlib/opt.hpp>
#include<vector>
#include<queue>
#include<cstdio>
#include<ctime>
#define ll long long
using namespace std;
priority_queue<int>q;
int main(int argcter, char **argv){
    rlib::opt_parser opt(argcter, argv);
    int n = std::stoi(opt.getValueArg("--size", "-s"));
  srand(time(0));
  printf("\n");
  printf("%d\n\n",n);
  ll ans=0;
  for(int i = 1;i<=n;i++){
    int x=rand()%100+1;
    printf("%d ",x);
    q.push(-x);
    ans+=x;
    if(i&1){
      int t=-q.top();q.pop();
      ans-=t*2;
    }
  }
  printf("\n");
  printf("\n");
  printf("%lld",ans);
}
