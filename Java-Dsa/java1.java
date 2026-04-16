package com.bhumika;
class SimpleDemo {

    public static void main(String[] args) {
        int a = 10;
        int b = 5;
        System.out.println("Addition: " + (a + b));
        System.out.println("Subtraction: " + (a - b));
        System.out.println("Multiplication: " + (a * b));
        System.out.println("Division: " + (a / b));
        int[] marks = {80, 85, 90};
        System.out.println("\nMarks:");
        for (int i = 0; i < marks.length; i++) {
            System.out.println(marks[i]);
        }
        String[] names = {"Bhumika", "Amit", "Riya"};
        System.out.println("\nNames:");
        for (int i = 0; i < names.length; i++) {
            System.out.println(names[i]);
        }
        String password = generatePassword("Bhumika", 123);

        System.out.println("\nGenerated Password: " + password);
    }
    static String generatePassword(String name, int number) {
        return name + "@" + number;
    }
}
