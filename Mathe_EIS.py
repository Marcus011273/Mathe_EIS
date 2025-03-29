import streamlit as st
import matplotlib.pyplot as plt

# Titel der App
st.title('Das EIS-Prinzip')

# Erklärung des EIS-Prinzips mit Mittelschulbezug
st.markdown('''
### EIS-Prinzip (enaktiv – ikonisch – symbolisch)

In dieser App erfahren Sie, wie Sie Brüche Ihren Schülerinnen und Schülern an der Mittelschule mithilfe des EIS-Prinzips schrittweise verständlich machen können:

- **Enaktiv**: Praktische Handlung (z.B. Pizza oder Schokolade teilen)
- **Ikonisch**: Visuelle Darstellungen (Kreisdiagramm, Rechteckmodell)
- **Symbolisch**: Mathematische Schreibweise (z.B. 1/2, 3/4)
''')

# Enaktive Ebene
st.header('1. Enaktive Ebene – praktische Handlung')
zaehler = st.slider('Wählen Sie den Zähler:', 1, 10, 1)
nenner = st.slider('Wählen Sie den Nenner:', 1, 10, 2)

if nenner == 0:
    st.error('Der Nenner darf nicht 0 sein!')
elif zaehler > nenner:
    st.warning('Achtung: Unechter Bruch! Dieser kann als gemischte Zahl dargestellt werden.')

st.markdown('''
**Unterrichtsidee:** Schülerinnen und Schüler teilen Schokolade oder Pizza (ggf. aus Papier oder Karton) in gleich große Stücke und entnehmen entsprechend dem gewählten Bruch.
''')

# Ikonische Ebene
st.header('2. Ikonische Ebene – visuelle Darstellung')
st.markdown('Visualisierung des gewählten Bruchs mithilfe eines Kreisdiagramms:')

fig, ax = plt.subplots()
if zaehler <= nenner:
    ax.pie([zaehler, nenner - zaehler], labels=['gewählter Anteil', 'restlicher Anteil'], 
           colors=['skyblue', 'lightgrey'], autopct='%1.1f%%', startangle=90)
else:
    ganze, rest = divmod(zaehler, nenner)
    st.write(f"Dies sind {ganze} ganze und {rest}/{nenner} Teile.")
    ax.pie([rest, nenner - rest], labels=['Restlicher Anteil', ''], 
           colors=['skyblue', 'lightgrey'], autopct='%1.1f%%', startangle=90)

ax.axis('equal')
st.pyplot(fig)

st.markdown('''
**Unterrichtsidee:** Schülerinnen und Schüler zeichnen Kreis- oder Rechteckmodelle zu Bruchteilen passend zur gewählten Zahl.
''')

# Symbolische Ebene
st.header('3. Symbolische Ebene – mathematische Schreibweise')
st.markdown(f'Der gewählte Bruch symbolisch: **{zaehler}/{nenner}**')
st.markdown(f'Dezimaldarstellung: **{zaehler / nenner:.2f}**')

st.markdown('''
**Unterrichtsidee:** Schülerinnen und Schüler wandeln verschiedene Brüche in Dezimalzahlen um und umgekehrt, um den Zusammenhang zwischen symbolischer und dezimaler Darstellung zu verstehen.
''')

# Zusätzliche Aufgaben für Sie
st.header('Zusätzliche Aufgaben für Sie')
st.markdown('''
- Entwickeln Sie mindestens drei weitere praktische Unterrichtsideen zur enaktiven Einführung von Brüchen.
- Erstellen Sie zusätzliche ikonische Darstellungen (z.B. Rechteckmodell, Balkendiagramm) für unterschiedliche Brüche.
- Formulieren Sie mögliche Schwierigkeiten, die Schülerinnen und Schüler beim Übergang von der ikonischen zur symbolischen Ebene haben könnten, und entwickeln Sie unterstützende Maßnahmen dazu.
- Überlegen Sie, wie Sie digitale Medien zusätzlich zur App einsetzen können, um das Verständnis des EIS-Prinzips zu fördern.
''')

