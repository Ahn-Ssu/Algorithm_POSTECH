int mcssN(int a[], int n, int *start, int *end){
    int i, j;
    int maxSum = 0, thisSum = 0;
 
    *start = *end = -1;
 
    for (i=0, j=0; j<n; j++)
    {
        thisSum += a[j]; //basic operation
 
        if (thisSum > maxSum)
        {
            maxSum = thisSum;
            *start = i;
            *end = j;
        }
        else if(thisSum < 0)
        {
            i = j+1;
            thisSum = 0;
        }
    }
    return maxSum;
}