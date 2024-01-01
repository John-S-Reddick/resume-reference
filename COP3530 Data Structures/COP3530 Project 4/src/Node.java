
public class Node {
	private Node left;
	private Node right;
	
	private String name;
	private double dr;
	
	public Node(String nm, double DR) {
		left = null;
		right = null;
		
		name = nm;
		dr = DR;
	}
	
	public boolean hasLeft() {
		return left != null;
	}
	
	public boolean hasRight() {
		return right != null;
	}

	public Node getLeft() {
		return left;
	}

	public void setLeft(Node left) {
		this.left = left;
	}

	public Node getRight() {
		return right;
	}

	public void setRight(Node right) {
		this.right = right;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public double getDr() {
		return dr;
	}

	public void setDr(double dr) {
		this.dr = dr;
	}
	
	
	public void print() {
		System.out.printf("%-20s %3.2f\n", name, dr);
	}
	
	


}

