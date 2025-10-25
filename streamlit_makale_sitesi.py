import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(
    page_title="Excannox – Gerçek Zamanlı Yorum Platformu", 
    page_icon="🪐"
)
st.markdown("""
<meta name="description" content="Excannox: Astropia paylaşımı için gerçek zamanlı yorum platformu.">
""", unsafe_allow_html=True)



st.markdown("""
<head>
  <title>excannox – Uzay, Evren ve Bilim Üzerine Makaleler</title>
  <meta name="description" content="Astronomia, evrenin sırlarını keşfetmek isteyenler için hazırlanmış bir dijital dergidir. Galaksiler, kara delikler, gezegenler ve kozmik olaylar hakkında güncel makaleler ve ilgi çekici bilgiler burada.">
  <meta name="keywords" content="excannox, uzay, evren, galaksi, kara delik, gezegen, astronomi, bilim, uzay araştırmaları, kozmoloji">
</head>
""", unsafe_allow_html=True)

st.title("🌌 Excannox")
st.write("Evrenin büyüleyici sırlarını keşfedin. Bilimle, merakla, yıldız tozuyla dolu makaleler sizi bekliyor.")

st.title("merhabalar arkadaşlar,bu haftanın konusu karadelikler")
st.write("uzun süredir sizde aynı eskiden benimde düşündüğüm gibi kara deliklerin anlamsızca herşeyi içine çektiğini düşünüyordunuz.")
st.write("Ama kara delikler öyle cisimler değiller,daha doğrusu cisim değiller")
st.image("https://share.google/images/xL9VhBP28BesOVcE2")
st.write("Bu cisimler delik değil bir uzay zaman çöküntüsüdür.nasıl işlediğini kısaca anlatıyım.")
st.write("Şimdi herkezin tanıdığı Einsthen'i siz de tanıyorsunuz,alman bilimadamı.onun genel görelilik kuralına göre her cisim her kütle uzay zamanı büker.")
st.write("uzayı bir örtü gibi düşünün,örtüyü 4 köşesinden gergin şekilde asın.örtünün üstüne bir ağır küre koyun.örtü bir miktar bükülecektir.")
st.write("peki miktarına görehafif bir küre koysaydınız,yine bükülürdü değilmi.ama o kütleyi bir bilyeye sığdırırsanız örtü yani uzay zaman tek noktadan gelen ağırlık sonucu")
st.write("yırtılır.yanibir uçakta giderken kapı açılırsa herşey dışarıya uçuşur.aynı onun gibi")
st.image("https://share.google/images/GWOR0hiNUDJeqnWdr")
st.write("görmüş olduğunuz üzere.peki kara delikler çok fazla besintoplarsa sizce ne olur.Tamam tamam bu gerçekten basitti.Belkide değildi.")
st.write("etrafındaki diske sıkıştırıp hapsedeler.ve çok fazla besin birikirse yoğun maddeden yıldızlar bile oluşabilir.yani bir galaksi kimvurduya doğar.")
st.write("Ne yazıkki resim bulamadım.o zaman bu haftalık bu kadar.Görüşürüz millet!.")

st.title("yorumlarda gerçek isimler yazın,sinirim bozuluyar arkadaşlar.mr.shawarma ne biçim isim yahu!?!")

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

st.write("siteyi beğendiysen bize destek olmak için yakında gelecek ibandan destekte buluna bilirsiniz!")
import streamlit as st

st.markdown("""
<div style="margin: 20px auto; width: 320px;">
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
  <ins class="adsbygoogle"
       style="display:block"
       data-ad-client="ca-app-pub-1636457491867924~9809142682"
       data-ad-slot="ca-app-pub-1636457491867924/9282916116"
       data-ad-format="auto"
       data-full-width-responsive="true"></ins>
  <script>
       (adsbygoogle = window.adsbygoogle || []).push({});
  </script>
</div>
""", unsafe_allow_html=True)
import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import os
st.title("resim yazılıları")

uploaded = st.file_uploader("bir resim yükle", type=["jpg", "png", "jpeg"])
text = st.text_input("yazılacak yazı")

size = st.slider("yazı boyutu", 10, 100, 50)
color = st.color_picker("yazı rengi", "#FF0000")

font_options = [
    "arial.ttf",
    "times.ttf",
    "calibri",
    "comic.ttf",
    "verdana.ttf"
]
selected_font = st.selectbox("yazı tipi seçin", font_options)

x = st.slider("X pozisyonu", 0, 800, 20)
y = st.slider("y pozisyonu", 0, 800, 20 )
if uploaded:
    image = Image.open(uploaded)
    draw = ImageDraw.Draw(image)


    try:
        font  = ImageFont.truetype(selected_font, size)
    except:
        font = ImageFont.load_default()

    draw.text((x, y), text, fill=color, font=font)
    st.image(image, caption="VELUDUDENDENDELEDİDAPDABİDAPDAPDABEDİ", use_column_width=True)

    image.save("sonuc.png")
    with open("sonuc.png", "rb") as file:
        st.download_button("kaydet", file, "sonuç.png")
