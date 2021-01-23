import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class minimumSwaps2 {

    // Complete the minimumSwaps function below.
    static int minimumSwaps(int[] arr)
    {
        int res = 0;
        int[] sortedArray = new int[arr.length], arrToWork = new int[arr.length];
        for( int i = 0; i < arr.length; i++)
        {
            sortedArray[i] =i; //Sorted array to compare it to the final array
        }
        for( int i = 0; i < arr.length; i++)
        {
            arrToWork[i] = arr[i] - 1;//We reduce one number to the array, to make it easier with the index
        }
        while(!Arrays.equals(arrToWork,sortedArray))//If the array is not sorted, the process will start again until it is sorted
        {
            for(int i = 0; i < arr.length; i++)
            {
                if (i!=arrToWork[i])//If the number is not where it is supposed to be
                {
                    int swap = arrToWork[arrToWork[i]];//arr[q] number to replace
                    arrToWork[arrToWork[i]] = arrToWork[i];
                    arrToWork[i] = swap;
                    res++;
                }
            }
        }
        return res;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException
    {
        int[] test = { 7,1,3,2,4,5,6 };
        int[] test2 = { 2, 3, 4, 1, 5};
        assert(minimumSwaps(test) == 5);
        assert(minimumSwaps(test2) == 3);
    }
}