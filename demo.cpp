#include<iostream>
#include<vector>
using namespace std;
int selection(int arr[]){
    int n=5;
    for(int i=0;i<n-1;i++){
        int smal=i;
        for(int j=i+1;j<n;j++){
            if(arr[j]<arr[smal]){
                smal=j;
            }

        }
    swap(arr[i],arr[smal]);
    }
    
}
int print(int arr[],int n){
    for(int i=0;i< n;i++){
        cout << arr[i] << endl;
    }
}

int main()
{
    int arr[]={4,5,2,1,3};
    selection(arr);
    print(arr,5);
    
    }
