import streamlit as st
import time
import numpy as np
import pandas as pd
from bokeh.plotting import figure

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
y = -100
# define os resultados da função
f = []
# define o escopo do chart VV
s = []
# abre espaço dentro do escopo e grava os resultados da função dentro do chart
while y <= 100:
    soma = (x5 * (y**5)) + (x4 * (y**4)) + (x3 * (y**3)) + (x2 * (y**2)) + (x * y) + c
    
    f.append(soma)
    s.append(y)
    y += 1

# inserção do chart
p = figure(
    title='grafo',
    x_axis_label='x',
    y_axis_label='y'
)
# inserção da linha
p.line(s, f, legend_label='f(x)', line_width=2)

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
chart = st.bokeh_chart(p, use_container_width=2)

progress_bar.empty()

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")