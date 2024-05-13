import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Declarations
        boolean outOfBounds;

        // Getting input from a user
        Scanner myScanner = new Scanner(System.in);
        int ussdCode;

        // Check if the user input is not out of bounds. Called error control
        do {
            outOfBounds = false; // Reset outOfBounds flag
            // Prompt user to enter information
            System.out.println("Menu: ");
            System.out.println("1. Check Balance \n2. Buy \n3. Voice  \n4. Just4you");
            ussdCode = myScanner.nextInt();

            if (ussdCode > 5 || ussdCode < 1) {
                System.out.println("This is out of bounds! Please enter a valid menu option");
                outOfBounds = true;
            }
        } while (outOfBounds);

        // Use switch and case statement
        switch (ussdCode) {
            // This code block executes if the user selects 1.
            case 1: {
                System.out.println("Check balance option selected");
                System.out.println("You do not have airtime, you think you'll have data?");
                break;
            }
            // This code block executes if the user selects 2.
            case 2: {
                System.out.println("Buy option selected");
                System.out.println("1. DATA \n2. VOICE \n3. SOCIAL BUNDLES \n4. SMS ");
                int option = myScanner.nextInt();

                switch (option) {
                    case 1: {
                        System.out.println("1. 10 mb for R10 \n2. 100 mb for R30 \n3. 1GB for R59 \n4. 5 GB for R99 ");
                        int dataOption = myScanner.nextInt();
                        if (dataOption == 1) {
                            System.out.println("You have successfully bought 10 mb for R10 ");
                        } else if (dataOption == 2) {
                            System.out.println("You have successfully bought 100 mb for R30 ");
                        } else if (dataOption == 3) {
                            System.out.println("You have successfully bought 1GB for R59 ");
                        } else if (dataOption == 4) {
                            System.out.println("You have successfully bought 5 GB for R99 ");
                        } else {
                            System.out.println("Invalid option selected");
                        }
                        break;
                    }
                    case 2: {
                        System.out.println("Buy voice option selected");
                        System.out.println("1. 10 mins at R10 for 3 days \n2. 30 mins at R5 for today \n3. 60 mins for 3 days at R19 \n4. 50 minutes for today at R5 ");
                        int dataOption = myScanner.nextInt();
                        if (dataOption == 1) {
                            System.out.println("You have successfully bought 10 mins at R10 for 3 days ");
                        } else if (dataOption == 2) {
                            System.out.println("You have successfully bought 30 mins at R5 for today");
                        } else if (dataOption == 3) {
                            System.out.println("60 mins for 3 days at R19 ");
                        } else if (dataOption == 4) {
                            System.out.println("50 minutes for today at R5 ");
                        } else {
                            System.out.println("Invalid option selected");
                        }
                        break;
                    }
                    case 3: {
                        System.out.println("Buy social bundles option selected");
                        System.out.println("1. 100 mb at R5 for 1 hour \n2. 1 GB for today at R19  \n3. 1 GB whatsapp at R49 for 30 days \n4. 5 GB youtube bundles for today at R35 ");
                        int dataOption = myScanner.nextInt();
                        if (dataOption == 1) {
                            System.out.println("You have successfully bought 100 mb at R5 for 1 hour ");
                        } else if (dataOption == 2) {
                            System.out.println("You have successfully bought 1 GB for today at R19");
                        } else if (dataOption == 3) {
                            System.out.println("You have successfully bought 1 GB whatsapp at R49 for 30 days");
                        } else if (dataOption == 4) {
                            System.out.println("You have successfully bought 5 GB youtube bundles for today at R35 ");
                        } else {
                            System.out.println("Invalid option selected");
                        }
                        break;
                    }
                    case 4: {
                        System.out.println("Buy SMS option selected");
                        System.out.println("1. 10 SMS at R5 for today \n2. 30 SMS at R6 for 5 days \n3. 50 SMS for 30 days at R20  ");
                        int dataOption = myScanner.nextInt();
                        if (dataOption == 1) {
                            System.out.println("You have successfully bought 10 SMS at R5 for today ");
                        } else if (dataOption == 2) {
                            System.out.println("You have successfully bought 30 SMS at R6 for 5 days");
                        } else if (dataOption == 3) {
                            System.out.println("50 SMS for 30 days at R20 ");
                        } else {
                            System.out.println("Invalid option selected");
                        }
                        break;
                    }
                    default:
                        System.out.println("Invalid option selected");
                }
                break;
            }
            // This code block executes if the user selects 3.
            case 3: {
                System.out.println("Buy voice option selected");
                System.out.println("1. All NETWORK \n2. VODA TO VODA ");
                int option = myScanner.nextInt();

                switch (option) {
                    case 1: {
                        System.out.println("All network option selected");
                        System.out.println("1. 10 mins at R10 for today \n2. 100 mins for 3 days at R30 \n3. 50 mins for taday at R29 ");
                        int dataOption = myScanner.nextInt();
                        if (dataOption == 1) {
                            System.out.println("You have successfully bought 10 mins at R10 for today ");
                        } else if (dataOption == 2) {
                            System.out.println("You have successfully bought 100 mins for 3 days at R30 ");
                        } else if (dataOption == 3) {
                            System.out.println("You have successfully bought 50 mins for taday at R29");
                        } else {
                            System.out.println("Invalid option selected");
                        }
                        break;
                    }
                    case 2: {
                        System.out.println("Voda to voda option selected");
                        System.out.println("1. 10 mins at R5 for today \n2. 30 mins at R10 for 3 days \n3. 60 mins for 3 days at R19 \n4. 50 minutes for today at R5 ");
                        int dataOption = myScanner.nextInt();
                        if (dataOption == 1) {
                            System.out.println("You have successfully bought 10 mins at R5 for today ");
                        } else if (dataOption == 2) {
                            System.out.println("You have successfully bought 30 mins at R10 for 3 days");
                        } else if (dataOption == 3) {
                            System.out.println("You have successfully bought 60 mins for 3 days at R19 ");
                        } else if (dataOption == 4) {
                            System.out.println("You have successfully bought 50 minutes for today at R5 ");
                        } else {
                            System.out.println("Invalid option selected");
                        }
                        break;

                    }
                    default:
                        System.out.println("Invalid option selected");
                }
                break;
            }
            // This code block executes if the user selects 4.
            case 4: {
                System.out.println("Buy just4you option selected");
                System.out.println("1. Student \n2. Town \n3. Everyday-ta ");
                int option = myScanner.nextInt();

                switch (option) {
                case 1: {
                    System.out.println("Student option selected");
                    System.out.println("1. 2 GB day and 2 GB night-owl at R50 \n2.  5 GB day and 5 GB night-owl at R150 \n3.  10 GB day and 10 GB night-owl at R299 ");
                    int dataOption = myScanner.nextInt();
                    if (dataOption == 1) {
                        System.out.println("You have successfully bought 2 GB day and 2 GB night-owl at R50 ");
                    } else if (dataOption == 2) {
                        System.out.println("You have successfully bought 5 GB day and 5 GB night-owl at R150");
                    } else if (dataOption == 3) {
                        System.out.println("You have successfully bought 10 GB day and 10 GB night-owl at R299 ");
                    } else {
                        System.out.println("Invalid option selected");
                    }
                    break;
                }
                case 2: {
                    System.out.println("Town bundles option selected");
                    System.out.println("1. 1 GB for today at R12 \n2. 5 GB for 3 days at R35 ");
                    int dataOption = myScanner.nextInt();
                    if (dataOption == 1) {
                        System.out.println("You have successfully bought 1 GB for today at R12 ");
                    } else if (dataOption == 2) {
                        System.out.println("You have successfully bought 5 GB for 3 days at R35");
                    } else {
                        System.out.println("Invalid option selected");
                    }
                    break;
                }
                case 3: {
                    System.out.println("Everyday-ta option selected");
                    System.out.println("1. 10 SMS at R5 for today \n2. 30 MB at R3 for 5 days \n3. 10 GB for 30 days at R75  ");
                    int dataOption = myScanner.nextInt();
                    if (dataOption == 1) {
                        System.out.println("You have successfully bought 10 SMS at R5 for today ");
                    } else if (dataOption == 2) {
                        System.out.println("You have successfully bought 30 MB at R3 for 5 days");
                    } else if (dataOption == 3) {
                        System.out.println("You have successfully bought 10 GB for 30 days at R75");
                    } else {
                        System.out.println("Invalid option selected");
                    }
                    break;
                }
                default:
                    System.out.println("Invalid option selected");
            }

                break;
            }

            default:
                System.out.println("Invalid option selected");
        }
    }
}
