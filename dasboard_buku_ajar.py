import streamlit as st
import base64
import os

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Dashboard Aplikom Statistik",
    page_icon="📊",
    layout="wide"
)

# --- FUNGSI UNTUK MERENDER PDF ---
def render_pdf(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="1000" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)
    else:
        st.error(f"File {file_path} tidak ditemukan.")

# --- DATABASE CODING (DARI LAMPIRAN-1) ---
list_contoh_soal = {
    "Soal-1": """# Contoh Soal-1: Statistik Deskripsi & Visualisasi
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# --- Contoh 1: Statistik Deskripsi ---
data_operasional = [12, 15, 14, 13, 16, 45, 14, 15, 12, 14, 13, 15]
df1 = pd.DataFrame(data_operasional, columns=['Operasional'])
print(df1.describe()) # Menampilkan mean, std dev, dll
print("median : ", np.median(data_operasional))
plt.boxplot(data_operasional)
plt.show()""",

    "Soal-2": """# Contoh Soal-2: Deteksi Outlier
import matplotlib.pyplot as plt
import seaborn as sns
# --- Contoh 2: Deteksi Outlier ---
pengeluaran = [12, 15, 14, 13, 16, 45, 14, 15, 12,
               14, 13, 15]
sns.boxplot(x=pengeluaran)
plt.title('Deteksi Outlier Pengeluaran Ritel')
plt.show()""",

    "Soal-3": """# Contoh Soal-3: Analisa Korelasi
import pandas as pd
import seaborn as sns

# --- Contoh 3: Korelasi (Pearson) ---
data_kor = {'Jam': [10, 15, 20, 25, 30],
            'Produktivitas': [60, 70, 80, 85, 95]}
df_kor = pd.DataFrame(data_kor)
print(df_kor.corr())""",

    "Soal-4": """# Contoh Soal-4: ANOVA 1, 2 Way
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
# --- Contoh 4: One-Way ANOVA ---
data_anova = pd.DataFrame({
    'Penjualan': [20, 22, 21, 19, 20,
                  25, 28, 26, 27, 29,
                  21, 23, 20, 22, 21],
    'Cabang': ['Sukun']*5 + ['Lowokwaru']*5 + ['Klojen']*5 })
model_anova = ols('Penjualan ~ C(Cabang)', data=data_anova).fit()
print(data_anova)
print(sm.stats.anova_lm(model_anova, typ=2))

import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
# --- Contoh 5: Two-Way ANOVA ---
data_tw = pd.DataFrame({
    'Penjualan': [20, 22, 21, 15, 16, 14, 28, 30, 29, 20, 19, 21],
    'Lokasi': ['Sukun']*6 + ['Lowokwaru']*6,
    'Media': (['Sosmed']*3 + ['Brosur']*3) * 2
})
model_tw = ols('Penjualan ~ C(Lokasi) + C(Media) + C(Lokasi):C(Media)', data=data_tw).fit()
print(data_tw)
print(sm.stats.anova_lm(model_tw, typ=2))
""",

    "Soal-5": """# Contoh Soal-5: Regresi Linear Sederhana
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
x = sm.add_constant([2, 4, 6, 8, 10]) # Menambah konstanta (intercept)
y = [10, 15, 25, 30, 40]
model = sm.OLS(y, x).fit()
print(model.summary())""",

    "Soal-6": """# Contoh Soal-6: Regresi Multilinear
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
data_multi = {'Y': [50, 60, 70, 80, 90], 'X1': [5, 7, 8, 10, 12], 'X2': [2, 3, 3, 4, 5]}
df_m = pd.DataFrame(data_multi)
X_m = sm.add_constant(df_m[['X1', 'X2']])
model_reg = sm.OLS(df_m['Y'], X_m).fit()
print(model_reg.summary())""",

    "Soal-7": """# Contoh Soal-7: Uji t dan Uji F (Signifikansi)
# Berdasarkan Model Regresi Multilinear Soal-6
# Uji F: Prob (F-statistic)
# Uji t: Kolom P>|t|
print(model_multi.summary())

#contoh lain
import statsmodels.api as sm
from statsmodels.formula.api import ols
from scipy import stats
# --- Contoh 10: One Sample T-Test ---
pengunjung = [45, 48, 44, 46, 45, 47, 44, 45, 46, 45]
t_stat, p_val = stats.ttest_1samp(pengunjung, 50)
print(f"P-Value: {p_val}")
""",

    "Soal-8": """# Contoh Soal-8: Prediksi Harga Properti
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
data = {'Penjualan': [50, 60, 70, 80, 90],
        'Iklan': [5, 7, 8, 10, 12],
        'Sales': [2, 3, 3, 4, 5]}
df_multi = pd.DataFrame(data)
X = df_multi[['Iklan', 'Sales']]
X = sm.add_constant(X)
Y = df_multi['Penjualan']
model_multi = sm.OLS(Y, X).fit()
print(model_multi.summary())
# Menggunakan model yang dihasilkan untuk prediksi baru
# Iklan = 10, Sales = 4
X_baru = [1, 10, 4] # 1 adalah konstanta
prediksi = model_multi.predict(X_baru)
print(f"Hasil Prediksi Penjualan: {prediksi[0]:.2f}")

# Contoh lain
# DIketahui Persamaan Regresi: Y = 200 + 5(Luas) - 10(Jarak)
luas = 100
jarak = 2

prediksi = 200 + (5 * luas) - (10 * jarak)
print(f"Prediksi Harga Rumah: {prediksi} Juta")""",

    "Soal-9": """# Contoh Soal-9: Uji Multikolinearitas (VIF)
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.outliers_influence import variance_inflation_factor

# --- Contoh 8 & 9: Uji Multikolinearitas (VIF) ---
data_multi = {'Y': [50, 60, 70, 80, 90], 'X1': [5, 7, 8, 10, 12], 'X2': [2, 3, 3, 4, 5]}
df_m = pd.DataFrame(data_multi)
X_m = sm.add_constant(df_m[['X1', 'X2']])
vif_data = pd.DataFrame()
vif_data["Variabel"] = X_m.columns
vif_data["VIF"] = [variance_inflation_factor(X_m.values, i) for i in range(len(X_m.columns))]
print(vif_data)
""",

    "Soal-10": """# Contoh Soal-10: One Sample T-Test
from scipy import stats

pengunjung = [45, 48, 44, 46, 45, 47, 44, 45, 46, 45]
t_stat, p_val = stats.ttest_1samp(pengunjung, 50)

print(f"P-Value: {p_val}")
if p_val < 0.05:
    print("Kesimpulan: Tolak H0 (Signifikan)")
else:
    print("Kesimpulan: Gagal Tolak H0")"""
}

