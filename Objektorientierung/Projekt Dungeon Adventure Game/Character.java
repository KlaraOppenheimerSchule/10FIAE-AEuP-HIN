public class Character {
    private String name;
    private int health;

    public Character(String name, int health) {
        this.name = name;
        this.health = health;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public static void main(String[] args) {
        Character c = new Character("Aragorn", 150);

        System.out.println(c.getName());

        c.setName("Legolas");

        System.out.println(c.getName());
    }
}
