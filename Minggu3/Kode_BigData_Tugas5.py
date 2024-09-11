import csv
from functools import reduce

# Fungsi mapper
def mapper(namafile):
    with open(namafile, 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        mapped_values = []
        for row in reader:
                nilai = float(row["nilai"])
                mapped_values.append((nilai, 1))
    return mapped_values

# Fungsi reducer_sum
def reducer_sum(values):
    total_sum = sum(value[0] for value in values)
    total_count = sum(value[1] for value in values)
    return total_sum, total_count

# Fungsi reducer_rata2
def reducer_rata2(sum_count_pair):
    total_sum, total_count = sum_count_pair
    rata2 = total_sum / total_count
    return rata2

def main():
    mapped_values = mapper('C:/Users/zhari/Documents/NilaiMhs.csv')

    sum_count_pair = reducer_sum(mapped_values)
    print(f"Total nilai dari {sum_count_pair[1]} data siswa adalah : {sum_count_pair[0]}")

    rata2 = reducer_rata2(sum_count_pair)
    print(f"Rata-rata nilai dari {sum_count_pair[1]} mahasiswa adalah : {rata2}")

if __name__ == "__main__":
    main()
