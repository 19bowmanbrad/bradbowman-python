import java.util.Arrays;

public class workSheetFourTwo {
    public static void main(String [] args){
        //1a
        System.out.println("14");
        System.out.println("6");
        System.out.println("2200");
        System.out.println("98");
        //1b
        System.out.println("[11, 4, 99, 2, 44, 0, 0, 0]");
        //1c
        System.out.println("[3, 3, 0, 0, 6, 9, 0, -18]");
        //1d
        int [] array1 = {5, 1, 8, 4, 1};
        int maxNum = forEachMax(array1);
        System.out.println(maxNum);
        //1e
        int [] array2 = {10, -2, 4, -4, 9, -5, 19, -7, 39, -1};
        double avgNum = average(array2);
        System.out.println(avgNum);
        //2a
        int[] doubleArray = doubleValues(array1);
        System.out.println(Arrays.toString(doubleArray));
    }
        //1d
    public static int forEachMax(int[] array){
        int maxNum = 0;
        for(int x: array){
            if (x > maxNum){
                maxNum = x;
            }
        }
        return maxNum;
    }
        //1e
    public static double average(int [] array){
        double sum = 0;
        for (int x: array){
            sum += x;
        }
        return (sum/ array.length);
    }
    public static int[] doubleValues(int [] array){
        for (int x = 0; x < array.length; x ++){
                array[x] *= 2;
        }
        return array;
    }
}
