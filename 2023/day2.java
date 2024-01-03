import java.util.*;

public class day2 extends AOC {
    public static void main(String[] args) throws Exception {
        ArrayList<String> input = read(2);
        int sum = 0;
        // PART 1
        // int MAX_RED = 12;
        // int MAX_GREEN = 13;
        // int MAX_BLUE = 14;

        for (String line : input) {
            // String game = line.split("Game |:")[1];
            String[] pulls = line.split(": ")[1].split("; ");
            // Boolean valid = true;
            int red = 0;
            int green = 0;
            int blue = 0;
            
            for (String pull : pulls) {
                for (String color : pull.split(", ")) {
                    int num = Integer.parseInt(color.split(" ")[0]);
                    String c = color.split(" ")[1];
                    
                    switch (c) {
                        case "red":
                            if (num > red) red = num;
                            // if (num > MAX_RED) valid = false;
                            break;
                            case "green":
                            if (num > green) green = num;
                            // if (num > MAX_GREEN) valid = false;
                            break;
                            case "blue":
                            if (num > blue) blue = num;
                            // if (num > MAX_BLUE) valid = false;
                            break;
                    
                        default:
                            break;
                    }
                }
            }
            // if (valid) sum += Integer.parseInt(game);
            sum += red*green*blue;
        }
        System.out.println(sum);
    }
}