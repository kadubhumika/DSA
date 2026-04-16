public class practical2 {
    public static void main(String[] args) {
        TypePeople p1 = new Introvert();
        TypePeople p2 = new Extrovert();
        TypePeople p3 = new Ambivert();
        p1.habit();  
        p2.habit();
        p3.habit();  
    }
}
class TypePeople {
    void habit() {
        System.out.println("People have habits");
    }
    void strength() {
        System.out.println("People have strengths");
    }
    void weakness() {
        System.out.println("People have weaknesses");
    }
    void message() {
        System.out.println("Everyone is unique");
    }
}
class Introvert extends TypePeople {
    @Override
    void habit() {
        System.out.println("Introvert likes quiet places");
    }
}
class Extrovert extends TypePeople {
    @Override
    void habit() {
        System.out.println("Extrovert likes social interaction");
    }
}
class Ambivert extends TypePeople {
    @Override
    void habit() {
        System.out.println("Ambivert balances both worlds");
    }
}

class SuccessPath {
    private String route;
    private String groundLevel;
    public void setRoute(String route) {
        this.route = route;
    }
    public String getRoute() {
        return route;
    }
    private void goodbye(String bye) {
        System.out.println(bye);
    }
}

