public class ReverseArray
{
	// Complete the reverseArray function below.
    static int[] reverseArray(int[] a)
    {
    	int[] res = new int[a.length];
    	for( int i = 0; i < a.length; i++)
    	{
    		res[i] = a[a.length - i - 1];
    	}
    	return res;
    }

    public static void main(String[] args)
    {
    	int[] test_array = {1,2,3};
    	int[] reversed_array = reverseArray(test_array);
    	System.out.println("Test Array: \n");
    	for(int i : test_array)
    	{
    		System.out.println(i);
    	}
    	System.out.println("Reversed Array: \n");
    	for(int i : reversed_array)
    	{
    		System.out.println(i);
    	}
    	assert(test_array == reversed_array);
    }
}