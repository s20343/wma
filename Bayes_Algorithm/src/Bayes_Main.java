
import java.util.ArrayList;
import java.util.List;

import java.util.Map;
import java.util.Scanner;
import java.util.stream.Collectors;

public class Bayes_Main {


    private List<Flower> flowerTrainList;
    private List<List<String>> attributesOptions;


    private static int VirginicaAndVirginica;
    private static int VirginicaButVersicolor;
    private static int VirginicaButSetosa;

    private static int VersicolorAndVersicolor;
    private static int VersicolorButVirginica;
    private static int VersicolorButSetosa;

    private static int SetosaAndSetosa;
    private static int SetosaButVersicolor;
    private static int SetosaButVirginica;

    public Bayes_Main(List<Flower> flowerTrainList) {
        this.flowerTrainList = flowerTrainList;
        this.attributesOptions = getAttributesOptions();
    }

    public static void main(String[] args) {
        VirginicaAndVirginica = 0;
        VirginicaButVersicolor = 0;
        VirginicaButSetosa = 0;

        VersicolorAndVersicolor = 0;
        VersicolorButVirginica = 0;
        VersicolorButSetosa = 0;

        SetosaAndSetosa = 0;
        SetosaButVersicolor = 0;
        SetosaButVirginica = 0;

        List<Flower> trainList = Parser.parseFromFile("src/iris_training.txt");
        List<Flower> testList = Parser.parseFromFile("src/iris_test.txt");

        Bayes_Main analyzer = new Bayes_Main(trainList);
        analyzer.analyseTestList(testList);
        userInput(analyzer);
    }

    private List<List<String>> getAttributesOptions() {
        Flower f = flowerTrainList.get(0);
        List<List<String>> result = new ArrayList<>();

        for (int i = 0; i < f.getFlowerAttributes().length; i++) {
            int indx = f.getFlowerAttributes().length - (f.getFlowerAttributes().length - i);
            List<String> currAttribOptions = flowerTrainList.stream()
                    .map(c -> c.getFlowerAttributes()[indx])
                    .distinct()
                    .collect(Collectors.toList());
            result.add(currAttribOptions);
        }
        return result;
    }

    private void analyseTestList(List<Flower> testList) {
        double correctCount = 0;
        for (Flower f : testList) {
            if (analyseTestFlower(f)) {
                correctCount++;
            }
        }
        System.out.printf("Correctly predicted %4.0f out of %4d, precision: %3.3f\n",
                correctCount, testList.size(), correctCount / testList.size());
        System.out.println("Giving information.");
        System.out.printf("\n\n\n\n\n\n\n\n\n");
        System.out.println("===================");
        System.out.println("Giving information.");
        System.out.println("===================");
        System.out.println("Accuracy:" + correctCount/testList.size() * 100 + "%");
        System.out.println("CONFUSION MATRIX:");

        System.out.println("    | Vir |  Ver | Set | ");
        System.out.println("Vir |" + VirginicaAndVirginica + "    | " + VirginicaButVersicolor + "    | " + VirginicaButSetosa + "   | ");
        System.out.println("Ver |" + VersicolorButVirginica + "    | " + VersicolorAndVersicolor + "    | " + VersicolorButSetosa + "   | ");
        System.out.println("Set |" + SetosaButVirginica + "    | " + SetosaButVersicolor + "    | " + SetosaAndSetosa + "  | ");


        float TPVirginica = VirginicaAndVirginica;
        float FNVirginica = VirginicaButVersicolor+VirginicaButSetosa;
        float FPVirginica = VersicolorButVirginica+SetosaButVirginica;
        float TNVirginica = VersicolorAndVersicolor+VersicolorButSetosa+SetosaButVersicolor+SetosaAndSetosa;

        float TPVersicolor = VersicolorAndVersicolor;
        float FNVersicolor = VersicolorButSetosa+VersicolorButVirginica;
        float FPVersicolor = VirginicaButVersicolor + SetosaButVersicolor;
        float TNVersicolor = VirginicaAndVirginica + SetosaAndSetosa + VirginicaButSetosa + SetosaButVirginica;

        float TPSetosa = SetosaAndSetosa;
        float FNSetosa = SetosaButVersicolor + SetosaButVirginica;
        float FPSetosa = VirginicaButSetosa + VersicolorButSetosa;
        float TNSetosa = VirginicaAndVirginica+VersicolorAndVersicolor+VirginicaButVersicolor+VersicolorButVirginica;



        float PreVirginica = TPVirginica/(TPVirginica + FPVirginica);
        float PreVersi = TPVersicolor/(TPVersicolor+FPVersicolor);
        if(FNSetosa == 0) FNSetosa = 1;
        float PreSeto = TPSetosa/(TPSetosa+FPSetosa);
        System.out.println("Precision:");
        System.out.println("Iris-virginica = " + PreVirginica*100  + "%");
        System.out.println("Iris-versicolor = " + PreVersi*100   + "%");
        System.out.println("Iris-setosa = " + PreSeto*100 + "%");

        float ReVirginica = TPVirginica/(TPVirginica+FNVirginica);
        float ReVersicolor = TPVersicolor/(TPVersicolor+FNVersicolor);
        float ReSetosa = TPSetosa/(TPSetosa+FNSetosa);
        System.out.println("Recall:");
        System.out.println("Iris-virginica = " + ReVirginica *100 + "%");
        System.out.println("Iris-versicolor = " +ReVersicolor  *100 + "%");
        System.out.println("Iris-setosa = " + ReSetosa *100 + "%");

        float FmVirginica = (2*ReVirginica*PreVirginica)/(PreVirginica+ReVirginica);
        float FmVersi = (2*ReVersicolor*PreVersi)/(PreVersi+ReVersicolor);
        float FmSeto = (2*ReSetosa*PreSeto)/(ReSetosa+PreSeto);
        System.out.println("F-Measure");
        System.out.println("Iris-virginica = " + FmVirginica *100  + "%");
        System.out.println("Iris-versicolor = " + FmVersi *100  + "%");
        System.out.println("Iris-setosa = " + FmSeto *100 + "%");

    }

