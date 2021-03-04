import java.lang.reflect.Method;

/**
 * Solution
 */
public class Solution
{
    static int[][] zeroMatrix(int [][] matrix)
    {
        for(int row = 0; row < matrix.length; row++)
        {
            for(int element = 0; element < matrix[0].length; element++)
            {
                if (matrix[row][element] == 0)
                {
                    for(int i = 0; i < matrix.length; i++)
                    {
                        matrix[i][element] = 0;
                    }
                    for(int i = 0; i < matrix[0].length; i++)
                    {
                        matrix[row][i] = 0;
                    }
                    return matrix;
                }
            }
        }
        return matrix;
    }
    public static void main(String[] args)
    {
        int[][] matrix = {{1,2,3,4},{5,0,7,8},{9,10,11,12}};
        int[][] result = zeroMatrix(matrix);
        for(int [] row : result)
        {
            for(int element : row)
            {
                System.out.print(element);
            }
            System.out.println();
        }
    }   
}