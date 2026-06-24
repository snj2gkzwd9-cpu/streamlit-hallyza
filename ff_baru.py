import pandas as pd
import streamlit as st

# ===========================================
# KONFIGURASI MEMORI LOGIN (SESSION STATE)
# ===========================================
# Membuat variabel penyimpan status login agar tidak hilang saat halaman di-refresh
if "status_login" not in st.session_state:
    st.session_state.status_login = False

# ===========================================
# 1. HALAMAN LOGIN (DIALIRKAN JIKA BELUM LOGIN)
# ===========================================
if not st.session_state.status_login:
    st.title("🔥 Garena Free Fire - Weapon Database")
    st.subheader("Silakan Login Terlebih Dahulu")
    st.write("Gunakan akun khusus Survivor untuk mengakses panel kontrol senjata.")
    st.markdown("---")

    # Form Input Login
    username = st.text_input("Username:", placeholder="Masukkan username Anda...")
    password = st.text_input("Password:", type="password", placeholder="Masukkan password Anda...")

    if st.button("Masuk Ke Panel 🔓"):
        # Validasi akun login
        if username == "survivor" and password == "booyah":
            st.session_state.status_login = True
            st.success("Login Berhasil! Membuka data...")
            st.rerun()  # Memuat ulang halaman langsung ke menu utama
        else:
            st.error("Username atau Password Salah! (Hint: survivor / booyah)")

# ===========================================
# 2. HALAMAN UTAMA (DIALIRKAN JIKA SUDAH LOGIN)
# ===========================================
else:
    # Header Utama Aplikasi
    st.title("🔥 Garena Free Fire - Weapon Control Panel")
    st.write("Selamat Datang kembali, **Survivor**! Panel analisis data siap digunakan.")
    st.markdown("---")

    # --- SIDEBAR NAVIGASI ---
    st.sidebar.title("🏰 NAVIGATION")
    menu = st.sidebar.selectbox(
        "PILIH MENU PROGRAM:",
        [
            "1. Conditional (Cek Amunisi)",
            "2. Data & Operasi (Hitung Akurasi)",
            "3. OOP (Buat Senjata Baru)",
            "4. Grafik Perbandingan Damage",
            "5. Tampilkan Pseudocode"
        ]
    )
    
    # Tombol Logout diletakkan di bagian bawah Sidebar
    st.sidebar.markdown("---")
    if st.sidebar.button("Logout / Keluar 🚪", use_container_width=True):
        st.session_state.status_login = False
        st.rerun()

    # ===========================================
    # MENU 1: CONDITIONAL
    # ===========================================
    if menu == "1. Conditional (Cek Amunisi)":
        st.header("🔫 Cek Tipe Amunisi Senjata")
        nama_senjata = st.text_input("Masukkan Nama Senjata FF (Contoh: AK47, MP40, M1014):")

        if st.button("Cek Amunisi Now"):
            senjata = nama_senjata.upper().replace(" ", "")
            
            if senjata in ["AK47", "M4A1", "SCAR", "GROZA"]:
                st.success("Tipe Amunisi: AR Ammo (Peluru Merah)")
            elif senjata in ["MP40", "UMP", "MP5", "THOMPSON"]:
                st.success("Tipe Amunisi: SMG Ammo (Peluru Hijau Muda)")
            elif senjata in ["M1014", "M1887", "MAG7"]:
                st.success("Tipe Amunisi: SG Ammo (Peluru Ungu)")
            elif senjata in ["AWM", "M82B", "KAR98K"]:
                st.success("Tipe Amunisi: Sniper Ammo (Peluru Hijau Tua)")
            else:
                st.warning("Senjata tidak terdaftar. Coba ketik: AK47 atau MP40")

    # ===========================================
    # MENU 2: DATA & OPERASI
    # ===========================================
    elif menu == "2. Data & Operasi (Hitung Akurasi)":
        st.header("🎯 Hitung Rasio Akurasi Tembakan")
        
        hit = st.number_input("Jumlah Peluru Mengenai Target (Hit):", min_value=0, value=0)
        total = st.number_input("Total Peluru yang Ditembakkan:", min_value=0, value=0)

        if st.button("Hitung Rasio"):
            if total == 0:
                rasio = 0.0
            else:
                rasio = hit / total

            akurasi_bagus = rasio >= 0.60
            attachments = ["Silencer", "Muzzle", "Foregrip", "Magazine", "Scope", "Stock"]

            st.metric(label="Rasio Akurasi Anda", value=f"{rasio * 100:.1f} %")
            st.write("Apakah tembakan akurat?", "🎯 Ya, Sangat Akurat!" if akurasi_bagus else "⚠️ Kurang Akurat, Pakai Attachment!")
            st.write("Daftar Item Attachment (Array Data):", attachments)

    # ===========================================
    # MENU 3: OOP (OBJECT ORIENTED PROGRAMMING)
    # ===========================================
    elif menu == "3. OOP (Buat Senjata Baru)":
        st.header("🏗️ OOP: Custom Weapon Builder")

        class SenjataCustom:
            def __init__(self, nama, tipe, dmg):
                self.nama = nama
                self.tipe = tipe
                self.dmg = dmg

            def info(self):
                return f"🛠️ Objek Senjata **{self.nama}** berhasil diciptakan lewat konsep OOP! Tipe: **{self.tipe}** dengan Base Damage: **{self.dmg} HP**."

        nama_custom = st.text_input("Beri Nama Senjata Buatanmu:")
        tipe_custom = st.selectbox("Jenis Senjata:", ["Assault Rifle", "Submachine Gun", "Shotgun", "Sniper Rifle"])
        damage_custom = st.slider("Atur Base Damage:", min_value=10, max_value=200, value=50)

        if st.button("Rakit Senjata (Buat Objek)"):
            if nama_custom:
                senjata_baru = SenjataCustom(nama_custom, tipe_custom, damage_custom)
                st.info(senjata_baru.info())
            else:
                st.error("Nama senjata tidak boleh kosong!")

    # ===========================================
    # MENU 4: GRAFIK DAMAGE (PANDAS NATIVE)
    # ===========================================
    elif menu == "4. Grafik Perbandingan Damage":
        st.header("📊 Grafik Komparasi Status Damage Senjata")
        
        data_ff = {
            "Nama Senjata": ["M1887", "M1014", "AWM", "AK47", "GROZA", "M4A1"],
            "Base Damage": [100, 94, 90, 61, 61, 54]
        }
        
        df = pd.DataFrame(data_ff)
        df = df.set_index("Nama Senjata")
        
        st.subheader("Visualisasi Grafik Batang (Native Chart)")
        st.bar_chart(df)

    # ===========================================
    # MENU 5: PSEUDOCODE
    # ===========================================
    elif menu == "5. Tampilkan Pseudocode":
        st.header("📝 Pseudocode Sistem Senjata Free Fire")
        
        st.code("""
START
INPUT username, password
IF username == "survivor" AND password == "booyah" THEN
    SET status_login = TRUE
    DISPLAY "Menu Utama"
ELSE
    DISPLAY "Login Gagal"
ENDIF
END
        """, language="text")