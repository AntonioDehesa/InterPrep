/*
Implement a method to perform basic string compression using the counts of repeated characters. 
For example, the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not become smaller
than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a-z).
*/
public class Solution
{
    static String compression(String s)
    {
        char temp = s.charAt(0);
        int counter = 0;
        String result = "";
        for ( char chr : s.toCharArray())
        {
            if (chr != temp)
            {
                result = result + temp + counter;
                temp = chr;
                counter = 1;
            }
            else
            {
                counter+=1;
            }
        }
        result = result + temp + counter;
        System.out.println(result);
        return result.length() < s.length() ? result : s;
    }
    public static void main(String[] args)
    {
        String s = "aabcccccaaa";
        String result = compression(s);
        assert(result == "a2b1c5a3");
    }    
}