/*
Given a string, write a function to check if it is a permutation of a palindrome. 
A palindrome is a word or phrase that is the same forwards and backwards.
A permutation is a rearragement of letters. 
The palindrome does not need to be limited to just dictionary words.
Example
Input: Tact Coa
Output: True (Permutations: taco cat, atco cta, etc)
*/

public class Solution
{
    static boolean checkPermutation(String s)
    {
        s = s.toLowerCase();
        s = s.replace(" ", "");
        boolean limitForMiddleChar = false;
        int[] freqMap = freqMap(s);//Creates the frequency map
        for(int i : freqMap)//for every element in the freqmap we test to see if it appears in even numbers, or, if it appears in odd numbers, there can not be another odd number
        {
            if (i %2 != 0)
            {
                if (limitForMiddleChar)
                {
                    return false;
                }
                limitForMiddleChar = true;
            }
        }
        System.out.println(s);
        return true;
    }

    static int[] freqMap(String s)
    {
        int[] map = new int[('z' - 97) - ('a' - 97)];//by taking 97 from the 'a', we make it 0
        for(char c : s.toCharArray())
        {
            map[c - 97]+=1;
        }
        return map;
    }
    public static void main(String[] args)
    {
        String s = "Tact Coa";    
        System.out.println(checkPermutation(s));
    }   
}