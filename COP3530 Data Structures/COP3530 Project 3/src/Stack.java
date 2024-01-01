public class Stack {
	
	private Node top;
	private Node bott;
	

	public Stack() {
		top = null;
		bott = null;
	}
	
	public void push(State temp) {		
		push(new Node(temp));
	}
	
	public void push(Node temp) {
		if(isEmpty())
			bott = temp;
		temp.setNext(top);
		top = temp;		
	}
	
	public Node pop() {
		if(isEmpty())
			return null;
		
		Node temp = top;				
		
		top = top.getNext();
		temp.setNext(null);
		
		return temp;		
	}
	
	public boolean isEmpty() {
		return top == null; 
	}
	
	public void printStack() {
		System.out.format(
				"Stack Contents:\n" +
				"%-14s   %-6s  %-4s   %-6s     %-8s   %-7s\n%s\n",
				"State","MHI","VCR","CFR","Case Rate","Death Rate",
				"-----------------------------------------------------------------"
				);
		top.recPrint();
	}
}
