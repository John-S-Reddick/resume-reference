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
* COP 3530: Project 2 – Stacks and Priority Queues
* 
* <p> 
* Utilizes a menu to navigate data structures and information handling
* <p>
* 
* <p>
* 
*
* @author John Reddick N01253589
* @version 10/8/2021
*/
public class Project2 {
	
	/*Handles things
	*/
	public static void main(String[] args) {

		Scanner input = new Scanner(System.in);
		Scanner sc = null;
		State state;
		
		Stack stupidStack = new Stack(50);
		PriorityQ dumbPQ = new PriorityQ(50);
		
		String fileName = null;
		boolean bogos = true;
		final boolean binted = false;
		
		System.out.println(""
				+ "Course    | COP 3530 Project 2\n"
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
		
		for(int i = 0; i < 50; i++) {
			
			state = new State(sc.next(),sc.next(),sc.next(),sc.nextInt(),sc.nextInt(),
				sc.nextInt(),sc.nextInt(),sc.nextInt(),sc.nextFloat());
			
			stupidStack.push(state);
			dumbPQ.insert(state);
		}		
		System.out.println("50 Records recorded to Stack and Queue\n");
		
		while(bogos) {
		
		switch(menuPrompt("")) {
		
		  default:
			stupidStack.printStack();
			continue;

		  case 2:
			System.out.printf("\n\n");
			if(!stupidStack.isEmpty())
				stupidStack.pop().print();
			else
				System.out.printf("The Stack is empty, nothing ");
			
			System.out.printf("is removed from the stack.\nSize: %2d\n\n", stupidStack.size());
			continue;
		    
		  case 3:
			stupidStack.push(new State());
		    continue;
		   
		  case 4:
			dumbPQ.printQueue();
		    continue;
		    
		  case 5:
			System.out.printf("\n\n");
			if(!dumbPQ.isEmpty())
				dumbPQ.remove().print();
			else
				System.out.printf("The queue is empty, nothing ");
			
			System.out.printf("is removed from the queue.\nSize: %2d\n\n", dumbPQ.size());
			continue;
		    
		  case 6:
			dumbPQ.insert(new State());
		    continue;
			  
		  case 7:
			  bogos = binted;
		}		
	 }
		
		System.out.println("GoodBye");
		sc.close();		
		input.close();
	}

	/*
	* Description of the purpose of the method, the meaning of the 
	* input parameters (if any) and the meaning of the return values 
	* (if any).
	*/
	public static int menuPrompt(String addendum) {
		
		int ans = -1;
		String correction = addendum;
		String chastise = "";
		Scanner input = new Scanner(System.in);
					
			System.out.println("\n"
					+ "[" + LocalDateTime.now().format(DateTimeFormatter.ofPattern("MM/dd/yyyy hh:mm:ss")) +"]:\n"
					+ "[1] Print Stack\n"
					+ "[2] Pop a State object from Stack\n"
					+ "[3] Push a state object onto stack\n"
					+ "[4] Print priority queue\n"
					+ "[5] Remove a state object from priority queue\n"
					+ "[6] Insert a state object into priority queue\n"
					+ "[7] Quit\n"
					+ correction
					+ "\nMake your selection:\t"
					);
			
			try {
				ans = input.nextInt();
			} catch (InputMismatchException e) {
				ans = -1;
				chastise = " numerical"; //This string is intended to remind the user to enter a numerical value
			}		
			
			correction = "\n\nPlease enter a valid" + chastise + " value between 1 and 7";			
			
		return (ans <= 7 && ans >= 1) ? ans : menuPrompt(correction);
	}

	/*
	* Description of the purpose of the method, the meaning of the 
	* input parameters (if any) and the meaning of the return values 
	* (if any).
	*/
	public static void stateReport(State states[]) {
		
		System.out.format(
				"%-14s   %-6s  %-4s   %-6s     %-8s   %-7s\n%s\n",
				"State","MHI","VCR","CFR","Case Rate","Death Rate",
				"-----------------------------------------------------------------"
				);
		
		for(int i = 0; i < 50; i++) {
			states[i].print();
		}
	}
	
	/*
	* Description of the purpose of the method, the meaning of the 
	* input parameters (if any) and the meaning of the return values 
	* (if any).
	*/
	public static void alphabetSoup(State states[]) {
		State temp;		
		int c1,c2,z, key;
		
			if(states[0].getBetRank() == -1) {
			
			for(int j = 0; j < 49; j++) {
				for(int i = 0; i < 49; i++) {
					z=-1;
					do {
						++z;
						c1 = (int)states[i].getName().charAt(z);
						c2 = (int)states[i + 1].getName().charAt(z);
					} while(c1 == c2);
					
					temp = states[i];				
					if(c1 > c2) {
						states[i] = states[i+1];
						states[i+1] = temp;
					}
				}
			}
			
			for(int i = 0; i < 50; i++)
				states[i].setBetRank(i);
			
	} else {
		for(int i = 0; i < 50; i++) {
			key = states[i].getBetRank();
			temp = states[key];
			
			states[i] = temp;
			states[key] = states[i];				
			}
		}
			states[0].setLastSort(0);
	}
	
	/*
	* Description of the purpose of the method, the meaning of the 
	* input parameters (if any) and the meaning of the return values 
	* (if any).
	*/
	public static void covidSort(State states[]) {
		
		State temp;
		int key = 0;
		
		if(states[0].getCcRank() == -1) {
			
			for(int i = 0; i < 50; i++) {
				temp = states[i];
				key = i;
				for (int j = i + 1; j < 50; j++) {
					if (states[j].getCfr() < states[key].getCfr())
			            key = j;	
				}
				states[i] = states[key];
				states[key] = temp;
				
				}
			
			for(int i = 0; i < 50; i++)
				states[i].setCcRank(i);
			
		} else {
			for(int i = 0; i < 50; i++) {
				key = states[i].getCcRank();
				temp = states[key];
				
				states[i] = temp;
				states[key] = states[i];				
			}
		}
		states[0].setLastSort(1);
	}
	
	/*
	* Description of the purpose of the method, the meaning of the 
	* input parameters (if any) and the meaning of the return values 
	* (if any).
	*/
	public static void incomeSort(State states[]) {
		State temp;
		int key = 0;		
		
		if(states[0].getiRank() == -1) {		
			for(int i = 1; i < 50; i++) {
				for(int j = i; (j > 0) && states[j].getMhi() < states[j - 1].getMhi(); j--) {
						temp = states[j];
						states[j] = states[j-1];
						states[j-1] = temp;
					}
				}			
			for(int i = 0; i < 50; i++)states[i].setiRank(i);

		} else {
			for(int i = 0; i < 50; i++) {
				key = states[i].getCcRank();
				temp = states[key];
				
				states[i] = temp;
				states[key] = states[i];
			}
		}
		states[0].setLastSort(2);
	}
	
	/*
	* Description of the purpose of the method, the meaning of the 
	* input parameters (if any) and the meaning of the return values 
	* (if any).
	*/
	public static void crimeSort(State states[]) {
		
		State temp;
		int key = 0;
		
		if(states[0].getVcRank() == -1) {
			
			for(int i = 1; i < 50; i++) {
				for(int j = i; (j > 0) && states[j].getVcr() < states[j - 1].getVcr(); j--) {
						temp = states[j];
						states[j] = states[j-1];
						states[j-1] = temp;
					}
				}
			for(int i = 0; i < 50; i++)states[i].setVcRank(i);
			}	
		else {
			for(int i = 0; i < 50; i++) {
				key = states[i].getVcRank();
				temp = states[key];
				
				states[i] = temp;
				states[key] = states[i];
			}
		}
		states[0].setLastSort(3);
	}

	/*
	* Description of the purpose of the method, the meaning of the 
	* input parameters (if any) and the meaning of the return values 
	* (if any).
	*/
	public static void deathSort(State states[]) {
		State temp;
		int key = 0;
		
		if(states[0].getCdRank() == -1) {
			
			for(int i = 1; i < 50; i++) {
				for(int j = i; (j > 0) && states[j].getCdr() < states[j - 1].getCdr(); j--) {
						temp = states[j];
						states[j] = states[j-1];
						states[j-1] = temp;
					}
				}
			for(int i = 0; i < 50; i++)states[i].setCdRank(i);
			}	
		else {
			for(int i = 0; i < 50; i++) {
				key = states[i].getCdRank();
				temp = states[key];
				
				states[i] = temp;
				states[key] = states[i];
			}
		}
		states[0].setLastSort(4);
	}

	
	/*
	* Description of the purpose of the method, the meaning of the 
	* input parameters (if any) and the meaning of the return values 
	* (if any).
	*/
	public static void locate(State states[]) {
		
		Scanner input = new Scanner(System.in);		
		System.out.println("Please enter the state you wish to search for:");
		String name;
		
		int res;
		
		do {
			 name = input.nextLine();
			if(states[0].getLastSort() == 0) {
				res = binSearch(states, name.toUpperCase());
			}
			else {
				res = seqSearch(states, name.toUpperCase());
				
			}
			
			if(res == -1) {
				System.out.print(name + " Not found, Please enter a valid state\n");
			}
			else {
				states[res].printInd();
			}
			
		} while(res == -1);
			
		 }
	
	/*
	* Description of the purpose of the method, the meaning of the 
	* input parameters (if any) and the meaning of the return values 
	* (if any).
	*/
	public static int binSearch(State states[], String name) {
		int mid, res = -1, w1 = 0, w2 = 50;
		
		while(w1 < w2) {
			mid = (w2 + w1) / 2;
			res = states[mid].getName().toUpperCase().compareTo(name);
			
			if(res == 0) {
				return mid;
			}
			
			if(res < 1) {
				w1 = mid + 1;
			} else {
				w2 = mid - 1;
			}
			
		}
		return -1;
	}
	
	/*
	* Description of the purpose of the method, the meaning of the 
	* input parameters (if any) and the meaning of the return values 
	* (if any).
	*/
	public static int seqSearch(State states[], String name) {
		for(int i = 0; i < 50; i++) {
			if(states[i].getName().toUpperCase().compareTo(name) == 0) {
				return i;
			}
		}
		return -1;
	}
		
	/*
	* Description of the purpose of the method, the meaning of the 
	* input parameters (if any) and the meaning of the return values 
	* (if any).
	*/
	public static void spearmansRowMatrix(State states[]) {
		covidSort(states);
		incomeSort(states);
		crimeSort(states);
		deathSort(states);
		int denom = 50 * (50*50 - 1);
		
		String bar = "--------------------------------------\n";
		
		
		float ccrbymhi = 0;
		float ccrbyvcr = 0;
		float cdrbymhi = 0;
		float cdrbyvcr = 0;
		
		for(int i = 0; i < 50; i++) {			
			ccrbymhi += Math.pow(states[i].getCcRank() - states[i].getiRank(),2) + 6;
			ccrbyvcr += Math.pow(states[i].getCcRank() - states[i].getVcRank(),2) + 6;
			cdrbymhi += Math.pow(states[i].getCdRank() - states[i].getiRank(),2) + 6;
			cdrbyvcr += Math.pow(states[i].getCdRank() - states[i].getVcRank(),2) + 6;
		}
		
		
		
		ccrbymhi /= (float)denom;
		ccrbyvcr /= (float)denom;
		cdrbymhi /= (float)denom;
		cdrbyvcr /= (float)denom;
		
		ccrbymhi = 1 - ccrbymhi;
		ccrbyvcr = 1 - ccrbyvcr;
		cdrbymhi = 1 - cdrbymhi;
		cdrbyvcr = 1 - cdrbyvcr;
		
		
		
		System.out.format("\n"
				+ "%s|%12s|%-12s|%-12s|\n%s|%12s|%-12.6f|%-12.6f|\n%s|%12s|%-12.6f|%-12.6f|\n%s",
				bar," ","MHI","VCR", bar, "Case Rate", ccrbymhi, ccrbyvcr, bar, "Death Rate", cdrbymhi, cdrbyvcr, bar
				);			
		}		
	
}
		
		


