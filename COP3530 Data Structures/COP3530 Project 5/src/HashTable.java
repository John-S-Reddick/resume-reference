
public class HashTable {
	int key;
	Node states[];
	
	public HashTable(int key) {
		this.key = key;
		states = new Node[key];
	}
	
	public void insert(String state, long population, long deaths) {
		insert(new Node(state, population, deaths));
	}
	
	public void insert(Node state) {
		int id = hashIt(state.getName());		
		if(states[id] == null) 
			states[id] = state;
		else {
			Node loc = states[id];
			
			while(loc.hasNextNode()) {
				loc = loc.getNextNode();
			}			
			loc.setNextNode(state);
		}	
		
	}
	
	public int hashIt(String name) {
		int len = name.length();
		int temp = 0;
		
		for(int i = 0; i < len; i++) {
			temp += (int)name.charAt(i);
		}
		
		return temp % key;
	}
	/* 4
	 * The method: public void display() that will traverse the table and will print the hash table 
	 */
	
	public void display() {
		
		System.out.printf("Num  %-30s %-20.2s", "State Name", "DR");
		
		for(int i = 0; i < key; i++) {
			System.out.printf("\n%3d. ",i);
			if(states[i] == null)
				System.out.print("Empty");
			else 
				states[i].recPrint();			
		}
		System.out.println();
		
	}
	
	public Node find(String state) {
		Node loc = states[hashIt(state)];
		while(loc != null) {
			if(loc.getName().equals(state))				
				return loc;
			else
				loc = loc.getNextNode();
		}		
		
		return null;
	}
	
	public void declare(String state) {
		Node loc = find(state);
		
		if(loc == null)
			System.out.printf("\n%s was not found\n", state);
		else
			System.out.printf(""
					+ "\n%s is found at index %d with DR of %.2f\n"
					,loc.getName(), hashIt(state), loc.getDr());
	}
	
	
	public void delete(String state) {
		Node loc = states[hashIt(state)];
		if(loc != null && loc.getName().equals(state)) {
			states[hashIt(state)] = loc.getNextNode();
			System.out.println(state + " was deleted");
		}
		else
			while(loc != null) {
				if(loc.hasNextNode() && loc.getNextNode().getName().equals(state)) {
					loc.setNextNode(loc.getNextNode().getNextNode());
					System.out.println(state + " was deleted");
				}
				else
					loc = loc.getNextNode();
			}
		
	}
	
	
	 
	/* 5
	* The method: public void printEmptyAndCollidedCells() that will print the number of 
	* empty cells and the number of collided cells in the hash table array.  Note that an empty cell 
	* is a cell of no state, and that a collided cell is a cell of multiple states. 
	*/
	
	public void printEmptyAndCollidedCells(){
		int collide = 0, empty = 0;
		for(int i = 0; i < key; i++) {
			if(states[i] == null)
				empty++;
			else if(states[i].hasNextNode())
				collide++;
		}
		
		System.out.printf(""
				+ "[%3d] Collided cells\n"
				+ "[%3d] Empty cells\n", collide, empty);		
	}

}
