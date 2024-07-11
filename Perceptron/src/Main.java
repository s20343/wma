import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        //not optimal but works, I just focus on something else then extracting data
        double[][] fileDataSetosa = Data.getDataFromFile("iris_training.txt", "Iris-setosa");
        double[][] fileDataVirginica = Data.getDataFromFile("iris_training.txt", "Iris-virginica");
        double[][] fileDataVersicolor = Data.getDataFromFile("iris_training.txt", "Iris-versicolor");

        double[][] fileTestSetosa = Data.getDataFromFile("iris_test.txt", "Iris-setosa");
        double[][] fileTestVirginica = Data.getDataFromFile("iris_test.txt", "Iris-virginica");
        double[][] fileTestVersicolor = Data.getDataFromFile("iris_test.txt", "Iris-versicolor");

        double[] weightSetosa;
        double[] weightVirginica;
        double[] weightVersicolor;

        weightSetosa = Perceptron.trainWeights(fileDataSetosa, 0.1, 10, 100);
        weightVirginica = Perceptron.trainWeights(fileDataVirginica, 0.1, 10, 100);
        weightVersicolor = Perceptron.trainWeights(fileDataVersicolor,0.1, 10, 100);

        System.out.print(" \n Setosa all weights changes: ");
        for (int i = 0; i < weightSetosa.length; i++) {
            System.out.print( weightSetosa[i] + " ");
        }
        System.out.print(" \n Virginica all weights changes: ");
        for (int i = 0; i < weightVirginica.length; i++) {
            System.out.print( weightVirginica[i] + " ");
        }
        System.out.println("\n Versicolor all weights changes: ");
        for (int i = 0; i < weightVersicolor.length; i++) {
            System.out.print( weightVersicolor[i] + " ");
        }

        double[] predictedSetosa = new double[fileTestSetosa.length];
        double[] actualSetosa = new double[fileTestSetosa.length];
        double[] predictedVirginica = new double[fileTestVirginica.length];
        double[] actualVirginica = new double[fileTestVirginica.length];
        double[] predictedVersicolor = new double[fileTestVersicolor.length];
        double[] actualVersicolor = new double[fileTestVersicolor.length];



        for (int i = 0; i < fileTestSetosa.length; i++) {
            double predictionSetosa = Perceptron.predict(fileTestSetosa[i], weightSetosa);
            double predictionVirginica = Perceptron.predict(fileTestVirginica[i], weightVirginica);
            double predictionVersicolor = Perceptron.predict(fileTestVersicolor[i], weightVersicolor);

            predictedSetosa[i] = predictionSetosa;
            actualSetosa[i] = fileTestSetosa[i][fileTestSetosa[i].length - 1];

            predictedVirginica[i] = predictionVirginica;
            actualVirginica[i] = fileTestVirginica[i][fileTestVirginica[i].length - 1];

            predictedVersicolor[i] = predictionVersicolor;
            actualVersicolor[i] = fileTestVersicolor[i][fileTestVersicolor[i].length - 1];
        }

        //printing accuracy of every assessment on the TEST data
        System.out.println("\n ==========ACCURACIES========== \n" );
        System.out.println("\nACCURACY SETOSA = " + Perceptron.accuracy(actualSetosa, predictedSetosa) + "%");

        System.out.println("\nACCURACY Virginica = " + Perceptron.accuracy(actualVirginica, predictedVirginica) + "%");

        System.out.println("\nACCURACY Versicolor = " + Perceptron.accuracy(actualVersicolor, predictedVersicolor) + "%");

        System.out.println("\n======================================");
        System.out.println("\nEND OF FILE");
        System.out.println("\n======================================");

        int dimensionsOfTheFile = fileDataSetosa[0].length - 1;

        while (true) {
            //size of plus one dimensions, so in our case size 5
            double[] customInstance = new double[dimensionsOfTheFile + 1];

            customInstance[dimensionsOfTheFile] = 0;

            //READING INPUT FROM THE USER
            ReadInput(dimensionsOfTheFile, customInstance, sc);

            System.out.println((Perceptron.predict(customInstance, weightSetosa) == 0.0 ? "Prediction: it's not " : "Prediction: it's ") + " Iris-Setosa");
            System.out.println((Perceptron.predict(customInstance, weightVersicolor) == 0.0 ? "Prediction: it's not " : "Prediction: it's ") + " Iris-Versicolor");
            System.out.println((Perceptron.predict(customInstance, weightVirginica) == 0.0 ? "Prediction: it's not " : "Prediction: it's ") + " Iris-Virginica");
        }
    }
    private static void ReadInput(int dimension, double[] customInstance, Scanner sc){
        for (int i = 0; i < dimension; i++) {
            System.out.println("Give " + "attribute number:  " + (i + 1));
            customInstance[i] = Double.parseDouble(sc.nextLine());
        }

    }
}