# --- DATA MATERI UTAMA ---
materi = {
    "Halaman Utama": {"file": "Cover_buku_ajar_Aplikom_Statistik.png", "kode": None},
    "Bab 1: Statistics Computer Application": {"file": "Bab1-STATISTICS COMPUTER APPLICATION.pdf", "kode": None},
    "Bab 2: Aplikasi Komputer Statistika": {"file": "Bab2-APLIKASI KOMPUTER STATISTIKA.pdf", "kode": None},
    "Bab 3: Menu Statistik Spreadsheet": {"file": "Bab3-MENU STATISTIKA DI SPREADSHEET (Excel_Calc Libreoffice).pdf", "kode": None},
    "Bab 4: Google Sheets & PSPP": {"file": "Bab4-MENU DI GOOGLE SHEET, XLMINER ANALYSIS TOOLPAK, DAN PSPP.pdf", "kode": None},
    "Bab 5: Deskripsi & Visualisasi": {"file": "Bab5-STATISTIK DESKRIPSI DAN VISUALISASI DATA.pdf", "kode": list_contoh_soal["Soal-1"]},
    "Bab 6: Korelasi": {"file": "Bab6-KORELASI.pdf", "kode": list_contoh_soal["Soal-3"]},
    "Bab 7: ANOVA": {"file": "Bab7-ANALYSIS OF VARIANCE (ANOVA).pdf", "kode": list_contoh_soal["Soal-4"]},
    "Bab 8: Regresi Linear": {"file": "Bab8-REGRESI LINEAR.pdf", "kode": list_contoh_soal["Soal-5"]},
    "Bab 9: Regresi Multilinear": {"file": "Bab9-REGRESI MULTILINEAR.pdf", "kode": list_contoh_soal["Soal-6"]},
    "Bab 10: Uji Parsial & Serentak": {"file": "Bab10-UJI PARSIAL DAN SERENTAK.pdf", "kode": list_contoh_soal["Soal-7"]},
    "Bab 11: Regresi Untuk Prediksi": {"file": "Bab11-MODEL REGRESI UNTUK PREDIKSI.pdf", "kode": list_contoh_soal["Soal-8"]},
    "Bab 12: Uji Asumsi Regresi": {"file": "Bab12-UJI ASUMSI PADA REGRESI.pdf", "kode": list_contoh_soal["Soal-9"]},
    "Bab 13: Hipotesis & Test Statistik": {"file": "Bab13-HIPOTESIS DAN TEST STATISTIK.pdf", "kode": list_contoh_soal["Soal-10"]},
    "Bab 14: Implementasi Skripsi": {"file": "Bab14-IMPLEMENTASI STATISTIK PADA SKRIPSI.pdf", "kode": None},
    "Bab 15: Summary & Evaluasi": {"file": "Bab15-SUMMARY DAN EVALUASI PEMBELAJARAN.pdf", "kode": None},
    "Bab 16: UAS": {"file": "Bab16-UJIAN AKHIR SEMESTER (UAS).pdf", "kode": None},
    "Daftar Pustaka": {"file": "Daftar_Pustaka.pdf", "kode": None},
    "Lampiran-1: Solusi Python": {"file": "Lampiran-1-PENYELESAIAN DENGAN PROGRAM PYTHON.pdf", "kode": "FULL_LIST"},
    "Lampiran-2: Daftar Tugas": {"file": "Lampiran-2-DAFTAR TUGAS.pdf", "kode": None}
}

