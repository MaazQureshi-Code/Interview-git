
public class s {
    
    public static void main(String[] args) {
        
        int[] arr = {10, 20, 30, 40, 50};

        for(int i =0 ; i < arr.length;i++){
            System.out.println(  arr[i] + " ");
        }
        
    }

    /// Find the target element in java 
    /// 
    public static  int target (int arr[] ,int numToFind){
        for(int i =0; i < arr.length;i++ ){
            if(arr[i] == numToFind){
                return i;
            }

        }
        return -1;
    }
}
