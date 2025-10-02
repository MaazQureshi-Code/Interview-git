import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;

public class merga{
    public static void main(String args[]){
        int [] arr1 = {1,2,3};
        int [] arr2 = {4,5,6};
        Arrays.sort(arr1);
        Arrays.sort(arr2);
        int [] newArray = merga(arr1, arr2);

        for(int i = 0; i < newArray.length;i++){
            System.out.print(newArray[i] + " ");
        }
    }

    

    public static int [] merga(int arr1[] , int arr2[]){
        int totalLength = arr1.length + arr2.length;
        int [] totalArray = new int[totalLength];
        int index = 0;

        for(int i =0; i < arr1.length;i++){
            totalArray[index++] = arr1[i];
            
        }

        for(int i =0; i < arr2.length;i++){
            totalArray[index++] = arr2[i];
        }
        return  totalArray;
    }


    public static int [] MergeSortedArraysSorted(int arr1[] , int arr2[]){

        int totalLength = arr1.length + arr2.length;
        int [] totalArray = new int[totalLength];
        int index = 0, i = 0, j = 0;

        /// array here should be sorted
        while (i < arr1.length && j < arr2.length) {
            if(arr1[i] < arr2[j]){
                totalArray[index++] = arr1[i++];
            }else{
                totalArray[index++] = arr2[j++];
            }
            
        }

        while (i < arr1.length) {
            totalArray[index++] = arr1[i++];
        }
        while (j < arr2.length) {
            totalArray[index++] = arr2[j++];
        }

        return  totalArray;
    }

    public static List<Integer> merge(int[] arr1, int[] arr2) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        
        // Add elements of both arrays
        for(int num : arr1) minHeap.add(num);
        for(int num : arr2) minHeap.add(num);
        
        // Extract elements in sorted order
        List<Integer> result = new ArrayList<>();
        while(!minHeap.isEmpty()) {
            result.add(minHeap.poll());
        }
        return result;
    }
}