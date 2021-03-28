package CTCI.BasicLinkedList;
//How to run it: javac -d . BasicLinkedList.java
// java CTCI.BasicLinkedList.BasicLinkedList

public class BasicLinkedList
{
    public static void main(String[] args)
    {
        Node root = new Node(10);
        root.appendToTail(9);
        root.appendToTail(8);
        root.appendToTail(7);
        System.out.println("Printing the one with value 7");
        Node n = root;
        while(n.next!= null && n.data != 7)
        {
            n = n.next;
        }
        System.out.println("Data = "+ n.data);
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