import java.util.ArrayList;
public class TwoDArray
{
	// Complete the hourglassSum function below.
    static int hourglassSum(int[][] arr)
    {
    	ArrayList<Integer> results = new ArrayList<Integer>();
    	for(int rows = 0; rows < arr.length - 2; rows++)
    	{
    		for(int cols = 0; cols < arr[0].length- 2; cols++)
    		{
    			int result = 0;
    			for(int i = cols; i < 3 + cols; i++)
    			{
    				result+=arr[rows][i];
    			}
    			result+=arr[rows+1][1+cols];
    			for(int i = cols; i < 3 + cols; i++)
    			{
    				result+=arr[rows+2][i];
    			}
    			results.add(result);

    		}
    	}
    	int finResult = Integer.MIN_VALUE;//Lowest int. No number can be lower, so this takes care of the cases where the max result is negative
    	for(int i : results)
    	{
    		if(i > finResult)
    		{
    			finResult = i;
    		}
    	}
    	return finResult;
    }

    public static void main(String[] args)
    {
    	//int[][] arr = {{-9,-9,-9,1,1,1},{0,-9,0,4,3,2},{-9,-9,-9,1,2,3},{0,0,8,6,6,0},{0,0,0,-2,0,0},{0,0,1,2,4,0}};
    	int[][] arr = {{-1,-1,0,-9,-2,-2},{-2,-1,-6,-8,-2,-5},{-1,-1,-1,-2,-3,-4},{-1,-9,-2,-4,-4,-5},{-7,-3,-3,-2,-9,-9},{-1,-3,-1,-2,-4,-5}};
    	System.out.println("Array = \n");
    	for(int[] i : arr)
    	{
    		for(int j : i)
    		{
    			System.out.print(j + " ");
    		}
    		System.out.println();
    	}
    	System.out.println("Result = " + hourglassSum(arr));
    	//assert(hourglassSum(arr) == 28);
    }
}