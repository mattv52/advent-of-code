import java.util.*;


public class day5p2 extends AOC {
    public static ArrayList<String> input = read(5);
    public static void main(String[] args) throws Exception {
        // int SOIL_INDEX = 3;
        // int FERT_INDEX = 33;
        // int WATER_INDEX = 50;
        // int LIGHT_INDEX = 90;
        // int TEMP_INDEX = 120;
        // int HUMID_INDEX = 168;
        // int LOC_INDEX = 180;
        int SOIL_INDEX = 3;
        int FERT_INDEX = 7;
        int WATER_INDEX = 12;
        int LIGHT_INDEX = 18;
        int TEMP_INDEX = 22;
        int HUMID_INDEX = 27;
        int LOC_INDEX = 31;
        
        Long num = (long) 0;
        String[] seedsInit = input.get(0).split(" ");
        while (true) {
            Long x = num;
            System.out.println(num);
            x = convert(x, LOC_INDEX);
            x = convert(x, HUMID_INDEX);
            x = convert(x, TEMP_INDEX);
            x = convert(x, LIGHT_INDEX);
            x = convert(x, WATER_INDEX);
            x = convert(x, FERT_INDEX);
            x = convert(x, SOIL_INDEX);
            if (checked(x, seedsInit)) {System.out.println(num); break;}
            num++;
        }
    }

    public static boolean checked(Long num, String[] seeds) {
        for (int i = 1; i < seeds.length; i+=2) {
            if (num >= Long.parseLong(seeds[i]) && num < Long.parseLong(seeds[i])+Long.parseLong(seeds[i+1])) {
                return true;
            }
        }
        return false;
    }

    public static Long convert(Long num, int index) {
        // Long[] next = seeds.clone();
        while(true) {
            String line = input.get(index);
            if (line.equals("") || index == input.size()-1) break;
            String[] split = line.split(" ");
            Long source = Long.parseLong(split[1]);
            Long destination = Long.parseLong(split[0]);
            Long step = Long.parseLong(split[2]);
            // System.out.printf("%d, %d, %d\n", source, destination, step);

            if (num >= destination && num < destination+step) {
                // System.out.println("true");
                // System.out.printf("%d, %d, %d\n", seeds[i], source, source+step);
                return source+(num-destination);
                // next[i] = (destination + (seeds[i]-source));
            }

            index++;
        }
        return num;
    }
}