# --- SIDEBAR ---
st.sidebar.image("Cover_buku_ajar_Aplikom_Statistik.png", use_container_width=True)
st.sidebar.title("📚 Navigasi")
selection = st.sidebar.radio("Pilih Materi:", list(materi.keys()))

# --- RESET SESSION STATE ---
if "last_selection" not in st.session_state:
    st.session_state.last_selection = selection

if st.session_state.last_selection != selection:
    st.session_state.last_selection = selection

# --- HEADER ---
st.title("Buku Ajar Aplikasi Komputer Statistik")
st.markdown(f"**Penyusun:** Ir. M Nasri AW, M.Eng.Sc, M.Kom - Dosen STIE Indonesia Malang, @2025")
st.divider()

# --- LOGIKA TAMPILAN ---
current = materi[selection]

if selection == "Halaman Utama":
    col1 = st.columns([90, 1])
    col1[0].info(
        "Selamat datang di platform digital perkuliahan Aplikom Statistik. "
        "Buku ini merupakan kelanjutan (melengkapi) kuliah Economic Statistics, disusun dengan bahasa yang sederhana dan mudah dipahami. Penulis berharap buku ini dapat membantu mahasiswa memahami prinsip-prinsip statistik, dilengkapi contoh mengerjakannya dengan Spreadsheet, Software PSPP (Perfect Statistics Professional Presented, alternatif open source selain SPSS) dan Pemrograman Python. "
        "Contoh sederhana dari masalah sehari-hari di Manajemen dan Keuangan. Sistematika buku ajar ini, tiap bab dimulai dengan Pokok Bahasan dan Tujuan Pembelajaran, sub bab dan penjelasannya dan Rangkuman, Contoh soal dan Tugas. Tiap bab sesuai pertemuan kuliah (mingguan), minggu ke-8 dilaksanakan Ujian Tengah Semester (UTS) dan minggu ke-16 Ujian Akhir Semester (UAS). "
        "Untuk memberikan pemahaman bagaimana mengerjakan dengan Aplikasi Komputer, di akhir buku diberikan lampiran source code python untuk Contoh Soal dan Tugas. "
        "Selamat belajar, semoga sukses dan bermanfaat untuk karir profesional di bidang Manajemen, Keuangan, Data Science, dan Riset Akademik."
    )

else:
    st.header(selection)
    
    # 1. Materi
    st.subheader("🖼️ Materi")
    render_pdf(current["file"])
    
    st.divider()

    # 2. Coding Python (Logika Khusus Lampiran-1)
    if current["kode"] == "FULL_LIST":
        st.subheader("🐍 Kumpulan Contoh Soal (Lampiran-1)")
        tabs = st.tabs([f"Soal {i}" for i in range(1, 11)])
        for i, tab in enumerate(tabs):
            tab.code(list_contoh_soal[f"Soal-{i+1}"], language='python')
    
    elif current.get("kode"):
        st.subheader("🐍 Contoh Coding Python")
        st.code(current["kode"], language='python')

    # 3. Download
    st.subheader("📥 Download")
    if os.path.exists(current["file"]):
        with open(current["file"], "rb") as f:
            st.download_button(label=f"Unduh {selection}", data=f, file_name=current["file"], mime="application/pdf")

st.divider()
st.caption("© 2025 Ir. M Nasri AW | Dashboard Akademik Digital")
