import pandas as pd

# Data awal

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

# Membuat DataFrame
df = pd.DataFrame(data)

# Pertanyaan 1:
# Menghitung gaji setiap karyawan setelah diberikan peningkatan sebesar 5% dari gaji saat ini
df['Gaji'] = df['Gaji'].apply(lambda x: x * 1.05)

# Pertanyaan 2:
# Menampilkan DataFrame yang sudah diperbarui
print("DataFrame setelah peningkatan gaji sebesar 5%:")
print(df)
# Ringkasan perubahan
print("\nRingkasan perubahan:")
print("Gaji setiap karyawan ditingkatkan sebesar 5%.")

# Pertanyaan 3:
# Mengevaluasi karyawan yang usianya di atas 30 tahun dan memberikan peningkatan tambahan sebesar 2%
df.loc[df['Usia'] > 30, 'Gaji'] = df.loc[df['Usia'] > 30, 'Gaji'].apply(lambda x: x * 1.02)

# Pertanyaan 4:
# Menampilkan DataFrame setelah peningkatan gaji tambahan
print("\nDataFrame setelah peningkatan gaji tambahan:")
print(df)
# Ringkasan hasil
print("\nRingkasan hasil:")
print("Gaji setiap karyawan ditingkatkan sebesar 5%. Karyawan dengan usia di atas 30 tahun menerima peningkatan tambahan sebesar 2%.")


# ---------------------------- #
# Buat Branch Baru pada repository github berikut dengan format KELAS_NRP_NAMA
# https://github.com/diashfirdaus-cyber/Pemdas_Itenas.git
# ---------------------------- #

# Catatan:

# Gunakan loop for dan fungsi lambda untuk mengimplementasikan operasi yang diminta.
# Pastikan untuk menyimpan hasil perubahan pada DataFrame.
# Tampilkan hasil dan ringkasan dengan jelas.
# Jangan lupa untuk menyesuaikan persentase peningkatan gaji sesuai dengan cerita.