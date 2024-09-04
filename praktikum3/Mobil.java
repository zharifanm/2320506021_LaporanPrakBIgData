package praktikum3;

public class Mobil {
    private String merk;
    private String model;
    private int tahun;
    private String warna;

    public Mobil(String merk, String model, int tahun, String warna) {
        this.merk = merk;
        this.model = model;
        this.tahun = tahun;
        this.warna = warna;
    }
    public String getMerk() {
        return merk;
    }
    public void setMerk(String merk) {
        this.merk = merk;
    }
    public String getModel() {
        return model;
    }
    public void setModel(String model) {
        this.model = model;
    }
    public int getTahun() {
        return tahun;
    }
    public void setTahun(int tahun) {
        this.tahun = tahun;
    }
    public String getWarna() {
        return warna;
    }
    public void setWarna(String warna) {
        this.warna = warna;
    }
    public void displayInfo() {
    System.out.println("\nMerk mobil tersebut adalah " + merk + " dengan Model " + model + 
                       " dan keluaran tahun " + tahun + " berwarna " + warna);
    }
    public void startEngine() {
        System.out.println("Mesin mobil " + merk + " menyala");
    }
    public void ubahWarna(String warnaBaru) {
    this.warna = warnaBaru;
    System.out.println("\nWarna mobil diubah menjadi " + warnaBaru);
    }

}
