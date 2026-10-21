import streamlit as st
import numpy as np
from functools import lru_cache

st.set_page_config(page_title="Analisis Kuadrat & PKB", layout="centered")

st.title("Kalkulator Fungsi Kuadrat & Rekursi Newton")
st.markdown("Analisis mendalam persamaan $f(x) = ax^2 + bx + c$")

with st.sidebar:
    st.header("Input Koefisien")
    a = st.number_input("Nilai a", value=1.0, step=1.0)
    b = st.number_input("Nilai b", value=-4.0, step=1.0)
    c = st.number_input("Nilai c", value=3.0, step=1.0)
    
    st.divider()
    st.header("Parameter HOTS")
    st.markdown("Orde eksponensial ($n$) untuk deret akar")
    n_val = st.number_input("Nilai n", min_value=0, max_value=100, value=3, step=1)

if a == 0:
    st.error("Nilai 'a' tidak boleh 0. Persamaan akan menjadi fungsi linear.")
else:
    # 1. Karakteristik Dasar
    D = b**2 - 4*a*c
    x_puncak = -b / (2*a)
    y_puncak = -D / (4*a)
    arah = "Atas (Minimum)" if a > 0 else "Bawah (Maksimum)"

    if D > 0:
        x1 = (-b + np.sqrt(D)) / (2*a)
        x2 = (-b - np.sqrt(D)) / (2*a)
        titik_potong_x = f"({x1:.2f}, 0) dan ({x2:.2f}, 0)"
    elif D == 0:
        x1 = -b / (2*a)
        titik_potong_x = f"Menyinggung di ({x1:.2f}, 0)"
    else:
        titik_potong_x = "Imajiner (Tidak memotong sumbu X)"

    st.subheader("Karakteristik Geometri")
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Diskriminan (D)", value=f"{D:.2f}")
        st.write(f"**Arah Grafik:** Terbuka ke {arah}")
        st.write(f"**Sumbu Simetri:** $x = {x_puncak:.2f}$")
        
    with col2:
        st.metric(label="Nilai Optimum (Yp)", value=f"{y_puncak:.2f}")
        st.write(f"**Titik Puncak:** ({x_puncak:.2f}, {y_puncak:.2f})")
        st.write(f"**Potong Sumbu Y:** (0, {c})")
        
    st.info(f"**Potong Sumbu X:** {titik_potong_x}")

    st.divider()

    # 2. Logika Rekursi Newton (Newton's Sums)
    @st.cache_data(max_entries=1000) 
    def nsr(n, a_val, b_val, c_val):
        if n == 0:
            return 2
        if n == 1:
            return -b_val / a_val
        return (-b_val * nsr(n-1, a_val, b_val, c_val) - c_val * nsr(n-2, a_val, b_val, c_val)) / a_val
        
    try:
        S_n = nsr(n_val, a, b, c)
        
        st.subheader("Analisis Akar Tingkat Lanjut (HOTS)")
        st.markdown(f"Mengevaluasi penjumlahan pangkat akar: $\\alpha = X_1^{n_val}$ dan $\\beta = X_2^{n_val}$")
        
        st.success(f"Nilai deret rekursi ($X_1^{n_val} + X_2^{n_val}$) adalah: **{S_n}**")

        # 3. Ekspansi HOTS: Persamaan Kuadrat Baru (PKB)
        # Menghitung hasil kali akar berpangkat n
        P_n = (c/a)**n_val
        
        st.markdown("### Konstruksi Persamaan Kuadrat Baru")
        st.markdown(f"Jika kita ingin membuat persamaan kuadrat baru yang memiliki akar-akar $X_1^{n_val}$ dan $X_2^{n_val}$, kita tidak perlu mencari akar aslinya. Kita menggunakan identitas:")
        st.latex(r"x^2 - (\alpha + \beta)x + (\alpha \cdot \beta) = 0")
        
        st.markdown(f"**1. Jumlah Akar Baru ($\\alpha + \\beta$):** Menggunakan nilai rekursi di atas = `{S_n}`")
        st.markdown(f"**2. Hasil Kali Akar Baru ($\\alpha \cdot \\beta$):** $(X_1 \\cdot X_2)^{n_val} = (c/a)^{n_val} = ({c}/{a})^{n_val} =$ `{P_n}`")
        
        # Format string agar tidak muncul x^2 - -5x menjadi x^2 + 5x
        sign_S = "+" if -S_n >= 0 else "-"
        sign_P = "+" if P_n >= 0 else "-"
        
        st.info("**Persamaan Kuadrat Baru (PKB) yang terbentuk:**")
        st.latex(f"x^2 {sign_S} {abs(S_n):.4f}x {sign_P} {abs(P_n):.4f} = 0")
        
    except Exception as e:
        st.error(f"Terjadi kesalahan pada perhitungan metrik lanjutan: {e}")