import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class maximumToys {

    // Complete the maximumToys function below.
    static int maximumToys(int[] prices, int k)
    {
        ArrayList<Integer> newPrices = new ArrayList<Integer>();
        for(int element : prices)
        {
            if(element <= k)
            {
                newPrices.add(element);
            }
        }
        Collections.sort(newPrices);
        int suma = 0, count = 0;
        for(int element : newPrices)
        {
            if ((suma + element)<=k)
            {
                suma+=element;
                count++;
            }
            else
            {
                break;
            }
        }
        return count;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException
    {
        int[] arr1 = {1,12,5,111,200,1000,10};
        int k = 50;
        System.out.println(maximumToys(arr1,k));
        int[] arr2 = {1,2,3,4};
        k = 7;
        System.out.println(maximumToys(arr2,k));
        /*
        arr = [1, 12, 5, 111, 200, 1000, 10]
        k = 50
        print(maximumToys(arr, k))
        arr = [1, 2, 3, 4]
        k = 7
        print(maximumToys(arr,k))
        */
        /*BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] nk = scanner.nextLine().split(" ");

        int n = Integer.parseInt(nk[0]);

        int k = Integer.parseInt(nk[1]);

        int[] prices = new int[n];

        String[] pricesItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < n; i++) {
            int pricesItem = Integer.parseInt(pricesItems[i]);
            prices[i] = pricesItem;
        }

        int result = maximumToys(prices, k);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();*/
    }
}
