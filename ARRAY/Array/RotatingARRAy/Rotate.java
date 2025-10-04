public class Rotate {
    public static void main(String args[]){
        int[] arr = {1,2,3,4,5,6,7};
        int K = 2;
        rotateArray(arr, K);
        for(int i =0 ; i < arr.length;i++){
            System.out.print(arr[i] + " ");
        }
      
    }


     public static void rotateArray(int[] arr, int K) {
        int N = arr.length;
        K = K % N;
        if (K < 0)
            K += N;

        reverse(arr, 0, N - K - 1);
        reverse(arr, N - K, N - 1);
        reverse(arr, 0, N - 1);
    }

    public static void reverse(int[] arr, int start, int end) {
        while (start < end) {
          int temp = arr[start];
          arr[start] = arr[end];
          arr[end] = temp;
          start++;
          end--;        
        }
    }







    
}
