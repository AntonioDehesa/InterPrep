import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class sherlockAndAnagrams
{

    // Complete the sherlockAndAnagrams function below.
    static int sherlockAndAnagrams(String s)
    {
        int res = 0;
        ArrayList<String> my_array = new ArrayList<String>();
        HashMap<String,Integer> my_hashmap = new HashMap<String,Integer>();
        String temporal = "",trans ="";
        for( int i = 0; i < s.length(); i++)
        {
            for(int j = i+1; j < s.length() + 1; j++)
            {
                for(int k = i; k < j; k++)
                {
                    temporal = s.substring(k,k+1);
                    temporal = temporal.trim();
                    my_array.add(temporal);
                }
                Collections.sort(my_array);
                trans = String.join("",my_array);
                if(my_hashmap.containsKey(trans))
                {
                    res+=my_hashmap.get(trans);
                    my_hashmap.put(trans,my_hashmap.get(trans)+1);
                }
                else
                {
                    my_hashmap.put(trans,1);
                }
                my_array.clear();
            }
        }
        return res;
    }

    //private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException
    {
        String s = "ifailuhkqq";
        System.out.println(sherlockAndAnagrams(s));
        /*BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int q = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int qItr = 0; qItr < q; qItr++) {
            String s = scanner.nextLine();

            int result = sherlockAndAnagrams(s);

            bufferedWriter.write(String.valueOf(result));
            bufferedWriter.newLine();
        }

        bufferedWriter.close();

        scanner.close();*/
    }
}
