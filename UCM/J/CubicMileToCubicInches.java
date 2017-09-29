import.java.util.Scanner;

class CubicMileToCubicInches{
	
	
	public static void main(String args[]){
		
				
		int mile = 1;
		int feet = 5280*mile;
		int inches = 12*feet;
		int foot;
		long cubicMmile = mile*mile*mile;
		long cubicInches = inches*inches*inches;
		Scanner scan = new Scanner(System.in);
		
		System.out.println(Enter a number for mile: );
		long mile = scan.nextInt();
		
		
		
		System.out.println("1 mile is 5280 feet");
		System.out.println("1 foot is 12 inches");
		System.out.println(mile +" mile is " + inches + " inches");
		System.out.println(cubicMmile +" cubic mile is "+ cubicInches+ " cubic inches");
		
	}
}