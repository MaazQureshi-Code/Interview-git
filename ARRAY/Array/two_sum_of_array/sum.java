public class sum {
    public static void main(String[] args) {
        int [] arr = {2, 7, 11, 15};
        int target = 9;
        int [] result = sum(arr, target);
        System.out.println("Indices: [" + result[0] + ", " + result[1] + "]");
    
    }
    public static int [] sum(int[] arr , int target){
        int sum = 0;
        for (int i = 0; i < arr.length; i++) {
            for(int j =0 ; j < arr.length;j++){
                if(arr[i] + arr[j] == target)
                    return new int[]{i,j};
            }

        }
        return new int[]{-1,-1};
    }
}
