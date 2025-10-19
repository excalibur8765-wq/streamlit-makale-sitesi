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


st.title("Teleskoplar ve filtreler")
st.write("Merhaba,bu gün konumuz teleskoplar,erçek yüzleri ve faydaları.Başlamadan önce tekrar duyuruyu yapalım,sitemiz Excannox'a her güncelleme cuma-cumartesi arası gelir")
st.title("hubble telescope")
st.image("https://share.google/images/DBzq9qrUgy1gDlFZt")
st.write("kartal bulutsusu gerçektende yıldızları doğumunda büyük rol oynar.kendisi hubble uzay teleskobundan bildiğimiz üzere etkileyici bir nebula.")
st.write("ama tabikide bu görüntüler sanıldığı gibi değil.çünkü bu görüntüler stacking,birdiğer adıyla üst üste oturtma yöntemiyle üretilmiştir")
st.write("konuyu biraz daha açarsak anltayım.öncelikle üst üste oturtmanın yöntemini anlatayım.bu yöntem teleskobun saatlerce hattağa bazen günlerce bir noktaya odaklanması.")
st.write("ve bu en iyi görüntüleri üst üste ekleriz.ama hala yeterli olmayacak.hubble ve james webb gibi teleskopların görüntüleri etkileyici")
st.write("orjinal halleri de güzel ama herzaman ekstra ile görüntüleri pohpohluyorlar")
st.title("bir ham görüntü")
st.image("https://share.google/images/H0dKUcBN1y7oSoXxg")
st.write("gömüş olduğunuz üzere o resimler gibi kaliteli değil,ama bir şey eksik,Hmm.")
st.write("tabikide renklendirme,ama bu doğal.biz bulutsulara bakarken normalde hiçbirşey görmeyiz,ama filtre takarsak görüntü iyileşir.")
st.title("gaz filtreleri")
st.write("gaz filtreleri bir camdır,işleyişii basittir.lensi göz merceğine takın ve bakın👌")
st.write("bu filtrelerin çeşitleri vardır,nebulanın hammaddesine göre değişir")
st.image("https://i.ebayimg.com/images/g/DBkAAOSwNldjrXMy/s-l960.jpg")
st.write("bu filtreler Hidrojen,ioksijen vb.materyaller den oluşur.ama hala yeterli değil.O zaman bütün filtreleri kullanalım ve üst üste oturtalım.")
st.write("Ama şimdi nasa gibi devlerin Rating toplaması gerek,o yüzden kalite gerekli.Bir tutam montaj yeterli olur.Açıklaması rahat olması için montajlı ve montajsız hali.")
st.title("montajsız")
st.image("https://getwallpapers.com/wallpaper/full/3/b/7/716611-popular-eagle-nebula-wallpaper-2500x1826-for-iphone-5.jpg")
st.title("montajlı")
st.image("https://telescope.live/sites/default/files/styles/photo_main/public/2023-01/20230121-M16-SHO.jpg?itok=CWMvMXxW")
st.write("Aradadaki farkı çakmış olmalısınız,canlılık,renk tonları ve belirginlik farkı belli.")
st.image("https://share.google/images/BUFVTI7wwuis5WfuG")
st.write("Bugün de NASA'nın foyasını ortaya çıkarttık.nede olsa insan kandırmak bedava.değilmi arkadaşlar.cumartesiyi bekleyin!")
st.image("https://avatars.mds.yandex.net/get-yapic/57243/dEsincgQ9vVoRDWdftLUr3t65g-1/orig")


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
