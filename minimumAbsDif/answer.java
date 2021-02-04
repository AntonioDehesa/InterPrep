import java.io.*;
import java.math.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class answer
{

    // Complete the minimumAbsoluteDifference function below.
    static int minimumAbsoluteDifference(int[] arr) 
    {
        Arrays.sort(arr);
        int minNumber = Math.abs(arr[0] - arr[1]);
        for(int i = 0; i < arr.length -1; i++)
        {
            minNumber = Math.min(minNumber, Math.abs(arr[i] - arr[i+1]));
            if (minNumber == 0)
            {
                break;
            }
        }
        return minNumber;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException 
    {
        //BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int[] arr = new int[n];

        String[] arrItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < n; i++) 
        {
            arr[i] = Integer.parseInt(arrItems[i]);
        }

        int result = minimumAbsoluteDifference(arr);

        /*bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();*/
        System.out.println(result);

        scanner.close();
    }
}
