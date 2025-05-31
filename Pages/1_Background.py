if page.startswith("1"):
    st.title("📚 Background")
    st.write("""
    Dashboard ini dibuat untuk menganalisis restoran di Semarang berdasarkan berbagai fitur seperti rating, harga, dan lokasi. 
    Dengan menggunakan visualisasi data dan teknik clustering, kita dapat melihat pola dan rekomendasi yang muncul dari dataset restoran tersebut.
    """)
    st.dataframe(df.head())
