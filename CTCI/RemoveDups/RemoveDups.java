import java.util.HashMap;
import java.util.concurrent.ThreadLocalRandom;
/**
 * Write code to remove duplicates from an unsorted linked list
*/
public class RemoveDups
{
    public static void main(String[] args)
    {
        HashMap<Integer, Integer> dups = new HashMap<Integer, Integer>();
        Node root = new Node(10);
        int random = 0;
        for(int i = 0; i < 100; i++)
        {
            random = ThreadLocalRandom.current().nextInt(1, 100 + 1);
            root.appendToTail(random);
        }
        Node prev = null;
        Node n = root;
        System.out.println("Original list: ");
        while(n.next != null)
        {
            System.out.println(n.data);
            n = n.next;
        }
        n = root;
        while(n.next != null)
        {
            if (dups.containsKey(n.data))
            {
                prev.next = n.next;
            }
            else
            {
                dups.put(n.data, 1);
                prev = n;
            }
            n = n.next;
        }
        n = root;
        System.out.println("Original list: ");
        while(n.next != null)
        {
            System.out.println(n.data);
            n = n.next;
        }
    }    
}


class Node
{
    Node next = null;
    int data;

    public Node(int d)
    {
        data = d;
    }

    void appendToTail(int d)
    {
        Node end = new Node(d);
        Node n = this;
        while(n.next!= null)
        {
            n = n.next;
        }
        n.next = end;
    }
}