import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.List;

public class Perceptron {

    double[] weights;
    double rate;
    String LangName;

    Perceptron(String LangName) {
        weights = new double[26];
        for (int i = 0; i < weights.length; i++) {
            weights[i] = Math.random();
        }
        this.rate = 0.3;
        this.LangName = LangName;
    }

    double computeOutput(Language language) {
        double result = 0;
        Double[] xs = language.getPercentage().values().toArray(new Double[26]);
        for (int j = 0; j < xs.length; j++) {
            result += xs[j] * weights[j];
        }
        return result;
    }

    void deltaTraining(List<Language> languages) {
        while (true) {
            for (Language language : languages) {
                Double[] xs = language.getPercentage().values().toArray(new Double[26]);
                double o = computeOutput(language);
                double t = language.getName().equals(LangName) ? 1 : 0;
                if (t - o >= 0 && t - o <= 0.01) {
                    System.out.println(LangName + " perceptron finished training. ");
                    return;
                }
                for (int j = 0; j < weights.length; j++) {
                    weights[j] += rate * (t - o) * xs[j];
                }
            }
        }

    }


    public static double accuracy(double[] actualAnswer, double[] predictedAnswer) {
        double correctAnswer = 0;
        for (int i = 0; i < actualAnswer.length; i++) {
            if (actualAnswer[i] == predictedAnswer[i]) correctAnswer++;
        }
        return correctAnswer / actualAnswer.length * 100;
    }


    public static void checkFile(File file, Perceptron perceptron)
    {
        String fileContent = null;
        try (BufferedReader br = new BufferedReader(new FileReader(file))) {
            String line;
            while ((line = br.readLine()) != null) {
                fileContent += line;
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        String reworkedFileContent = fileContent.replaceAll("[^a-zA-z]","");
        double result = perceptron.computeOutput(new Language().addData(reworkedFileContent));

    }
}
