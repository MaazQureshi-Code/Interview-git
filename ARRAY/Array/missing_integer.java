public class missing_integer{
    public static void main(String args[]){
      int n = 100;

      int arr[] = new int[n -1];
        int index = 0;
      for(int i =1 ; i <= n; i++){
        if(i != 54){
            arr[index++] = i;
        }

    }

        System.out.println(" the missing number is : " + findMissingNumber(arr,n));
      }


    

    public static int findMissingNumber(int arr[], int n){

        int expectedSum = (n*(n+1))/2;
        int actualSum = 0;
        for(int i = 0 ; i < arr.length; i++){
            actualSum += arr[i];
        }
        

        return  expectedSum - actualSum;
    }
}