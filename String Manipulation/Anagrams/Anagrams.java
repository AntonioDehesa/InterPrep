import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Anagrams {

    // Complete the makeAnagram function below.
    static int makeAnagram(String a, String b)
    {
        HashMap<Character, Integer> hmA = new HashMap<Character, Integer>();      
        HashMap<Character, Integer> hmB = new HashMap<Character, Integer>();
        HashMap<Character, Integer> hmC = new HashMap<Character, Integer>();
        int res = 0;
        for(int i = 0; i < a.length(); i++)
        {
            hmA.put(a.charAt(i), (hmA.containsKey(a.charAt(i)) ? hmA.get(a.charAt(i)):0) + 1);
            hmC.put(a.charAt(i), (hmC.containsKey(a.charAt(i)) ? hmC.get(a.charAt(i)):0) + 1);
        }
        for(int i = 0; i < b.length(); i++)
        {
            hmB.put(b.charAt(i), (hmB.containsKey(b.charAt(i)) ? hmB.get(b.charAt(i)):0) + 1);
        }
        for(Character c : hmB.keySet())
        {
            hmC.put(c, (hmA.containsKey(c) ? hmA.get(c) : 0) - hmB.get(c));
        }
        for(Character c : hmC.keySet())
        {
            res+= Math.abs(hmC.get(c));
        }
        return res;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        //BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String a = scanner.nextLine();

        String b = scanner.nextLine();

        int res = makeAnagram(a, b);
        System.out.println(res);
        /*bufferedWriter.write(String.valueOf(res));
        bufferedWriter.newLine();

        bufferedWriter.close();*/

        scanner.close();
    }
}
