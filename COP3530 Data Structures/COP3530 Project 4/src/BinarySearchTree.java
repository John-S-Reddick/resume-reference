
public class BinarySearchTree {
	
	Node root;

/*1. A no-parameter constructor that creates an empty tree.*/

	public BinarySearchTree() {
		root = null;
	}


/*2. The method: public void insert(String name, double DR) that will insert a node into the
proper position in the search tree based on state name.*/
	
	public void insert(String name, double DR) {
		insert(new Node(name, DR));
	}

	public void insert(Node N) {
		Node temp = root;
		if(root == null)
			root = N;
		else
			while(temp.getName().compareToIgnoreCase(N.getName()) != 0) {
				
				if(temp.getName().compareToIgnoreCase(N.getName()) < 0) 
					if(temp.hasRight())
						temp = temp.getRight();
					else
						temp.setRight(N);
				else
					if(temp.hasLeft())
						temp = temp.getLeft();
					else
						temp.setLeft(N);
		}
		
	}


/*3. The method: public double find(String name) that will search the tree for the state of the
given name and if found will return the DR or -1 if not found. If found, this method should
print out the path of the found node. The path of a node is defined as the sequence of nodes
from root to the node.*/
	
	public double find(String name) {
		Node temp = root;
		
		System.out.print("\n[*] ");
		
		while(temp.getName().compareToIgnoreCase(name) != 0) {
			temp.print();
			
			if(temp.getName().compareToIgnoreCase(name) < 0) 
				if(temp.hasRight()) {
					temp = temp.getRight();
					System.out.print("[R] ");
				}
				else {
					System.out.printf("\n[X]%-20sNot Found\n",name);
					return -1;
				}
					
			else
				if(temp.hasLeft()) {
					temp = temp.getLeft();
					System.out.print("[L] ");
				}
				else {
					System.out.printf("\n[X]/%-20sNot Found\n",name);
					return -1;
				}
					
		}
		
		temp.print();
		
		return temp.getDr();
		
	}



/*4. The method: public void delete(String name) that will find and delete the given state from
the tree.*/
	//TODO Fix this
	public void delete(String name) {
		Node temp = root;
		Node NL = null;
		Node NR = null;
		
		
		if(root.getName().compareToIgnoreCase(name) == 0) {
			NL = temp.getLeft();
			NR = temp.getRight();
			root = null;
			
		}			
		else
			while(temp != null) {
				
				if(temp.hasLeft() && temp.getLeft().getName().compareToIgnoreCase(name) == 0) {
					NL = temp.getLeft().getLeft();
					NR = temp.getLeft().getRight();
					temp.setLeft(null);
				}
					
				
				if(temp.hasRight() && temp.getRight().getName().compareToIgnoreCase(name) == 0) {
					NL = temp.getRight().getLeft();
					NR = temp.getRight().getRight();
					temp.setRight(null);
				}
				
				if(temp.getName().compareToIgnoreCase(name) < 0) 
					temp = temp.getRight();
				else
					temp = temp.getLeft();
			}
		
		if(NL != null)
			insert(NL);
		
		if(NR != null)
			insert(NR);
	}
	
	public void distribute(Node N) {
		N.print();
		if(N.hasLeft())
			insert(N.getLeft());
		
		if(N.hasRight())
			insert(N.getRight());
	}



/*5. The method: public void printInorder() that will traverse the tree in using a Inorder
traversal (LNR) and print each node.*/
	
	public void printInorder() {
		printInorder(root);
	}
	
	public void printInorder(Node N) {
		if(N.hasLeft())
			printInorder(N.getLeft());
		
		N.print();
		
		if(N.hasRight())
			printInorder(N.getRight());
	}
	
/*6. The method: public void printPreorder() that will traverse the tree in using a Preorder
traversal (NLR) and print each node.*/
	
	public void printPreorder() {
		printPreorder(root);
	}
	
	public void printPreorder(Node N) {
		N.print();
		
		if(N.hasLeft())
			printPreorder(N.getLeft());
		
		if(N.hasRight())
			printPreorder(N.getRight());
	}
	

/*7. The method: public void printPostorder() that will traverse the tree in using a Postorder
traversal (LRN) and print each node.*/
	
	public void printPostorder() {
		printPostorder(root);
	}
	
	public void printPostorder(Node N) {		
		if(N.hasLeft())
			printPostorder(N.getLeft());
		
		if(N.hasRight())
			printPostorder(N.getRight());
		
		N.print();
	}
	
/*8. The method: public void printBottomStates(int c) that will find and print in order the
bottom c states regarding DR, that is, the c states with highest DR. These states should be
printed in a descending order. If there are less than c states in the tree, print all of them.
(Note: for this method, you are required NOT to use any extra binary search tree and NOT
to use any sorting method. Hint: you may consider using an array of size c and a few
other constant-memory variables.)*/

	public void printBottomStates(int c) {
		Node temp;
		double min = -1;
		
		for(int i = 0; i < c; i++) {
			temp = lowest(root, min);
			min = temp.getDr();
			
			if(min > 10000)
				i = c + 1;
			else
				temp.print();
		}
		
		
	}
	
	public Node lowest (Node N, double min) {
		Node lowest = N.getDr() > min ? N : new Node("FaKington", 200000);
		
		if(N.hasLeft() && lowest(N.getLeft(), min).getDr() > min && lowest.getDr() > lowest(N.getLeft(), min).getDr())
			lowest = lowest(N.getLeft(), min);
		
		if(N.hasRight() && lowest(N.getRight(), min).getDr() > min && lowest.getDr() > lowest(N.getRight(), min).getDr())
			lowest = lowest(N.getRight(), min);		
		
		return lowest;		
	}

/*9. The method: public void printTopStates(int c) that will find and print in order the top c
states regarding DR, that is, the c states with lowest DR. These states should be printed in an
ascending order. If there are less than c states in the tree, print all of them. (Note: for this
method, you are required NOT to use any extra binary search tree and NOT to use any
sorting method. Hint: you may consider using an array of size c and a few other constantmemory variables.)*/
	
	public void printTopStates(int c) {
		Node temp;
		double max = 200000;
		
		for(int i = 0; i < c; i++) {
			temp = highest(root, max);
			max = temp.getDr();
			
			if(max < 0)
				i = c + 1;
			else
				temp.print();
		}
		
	}
	
	public Node highest (Node N, double max) {
		Node highest = N.getDr() < max ? N : new Node("FaKington", -1);
		
		if(N.hasLeft() && highest(N.getLeft(), max).getDr() < max && highest.getDr() < highest(N.getLeft(), max).getDr())
			highest = highest(N.getLeft(), max);
		
		if(N.hasRight() && highest(N.getRight(), max).getDr() < max && highest.getDr() < highest(N.getRight(), max).getDr())
			highest = highest(N.getRight(), max);		
		
		return highest;		
	}
}