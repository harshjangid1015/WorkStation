package JavaPractice;
//Guess the letter game, 3rd version
public class Guess3 {
	public static void main(String[] args) 
			throws java.io.IOException{
		char ch, answer='K';
		System.out.println("I am thinking of a letter between A and Z");
		System.out.println("Can you guess it?");
		ch=(char) System.in.read();
		if (ch==answer) {
			System.out.println("**Right**");
		}
		else {
			System.out.println("...Sorry, you're ");
			if (ch<answer) {
				System.out.println("too low");
			}
			else {
				System.out.println("too high");
			}
		}
	}

}
