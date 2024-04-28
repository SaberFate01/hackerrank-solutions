import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

//Java if-else
public class Solution {

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int N = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
        if (N % 2 != 0) {
            System.out.println("Weird");
        } else {
            if (N >= 2 && N <= 5) {
                System.out.println("Not Weird");
            } else if (N >= 6 && N <= 20) {
                System.out.println("Weird");
            } else {
                System.out.println("Not Weird");
            }
        }
        scanner.close();
    }
}

// Java Stdin and Stdout II
public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int a = scan.nextInt();
        int b = scan.nextInt();
        int c = scan.nextInt();
        scan.close();
        System.out.println(a);
        System.out.println(b);
        System.out.println(c);
    }
}

// Java Stdin and Stdout II
import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int i = scan.nextInt();

        // Write your code here.
        double d = scan.nextDouble();
        scan.nextLine();
        String s = scan.nextLine();
        scan.close();

        System.out.println("String: " + s);
        System.out.println("Double: " + d);
        System.out.println("Int: " + i);
    }
}

// Java output formatting
import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("================================");
        for (int i = 0; i < 3; i++) {
            String s1 = sc.next();
            int x = sc.nextInt();
            // Complete this line
            int stringLen = s1.length();
            int xLen = String.valueOf(x).length();
            String space = " ".repeat(15 - stringLen);
            if (xLen != 3) {
                String lackChar = "0".repeat(Math.max(0, 3 - xLen));
                String b = lackChar + String.valueOf(x);
                System.out.println(s1 + space + b);
            } else {
                System.out.println(s1 + space + x);
            }
        }
        System.out.println("================================");

    }
}

// Java Loops I
public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(bufferedReader.readLine().trim());
        for (int i = 1; i < 11; i++) {
            System.out.println(N + " x " + i + " = " + N * i);
        }
        bufferedReader.close();
    }
}

// Java Loops II
class Solution {
    public static void main(String[] argh) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        int array[];
        for (int i = 0; i < t; i++) {
            int a = in.nextInt(); // 0
            int b = in.nextInt(); // 2
            int n = in.nextInt(); // 10

            int result = a;
            for (int j = 0; j < n; j++) {
                result += (b * (Math.pow(2, j)));
                System.out.print("" + result + " ");
            }
            System.out.println();

        }
        in.close();
    }
}

// Java Datatypes
class Solution {
    public static void main(String[] argh) {

        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        for (int i = 0; i < t; i++) {

            try {
                long x = sc.nextLong();
                System.out.println(x + " can be fitted in:");
                if (x >= -128 && x <= 127)
                    System.out.println("* byte");
                if (x >= -32768 && x <= 32767)
                    System.out.println("* short");
                if (x >= Math.pow(-2, 31) && x <= Math.pow(2, 31) - 1)
                    System.out.println("* int");
                if (x >= Math.pow(-2, 63) && x <= Math.pow(2, 63) - 1)
                    System.out.println("* long");
                // Complete the code
            } catch (Exception e) {
                System.out.println(sc.next() + " can't be fitted anywhere.");
            }

        }
    }
}

// Java End-of-file
public class Solution {

    public static void main(String[] args) {
        /*
         * Enter your code here. Read input from STDIN. Print output to STDOUT. Your
         * class should be named Solution.
         */
        Scanner scan = new Scanner(System.in);
        int i = 1;
        while (scan.hasNext() == true) {
            String s = scan.nextLine();
            System.out.println(i + " " + s);
            i++;
        }
        scan.close();
    }
}

// Java Static Initializer Block
public class Solution {

