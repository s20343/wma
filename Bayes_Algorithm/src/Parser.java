import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Pattern;

public class Parser
{
    public static List<Flower> parseFromFile(String path) {
        List<Flower> list = new ArrayList<>();
        File file = new File(path);

        try (BufferedReader reader = new BufferedReader(new InputStreamReader(new FileInputStream(file)))) {
            String line;
            while ((line = reader.readLine()) != null) {
                list.add(parseFromString(line));
            }
        } catch (IOException e) {
            System.out.println("FILE NOT FOUND: " + path);
            System.exit(1);
        }
        return list;
    }


    public static Flower parseFromString(String str) {
        String[] flowerstr = str.split(",");
        return  new Flower(flowerstr);
    }

}
