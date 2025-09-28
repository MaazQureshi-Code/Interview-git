import java.util.Arrays;

public class equality{
    public static void main(String args[]){
         int[] array1 = {1, 2, 3, 4};
        int[] array2 = {1, 2, 3, 4};

        if(equalArray(array1, array2)){
            System.out.println("The are equal");
        }else {
            System.out.println("No they are not ");
        }
        // Here problem array is object 

        if(array1.equals(array2)){
            System.out.println("They are also equal ");
        }else{
            System.out.println("They are not equal");
        }

        if(Arrays.equals(array1, array2)){
    System.out.println("Arrays are equal");
}else{
    System.out.println("Arrays are not equal");
}



   
        

    }

    public static boolean equalArray(int[] arr1 , int[] arr2){
        if(arr1.length != arr2.length) return false;

        for(int i =0 ; i < arr1.length;i++){
            if(arr1[i] != arr2[i]){
                return false;
            }
        }
        return true;
    }
}