import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class answer
{

    // Complete the getMinimumCost function below.
    static int getMinimumCost(int k, int[] c)
    {
        if (k >= c.length)
        {
            return Arrays.stream(c).sum();
        }
        Arrays.sort(c);
        int sum = 0, i = 0, counter = 0;
        for(int j = c.length - 1; j >= 0; j--)
        {
            sum = (i+1) * c[j] + sum;
            counter++;
            if(counter >= k)
            {
                counter = 0;
                i+= 1;
            }
        }
        return sum;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException
    {
        //BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));
        String[] nk = scanner.nextLine().split(" ");
        int n = Integer.parseInt(nk[0]);
        int k = Integer.parseInt(nk[1]);
        int[] c = new int[n];
        String[] cItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
        for (int i = 0; i < n; i++)
        {
            int cItem = Integer.parseInt(cItems[i]);
            c[i] = cItem;
        }
        int minimumCost = getMinimumCost(k, c);
        System.out.println(minimumCost);
        /*bufferedWriter.write(String.valueOf(minimumCost));
        bufferedWriter.newLine();
        bufferedWriter.close();*/
        scanner.close();
    }
}
