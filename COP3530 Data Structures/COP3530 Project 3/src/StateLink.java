
public class StateLink {

	private StateLink next;
	private StateLink prv;
	private State state;
	
	public StateLink(StateLink prv, StateLink next, State state) {
		this.next = next;
		this.prv = prv;
		this.state = state;
	}
	
	public StateLink(State state) {
		next = null;
		prv = null;
		this.state = state;
	}

	public StateLink getNext() {
		return next;
	}

	public void setNext(StateLink next) {
		this.next = next;
	}

	public StateLink getPrv() {
		return prv;
	}

	public void setPrv(StateLink prv) {
		this.prv = prv;
	}

	public State getState() {
		return state;
	}

	public void setState(State state) {
		this.state = state;
	}
	
	
}
