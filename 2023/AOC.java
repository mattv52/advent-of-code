import java.io.*;
import java.util.*;

// Super class to manage data handling for each day.
public class AOC {
    public static ArrayList<String> read(int day) {
        File file = new File(String.format("input/%d.txt", day));

        ArrayList<String> input = new ArrayList<String>();

        BufferedReader br = null;
        try {
            br = new BufferedReader(new FileReader(file));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        String s;
        try {
            while ((s = br.readLine()) != null) {
                input.add(s);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        try {
            br.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return input;
    }

}