    private boolean analyseTestFlower(Flower f) {

        String predicted = predictFlowerType(f);
        boolean isCorrect = predicted.equals(f.getFlowerDecision());
        if(isCorrect & predicted.equals("Iris-virginica"))
        {
            VirginicaAndVirginica++;
        }else if (!isCorrect & f.getFlowerDecision().equals("Iris-versicolor"))
        {
            VirginicaButVersicolor++;
        }else if (!isCorrect & f.getFlowerDecision().equals("Iris-setosa"))
        {
            VirginicaButSetosa++;
        }else if(isCorrect & predicted.equals("Iris-versicolor"))
        {
            VersicolorAndVersicolor++;
        }else if (!isCorrect & f.getFlowerDecision().equals("Iris-virginica"))
        {
            VersicolorButVirginica++;
        }else if(!isCorrect & f.getFlowerDecision().equals("Iris-Setosa")) {
            VersicolorButSetosa++;
        }else if(isCorrect & predicted.equals("Iris-setosa"))
        {
            SetosaAndSetosa++;
        }else if (!isCorrect & f.getFlowerDecision().equals("Iris-versicolor"))
        {
            SetosaButVersicolor++;
        }else SetosaButVirginica++;


        System.out.printf("predicted: %7s | actual: %7s | %1s\n", predicted, f.getFlowerDecision(), isCorrect ? "+" : "-");
        return isCorrect;
    }

    private String predictFlowerType(Flower f) {
        Map<String, Double> decisionProbabilities = attributesOptions.get(attributesOptions.size() - 1).stream()
                .collect(Collectors.toMap(s -> s, s -> computeDecisionProbability(s, f)));
        String maxKey = null;
        for (Map.Entry<String, Double> entry : decisionProbabilities.entrySet()) {
            if (maxKey == null || decisionProbabilities.get(maxKey) < entry.getValue()) {
                maxKey = entry.getKey();
            }
        }
        return maxKey;
    }

    private double computeDecisionProbability(String decision, Flower flower) {
        double result = 1;
        List<Flower> flowersByDecision = flowerTrainList.stream()
                .filter(c -> c.getFlowerDecision().equals(decision))
                .collect(Collectors.toList());
        for (int i = 0; i < flower.getFlowerAttributes().length; i++) {
            if (i == flower.getFlowerAttributes().length - 1) {
                result *= computeAttribProbability(i, decision, flowerTrainList);
            } else {
                result *= computeAttribProbability(i, flower.getFlowerAttributes()[i], flowersByDecision);
            }
        }
        return result;
    }

    public double computeAttribProbability(int indx, String val, List<Flower> universe) {
        double nominator = universe.stream()
                .filter(c -> c.getFlowerAttributes()[indx].equals(val))
                .count() + 1;
        double denominator = universe.size() + attributesOptions.get(indx).size();

        //SMOOTHING
        if(nominator == 0)
        {
            nominator++;
            denominator = denominator + universe.get(0).getFlowerAttributes().length-1;
        }
        return nominator / denominator;
    }


    private static void userInput(Bayes_Main analyser) {
        Scanner sc = new Scanner(System.in);
        String in;
        while (true) {
            System.out.println("Enter data or write 'zero' to exit");
            in = sc.nextLine();
            if (in.equals("zero")) {
                break;
            }
            Flower f = Parser.parseFromString(in);
            analyser.analyseTestFlower(f);
        }
    }

}
