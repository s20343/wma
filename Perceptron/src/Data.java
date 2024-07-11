import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class Data {



    //DATA FROM FILE TO A 2-DIMENSION DOUBLE ARRAY,
    //LAST COLUMNT CONSTAINS A DOUBLE INSTAED OF ORIGINAL STRING

    public static double[][] getDataFromFile(String fileName, String correctString) {
        String line;
        ArrayList<String[]> al = new ArrayList<>();
        System.out.println("Reading the file...");
        try {
            FileReader fileReader = new FileReader(fileName);

            BufferedReader bufferedReader = new BufferedReader(fileReader);

            while ((line = bufferedReader.readLine()) != null) {
                String[] temp = line.split("[\\s]+");
                if (temp[0].isEmpty()) {
                    String[] temp2 = new String[temp.length - 1];
                    for (int i = 0; i < temp2.length; i++) {
                        temp2[i] = temp[i + 1];
                    }
                    temp = temp2;
                }
                al.add(temp);

            }
            bufferedReader.close();
        } catch (FileNotFoundException ex) {
            System.err.println("Error whilst opening the file: " + fileName);
        } catch (IOException ex) {
            ex.printStackTrace();
        }

        //working on file: CHANGING COMMAS INTO DOTS BECAUSE ITS NOT GOOOD ENGLISH NOTATION BUT BAD POLISH
        String[][] data = new String[al.size()][al.get(0).length];
        for (int i = 0; i < data.length; i++) {
            if (isCommaFormatted(al.get(i)))
                commasToDots(al.get(i));
            data[i] = al.get(i);
        }

//assign to the flower names
        for (int i = 0; i < data.length; i++) {
            String text = data[i][data[i].length - 1];
            if (text.equalsIgnoreCase(correctString)) {
                data[i][data[i].length - 1] = "1";
            } else {
                data[i][data[i].length - 1] = "0";
            }
        }

        double[][] dataArray = new double[data.length][data[0].length];
        for (int i = 0; i < data.length; i++) {
            for (int j = 0; j < data[i].length; j++) {
                dataArray[i][j] = Double.parseDouble(data[i][j]);
            }
        }
        System.out.println("Reading finished...");
        return dataArray;
    }


    //checks if numbers have commas instead of dots
    //true if there is at least one comma
    public static boolean isCommaFormatted(String[] data) {
        for (int i = 0; i < data.length - 1; i++) {
            if (data[i].contains(",")) {
                return true;
            }
        }
        return false;
    }


    //REPLACE EVERY COMMA TO DOT
    public static void commasToDots(String[] data) {
        for (int i = 0; i < data.length - 1; i++) {
            data[i] = data[i].replace(',', '.');
        }
    }
}