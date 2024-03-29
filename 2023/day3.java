import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class day3 extends AOC {
    public static void main(String[] args) throws Exception {
        ArrayList<String> input = read(3);
        ArrayList<ArrayList<String>> formatted = new ArrayList<ArrayList<String>>();
        for (String line : input) {
            formatted.add(new ArrayList<String>(Arrays.asList(line.split(""))));
        }
        int sum = 0;
        // Pattern pattern_symbol = Pattern.compile("[@#$%&*+=\\-\\/]");
        Pattern pattern_gear = Pattern.compile("\\*");
        Pattern pattern_num = Pattern.compile("\\d");
        int row = 0;
        int col = 0;
        int count = 0;
        int ratio = 1;
        for (ArrayList<String> line : formatted) {
            for (String symbol : line) {
                // Matcher m = pattern_symbol.matcher(symbol);
                Matcher m = pattern_gear.matcher(symbol);
                if (m.find()) {
                    // Found a symbol
                    for (int i=1; i>=-1; i--) {   
                        // System.out.printf("%d, %d\n", row, col);
                        if (pattern_num.matcher(formatted.get(row-i).get(col-1)).find()) {
                            count++;
                            ratio *= number_at(row-i, col-1, formatted);
                            // sum += number_at(row-i, col-1, formatted);
                        }
                        if (pattern_num.matcher(formatted.get(row-i).get(col)).find() && !pattern_num.matcher(formatted.get(row-i).get(col-1)).find()) {
                            count++;
                            ratio *= number_at(row-i, col, formatted);
                            // sum += number_at(row-i, col, formatted);
                        }
                        if (pattern_num.matcher(formatted.get(row-i).get(col+1)).find() && !pattern_num.matcher(formatted.get(row-i).get(col)).find()) {
                            count++;
                            ratio *= number_at(row-i, col+1, formatted);
                            // sum += number_at(row-i, col+1, formatted);
                        }
                    }
                }
                if (count == 2) {
                    sum += ratio;
                }
                count = 0;
                ratio = 1;
                col += 1;
                // System.out.println(sum);
            }
            row += 1;
            col = 0;
        }

        System.out.println(sum);
    }

    public static int number_at(int row, int col, ArrayList<ArrayList<String>> data) {
        ArrayList<String> line = data.get(row);
        Pattern pattern_num = Pattern.compile("\\d");

        int index = col;
        boolean skip = false;
        while (pattern_num.matcher(line.get(index)).find()) {
            if (index != 0) index--; 
            else {
                skip = true;
                break;
            }
        }
        if (!skip) index++;

        String num = "";
        while (pattern_num.matcher(line.get(index)).find()) {
            num += line.get(index);
            if (index == line.size()-1) break;
            index++;
        }
        // System.out.println(num);
        return Integer.parseInt(num);
    }
}