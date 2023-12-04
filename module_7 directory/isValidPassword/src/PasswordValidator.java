/*
Shane Tinsley Module 7 Assignment - 11/20/23
This code first imports the Scanner class to allow user input. 
The main method prompts the user to enter a password, checks its validity 
using the isValidPassword method, and displays the corresponding message. 
It also provides an option to check another password or exit the loop. 
The isValidPassword method checks the password length and ensures it contains 
at least one letter, digit, uppercase character, and lowercase character.
Resource used: text book and Sololearn
*/

import java.util.Scanner;

public class PasswordValidator 
{ public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.print("Enter your password: ");
            String password = scanner.nextLine();

            if (isValidPassword(password)) {
                System.out.println("Valid password.");
            } else {
                System.out.println("Invalid password.");
            }

            System.out.println("Would you like to check another password? (Y/N): ");
            String input = scanner.nextLine();
            if (!input.equalsIgnoreCase("Y")) {
                break;
            }
        }

        scanner.close();
    }

    private static boolean isValidPassword(String password) {
        if (password.length() < 8) {
            return false;
        }

        boolean hasLetter = false;
        boolean hasDigit = false;
        boolean hasUpperCase = false;
        boolean hasLowerCase = false;

        for (char c : password.toCharArray()) {
            if (Character.isLetter(c)) {
                hasLetter = true;
            }

            if (Character.isDigit(c)) {
                hasDigit = true;
            }

            if (Character.isUpperCase(c)) {
                hasUpperCase = true;
            }

            if (Character.isLowerCase(c)) {
                hasLowerCase = true;
            }
        }

        return hasLetter && hasDigit && hasUpperCase && hasLowerCase;
    }
}