import streamlit as st
import sqlite3
import pandas as pd

st.title("Astronomia'ya hoş geldin ")
st.image("https://cdn.mos.cms.futurecdn.net/NtQuZn2zgLZwp4XW57QqnU-1280-80.jpg")
st.write("merhaba.Astronomia'ya hoş geldiniz!burada astronomi,uzay ve astrofizik hakkında konuşabiliriz.gelecekte güncelleme getireceğim.her hafta farklı bir yazı gelecek.")
st.image("https://i.pinimg.com/originals/8a/f2/ab/8af2abc7bdf87223f87a5f8a5bee47e6.jpg")
st.image("https://www.nasa.gov/wp-content/uploads/2019/09/stsci-h-p1943a-f-2076x1484-2.png")
st.title("teleskoplar&gözlemler.")
st.write("teleskopların çeşitleri vardır.aynalı(newton reflektör),mercekli(gslileo galilei nin teleskobu),hem aynlaı hem mercekli(mutant).")
st.title("aynalı teleskoplar")
st.image("https://imvm.letgo.com/v1/files/50d25603cba04-OLXAUTOTR/image;s=1080x1080")
st.write("aynalı teleskoplar karmaşık bir yapıya sahiptir.aynadan aynaya ışık sekmesi sonucu yoğun bir ışık merceğe yansır.daha basit şekilde ışık teleskobun içindeki aynaya gider.")
st.write("bu ayna eğiktir ve ışığı tek bir noktaya toplar ve detayları belli eder.eğik aynadan yansıyan ışık ikicil aynaya yansır,ve oradangöz merceğine gider")
st.image("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhmarhTMqD4XWjMctPDeYCOlq8TsHLCLX8wH_dq-3q3aN4DLV17KvcVEeNpit3CS9J5CE_nSTzjeFqWosl99MtBzaMwSXqlgo-GCF6WBBVp648kYhI1JH_3oXlSdOTp1lysrli7djARlLaq8gcxd55Zu1VSUH3ma_Kvwpkv81bD6BEdKWqrKBNIgr3Dfg/s841/teleskop%20%C3%A7ukur%20ayna.jpg")
st.write("ve bu görüntüyü merceklerle yakınlaştırırız.merceğin cam boyutu ne kadar küçülürse görüntü okadar büyür.ama bir dez avantajı var.")
st.write("görüntü büyüdükçe detay kaybeder.ve burada çare cüzdanda.ne kadar geniş aynalı bir teleskop alırsanız görüntü o kadar netleşir(dobsonian öneririm)")
st.title("mercekli")
st.write("mercekli teleskoplar ışığı kırarlar ve onu merceğe yansıtırlar.burada merceklerin uzaklığı yakınlaştırmada önemli rol oynar")
st.image("https://www.harrisontelescopes.co.uk/acatalog/9621801f.jpg")
st.image("http://astroteknik.com/wp-content/uploads/2021/05/path-rays-refractor.png")

st.title("Yorum Kutusu")

# Session state ile yorumları saklayalım
if "comments" not in st.session_state:
    st.session_state.comments = []

# Yorum ekleme formu
with st.form("comment_form"):
    name = st.text_input("İsim", value="Anonim")
    content = st.text_area("Yorum", "")
    submitted = st.form_submit_button("Gönder")
    if submitted and content.strip():
        st.session_state.comments.insert(0, {"name": name.strip() or "Anonim", "content": content.strip()})
        st.success("Yorum eklendi!")

st.markdown("### Gönderilmiş Yorumlar")

if st.session_state.comments:
    # Yorumları listelerken silme butonu
    for idx, comment in enumerate(st.session_state.comments):
        st.markdown(f"**{comment['name']}**: {comment['content']}")
        delete = st.button(f"Sil {idx}", key=f"del_{idx}")
        if delete:
            st.session_state.comments.pop(idx)
            st.experimental_rerun()  # Sayfayı yeniden yükle
else:
    st.write("Henüz yorum yok.")
