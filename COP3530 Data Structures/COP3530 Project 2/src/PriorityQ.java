import java.util.Scanner;

public class PriorityQ {
	
	private State arr[];
	private int size;
	private int bott;
	
	public PriorityQ(int sz) {
		arr = new State[sz];
		size = sz;
		bott = sz;
	}
	
	public int size() {
		return size - bott;
	}

	
	public void insert(State state) {
		boolean insert = true;
		if(isFull()) {
			System.out.print("The Queue is full, would you like to replace the following state?\nCurrent State:\n");
			arr[bott].print();
			System.out.print("\nWith\n\nNew State:\n");
			state.print();
			System.out.print("?\n[Y/N]");
			String str = new Scanner(System.in).next();
			insert = str.toUpperCase().equals("Y") || str.equals("1");
		}
		
		if(insert) {
		State temp;
		arr[bott > 0 ? --bott: bott] = state;
			for(int i = bott + 1; i < size && arr[i - 1].getCdr() > arr[i].getCdr(); i++) {
				temp = arr[i-1];
				arr[i-1] = arr[i];
				arr[i] = temp;
			}
		}
		}
	
	public void printQueue() {
		System.out.format(
				"%-5s %-14s   %-6s  %-4s   %-6s     %-8s   %-7s\n%s\n",
				"Place", "State","MHI","VCR","CFR","Case Rate","Death Rate",
				"-----------------------------------------------------------------"
				);
		for(int i = bott; i < size; i++) {
			System.out.format("[%2d]: ", i + 1);
			arr[i].print();
		}
	}
	
	public State remove() {
		return arr[bott < size ? bott++: bott];
	}

	public boolean isFull() {
		return bott == 0;
	}
	
	public boolean isEmpty() {
		return bott == size;
	}
}
