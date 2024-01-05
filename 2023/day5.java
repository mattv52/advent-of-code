import java.util.*;


public class day5 extends AOC {
    public static ArrayList<String> input = read(5);
    public static int index = 0;
    public static void main(String[] args) throws Exception {
        // ArrayList<String> input = read(5);
        String[] seedsInit = input.get(0).split(" ");
        Long[] seeds = new Long[seedsInit.length -1];
        for (int i=0; i<seeds.length; i++) {
            seeds[i] = Long.parseLong(seedsInit[i+1]);
        }
        
        index = 3;
        // Seed to soil
        seeds = convert(seeds);

        // Soil to fertilizer
        seeds = convert(seeds);

        // fert to water
        seeds = convert(seeds);

        // water to light
        seeds = convert(seeds);

        // light to temp
        seeds = convert(seeds);

        // temp to humid
        seeds = convert(seeds);

        // humid to location
        seeds = convert(seeds);
        Arrays.sort(seeds);
        System.out.println(seeds[0]);
        System.out.println(seeds[1]);
        
    }

    public static Long[] convert(Long[] seeds) {
        Long[] next = seeds.clone();
        while(true) {
            String line = input.get(index);
            if (line.equals("") || index == input.size()-1) break;
            String[] split = line.split(" ");
            Long source = Long.parseLong(split[1]);
            Long destination = Long.parseLong(split[0]);
            Long step = Long.parseLong(split[2]);
            // System.out.printf("%d, %d, %d\n", source, destination, step);

            for (int i = 0; i < seeds.length; i++) {
                if (seeds[i] >= source && seeds[i] < source+step) {
                    // System.out.println("true");
                    // System.out.printf("%d, %d, %d\n", seeds[i], source, source+step);
                    next[i] = (destination + (seeds[i]-source));
                }
            }

            index++;
        }
        index+=2;
        return next;
    }
}