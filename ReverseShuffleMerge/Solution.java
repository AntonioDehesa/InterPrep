import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;
import java.util.stream.Collectors;

public class Solution
{
    // Complete the reverseShuffleMerge function below.
    static String reverseShuffleMerge(String s)
    {
        HashMap<Character, Integer> splitted = new HashMap<Character, Integer>();
        for(char chr : s.toCharArray())
        {
            if (splitted.containsKey(chr))
            {
                splitted.put(chr, splitted.get(chr) + 1);
            }
            else
            {
                splitted.put(chr, 1);
            }
        }
        for(char chr : splitted.keySet())
        {
            splitted.put(chr, splitted.get(chr) / 2);
        }
        HashMap<Character, Integer> rever = new HashMap<Character, Integer>(splitted);
        ArrayList<Character> res = new ArrayList<Character>();
        StringBuilder temp = new StringBuilder();
        temp.append(s);
        temp.reverse();
        s = temp.toString();
        char removed;
        for( char chr : s.toCharArray())
        {
            if (splitted.get(chr) > 0)
            {
                while (!res.isEmpty() && res.get(res.size() - 1) > chr && rever.get(res.get(res.size() - 1)) > 0)
                {
                    removed = res.remove(res.size() - 1);
                    splitted.put(removed, splitted.get(removed) + 1);
                    rever.put(removed, rever.get(removed) - 1);
                }
                res.add(chr);
                splitted.put(chr, splitted.get(chr) - 1);
            }
            else
            {
                rever.put(chr, rever.get(chr) - 1);
            }
        }
        return res.stream().map(Object::toString)
        .collect(Collectors.joining(""));
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        //BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String s = scanner.nextLine();

        String result = reverseShuffleMerge(s);

        //bufferedWriter.write(result);
        //bufferedWriter.newLine();

        //bufferedWriter.close();
        System.out.println(result);
        scanner.close();
    }
}
