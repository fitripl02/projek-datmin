elif page.startswith("2"):
    st.title("📈 Data Visualization")

    st.subheader("Distribusi Rating")
    fig, ax = plt.subplots()
    sns.histplot(df['rating'], bins=20, kde=True, ax=ax)
    st.pyplot(fig)

    st.subheader("Harga vs Rating")
    fig2, ax2 = plt.subplots()
    sns.scatterplot(data=df, x='average_price', y='rating', hue='category', ax=ax2)
    st.pyplot(fig2)
