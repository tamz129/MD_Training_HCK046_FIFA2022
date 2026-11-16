# ⚽ Prediksi Rating Pemain FIFA 2022

Proyek machine learning (regresi) untuk memprediksi **overall rating** pemain FIFA 2022 berdasarkan atribut fisik dan statistik pemain. Model di-deploy dalam bentuk aplikasi web sederhana menggunakan **Streamlit**.

## 📌 Latar Belakang

Rating pemain di FIFA ditentukan dari banyak atribut (kecepatan, passing, shooting, dll). Proyek ini membuat model yang bisa memperkirakan rating pemain dari atribut tersebut, sekaligus mencari tahu atribut apa yang paling berpengaruh.

## 🎯 Tujuan

- Membangun model regresi untuk memprediksi `overall` rating pemain
- Mengetahui fitur yang paling berpengaruh terhadap rating
- Men-deploy model agar bisa dicoba langsung lewat aplikasi web

## 📂 Dataset

- **Sumber:** FIFA 2022 Players Dataset
- **Jumlah data:** Sekitar 20.000 baris
- **Target:** `overall`

**Fitur yang dipakai model:**

| Tipe | Fitur |
|------|-------|
| Numerik | `Age`, `Height`, `Weight`, `Price`, `PaceTotal`, `ShootingTotal`, `PassingTotal`, `DribblingTotal`, `DefendingTotal`, `PhysicalityTotal` |
| Kategorikal | `AttackingWorkRate`, `DefensiveWorkRate` (Low / Medium / High) |

## 🔄 Alur Pengerjaan

1. **Data Loading** - membaca dataset dengan pandas
2. **Data Cleaning** - cek missing value & duplikat
3. **EDA** - distribusi rating, korelasi antar fitur
4. **Preprocessing** - split numerik/kategorikal, scaling, encoding
5. **Modeling** - Linear Regression
6. **Evaluasi** - MAE, RMSE, dan R²
7. **Deployment** - aplikasi Streamlit

## 🌐 Aplikasi Streamlit

User mengisi form berikut, lalu menekan tombol **Predict Player Rating**:

- Nama, usia, tinggi, berat, dan harga pemain
- Attacking & Defensive Work Rate
- Total Pace, Shooting, Passing, Dribbling, Defending, dan Physicality (0-100)

Data input di-scaling (numerik) dan di-encoding (kategorikal) dengan objek yang sama seperti saat training, lalu diprediksi oleh model Linear Regression. Hasilnya berupa rating pemain (angka bulat).

## 🛠️ Tools

- Python 3
- pandas, numpy
- matplotlib, seaborn
- scikit-learn
- Streamlit
- Jupyter Notebook

## 🚀 Cara Menjalankan

```bash
# 1. Clone repository
git clone https://github.com/username/nama-repo.git
cd nama-repo

# 2. Install library
pip install -r requirements.txt

# 3. Jalankan aplikasi
streamlit run app.py
```

## 📁 Struktur Folder

```
├── app.py                  # aplikasi Streamlit
├── model_lin_reg.pkl       # model Linear Regression
├── model_scaler.pkl        # scaler untuk kolom numerik
├── model_encoder.pkl       # encoder untuk kolom kategorikal
├── list_num_cols.txt       # daftar kolom numerik
├── list_cat_cols.txt       # daftar kolom kategorikal
├── notebook.ipynb          # EDA & training model
├── requirements.txt
└── README.md
```

## 👤 Author

- Nama: Rizqi Utama
