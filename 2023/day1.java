import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class day1 extends AOC {
    public static void main(String[] args) throws Exception {
        ArrayList<String> input = read(1);

        int sum = 0;

        Pattern pattern = Pattern.compile("\\d|one|eno|two|owt|three|eerht|four|ruof|five|evif|six|xis|seven|neves|eight|thgie|nine|enin");
        for (String line : input) {
            // System.out.println(line);
            Matcher m = pattern.matcher(line);
            m.find();
            String first = m.group();
            m = pattern.matcher(new StringBuilder(line).reverse().toString());
            m.find();
            String last = m.group();
            sum += Integer.parseInt(convert(first)+convert(last));
            System.out.printf("%s: %d\n", line, Integer.parseInt(convert(first)+convert(last)));
        }
        System.out.println(sum);
    }

    public static String convert(String word) {
        String res;
        switch (word) {
            case "one":
            case "eno":
                res = "1";
                break;
            case "two":
            case "owt":
                res = "2";
                break;
            case "three":
            case "eerht":
                res = "3";
                break;
            case "four":
            case "ruof":
                res = "4";
                break;
            case "five":
            case "evif":
                res = "5";
                break;
            case "six":
            case "xis":
                res = "6";
                break;
            case "seven":
            case "neves":
                res = "7";
                break;
            case "eight":
            case "thgie":
                res = "8";
                break;
            case "nine":
            case "enin":
                res = "9";
                break;
    
            default:
                res = word;
                break;
        }
        return res;
    }
}