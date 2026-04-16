public class playgames {
    public static void main(String[] args) {
        TypeGame game1 = new Badminton();
        TypeGame game2 = new Cricket();
        TypeGame game3 = new Chess();
        game1.start();
        game1.play();
        game1.setScore(21);
        System.out.println("Score: " + game1.getScore());
        game1.end();
        game2.start();
        game2.play();
        game2.setScore(250);
        System.out.println("Score: " + game2.getScore());
        game2.end();
        game3.start();
        game3.play();
        game3.setScore(1);
        System.out.println("Score: " + game3.getScore());
        game3.end();
    }
}
abstract class TypeGame {
    private int score; 
    abstract void start();
    abstract void play();
    abstract void end();
    public int getScore() {
        return score;
    }
    public void setScore(int score) {
        this.score = score;
    }
}
class Badminton extends TypeGame {
    void start() {
        System.out.println("Badminton game started");
    }
    void play() {
        System.out.println("Playing Badminton");
    }
    void end() {
        System.out.println("Badminton game ended");
    }
}
class Cricket extends TypeGame {
    void start() {
        System.out.println("Cricket match started");
    }
    void play() {
        System.out.println("Playing Cricket");
    }
    void end() {
        System.out.println("Cricket match ended");
    }
}
class Chess extends TypeGame {
    void start() {
        System.out.println("Chess game started");
    }
    void play() {
        System.out.println("Playing Chess");
    }
    void end() {
        System.out.println("Chess game ended");
    }
}
