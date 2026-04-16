import java.util.*;
public class condition{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int  operation = sc.nextInt();
        switch (operation) {
            case '+':int sum = a+b;
            System.out.println("Addition of two number :");
            System.out.println(sum);
                
                break;
                case '-': int minus = a-b;
                System.out.println("Substraction of two number is :");
                System.out.println(minus);
                break;
                case '*': int multiply = a*b;
                System.out.println("Multiplication of two munber is :");
                System.out.println(multiply);
                break;
                case '/': int division = a/b;
                System.out.println("Division of two number is : ");
                System.out.println(division);
                break;
                case '%' : int module = a%b;
                System.out.println("Remainder of two number is :");
                System.out.println(module);
                break;
        
            default:System.out.println("invalid operation.");
                break;
        }
        
    }
}
