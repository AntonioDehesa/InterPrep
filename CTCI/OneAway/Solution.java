public class Solution
{
    static boolean oneAwayReplace(char[] sa, char[] sb)
    {
        boolean limit = false;
        for(int i = 0; i < sa.length; i++)
        {
            if (sa[i] != sb[i])
            {
                if (limit)
                {
                    return false;
                }
                limit = true;
            }
        }
        return true;
    }

    static boolean oneAwayInsert(char[] sa, char[] sb)
    {
        int i = 0;
        int j = 0;
        while(i < sa.length && j < sb.length)
        {
            if (sa[i] != sb[j])
            {
                if (i != j)
                {
                    return false;
                }
                j++;
            }
            else
            {
                i++;
                j++;
            }
        }
        return true;
    }

    static boolean oneAway(String sa, String sb)
    {
        sa = sa.replace(" ", "");
        sb = sb.replace(" ", "");
        if (Math.abs(sa.length() - sb.length()) > 1)
        {
            return false;
        }
        char[] saArr = sa.toCharArray();
        char[] sbArr = sb.toCharArray();
        if (sa.length() == sb.length())
        {
            return oneAwayReplace(saArr, sbArr);
        }
        if (sa.length()+1 == sb.length())
        {
            return oneAwayInsert(saArr, sbArr);
        }
        if (sa.length()-1 == sb.length())
        {
            return oneAwayInsert(sbArr, saArr);
        }
        return false;
    }
    public static void main(String[] args)
    {
        String sa = "pale";
        String sb = "ple";
        System.out.println(oneAway(sa, sb));
        assert(oneAway(sa, sb) == true);
        sa = "pales";
        sb = "pale";
        System.out.println(oneAway(sa, sb));
        assert(oneAway(sa, sb) == true);
        sa = "pale";
        sb = "bale";
        System.out.println(oneAway(sa, sb));
        assert(oneAway(sa, sb) == true);
        sa = "pale";
        sb = "bake";
        System.out.println(oneAway(sa, sb));
        assert(oneAway(sa, sb) == true);
    }    
}