import streamlit as st
import time
import numpy as np
import pandas as pd


st.title('Aplicação para o Método da Bissecção')
st.write('Dada a função: X^5+X^4+X^3+X^2+X+C')
st.write('Insira os valores da função:')

num_input1 = st.number_input("Xˆ5: ", min_value = -100, max_value=100, value=0, step=1) 
num_input2 = st.number_input("Xˆ4: ", min_value = -100, max_value=100, value=0, step=1) 
num_input3 = st.number_input("Xˆ3: ", min_value = -100, max_value=100, value=0, step=1) 
num_input4 = st.number_input("Xˆ2: ", min_value = -100, max_value=100, value=0, step=1) 
num_input5 = st.number_input("X: ", min_value = -100, max_value=100, value=0, step=1) 
num_input6 = st.number_input("C: ", min_value = -100, max_value=100, value=0, step=1) 
num_input7 = st.number_input("Epsilon: ", min_value = -100, max_value=100, value=0, step=1) 
st.button("Entra")


d = {'f(x)': [1,2,3,4,5], 'g(x)': [5,4,3,2,1], 'h(x)': [6,7,8,9,10]}

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = pd.DataFrame(data=d)
chart = st.line_chart(last_rows)

d = {'f(x)': [], 'g(x)': [], 'h(x)': []}

# st.write('Obs: grafico teste')
# for i in range(1, 101):
#     new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
#     status_text.text("%i%% Complete" % i)
#     chart.add_rows(new_rows)
#     progress_bar.progress(i)
#     last_rows = new_rows
#     time.sleep(0.05)

progress_bar.empty()

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")