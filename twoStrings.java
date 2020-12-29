import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class twoStrings {

    // Complete the twoStrings function below.
    static String twoStrings(String s1, String s2)
    {
        HashMap<Character,Integer> my_map = new HashMap<Character,Integer>();
        for(char c : s1.toCharArray())
        {
            if(!my_map.containsKey(c))
            {
                my_map.put(c,1);
            }
        }
        for(char c : s2.toCharArray())
        {
            if(my_map.containsKey(c))
            {
                return "YES";
            }
        }
        return "NO";
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException
    {
        String s1 = "hello",s2 = "world";
        System.out.println(twoStrings(s1,s2));
        assert(twoStrings(s1,s2) == "YES");
        s1 = "hi";
        System.out.println(twoStrings(s1,s2));
        assert(twoStrings(s1,s2) == "NO");
        /*BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int q = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int qItr = 0; qItr < q; qItr++) {
            String s1 = scanner.nextLine();

            String s2 = scanner.nextLine();

            String result = twoStrings(s1, s2);

            bufferedWriter.write(result);
            bufferedWriter.newLine();
        }

        bufferedWriter.close();

        scanner.close();*/
    }
}
