public class Perceptron {

    //PREDICTS WHETHER THE PERCEPTRON WILL ACTIVATE OR NOT
    //NET VALUE
    public static double predict(double[] row, double[] weights) {
        double activation = weights[0];
        for (int i = 0; i < weights.length - 1; i++) {
            activation += weights[i + 1] * row[i];
        }
        //1.0 activated , 0.0 not activated THRESHOLD 0
        return activation >= 0 ? 1.0 : 0.0;
    }

    //CALCULATING NUMBER OF GOOD PREDICTIONS
    public static double accuracy(double[] actualAnswer, double[] predictedAnswer) {
        double correctAnswer = 0;
        for (int i = 0; i < actualAnswer.length; i++) {
            if (actualAnswer[i] == predictedAnswer[i]) correctAnswer++;
        }
        return correctAnswer / actualAnswer.length * 100;
    }

    /*
       calculating weights until it reaches acc good accuracy or n number of iterations
        rows , has 1 if correct answer or 0 if incorrect
        alpha, 'speed' of learning
        returns array of weights that is the same length as any row
     */
    public static double[] trainWeights(double[][] rows, double alpha, double n, double acc) {
        double[] weights = new double[rows[0].length];
        double accuracy = 0;
        for (int i = 0; i < n && accuracy < acc; i++) {
            int errors = 0;

            for (int j = 0; j < rows.length; j++) {
                double prediction = predict(rows[j], weights);
                //training weights algorithm
                int error = (int) (rows[j][rows[j].length - 1] - prediction);
                //1-1 = 0, 0-1 = -1, 1-0 = 1 0-0 = 0, TO CALCULATE NUMBER OF ERRORS
                //absolute value of error
                errors += Math.abs(error);
                weights[0] = weights[0] + alpha * error;

                for (int k = 0; k < rows[j].length - 1; k++) {
                    //ALGORITHM FOR TRAINING WEIGHTS
                    //W' = W + alpha(d-y)*X
                    weights[k + 1] = weights[k + 1] + alpha * error * rows[j][k];
                }
            }
            System.out.println("\n Loop: " + (i + 1) + " Alpha: " + alpha + " Errors: " + errors);
            accuracy = (100 - (double) errors / rows.length * 100);
            System.out.println("acc = " + accuracy);
        }
        return weights;
    }


}