package CTCI.StringRotation;
public class solution
{
    static boolean isSubstring(String s1, String s2)
    {
        if (s1.length() != s2.length())
        {
            return false;
        }
        int i = s2.indexOf(s1.charAt(0));
        for(char chr : s1.toCharArray())
        {
            if( i >= s2.length())
            {
                i = 0;
            }
            if (chr != s2.charAt(i))
            {
                return false;
            }
            i++;
        }
        return true;
    }
    public static void main(String[] args)
    {
        String s1 = "waterbottle";
        String s2 = "erbottlewat";
        System.out.println(isSubstring(s1, s2));
    }
}