elif page.startswith("4"):
    st.title("🏷️ Restaurant by Cluster")

    if 'cluster' in df.columns:
        cluster_num = st.selectbox("Pilih cluster:", sorted(df['cluster'].unique()))
        st.write(df[df['cluster'] == cluster_num])
    else:
        st.warning("Silakan lakukan clustering terlebih dahulu di halaman 'Clustering'.")
