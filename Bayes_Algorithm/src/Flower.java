import java.util.Arrays;

public class Flower {
    private String[] attributes;

    public Flower(String[] attributes) {
        this.attributes = attributes;
    }
    public String getFlowerDecision() {
        return attributes[attributes.length - 1];
    }
    public String[] getFlowerAttributes() {
        return attributes;
    }


}
