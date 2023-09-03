import streamlit as st
import pandas as pd
import altair as alt

st.header("Wie sieht für Sie eine perfekte Beziehung aus?")
st.subheader("18-24 Jahre")

source = pd.DataFrame({
        'Anteil (%)': [28, 41, 2, 11, 7, 11],
        'Wie sieht es aus?': ['Zusammen wohnen', 'Verheiratet mit Kindern', 'Getrennt wohnen', 'Verheiratet', 'Doppeltes Einkommen, keine Kinder', 'Gemeinsames Wohneigentum besitzen']
})
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil (%):Q',
        x='Wie sieht es aus?:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    Juli 2019
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle: Statista")