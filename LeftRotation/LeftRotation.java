// Complete the rotLeft function below.
    static int[] rotLeft(int[] a, int d)
    {
        int temporal;
        for(int i = 0; i < d ; i++)
        {
            temporal = a[0];
            for(int j = 0; j < a.length - 1; j++)
            {
                a[j] = a[j + 1];
            }
            a[a.length-1] = temporal;
        }
        return a;
    }