
public class Node {
	private Node next;
	private Node prv;
	private State data;
	
	public Node(State state) {
		next = null;
		prv = null;
		data = state;
	}
	
	public Node(State state, Node next) {
		this.next = next;
		prv = null;
		data = state;
	}
	
	public Node getNext() {
		return next;
	}

	public void setNext(Node next) {
		this.next = next;
	}

	public Node getPrv() {
		return prv;
	}

	public void setPrv(Node prv) {
		this.prv = prv;
	}
	
	public boolean hasNext() {
		return next != null;
	}
	
	public double getCdr() {
		return data.getCdr();
	}
	
	public void recPrint() {
		data.print();
		if(hasNext())
			next.recPrint();			
	}

}

