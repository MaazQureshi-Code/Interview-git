public class removeing_element {
    
    public static void main(String[] args) {
     int arr[] = {1,2,3,4,5,6};
     int element = 4;

        int newArr[] = removeElement(arr, element);

        for(int i =0 ; i < newArr.length;i++){
            System.out.print(  newArr[i] + " ");
        }
        
    }

    public static int[] removeElement(int[] arr, int element) {
        int newArr[] = new int[arr.length - 1];
        int index = 0;

        for(int i =0 ; i < arr.length;i++){

        if(arr[i] != element){
            newArr[index++] = arr[i];
        }
        }



        return  newArr;

    }
}
