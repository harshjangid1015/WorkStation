class CharAirthDemo{
	public static void main(String args[]){
		char ch;
		ch = 'X';
		System.out.println("ch is "+ch);
		ch++;
		System.out.println("ch is now "+ch);
		ch = 98;
		System.out.println("ch is now "+ch);
		
		for (ch=1; ch<128; ch++){
			System.out.print(ch);
		}
		
	}
}