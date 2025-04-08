import streamlit as st
from duckduckgo_search import DDGS

st.set_page_config(page_title="量子特許AI", layout="wide")
st.title("🔍 量子コンピュータ特化型・先行特許調査AI")

st.markdown("発明の概要を入力してください。Google Patents から類似特許を探します。")

query = st.text_area("📘 発明の概要を入力", height=200, placeholder="例：量子演算結果に対して、AIでデコヒーレンス補正を行い、冷却不要の量子コンピューターを構成...")

if st.button("🔍 調査開始"):
    with st.spinner("Google Patentsから類似特許を検索中..."):
        with DDGS() as ddgs:
            results = list(ddgs.text(f"{query} site:patents.google.com", max_results=5))

    for idx, r in enumerate(results):
        st.subheader(f"🧾 類似特許 {idx+1}")
        st.markdown(f"🔗 [タイトル]({r['href']}): {r['title']}")
        st.markdown(f"📌 概要: {r['body']}")
