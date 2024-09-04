package praktikum3;

public class Main {
    public static void main(String[] args) {
        Hewan kucing = new Hewan("Milo", 2);
        kucing.suara();
        kucing.info();

        Hewan anjing = new Hewan("Dino", 3);
        anjing.berlari();
        anjing.info();
    }
}
