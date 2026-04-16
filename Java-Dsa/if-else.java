import java.util.Scanner;
class StudentEvaluation {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter marks (0-100): ");
        int marks = sc.nextInt();
        if (marks >= 40) {
            System.out.println("Status: PASS");
            if (marks >= 75) {
                System.out.println("Remark: Distinction");
            } else if (marks >= 60) {
                System.out.println("Remark: First Class");
            } else if (marks >= 50) {
                System.out.println("Remark: Second Class");
            } else {
                System.out.println("Remark: Pass Class");
            }
            switch (marks / 10) {
                case 10:
                case 9:
                    System.out.println("Grade: A");
                    break;
                case 8:
                    System.out.println("Grade: B");
                    break;
                case 7:
                    System.out.println("Grade: C");
                    break;
                case 6:
                    System.out.println("Grade: D");
                    break;
                case 5:
                case 4:
                    System.out.println("Grade: E");
                    break;
                default:
                    System.out.println("Grade: F");
            }
        } else {
            System.out.println("Status: FAIL");
            System.out.println("Remark: Better luck next time");
            System.out.println("Grade: F");
        }
    }
}
