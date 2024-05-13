// imports go here
import java.util.Scanner;
//import java.swing.JOptionPane;


//main class and main function go here
public class Main {
    public static void main(String[] args){
        // declare scanner that you are going to use
        Scanner inputScanner = new Scanner(System.in);


        // this is a for loop
        for (int i = 0; i<= 5; i++){
            //let's print value of the increment
            System.out.println(i);
        }

        // this is a while loop
        int i =0;
        while (i <= 5){
            System.out.println(i);

            // don't forget to increment counter variable to avoid non-terminating loop
            i++;

        }

        // this is a do while loop
        int counterForWhile = 0;
        do{
            System.out.println(counterForWhile);
            counterForWhile++;
        }
        while(counterForWhile <= 5);

        // this is a for each loop. works best with arrays []
        // arrays need to be initialized with a number. no other way. only way is to do it with ArrayList

        String[] arrayNames = new String[10];
        // String[] arrayNames = {"Peter", "Petter"};  -- different ways to create arrays!

        for (int counter = 0; i < arrayNames.length; i++){
            arrayNames[counter] = inputScanner.nextLine();
        }

        for(String displayArray : arrayNames){
            System.out.println(displayArray);
        }

    }
}