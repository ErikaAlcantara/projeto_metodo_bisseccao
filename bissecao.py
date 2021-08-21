import streamlit as st
import time
import numpy as np


st.title('Aplicação para o Método da Bissecção')
st.write('Insira os valores da função:')
num_input1 = st.number_input("Xˆ5: ", min_value = -100, max_value=100, value=0, step=1) 
num_input2 = st.number_input("Xˆ4: ", min_value = -100, max_value=100, value=0, step=1) 
num_input3 = st.number_input("Xˆ3: ", min_value = -100, max_value=100, value=0, step=1) 
num_input4 = st.number_input("Xˆ2: ", min_value = -100, max_value=100, value=0, step=1) 
num_input5 = st.number_input("X: ", min_value = -100, max_value=100, value=0, step=1) 
num_input6 = st.number_input("C: ", min_value = -100, max_value=100, value=0, step=1) 
num_input7 = st.number_input("Epsilon: ", min_value = -100, max_value=100, value=0, step=1) 
st.button("Entra")



progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)

st.write('Obs: grafico teste')
for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text("%i%% Complete" % i)
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.05)

progress_bar.empty()

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")