import java.util.Scanner;

public class Node { 
	String name; 
	long population; 
	long deaths; 
	Node nextNode; 
 
   public Node(String name, long population, long deaths) { 
	this.name = name; 
	this.population = population; 
	this.deaths = deaths;
	nextNode = null;
   }
  
 
   public void printNode() { 
	   System.out.printf("%-30s %-20.2f", name, 
			   (double)deaths/population*100000); 
   }
   
   public double getDr() {
	   return (double)deaths/population*100000;
   }
   
   public void recPrint() {
	   printNode();
	   if(hasNextNode()) {
		   System.out.printf("\n     ");
		   nextNode.recPrint();
	   }
   }
   

	public String getName() {
		return name;
	}
	
	public void setName(String name) {
		this.name = name;
	}
	
	public long getPopulation() {
		return population;
	}
	
	public void setPopulation(long population) {
		this.population = population;
	}
	
	public long getDeaths() {
		return deaths;
	}
	
	public void setDeaths(long deaths) {
		this.deaths = deaths;
	}
	
	public Node getNextNode() {
		return nextNode;
	}
	
	public void setNextNode(Node nextNode) {
		this.nextNode = nextNode;
	}
	
	public boolean hasNextNode() {
		return nextNode != null;
	}
}