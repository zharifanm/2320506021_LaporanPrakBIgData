import csv

# Fungsi mapper untuk memproses satu kolom
def mapper(namafile):
    with open(namafile, 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        mapped_values = []
        for row in reader:
            try:
                # Ambil nilai dari satu-satunya kolom yang ada
                nilai = float(list(row.values())[0])
                mapped_values.append(nilai)
            except ValueError:
                continue 
    return mapped_values

# Fungsi menghitung frekuensi nilai 80 dan 90
def count_specific_values_no_if(values, specific_values):
    return {value: len(list(filter(lambda x: x == value, values))) for value in specific_values}

def main():
    # Panggil mapper untuk membaca file CSV
    mapped_values = mapper('C:/Users/zhari/Documents/PRAKBIGDATA/Minggu3/NilaiMhs.csv') or exit("Tidak ada data yang bisa diproses.")
    
    # Daftar nilai yang ingin dihitung frekuensinya (80 dan 90)
    specific_values = [80, 90]
    
    # Menghitung frekuensi nilai 80 dan 90
    specific_value_freq = count_specific_values_no_if(mapped_values, specific_values)
    
    # Menampilkan hasil perhitungan frekuensi
    print("Frekuensi nilai 80 dan 90:")
    for nilai, frekuensi in specific_value_freq.items():
        print(f"Nilai: {nilai}, Frekuensi: {frekuensi}")

if __name__ == "__main__":
    main()
