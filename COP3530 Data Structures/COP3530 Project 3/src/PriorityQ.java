public class PriorityQ {
	
	private Node front;
	private Node end;
	
	public PriorityQ() {		
		front = null;
		end = null;
	}

	public void insert(State state) {
		insert(new Node(state));
	}
	
	public void insert(Node state) {		
		if(isEmpty()) {
			front = state;
			end = state;		
		} 
		else if(state.getCdr() > front.getCdr()) {
			front.setNext(state);
			state.setPrv(front);
			front = state;
		} 
		else if (state.getCdr() < end.getCdr()) {
			end.setPrv(state);
			state.setNext(end);
			end = state;
		} 
		else {
			Node temp = end;
			
			while(temp.getCdr() < state.getCdr()) {
				temp = temp.getNext();
				}
			
			if(temp.getPrv() != null) {
				temp.getPrv().setNext(state);
				state.setPrv(temp.getPrv());
			}
			
			state.setNext(temp);
			temp.setPrv(state);
		}
	}
		
	public Node remove() {
		Node temp = front;
		front = front.getPrv();
		
		return temp;
	}
	
	public PriorityQ intervalDelete(double one, double two) {
		
		PriorityQ tempQ = new PriorityQ();
		Node temp = end;
		
		while(temp.getCdr() < one && temp != null) {
			temp = temp.getNext();
		}
		
		tempQ.setEnd(temp);
		
		while(temp.getCdr() <= two && temp != null) {
			temp = temp.getNext();
		}
		
		tempQ.setFront(temp);
		
		if(tempQ.end.getPrv() != null)
			tempQ.end.getPrv().setNext(tempQ.front.getNext());
		
		if(tempQ.front.getNext() != null)
			tempQ.front.getNext().setPrv(tempQ.end.getPrv());
		
		tempQ.end.setPrv(null);
		tempQ.front.setNext(null);
		
		return tempQ;
	}
	
	public Node getFront() {
		return front;
	}

	public void setFront(Node front) {
		this.front = front;
	}

	public Node getEnd() {
		return end;
	}

	public void setEnd(Node end) {
		this.end = end;
	}

	public boolean isEmpty() {
		return end == null;
	}
	
	
	public void printQueue() {
		System.out.format(
				"Priority Queue Contents:\n" +
				"%-14s   %-6s  %-4s   %-6s     %-8s   %-7s\n%s\n",
				"State","MHI","VCR","CFR","Case Rate","Death Rate",
				"-----------------------------------------------------------------"
				);
		end.recPrint();
	}

}
