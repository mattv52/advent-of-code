import java.util.*;


public class day4 extends AOC {
    public static void main(String[] args) throws Exception {
        ArrayList<String> input = read(4);

        int sum = 0;
        for (String card : input) {
            Set<String> nums = new HashSet<String>();
            nums.addAll(Arrays.asList(card.split(": | \\| ")[2].split(" +")));
            String[] winners = card.split(": | \\| ")[1].split(" +");
            // System.out.println(nums);
            int count = -1;
            for (String win : winners) {
                if (nums.contains(win)) count++;
            }
            if (count != -1) sum += Math.pow(2, count);
        }

        System.out.println(sum);
    }
}