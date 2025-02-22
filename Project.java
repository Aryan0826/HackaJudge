import java.util.Scanner;

public class Project {
    public String name;
    public int innovation;
    public int execution;
    public int impact;
    public int design;
    public int pitch;

    // A single Scanner instance for the entire class
    private static Scanner scanner = new Scanner(System.in);

    // Constructor: sets name and defaults scores to 0
    public Project(String name) {
        this.name = name;
        this.innovation = 0;
        this.execution = 0;
        this.impact = 0;
        this.design = 0;
        this.pitch = 0;
    }

    // Method to input the innovation score
    public void inputInnovationScore() {
        System.out.print("Enter innovation score: ");
        this.innovation = scanner.nextInt();
    }

    // Method to input the execution score
    public void inputExecutionScore() {
        System.out.print("Enter execution score: ");
        this.execution = scanner.nextInt();
    }

    // Method to input the impact score
    public void inputImpactScore() {
        System.out.print("Enter impact score: ");
        this.impact = scanner.nextInt();
    }

    // Method to input the design score
    public void inputDesignScore() {
        System.out.print("Enter design score: ");
        this.design = scanner.nextInt();
    }

    // Method to input the pitch score
    public void inputPitchScore() {
        System.out.print("Enter pitch score: ");
        this.pitch = scanner.nextInt();
    }

    public int totalScore() {
        return innovation + execution + impact + design + pitch;
    }
}



