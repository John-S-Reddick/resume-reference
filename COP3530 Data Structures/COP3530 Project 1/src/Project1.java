import java.io.File;
import java.io.FileNotFoundException;
import java.util.InputMismatchException;
import java.util.Scanner;
/**
* COP 3530: Project 1 – Array Searches and Sorts
* 
* <p>
* This Project is written in Java, and is the first project in my Data Structures 
* course. The requirements for this assignment Include the following:
* 
* 1. Reading data from a CSV file.
* 2. Processing the data from the CSV file
* 3. Storing that data in an array
* 4. The implementation of binary sorting
* 5. Manipulation of data within the array
* 6. Writing output information to a CSV file
*
* This also deals with error handling
* <p>
* 
*
* @author John Reddick
* @original version 9 /16/2021
* @updated version  12/27/2023
*/
public class Project1 {
	
	/*
	* The main method is responsible for calling and coordinating
    * Interactions between methods
	*/
	public static void main(String[] args) {

		Scanner input = new Scanner(System.in);
		Scanner sc = null;
		State states[] = new State[50];		
		String fileName = "";
		boolean prompt = true;
		
        //Header
		System.out.println(""
				+ "COP 3530 Project 1\n"
				+ "Instructor: Xudong Liu\n"
				+ "\n\n"
				+ "Array Searches and Sorts\n"
				+ "Enter file name\n");
        //File input and error handling
		while(sc == null) {
			try {
				sc = new Scanner(new File(input.nextLine()));
			} catch (FileNotFoundException e) {
				System.out.println("File not found, try again?");
				sc = null;
			}
		}
		
		
		sc.useDelimiter(",|\n");
		sc.nextLine();
		
        //File input and processing
		for(int i = 0; i < 50; i++) {
			
			states[i] = new State(
					sc.next(),
					sc.next(),
					sc.next(),
					sc.nextInt(),
					sc.nextInt(),
					sc.nextInt(),
					sc.nextInt(),
					sc.nextInt(),
					sc.nextFloat()
					);
		}
		
        //Prompts the user and takes input
		while(prompt) {
		
		switch(menuPrompt("")) {
		
		  default:
			 stateReport(states);
			 continue;

		  case 2:
			alphabetSoup(states);
			continue;
		    
		  case 3:
			covidSort(states);
		    continue;
		   
		  case 4:
			incomeSort(states);
		    continue;
		    
		  case 5:
			locate(states);
		    continue;
		    
		  case 6:
			spearmanrho(states);
		    continue;
			  
		  case 7:
			  prompt = false;
		}
	 }
		sc.close();		
		input.close();
	}

	/*
	* menuPrompt prompts the user to make a menu selection
    * menuPrompt takes in a String "addendum" as input
    * addendum is to add any additional notes or information to the menu
    * i.e.  alert the user to a misinput
    *
    * menuPrompt returns an int to be used in the switch statement in main
	*/
	public static int menuPrompt(String addendum) {
		
		int ans = -1;
		String correction = addendum;
		String chastise = "";
		Scanner input = new Scanner(System.in);
			
            //Menu Prompt		
			System.out.println("\n"
					+ "[1] Print States report\n"
					+ "[2] Sort by Name\n"
					+ "[3] Sort by Case Fatality rate\n"
					+ "[4] Sort by Median Household Income\n"
					+ "[5] Find and Print a given State\n"
					+ "[6] Print Spearman's rho matrix\n"
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
    * State Printing
    * 
	* stateReport takes in an array of state objects and calls the print function on them
    * stateReport prints a header, and then all of the states in the array
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
    * Alphabetical Ranking
    *
	* alphabetSoup takes in an array of states and assigns each one
    * a rank based on their order alphabetically
    * It does not return anything, it takes advantage of pass by reference
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
	*Sort by covid stats 
    *
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
	* Sort states by income
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
	* Sort states by crime rate
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
	* Sorts states by death statistics
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
	* Locates a state matching a name entered by the user
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
	* Performs the binary search to find a state by name
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
	* Performs a sequential search to locate a state by name
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
	* Calculates the Spearman's rho of the entire array to determine correlation statistics
	*/
	public static void spearmanrho(State states[]) {
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
		
		


