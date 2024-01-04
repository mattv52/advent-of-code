import java.util.*;
import java.util.stream.IntStream;


public class day4 extends AOC {
    public static void main(String[] args) throws Exception {
        ArrayList<String> input = read(4);
        int[] copies = new int[input.size()];
        Arrays.fill(copies, 1);

        // int sum = 0;
        for (String card : input) {
            Set<String> nums = new HashSet<String>();
            // System.out.println(card);
            int game = Integer.parseInt(card.split("Card +|: ")[1])-1;
            nums.addAll(Arrays.asList(card.split(": | \\| ")[2].split(" +")));
            String[] winners = card.split(": | \\| ")[1].split(" +");
            // System.out.println(nums);
            int count = 0;
            for (String win : winners) {
                if (nums.contains(win)) count++;
            }
            for (int i=1; i < count+1; i++) {
                copies[game+i]+= copies[game];
            }
            // if (count != 0) sum += Math.pow(2, count-1);
        }

        // System.out.println(sum);
        System.out.println(IntStream.of(copies).sum());
    }
}