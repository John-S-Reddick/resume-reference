import java.io.BufferedOutputStream;
import java.io.DataOutputStream;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.PrintStream;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.InputMismatchException;
import java.util.Scanner;
/**
* COP 3530: Project 3 – Stacks and Priority Queues With linked lists!
* 
* <p> 
* Utilizes a menu to navigate data structures and information handling
* <p>
* 
* <p>
* 
*
* @author John Reddick N01253589
* @version 10/22/2021
*/
public class Project3 {
	
	/*Handles things
	*/
	public static void main(String[] args) {

		Scanner input = new Scanner(System.in);
		Scanner sc = null;
		State state;
		
		Stack stupidStack = new Stack();
		PriorityQ dumbPQ = new PriorityQ();
		
		String fileName = null;
		int count = 0;
		boolean bogos = true;
		final boolean binted = false;
		
		//prints out information
		System.out.println(""
				+ "Course    | COP 3530 Project 3\n"
				+ "Instructor| Xudong Liu\n"
				+ "Student   | John Reddick\n"
				+ "N number  | N01253589\n"
				+ "Topic     | Stacks and Queues!\n\n"
				+ "Date      | " + LocalDateTime.now().format(DateTimeFormatter.ofPattern("EEEE, MMMM dd yyyy")) +"\n"
			    + "Time      | " + LocalDateTime.now().format(DateTimeFormatter.ofPattern("hh:mm:ss")) +"\n\n"				
				+ "Enter file name\n");
		
		while(sc == null) {
			try {
				sc = new Scanner(new File(fileName == null ? input.nextLine() : fileName));
			} catch (FileNotFoundException e) {
				System.out.println("File not found, try again?");
				sc = null;
			}
		}
		
		System.out.println("\nFile successfully loaded");		
		sc.useDelimiter(",|\n");
		sc.nextLine();
		
		//Reads values into a new state and adds them to the stack
		for(int i = 0; i < 50; i++) {			
			state = new State(sc.next(),sc.next(),sc.next(),sc.nextInt(),sc.nextInt(),
				sc.nextInt(),sc.nextInt(),sc.nextInt(),sc.nextFloat());

			//Validates each value is between FAIR, GOOD, and VGOOD
			if(state.getCdr() >= 70 && state.getCdr() < 250) {
				stupidStack.push(state);
				count++;
			}
				
		}
		
		System.out.println("50 Records read\n" + count
				+ " Qualified records inserted into the stack\n");
		
		stupidStack.printStack();
		
		while(!stupidStack.isEmpty()) {
			dumbPQ.insert(stupidStack.pop());
		}
		
		System.out.println("\n" + count + 
				" Records popped from the stack," +
				" and inserted into the priority queue");
		
		System.out.println();
		dumbPQ.printQueue();
		
		while(bogos) {
			System.out.println("\n"
					+ "[" + LocalDateTime.now().format(DateTimeFormatter.ofPattern("MM/dd/yyyy hh:mm:ss")) +"]:\n"
					+ "[1] Enter a DR interval for deletions\n"
					+ "[2] Print priority queue\n"
					+ "[3] Exit\n"
					+ "\nMake your selection:\t"
					);
		
		switch(input.next()) {
		
			default:
				System.out.println("Invalid choice, please enter a number 1-3");
				break;
			
			case "1":
				intervalDelete(dumbPQ, input);
				break;
			
			case "2":
				dumbPQ.printQueue();
				break;
			
			case "3":
				bogos = binted;
				break;		
		}		
	 }
		
		System.out.println("GoodBye");
		sc.close();		
		input.close();
	}
	
	
	public static void intervalDelete(PriorityQ PQ, Scanner input) {
		float x = -1, y = -1;
		
		
		while(x < 0 || y < 0) {
			System.out.println("Enter DR interval like [x,y]:");
			
			while(x == -1)
				try {
					System.out.print("\nX:");
					x = input.nextInt();
				} catch(Exception e) {
					System.out.print("Please enter a numerical value");
					input.nextLine();
					x = -1;
				}
			
			
			while(y == -1)
				try {
					System.out.print("\nY:");
					y = input.nextInt();
				} catch(Exception e) {
					System.out.print("Please enter a numerical value");
					input.nextLine();
					y = -1;
				}
			
			if(x > y) {
				System.out.println("X is greater than Y, re-enter values");
				continue;
			}
			System.out.print("Removed ");			
			PQ.intervalDelete(x,y).printQueue();
		}		
		
		
	}
	
}


