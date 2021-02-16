import java.io.*;
import java.math.*;
//import java.security.*;
//import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class sol
{

    // Complete the maxMin function below.
    static int maxMin(int k, int[] arr)
    {
        Arrays.sort(arr);
        ArrayList<Integer> results = new ArrayList<Integer>();
        ArrayList<Integer> chunks = new ArrayList<Integer>();
        for(int i = 0; i < k; i++)
        {
            chunks.add(arr[i]);
        }
        for(int i = 0; i < (arr.length - k); i++)
        {
            results.add(chunks.get(k-1) - chunks.get(0));
            chunks.remove(0);
            chunks.add(arr[i+k]);
        }
        results.add(chunks.get(k-1) - chunks.get(0));
        return Collections.min(results);
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException
    {
        //BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));
        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
        int k = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
        int[] arr = new int[n];
        for (int i = 0; i < n; i++)
        {
            int arrItem = scanner.nextInt();
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
            arr[i] = arrItem;
        }
        int result = maxMin(k, arr);
        /*bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();
        bufferedWriter.close();*/
        System.out.println(result);
        scanner.close();
    }
}
