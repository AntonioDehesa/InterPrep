import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class ransomNote {

    // Complete the checkMagazine function below.
    static String checkMagazine(String[] magazine, String[] note)
    {
        HashMap<String,Integer> my_dict = new HashMap<String,Integer>();
        for(String word : magazine)
        {
            if (!my_dict.containsKey(word))
            {
                my_dict.put(word,1);
            }
            else
            {
                my_dict.put(word, my_dict.get(word) + 1);
            }
        }
        for(String word : note)
        {
            if((!my_dict.containsKey(word)) || my_dict.get(word) < 1)
            {
                return "No";
            }
            else
            {
                my_dict.put(word, my_dict.get(word) - 1);
            }
        }
        return "Yes";
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args)
    {
        String[] magazine = {"give", "me", "one", "grand", "today", "night"};
        String[] note = {"give", "one", "grand", "today"};

        assert(checkMagazine(magazine,note) == "Yes");

        System.out.println("Value: " + checkMagazine(magazine,note));

        String[] magazine2 = {"two", "times", "three", "is", "not", "four"};
        String[] note2 = {"two", "times", "two", "is", "four"};

        assert(checkMagazine(magazine2,note2) == "No");
        System.out.println("Value: " + checkMagazine(magazine2,note2));

        String[] magazine3 = {"ive", "got", "a", "lovely", "bunch", "of", "coconuts"};
        String[] note3 = {"ive", "got", "some", "coconuts"};

        assert(checkMagazine(magazine3,note3) == "No");
        System.out.println("Value: " + checkMagazine(magazine3,note3));
        /*String[] mn = scanner.nextLine().split(" ");

        int m = Integer.parseInt(mn[0]);

        int n = Integer.parseInt(mn[1]);

        String[] magazine = new String[m];

        String[] magazineItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < m; i++) {
            String magazineItem = magazineItems[i];
            magazine[i] = magazineItem;
        }

        String[] note = new String[n];

        String[] noteItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < n; i++) {
            String noteItem = noteItems[i];
            note[i] = noteItem;
        }

        checkMagazine(magazine, note);

        scanner.close();*/
    }
}