    public static void main(String[] args) {
        /*
         * Enter your code here. Read input from STDIN. Print output to STDOUT. Your
         * class should be named Solution.
         */
        Scanner scan = new Scanner(System.in);
        int B = scan.nextInt();
        int H = scan.nextInt();
        if (B < 0 || B > 99) {
            System.out.println("java.lang.Exception: Breadth and height must be positive");
        } else if (H < 0 || H > 99) {
            System.out.println("java.lang.Exception: Breadth and height must be positive");
        } else {
            System.out.println(B * H);
        }

    }

}

    // Java Date and Time
    // Return the day of week in String #Wednesday
    public static String findDay(int month, int day, int year) {
        Calendar calendar = Calendar.getInstance();
        String cDate = String.valueOf(day) + " " + String.valueOf(month) + " " + String.valueOf(year);
        System.out.println(cDate);
        calendar.set(year, month - 1, day);
        System.out.print(calendar.getTime());
        System.out.print(Calendar.SATURDAY);
        SimpleDateFormat dateFormat = new SimpleDateFormat("EEEEE");
        String dayOfWeek = dateFormat.format(calendar.getTime());
        return String.valueOf(dayOfWeek.toUpperCase());
    }

    // Java Currency Formatter
    public class Solution {

        public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);
            double payment = scanner.nextDouble();
            scanner.close();
            NumberFormat us = NumberFormat.getCurrencyInstance(Locale.US);
            Locale IndiaLocale = new Locale("en", "IN");
            NumberFormat india = NumberFormat.getCurrencyInstance(IndiaLocale);
            NumberFormat china = NumberFormat.getCurrencyInstance(Locale.CHINA);
            NumberFormat france = NumberFormat.getCurrencyInstance(Locale.FRANCE);

            // Write your code here.

            System.out.println("US: " + us.format(payment));
            System.out.println("India: " + india.format(payment));
            System.out.println("China: " + china.format(payment));
            System.out.println("France: " + france.format(payment));
        }
    }

    // Java Substring
    public class Solution {

        public static void main(String[] args) {
            Scanner in = new Scanner(System.in);
            String S = in.next();
            int start = in.nextInt();
            int end = in.nextInt();
            System.out.print(S.substring(start, end));
        }
    }

    // Java Substring Comparison
    public static String getSmallestAndLargest(String s, int k) {
        String smallest = "";
        String largest = "";

        // Complete the function
        // 'smallest' must be the lexicographically smallest substring of length 'k'
        // 'largest' must be the lexicographically largest substring of length 'k'
        // System.out.print(s.substring(0, k));
        smallest = s.substring(0, k);
        largest = s.substring(0, k);
        for (int i = 0; i < s.length(); i++) {
            if (i + k > s.length()) {
                break;
            }
            String sub = s.substring(i, i + k);
            if (sub.compareTo(smallest) < 0) {
                // System.out.println("sub: "+ sub + "small: " + smallest);
                smallest = sub;
            } else if (sub.compareTo(largest) > 0) {
                // System.out.println("sub: "+ sub + "largest: " + largest);
                largest = sub;
            }
        }
        return smallest + "\n" + largest;
    }

    // Java String Reverse
    public class Solution {

        public static void main(String[] args) {

            Scanner sc = new Scanner(System.in);
            String A = sc.next();
            String B = "";
            /* Enter your code here. Print output to STDOUT. */
            for (int i = A.length() - 1; i >= 0; i--) {
                // Reverse String with for loop
                B = B + (A.charAt(i));
            }
            if (B.compareTo(A) == 0) {
                System.out.print("Yes");
            } else {
                System.out.print("No");
            }
        }
    }

    // Java Anagrams
    public class Solution {

        public static String anagram(String a, String b) {
            char[] c = a.toLowerCase().toCharArray(); // Convert to char array
            char[] h = b.toLowerCase().toCharArray();
            Arrays.sort(c); // sort the arrays
            Arrays.sort(h);
            String s = String.valueOf(c); // convert to string
            String t = String.valueOf(h);
            if (s.equals(t)) {
                return "Anagrams";
            }
            return "Not Anagrams";
        }

        public static void main(String[] args) {

            Scanner s = new Scanner(System.in);
            String a = s.nextLine();
            String b = s.nextLine();
            String res = anagram(a, b);
            System.out.println(res);
        }
    }

    // Java Strings Introduction
    public class Solution {

        public static void main(String[] args) {

            Scanner sc = new Scanner(System.in);
            String A = sc.next();
            String B = sc.next();
            /* Enter your code here. Print output to STDOUT. */
            int Len = (A + B).length();
            System.out.println(Len);
            if (A.compareTo(B) > 0) {
                System.out.println("Yes");
            } else {
                System.out.println("No");
            }
            String AuP = A.substring(0, 1).toUpperCase();
            String BuP = B.substring(0, 1).toUpperCase();
            A = AuP + A.substring(1, A.length());
            B = BuP + B.substring(1, B.length());
            System.out.println(A + " " + B);
        }
}

// Java 1D Array
import java.util.*;

public class Solution {

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < a.length; i++) {
            a[i] = scan.nextInt();
        }
        scan.close();

        // Prints each sequential element in array a
        for (int i = 0; i < a.length; i++) {
            System.out.println(a[i]);
        }
    }

}

    // Java String Tokens
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();
        s = s.trim();

        // Write your code here.

        String[] wrd = s.split("[^A-Za-z]+");

        if (s.isEmpty()) {
            System.out.println(0);
        } else {
            System.out.println(wrd.length);
            for (String tkn : wrd) {
                System.out.println(tkn);
            }

        }

        scan.close();
    }
}

//Java Pattern Syntax Checker
public class Solution
{
	public static void main(String[] args){
		Scanner in = new Scanner(System.in);
		int testCases = Integer.parseInt(in.nextLine());
		while(testCases>0){
			String pattern = in.nextLine();
          	//Write your code
            try{
                Pattern compiledPattern = Pattern.compile(pattern);
                System.out.println("Valid");
            }
            catch(Exception e){
                System.out.println("Invalid");
            }
            testCases --;
		}
	}
}

