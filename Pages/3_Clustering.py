elif page.startswith("3"):
    st.title("🔍 Clustering Restoran")

    features = ['rating', 'average_price']
    X = df[features].dropna()
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    k = st.slider("Pilih jumlah cluster:", 2, 10, 3)
    model = KMeans(n_clusters=k, random_state=42)
    df['cluster'] = model.fit_predict(X_scaled)

    st.write("Hasil clustering ditampilkan dalam grafik berikut:")
    fig3, ax3 = plt.subplots()
    sns.scatterplot(data=df, x='rating', y='average_price', hue='cluster', palette='viridis', ax=ax3)
    st.pyplot(fig3)
