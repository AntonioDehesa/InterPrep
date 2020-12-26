import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class arrayManipulation {

    // Complete the arrayManipulation function below.
    static long arrayManipulation(int n, int[][] queries)
    {
        int[] arrToWork = new int[n+1];
        for(int [] query : queries)
        {
            arrToWork[query[0]-1]+= query[2];
            arrToWork[query[1]] -= query[2];
        }
        long sum = 0;
        long max = 0;
        for(int i : arrToWork)
        {
            sum+=i;
            max = Math.max(max,sum);
        }
        return max;
    }

    public static void main(String[] args) throws IOException
    {
        int n = 10;
        int[][] queries = {{1,5,3},{4,8,7},{6,9,1}};
        System.out.println("Result: " + arrayManipulation(n,queries));
        n = 10;
        int[][] quer = {{2,6,8},{3,5,7},{1,8,1},{5,9,15}};
        System.out.println("Result: " + arrayManipulation(n,quer));
        n = 5;
        int [][] quers = {{1,2,100},{2,5,100},{3,4,100}};
        System.out.println("Result: " + arrayManipulation(n,quers));
    }
}