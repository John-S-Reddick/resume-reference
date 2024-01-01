import java.io.File;
import java.io.FileNotFoundException;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Scanner;
/**
* COP 3530: Project 4 – Binary search Trees
* 
* <p> 
* Utilizes a menu to navigate data structures and information handling
* <p>
* 
* <p>
* 
*
* @author John Reddick N01253589
* @version 11/16/2021
*/
public class Project4 {
	
	/*Handles things
	*/
	public static void main(String[] args) {

		Scanner input = new Scanner(System.in);
		Scanner sc = null;
		State state;
		
		
		BinarySearchTree bst = new BinarySearchTree();

		String fileName = null;
		
		int count = 0;
		boolean bogos = true;
		final boolean binted = false;
		
		//prints out information
		System.out.println(""
				+ "Course    | COP 3530 Project 4\n"
				+ "Instructor| Xudong Liu\n"
				+ "Student   | John Reddick\n"
				+ "N number  | N01253589\n"
				+ "Topic     | Binary search trees!\n\n"
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
		
		
		for(int i = 0; i < 50; i++) {			
			state = new State(sc.next(),sc.next(),sc.next(),sc.nextInt(),sc.nextInt(),
				sc.nextInt(),sc.nextInt(),sc.nextInt(),sc.nextFloat());

			bst.insert(state.getName(), state.getCdr());				
		}
		
		while(bogos) {
			
			System.out.println("\n"
					+ "[" + LocalDateTime.now().format(DateTimeFormatter.ofPattern("MM/dd/yyyy hh:mm:ss")) +"]:\n"
					+ "[1] Print tree inorder\n"
					+ "[2] Print tree preorder\n"
					+ "[3] Print tree postorder\n"
					+ "[4] Delete a state for a given name\n"
					+ "[5] Search and print a state and its path for a given name.\n"
					+ "[6] Print bottom states regarding DR\n"
					+ "[7] Print top states regarding DR\n"
					+ "[8] Exit\n"
					+ "\nMake your selection:\t"
					);
		
		switch(input.next()) {
		
			case "1":
				bst.printInorder();
				break;
			
			case "2":
				bst.printPreorder();
				break;
			
			case "3":
				bst.printPostorder();
				break;
				
			case "4":
				System.out.println("Type out the name of the state\nYou would like to delete:");
				bst.delete(input.next());
				break;
			
			case "5":
				System.out.println("Type out the name of the state\nYou would like to find:");
				bst.find(input.next());
				break;
			
			case "6":
				System.out.println("How many states?");
				bst.printBottomStates(input.nextInt());
				break;
				
			case "7":
				System.out.println("How many states?");
				bst.printTopStates(input.nextInt());
				break;
			
			case "8":
				bogos = binted;
				continue;
			
			default:
				System.out.println("Invalid choice, please enter a number 1-8");
		}		
	 }
		
		System.out.println("GoodBye");
		sc.close();		
		input.close();
		
		
	}
	

	
}


