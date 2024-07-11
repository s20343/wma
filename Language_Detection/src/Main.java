import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.concurrent.atomic.AtomicReference;

public class Main {

    private final static String LANGUAGE_PATH = "LanguageDepository/TrainingLanguages";
    private final static String LANGUAGE_TEST_PATH = "LanguageDepository/TestLanguages";
    private static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        /**
         * TRAINING PERCEPTRONS
         */
        ArrayList<Language> languageList = new ArrayList<>();
        BufferedReader reader;
        File LangFolder = new File(LANGUAGE_PATH);
        File[] allLanguages = LangFolder.listFiles();
        assert allLanguages != null;
        for (File allLanguage : allLanguages) {
            Language language = new Language(allLanguage.getName());
            ArrayList<String> data = new ArrayList<>();
            File LangDataFolder = new File(LANGUAGE_PATH + "/" + allLanguage.getName());
            File[] LangData = LangDataFolder.listFiles();
            //for (int j = 0; j < LangData.length; j++) {
            for (int j = 0; j < 1; j++) {
                reader = new BufferedReader(new FileReader(LANGUAGE_PATH + "/" + allLanguage.getName() + "/" + LangData[j].getName()));
                String line;
                while ((line = reader.readLine()) != null) {
                    //delete all non A-Z signs
                    data.add(line.replaceAll("[^a-zA-z]", ""));
                }
            }
            language.setData(data);
            languageList.add(language);
        }
        System.out.println("Number of  languages:  " + languageList.size() );

        languageList.forEach(language -> {
            System.out.println("Language name: " + "| " + language.getName() + " \n");
            System.out.println(language.getPercentage());

        });

        ArrayList<Language> languageTestList = new ArrayList<>();
        BufferedReader readerTest;
        File LangTestFolder = new File(LANGUAGE_TEST_PATH);
        File[] allTestLanguages = LangTestFolder.listFiles();
        assert allTestLanguages != null;
        for (File allLanguage : allTestLanguages) {
            Language language = new Language(allLanguage.getName());
            ArrayList<String> data = new ArrayList<>();
            File LangDataFolder = new File(LANGUAGE_TEST_PATH + "/" + allLanguage.getName());
            File[] LangData = LangDataFolder.listFiles();
            //for (int j = 0; j < LangData.length; j++) {
            for (int j = 0; j < 1; j++) {
                readerTest = new BufferedReader(new FileReader(LANGUAGE_TEST_PATH + "/" + allLanguage.getName() + "/" + LangData[j].getName()));
                String line;
                while ((line = readerTest.readLine()) != null) {
                    //delete all non A-Z signs
                    data.add(line.replaceAll("[^a-zA-z]", ""));
                }
            }
            language.setData(data);
            languageTestList.add(language);
        }
        System.out.println("Number of test languages:  " + languageTestList.size() );


        languageTestList.forEach(language -> {
            System.out.println("Language name: " + "| " + language.getName() + " \n");
            System.out.println(language.getPercentage());

        });

        ArrayList<Perceptron> perceptronList = new ArrayList<>();
        languageList.forEach(
                language -> {
                    Perceptron perceptron = new Perceptron(language.getName());
                    perceptron.deltaTraining(languageList);
                    perceptronList.add(perceptron);
                }
        );

        System.out.println("Perceptrons finished training.");

        for (Perceptron perceptron : perceptronList) {
            System.out.println("Tested perceptron: " + perceptron.LangName);

        }

        /**
         * TEST PERCEPTRONS
        */
        System.out.println(perceptronList);



        /*ArrayList<Perceptron> perceptronTestList = new ArrayList<>();
        languageTestList.forEach(
                language -> {
                    Perceptron perceptron = new Perceptron(language.getName());
                    perceptron.deltaTraining(languageTestList);
                    perceptronTestList.add(perceptron);
                }
        );*/

        System.out.println("\n*Custom values*");
        boolean inputValues = true;

        while(true)
        {
            HandleInput(perceptronList);
        }

       /* GUI.perceptronList = perceptronList;
        GUI.launch(args);*/
    }



    private static void HandleInput(List<Perceptron> perceptronList)
    {
        System.out.println("Give word (give 0 to exit the programme): \n");
        String input = sc.nextLine();
        System.out.println("Given input: " + input);
        String inputAfterWork = input.replaceAll("[^a-zA-z]","");
        System.out.println("Input analysed: " + inputAfterWork);
        if(input.equalsIgnoreCase("0"))
        {
            System.exit(0);
        }
        AtomicReference<Perceptron> max = new AtomicReference<>();
        perceptronList.forEach(perceptron -> {
            double result = perceptron.computeOutput(new Language().addData(inputAfterWork));
            if (max.get() == null) max.set(perceptron);
            if (result > max.get().computeOutput(new Language().addData(inputAfterWork))) max.set(perceptron);
        });
        System.out.println("This word is in: " + max.get().LangName);
    }



}
