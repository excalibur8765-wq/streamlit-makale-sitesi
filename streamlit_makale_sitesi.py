import streamlit as st
import sqlite3
import pandas as pd

# --- Sayfa ayarları ---
st.set_page_config(page_title="Kişisel Portfolyo", page_icon="👩‍💻", layout="centered")

# --- Veritabanı bağlantısı ---
conn = sqlite3.connect("portfolio.db")
cursor = conn.cursor()

# Yorum tablosu oluştur
cursor.execute("""
CREATE TABLE IF NOT EXISTS comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    comment TEXT
)
""")
conn.commit()

# --- Başlık ve tanıtım ---
st.title("👩‍💻 Merhaba, ben Elif!")
st.write("Ben bir yazılım geliştiricisiyim. Python, Streamlit ve tasarımla ilgileniyorum 🎨")

# --- Profil fotoğrafı ---
st.image("https://randomuser.me/api/portraits/women/44.jpg", caption="Benim Profil Fotoğrafım", width=200)

# --- Hakkımda bölümü ---
st.header("💬 Hakkımda")
st.write("""
Ben Elif. Kod yazmayı, kullanıcı arayüzü tasarlamayı ve yeni teknolojileri öğrenmeyi seviyorum.  
Bu sayfa benim mini portfolyom. Burada projelerimi ve kendimi tanıtıyorum 🌟
""")

# --- Video tanıtımı ---
st.header("🎥 Tanıtım Videom")
st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

# --- Projeler bölümü ---
st.header("💼 Projelerim")

st.subheader("📱 Python Kodlama Projesi")
st.image("https://cdn.pixabay.com/photo/2016/03/31/20/58/code-1295356_1280.png", caption="Kodlama Projem")

st.subheader("🌐 Streamlit Web Uygulaması")
st.image("https://cdn.pixabay.com/photo/2015/01/08/18/26/typing-593333_1280.jpg", caption="Streamlit ile Web Uygulaması")

# --- Sosyal medya bağlantıları ---
st.header("🔗 Sosyal Medya")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("[💼 LinkedIn](https://linkedin.com)")
with col2:
    st.markdown("[🐙 GitHub](https://github.com)")
with col3:
    st.markdown("[📸 Instagram](https://instagram.com)")

# --- YORUM EKLEME BÖLÜMÜ ---
st.header("💬 Yorum Bırak")

with st.form("yorum_formu", clear_on_submit=True):
    name = st.text_input("Adınız")
    comment = st.text_area("Yorumunuz")
    submitted = st.form_submit_button("Gönder")

    if submitted:
        if name and comment:
            cursor.execute("INSERT INTO comments (name, comment) VALUES (?, ?)", (name, comment))
            conn.commit()
            st.success("✅ Yorumunuz kaydedildi, teşekkürler!")
        else:
            st.warning("⚠️ Lütfen adınızı ve yorumunuzu girin!")

# --- YORUMLARI GÖSTER ---
st.subheader("🗣️ Yapılan Yorumlar")

df = pd.read_sql("SELECT * FROM comments ORDER BY id DESC", conn)

if not df.empty:
    for _, row in df.iterrows():
        st.markdown(f"**👤 {row['name']}**: {row['comment']}")
        st.write("---")
else:
    st.info("Henüz yorum yapılmamış. İlk yorumu sen yap! ✍️")