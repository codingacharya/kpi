import streamlit as st

def export_csv(df, filename):
    st.download_button(
        label="📤 Download CSV",
        data=df.to_csv(index=False),
        file_name=filename,
        mime="text/csv"
    )
