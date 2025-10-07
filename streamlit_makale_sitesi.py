import streamlit as st
import sqlite3
from datetime import datetime
import os
from pathlib import Path
import base64

# ------- Ayarlar -------
DB_PATH = "articles.db"
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)
ADMIN_PASSWORD = "admin123"  # Deploy ederken değiştir

# ------- Veritabanı -------
def get_conn():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_conn()
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT,
            content TEXT NOT NULL,
            tags TEXT,
            image TEXT,
            created_at TEXT NOT NULL,
            updated_at TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

# ------- CRUD İşlemleri -------
def add_article(title, author, content, tags=None, image_path=None):
    conn = get_conn()
    c = conn.cursor()
    now = datetime.utcnow().isoformat()
    c.execute(
        "INSERT INTO articles (title, author, content, tags, image, created_at) VALUES (?,?,?,?,?,?)",
        (title, author, content, tags, image_path, now),
    )
    conn.commit()
    conn.close()

def update_article(article_id, title, author, content, tags=None, image_path=None):
    conn = get_conn()
    c = conn.cursor()
    now = datetime.utcnow().isoformat()
    c.execute(
        "UPDATE articles SET title=?, author=?, content=?, tags=?, image=?, updated_at=? WHERE id=?",
        (title, author, content, tags, image_path, now, article_id),
    )
    conn.commit()
    conn.close()

def delete_article(article_id):
    conn = get_conn()
    c = conn.cursor()
    c.execute("DELETE FROM articles WHERE id=?", (article_id,))
    conn.commit()
    conn.close()

def get_article(article_id):
    conn = get_conn()
    c = conn.cursor()
    c.execute("SELECT * FROM articles WHERE id=?", (article_id,))
    row = c.fetchone()
    conn.close()
    return row

def list_articles(search=None, tag=None, sort_desc=True):
    conn = get_conn()
    c = conn.cursor()
    query = "SELECT * FROM articles"
    params = []
    conditions = []
    if search:
        conditions.append("(title LIKE ? OR content LIKE ? OR author LIKE ?)")
        s = f"%{search}%"
        params.extend([s, s, s])
    if tag:
        conditions.append("tags LIKE ?")
        params.append(f"%{tag}%")
    if conditions:
        query += " WHERE " + " AND ".join(conditions)
    query += " ORDER BY created_at " + ("DESC" if sort_desc else "ASC")
    c.execute(query, params)
    rows = c.fetchall()
    conn.close()
    return rows

# ------- Yardımcılar -------
def save_uploaded_file(uploaded_file):
    if uploaded_file is None:
        return None
    ext = Path(uploaded_file.name).suffix
    timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S%f")
    filename = f"{timestamp}{ext}"
    path = UPLOAD_DIR / filename
    with open(path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return str(path)

# ------- Streamlit UI -------
st.set_page_config(page_title="Streamlit Makale Sitesi", layout="wide")

st.title("📚 Basit Streamlit Makale Sitesi")

menu = st.sidebar.selectbox("Menü", ["Ana Sayfa", "Yeni Makale", "Yönetim"])

# ---------------- Ana Sayfa ----------------
if menu == "Ana Sayfa":
    st.header("Güncel Yazılar")
    col1, col2 = st.columns([3,1])
    with col2:
        search = st.text_input("Ara")
        tag_filter = st.text_input("Etiket ile filtrele")
        sort_desc = st.checkbox("Yeni önce", value=True)

    with col1:
        articles = list_articles(search=search)
        if tag_filter:
            tag = tag_filter.strip()
            articles = [a for a in articles if (a['tags'] and tag in a['tags'])]
        if not articles:
            st.info("Henüz hiç makale yok. 'Yeni Makale' sekmesinden ekleyebilirsin.")
        else:
            for a in articles:
                st.subheader(a['title'])
                meta = f"Yazar: {a['author'] or 'Bilinmiyor'} — {a['created_at'][:16].replace('T',' ')}"
                if a['tags']:
                    meta += f" — Etiketler: {a['tags']}"
                st.caption(meta)
                if a['image']:
                    st.image(a['image'], use_column_width=True)
                preview = a['content'][:300]
                st.markdown(preview + ("..." if len(a['content'])>300 else ""), unsafe_allow_html=True)

# ---------------- Yeni Makale ----------------
elif menu == "Yeni Makale":
    st.header("Yeni Makale Ekle")
    with st.form("new_article"):
        title = st.text_input("Başlık")
        author = st.text_input("Yazar")
        tags = st.text_input("Etiketler (virgülle ayrılmış)")
        uploaded_image = st.file_uploader("Kapak resmi (isteğe bağlı)")
        content = st.text_area("İçerik (Markdown destekli)", height=300)
        submit_btn = st.form_submit_button("Yayınla")

    if submit_btn:
        if not title or not content:
            st.error("Başlık ve içerik zorunludur.")
        else:
            img_path = save_uploaded_file(uploaded_image)
            add_article(title, author, content, tags, img_path)
            st.success("Makale başarıyla eklendi!")

# ---------------- Yönetim ----------------
elif menu == "Yönetim":
    st.header("Yönetim Paneli")
    pwd = st.text_input("Admin şifresi", type="password")
    if pwd != ADMIN_PASSWORD:
        st.warning("Yönetici şifresini girin.")
        st.stop()

    st.success("Yönetici girişi başarılı ✅")
    articles = list_articles()
    if not articles:
        st.info("Hiç makale yok.")
    else:
        for a in articles:
            with st.expander(f"{a['title']} (Yazar: {a['author']})"):
                st.markdown(a['content'])
                col1, col2 = st.columns(2)
                if col1.button("Sil", key=f"del-{a['id']}"):
                    delete_article(a['id'])
                    st.experimental_rerun()
                if col2.button("Düzenle", key=f"edit-{a['id']}"):
                    st.session_state["edit_id"] = a["id"]

    if "edit_id" in st.session_state:
        art = get_article(st.session_state["edit_id"])
        st.subheader(f"Düzenle: {art['title']}")
        with st.form("edit_article"):
            title = st.text_input("Başlık", value=art["title"])
            author = st.text_input("Yazar", value=art["author"])
            tags = st.text_input("Etiketler", value=art["tags"])
            content = st.text_area("İçerik", value=art["content"], height=300)
            uploaded_image = st.file_uploader("Yeni kapak resmi (isteğe bağlı)")
            save_btn = st.form_submit_button("Kaydet")
        if save_btn:
            img_path = art["image"]
            new_img = save_uploaded_file(uploaded_image)
            if new_img:
                img_path = new_img
            update_article(art["id"], title, author, content, tags, img_path)
            st.success("Makale güncellendi.")
            del st.session_state["edit_id"]
            st.experimental_rerun()

st.markdown("---")
st.caption("📝 Streamlit ile yapılmış basit bir makale yönetim sistemi. Örnek amaçlıdır.")
