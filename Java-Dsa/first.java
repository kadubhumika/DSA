import java.util.*;
public class first{
	public static void main(String[] args){
		Scanner sc = new Scanner (System.in);

		System.out.println("Enter marks value : \n");
		int marks = sc.nextInt();
		int number;
		
		do{
			if(marks>=0&&marks<=30){
				System.out.println("You are failed . please try next time .");
			}
			else if(marks>=30&&marks<=50){
				System.out.println("Better luck . Need more Effort. ");
			}
			else if(marks>=50&&marks<=80){
				System.out.println("Good job!!. Keep it up.");
			}
			else if(marks>80&&marks<=100){
				System.out.println("Excellent...");
			}
			else{
				System.out.println("Invalid Input");
			}
			
			System.out.println("Wnt to contiune if yess(1), if no(0)");
			
			number=sc.nextInt();
			System.out.println("Enter value : ");
			
			
				
		
		
			
		
	}
	while(number==1);
}
		
}	