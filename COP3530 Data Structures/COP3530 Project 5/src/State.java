import java.util.Scanner;

/*
* @author John Reddick
* @version 9/16/2021
*/

public class State {
	private String name, capitol, region;
	private long population;
	private int seats, covidCases, covidDeaths, mhi;
	private double vcr, ccr, cdr, cfr;
	
	
	
	public State(
			String name,
			String capitol,
			String region,
			int seats,
			int population,
			int covidCases,
			int covidDeaths,
			int mhi,
			float vcr
			){
		
		this.name = name;
		this.capitol = capitol;
		this.region = region;
		this.seats = seats;
		this.population = population;
		this.covidCases = covidCases;
		this.covidDeaths = covidDeaths;
		this.mhi = mhi;
		this.vcr = vcr;
		
		this.ccr = 100000 * (covidCases/(float)population); 	//Covid Case rate
		this.cdr = 100000 * (covidDeaths/(float)population);	//Covid death rate
		this.cfr = covidDeaths/(float)covidCases;				//Covid Fatality rate
	}
	
	
	public State() {
		manualEntry();
	}
	
	public void manualEntry() {
		Scanner input = new Scanner(System.in);
		
		quickPrint("name"); name = input.next();
		quickPrint("capitol"); capitol = input.next();
		quickPrint("region"); region = input.next();
		quickPrint("seats"); seats = input.nextInt();
		quickPrint("population"); population = input.nextInt();
		quickPrint("covid cases"); covidCases = input.nextInt();
		quickPrint("covid deaths"); covidDeaths = input.nextInt();
		quickPrint("mhi"); mhi = input.nextInt();
		quickPrint("vcr"); vcr = input.nextFloat();
		
		this.ccr = 100000 * (covidCases/(float)population); 	//Covid Case rate
		this.cdr = 100000 * (covidDeaths/(float)population);	//Covid death rate
		this.cfr = covidDeaths/(float)covidCases;				//Covid Fatality rate

	}
		
	private void quickPrint(String str) {
		System.out.printf("\nEnter %s:",str);
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getCapitol() {
		return capitol;
	}

	public void setCapitol(String capitol) {
		this.capitol = capitol;
	}

	public String getRegion() {
		return region;
	}

	public void setRegion(String region) {
		this.region = region;
	}

	public int getSeats() {
		return seats;
	}

	public void setSeats(int seats) {
		this.seats = seats;
	}

	public long getPopulation() {
		return population;
	}

	public void setPopulation(long population) {
		this.population = population;
	}

	public int getCovidCases() {
		return covidCases;
	}

	public void setCovidCases(int covidCases) {
		this.covidCases = covidCases;
	}

	public int getCovidDeaths() {
		return covidDeaths;
	}

	public void setCovidDeaths(int covidDeaths) {
		this.covidDeaths = covidDeaths;
	}

	public int getMhi() {
		return mhi;
	}

	public void setMhi(int mhi) {
		this.mhi = mhi;
	}

	public double getVcr() {
		return vcr;
	}

	public void setVcr(float vcr) {
		this.vcr = vcr;
	}

	public double getCcr() {
		return ccr;
	}

	public void setCcr(float ccr) {
		this.ccr = ccr;
	}

	public double getCdr() {
		return cdr;
	}

	public void setCdr(float cdr) {
		this.cdr = cdr;
	}

	public double getCfr() {
		return cfr;
	}

	public void setCfr(float cfr) {
		this.cfr = cfr;
	}
	


	
	public void print() {
		System.out.format(
			"%-14s\t%6d   %4.1f   %.6f   %8.2f\t%7.2f\n"
			,this.name, this.mhi, this.vcr, this.cfr, this.ccr, this.cdr);
	}
	

	
	/*
	* Description of the purpose of the method, the meaning of the 
	* input parameters (if any) and the meaning of the return values 
	* (if any).
	*/
	public void printInd() {
		System.out.format("\n"				
			+ "Name:        %-14s\n"
			+ "MHI:         %-6d\n"
			+ "VCR:         %-4.1f\n"
			+ "CFR:         %-6.6f\n"
			+ "Case Rate:   %-8.2f\n"
			+ "Death Rate:  %-7.2f\n"
			,this.name, this.mhi, this.vcr, this.cfr, this.ccr, this.cdr);
	}

		
	}
