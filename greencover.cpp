#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;

map<ll,vector<vector<ll>>>maps;
void fun(ll index,ll steps,vector<vector<ll>>&vec,vector<vector<ll>>&arr){
    if(index<=0){
     maps[steps]=arr;
      return ;
    }

    for(auto&iter:vec){
        if(iter[1]==index){
            arr.push_back(iter);
          
            if(iter[0]!=iter[1])fun(iter[0],steps+1,vec,arr);
            //popping back
             arr.pop_back();
        }
    }
  	return ;
}
int main(){
    ll tt;ll edg1,edg2,n,m;
  	cin>>tt;
   while(tt--){
     
       vector<vector<ll>>vec;
   
        cin>>n>>m;
    ll maximum=INT_MIN;
    while(m--){
        
        cin>>edg1>>edg2;
        maximum=max(maximum,edg2);
        vector<ll>arr={edg1,edg2};
        vec.push_back(arr);
    }
 
      maps.clear();
      for(int j=n;j<=maximum;j++){
           vector<vector<ll>>arr; 
           fun(j,0,vec,arr);
      }
     
     if(!maps.size())cout<<"0\n";
     else{
         
       
       auto iter=maps.begin();
       
       cout<<iter->first<<"\n";
        vector<vector<ll>>b;
        for(auto&x:iter->second){
           b.push_back(x);
            
        }
        reverse(b.begin(),b.end());
        for(int i=0;i<b.size();i++){
            cout<<b[i][0]<<" "<<b[i][1]<<"\n";
        }
        
     }
   }
    
     
}