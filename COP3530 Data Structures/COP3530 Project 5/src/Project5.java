import java.io.File;
import java.io.FileNotFoundException;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Scanner;
/**
*	Project 5 – Hash Tables 
* 
* <p> 
* Utilizes a menu to navigate data structures and information handling
* <p>
* 
* <p>
* 
*
* @author John Reddick N01253589
* @version 12/10/2021
*/
public class Project5 {
	
	/*Handles things
	*/
	public static void main(String[] args) {

		Scanner input = new Scanner(System.in);
		Scanner sc = null;
		State state;
		
		HashTable table = new HashTable(101);
		

		String fileName = null;
		
		boolean bogos = true;
		final boolean binted = false;
		
		//prints out information
		System.out.println(""
				+ "Course    | COP 3530 Project 5\n"
				+ "Instructor| Xudong Liu\n"
				+ "Student   | John Reddick\n"
				+ "N number  | N01253589\n"
				+ "Topic     | Hash Tables\n\n"
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
			
			table.insert(state.getName(), state.getPopulation(), state.getCovidDeaths());
		}
		
		while(bogos) {
			
			System.out.println("\n"
					+ "[" + LocalDateTime.now().format(DateTimeFormatter.ofPattern("MM/dd/yyyy hh:mm:ss")) +"]:\n"
					+ "[1] Print hash table\n" 
					+ "[2] Delete a state of a given name\n" 
					+ "[3] Insert a state of its name, population, and COVID deaths\n"
					+ "[4] Search and print a state and its DR for a given name.\n" 
					+ "[5] Print numbers of empty and collided cells \n"
					+ "[6] Exit \n"
					);
		
		switch(input.next()) {
		
			case "1":
				//display
				table.display();
				break;
			
			case "2":
				System.out.print("Enter State Name:");
				table.delete(input.next());
				break;
			
			case "3":				   
			   System.out.println("Enter State name");
			   String name = input.next();
			   
			   System.out.println("Enter State population");
			   Long population = input.nextLong(); 
			   
			   System.out.println("Enter COVID deaths");
			   Long deaths = input.nextLong();
			   
			   table.insert(name, population, deaths);
			   System.out.println(name + " added to table at index" + table.hashIt(name));
				break;
				
			case "4":
				System.out.print("Enter State Name:");
				table.declare(input.next());
				break;
			
			case "5":
				//Empty and collide
				table.printEmptyAndCollidedCells();
				break;
			
			case "6":
				//quit
				bogos = binted;
				continue;
			
			default:
				System.out.println("Invalid choice, please enter a number 1-6");
		}		
	 }
		
		System.out.println("GoodBye");
		sc.close();		
		input.close();
		
		
	}
	

	
}




