import java.util.Scanner;

public class Stack {
	
	private State arr[];
	private int ln;
	private int top;

	public Stack(int sz) {

		arr = new State[sz];
		ln = sz;
		top = 0;
	}
	
	public int size() {
		return top;
	}
	
	public void push(State temp) {
		boolean insert = true;
		if(isFull()) {
			System.out.print("The Stack is full, would you like to replace the following state?\n");
			arr[top].print();
			System.out.print("\nWith\n\nNew State:\n");
			temp.print();
			System.out.print("\n[Y/N]");
			String str = new Scanner(System.in).next();
			insert = str.toUpperCase().equals("Y") || str.equals("1");
		}
		if(insert) {
			arr[top < ln? top++: top] = temp;
		}
	}
	
	public State pop() {
		if(!isEmpty())
		return arr[--top];
		
		else
			return null;
	}
	
	public boolean isEmpty() {
		return top == 0;
	}
	
	public boolean isFull() {
		return top == ln - 1 && arr[top] != null;
	}
	
	public void printStack() {
		System.out.format(
				"%-5s %-14s   %-6s  %-4s   %-6s     %-8s   %-7s\n%s\n",
				"Place","State","MHI","VCR","CFR","Case Rate","Death Rate",
				"-----------------------------------------------------------------"
				);
		for(int i = top - 1; i >= 0; i--) {
			System.out.format("[%2d]: ", i + 1);
			arr[i].print();
		}
		
	}
}
