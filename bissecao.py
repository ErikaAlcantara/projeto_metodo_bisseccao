import streamlit as st
import time
import numpy as np
import pandas as pd


st.title('Aplicação para o Método da Bissecção')
st.write('Dada a função: _X^5+_X^4+_X^3+_X^2+_X+C')
st.write('Insira os valores da função:')

x5 = st.number_input("_Xˆ5: ", min_value = -100, max_value=100, value=0, step=1) 
x4 = st.number_input("_Xˆ4: ", min_value = -100, max_value=100, value=0, step=1) 
x3 = st.number_input("_Xˆ3: ", min_value = -100, max_value=100, value=0, step=1) 
x2 = st.number_input("_Xˆ2: ", min_value = -100, max_value=100, value=0, step=1) 
x = st.number_input("_X: ", min_value = -100, max_value=100, value=0, step=1) 
c = st.number_input("C: ", min_value = -100, max_value=100, value=0, step=1) 
e = st.number_input("Epsilon: ", min_value = -100, max_value=100, value=0, step=1) 
y= -200

d = {
    'f(x)': []
}
# ^^^, 'g(x)': [1,2], 'h(x)': [1,2]
while y <= 200:
    soma = (x5 * (y**5)) + (x4 * (y**4)) + (x3 * (y**3)) + (x2 * (y**2)) + (x * y) + c
    d['f(x)'].append(soma) 
    y += 1

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = pd.DataFrame(data=d)
chart = st.line_chart(last_rows)



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