#include<stdio.h>
void main()
{

    int n,i;
    scanf("%d",&n);
    int array[n],total=0,max=0,remainder=0;
    for(i=0;i<n;i++)
    {
        scanf("%d",&array[i]);
        total=(total+array[i]);
        if(array[i]>=max)
        {
            max=array[i];
        }
    }
    remainder = (total % max);
    printf("%d",remainder);
    

}
