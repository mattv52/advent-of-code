import java.io.*;
import java.util.*;

// Super class to manage data handling for each day.
public class AOC {
    public static ArrayList<String> read(int day) throws Exception {
        File file = new File(String.format("input/%d.txt", day));

        ArrayList<String> input = new ArrayList<String>();

        BufferedReader br = new BufferedReader(new FileReader(file));

        String s;
        while ((s = br.readLine()) != null) {
            input.add(s);
        }
        br.close();
        return input;
    }

}