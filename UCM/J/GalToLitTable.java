class GalToLitTable{
	public static void main(String args[]){
		double gallons;
		double liters;
		
		gallons=1;
		liters= gallons*3.7854;
		
		for(gallons=1; gallons<=30; gallons++){
			liters= gallons*3.7854;
			System.out.println(gallons+" gallons is "+liters+" liters");
			
			if(gallons%10==0){
				System.out.println();
			}
		}	
	}
}