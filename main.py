import streamlit as st
import pandas as pd
from modules.cyk import is_accepted, get_table_element


def display_results(text_accepted, text, data):
    if text_accepted:
        st.success("Kalimat diterima:")
        
    else:
        st.error("Kalimat tidak diterima.")
    st.write(text)

    if data is not None:
        st.write("Tabel Parsing:")
        st.table(data)


def main():
    st.title("Parsing Kalimat Bahasa Bali")
    st.divider()

    st.subheader("Kelompok A3")
    st.caption(
        "I Gede Parama Sathiyam Yuda Yana (2308561013), Adriel Malvin Manurung (2308561067), Ida Bagus Gede Widiastana Bawaskara (2308561097), Jeremy Vidinov Binsar (2308561123), Putu Dena Satwika Sandi (2308561115)"
    )
    st.caption("")
    st.divider()

    input_text = st.text_input("Input kalimat Frasa Nominal")
    text = input_text.lower().split(" ")

    text_accepted = is_accepted(text)
    result = get_table_element(input_text)

    data = pd.DataFrame(result)
    data = data.style.highlight_null(props="color: transparent;")

    if st.button("Periksa") and text:
        display_results(text_accepted, text, data)
    elif not text:
        st.warning("Masukkan kalimat untuk diperiksa.")


if __name__ == "__main__":
    main()
