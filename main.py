import streamlit as st
from streamlit_navigation_bar import st_navbar

def mean(data):
    return sum(data) / len(data)

def median(data):
    if len(data) % 2 == 0:
        return (data[len(data) // 2-1] + data[(len(data) // 2)]) / 2
    else:
        return data[len(data) // 2]

def modus(data):
    if not data:
        print("ADSADsa")
    
    banyak = {}

    for item in data:
        if item in banyak:
            banyak[item] += 1
        else:
            banyak[item] = 1
    
    max_banyak = max(banyak.values())

    moduss = [key for key, value in banyak.items() if value == max_banyak]

    if len(moduss) == 1:
        return moduss[0]
    else:
        return moduss
    
def kuartil(data):
    if len(data) % 2 == 0:
        kuartil_1 = 1/4 * len(data)
        q1 = (data[int(kuartil_1-1)] + data[int(kuartil_1)]) / 2
        q2 = median(data)
        kuartil_3 = 3/4 * len(data)
        q3 = (data[int(kuartil_3-1)] + data[int(kuartil_3)]) / 2
        rentang_quartil = q3 - q1
    else:
        kuartil_1 = 1/4 * (len(data) + 1) - 0.5
        q1 = (data[int(kuartil_1-1)] + data[int(kuartil_1)]) / 2
        q2 = median(data)
        kuartil_3 = 3/4 * (len(data) + 1) - 0.5
        q3 = (data[int(kuartil_3-1)] + data[int(kuartil_3)]) / 2
        rentang_quartil = q3 - q1

    simpangan_quartil = rentang_quartil / 2

    return [q1, q2, q3, rentang_quartil, simpangan_quartil]

def kuartil_1(data):
    if len(data) % 2 == 0:
        return data[1/4 * len(data) + 1/2]
    else:
        return data[1/4 * (len(data) + 1)]

def kuartil_2(data):
    if len(data) % 2 == 0:
        return data[2/4 * len(data) + 1/2]
    else:
        return data[2/4 * (len(data) + 1)]

def kuartil_3(data):
    if len(data) % 2 == 0:
        return data[3/4 * len(data) + 1/2]
    else:
        return data[3/4 * (len(data) + 1)]

def jangkauan(data):
    return max(data) - min(data)

def main():
    st.set_page_config("St4ts")
    page = st_navbar(["Home","About", "Mean", "Median", "Modus", "Range", "Kuartil"])

    match page:
        case "Home":
            st.markdown("<h1>St<span style='color: #ffc107;'>4</span>ts</h1>", unsafe_allow_html=True)
            st.markdown("""
                <p>Selamat datang di St<span style='color: #ffc107;'>4</span>ts, alat yang andal dan mudah digunakan untuk menganalisis data statistik dasar Anda. 
                Aplikasi ini dirancang untuk membantu Anda menghitung Mean, Median, Modus, Range, dan Kuartil secara cepat dan akurat.</p>
                <p>Dengan St<span style='color: #ffc107;'>4</span>ts, Anda dapat:</p>
                <ul>
                    <li>Menghitung nilai rata-rata (Mean) untuk memahami tren umum dalam data Anda.</li>
                    <li>Menentukan nilai tengah (Median) untuk mendapatkan wawasan tentang distribusi data.</li>
                    <li>Mengidentifikasi nilai yang paling sering muncul (Modus) dalam dataset Anda.</li>
                    <li>Menghitung rentang (Range) untuk melihat variasi dalam data Anda.</li>
                    <li>Menganalisis kuartil untuk memahami penyebaran dan distribusi data dengan lebih mendalam.</li>
                </ul>
                <p>Mulailah dengan memilih salah satu menu di atas dan masukkan data Anda untuk mendapatkan hasil statistik yang akurat.</p>
            """, unsafe_allow_html=True)

        case "About":
            st.markdown("<h1>About</h1>", unsafe_allow_html=True)
            st.markdown("<p>Selamat Datang di aplikasi St4ts. Aplikasi ini dirancang untuk membantu anda menghitung Mean, Median, Modus, Dan Kuartil dengan mudah. Cocok untuk pelajar, profesional, atau siapa saja yang ingin menganalisis data.</p>", unsafe_allow_html=True)
            st.markdown("""
                <p>St<span style='color: #ffc107;'>4</span>ts adalah aplikasi yang dikembangkan untuk memudahkan proses analisis statistik dasar. 
                Dengan antarmuka yang sederhana dan fungsionalitas yang kuat, St<span style='color: #ffc107;'>4</span>ts cocok untuk pelajar, profesional, 
                atau siapa saja yang ingin menganalisis data secara cepat dan efisien.</p>
                <p>Fitur-fitur utama St<span style='color: #ffc107;'>4</span>ts:</p>
                <ul>
                    <li><strong>Mean:</strong> Menghitung nilai rata-rata dari data yang Anda masukkan.</li>
                    <li><strong>Median:</strong> Menentukan nilai tengah dari dataset.</li>
                    <li><strong>Modus:</strong> Mengidentifikasi nilai yang paling sering muncul dalam data.</li>
                    <li><strong>Range:</strong> Menghitung rentang antara nilai tertinggi dan terendah dalam dataset.</li>
                    <li><strong>Kuartil:</strong> Menganalisis kuartil untuk mendapatkan wawasan tentang distribusi data.</li>
                </ul>
                <p>St4ts dirancang dengan fokus pada kemudahan penggunaan dan keakuratan hasil, menjadikannya alat yang ideal 
                untuk analisis statistik sehari-hari. Kami berharap aplikasi ini dapat membantu Anda dalam mengelola dan 
                memahami data Anda dengan lebih baik.</p>
            """, unsafe_allow_html=True)

        case "Mean":
            st.markdown("<h1>Mean (Rata-Rata)</h1>", unsafe_allow_html=True)
            data = st.text_input("Masukan data (pisahkan dengan spasi) : ").split()
            data = sorted([int(x) for x in data])
            if st.button("Hitung"):
                hasil = mean(data)
                st.success(f"Nilai rata-rata nya adalah = {hasil}")

        case "Median":
            st.markdown("<h1>Median (Nilai Tengah)</h1>", unsafe_allow_html=True)
            data = st.text_input("Masukan data (pisahkan dengan spasi) : ").split()
            data = sorted([int(x) for x in data])
            if st.button("Hitung"):
                hasil = median(data)
                st.success(f"Nilai tengah nya adalah = {hasil}")

        case "Modus":
            st.markdown("<h1>Modus (Nilai yang sering muncul)</h1>", unsafe_allow_html=True)
            data = st.text_input("Masukan data (pisahkan dengan spasi) : ").split()
            data = [int(x) for x in data]
            if st.button("Hitung"):
                hasil = modus(data)
                st.success(hasil)
                st.success(f"Nilai yang paling sering muncul adalah = {hasil}")

        case "Range":
            st.markdown("<h1>Range (Jangkauan)</h1>", unsafe_allow_html=True)
            data = st.text_input("Masukan Data (pisahkan dengan spasi) : ").split()
            data = [int(x) for x in data]
            if st.button("Hitung"):
                hasil = jangkauan(data)
                st.success(f"Range nya adalah {hasil}")

        case "Kuartil":
            st.markdown("<h1>Kuartil</h1>", unsafe_allow_html=True)
            pilih = st.selectbox("Pilih : ", ("Kuartil 1", "Kuartil 2", "Kuartil 3", "Jangkauan Semi Interkuartil", "Jangkauan Interkuartil"))

            match pilih:
                case "Kuartil 1":
                    st.markdown("<h1>Kuartil 1 (Bawah)</h1>", unsafe_allow_html=True)
                    data = st.text_input("Masukan data (pisahkan dengan spasi) : ").split()
                    data = sorted([int(x) for x in data])

                    if st.button("Hitung"):
                        hasil = kuartil(data)
                        st.success(f"Kuartil 1 nya adalah = {hasil[0]}")

                case "Kuartil 2":
                    st.markdown("<h1>Kuartil 2 (Median)</h1>", unsafe_allow_html=True)
                    data = st.text_input("Masukan data (pisahkan dengan spasi) : ").split()
                    data = sorted([int(x) for x in data])

                    if st.button("Hitung"):
                        hasil = kuartil(data)
                        st.success(f"Kuartil 2 nya adalah = {hasil[1]}")

                case "Kuartil 3":
                    st.markdown("<h1>Kuartil 3 (Atas)</h1>", unsafe_allow_html=True)
                    data = st.text_input("Masukan data (pisahkan dengan spasi) : ").split()
                    data = sorted([int(x) for x in data])

                    if st.button("Hitung"):
                        hasil = kuartil(data)
                        st.success(f"Kuartil 3 nya adalah = {hasil[2]}")

                case "Jangkauan Semi Interkuartil":
                    st.markdown("<h1>Jangkauan Semi Interkuartil (Simpangan Kuartil)</h1>", unsafe_allow_html=True)
                    data = st.text_input("Masukan data").split()
                    data = sorted([int(x) for x in data])

                    if st.button("Hitung"):
                        hasil = kuartil(data)
                        st.success(f"Simpangan kuartil nya adalah = {hasil[4]}")

                case "Jangkauan Interkuartil":
                    st.markdown("<h1>Jangkauan Interkuartil (Hamparan Kuartil)</h1>", unsafe_allow_html=True)
                    data = st.text_input("Masukan data (pisahkan dengan spasi) : ").split()
                    data = sorted([int(x) for x in data])

                    if st.button("Hitung"):
                        hasil = kuartil(data)
                        st.success(f"Jangkauan interkuartil nya adalah = {hasil[3]}")

if __name__ == "__main__":
    main()
