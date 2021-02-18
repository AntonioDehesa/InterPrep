import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

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
        
        /*
# Complete the reverseShuffleMerge function below.
def reverseShuffleMerge(s):
    splitted, rever = splitString(s)
    res = []
    for char in reversed(s):
        if splitted[char] > 0:
            while res and res[-1] > char and rever[res[-1]] > 0:
                # while res -> if the res array is not empty
                # while res[-1] > char -> if the last element of res is lexicographically bigger than the current char 
                # rever[res[-1]] > 0 -> if there are available chars in rever
                removed = res.pop() # the first element of res is deleted, and we increment one in the available chars, and decrease one in the used chars
                splitted[removed] += 1
                rever[removed] -= 1
            res.append(char)
            splitted[char] -= 1
        else:
            rever[char] -= 1
    return "".join(res)
        */
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String s = scanner.nextLine();

        String result = reverseShuffleMerge(s);

        bufferedWriter.write(result);
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
