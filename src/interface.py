import streamlit as st
import time
import numpy as np
import pandas as pd
from bokeh.plotting import figure
from bissection import Bissection
# Erika, preciso que vc instale o bokeh pra poder usar o grafo, vai no seu bash e digite [ pip install bokeh==2.2.0 ], caso contrário vc não vai conseguir ver o chart e vai dar erro no streamlit. :p

st.sidebar.title('Método da Bissecção')
st.sidebar.write('Dada a função: ')
st.sidebar.latex(r'''a xˆ5 + b xˆ4 + c xˆ3 + d xˆ2 + ex + k''')
st.sidebar.write('Insira os valores para as variáveis: ')
# vale lembrar que o valor de X é dado pelo eixo X, ele não é passado na montagem da formula em si :D
# fiz apenas algumas alterações nos titulos

x5 = st.sidebar.number_input("a: ", min_value = -100, max_value=100, value=0, step=1) 
x4 = st.sidebar.number_input("b: ", min_value = -100, max_value=100, value=0, step=1) 
x3 = st.sidebar.number_input("c: ", min_value = -100, max_value=100, value=0, step=1) 
x2 = st.sidebar.number_input("d: ", min_value = -100, max_value=100, value=0, step=1) 
x1 = st.sidebar.number_input("e: ", min_value = -100, max_value=100, value=0, step=1) 
k= st.sidebar.number_input("k: ", min_value = -100, max_value=100, value=0, step=1) 
ep = st.sidebar.number_input("Epsilon: ", min_value = -100, max_value=100, value=0, step=1) 

grau = 0
if x1!=0: grau = 1
if x2!=0: grau = 2
if x3!=0: grau = 3
if x4!=0: grau = 4
if x5!=0: grau = 5

y = -100
# define os resultados da função
f = []
# define o escopo do chart VV
s = []
# abre espaço dentro do escopo e grava os resultados da função dentro do chart
while y <= 100:
    soma = (x5 * (y**5)) + (x4 * (y**4)) + (x3 * (y**3)) + (x2 * (y**2)) + (x1 * y) + k
    
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

# progress_bar.empty()

def mk_table(x):
    # self.ep = ep
    a = []
    b = []
    c = []
    Fa = []
    Fb = []
    Fc = []
    b_a = []
    a.append(x[0])
    b.append(x[1])
    c.append((x[0]+x[1])/2)
    Fa.append(bissection_solver.solve_function(x[0]))
    Fb.append(bissection_solver.solve_function(x[1]))
    Fc.append(bissection_solver.solve_function((x[0] + x[1]) / 2))
    b_a.append(x[0] - x[1])



    return pd.DataFrame(data = {'A':a, 'B':b, 'F(a)':Fa, 'F(b)':Fb,'C=(a+b)/2':c,'F(c)':Fc, 'B-A':b_a})
# essa linha abaixo vai fazer uma tabela de qualquer coisa que vc por dentro, por isso q eu preciso saber como vc vai me passar os dados
bissection_solver = Bissection(0,0,1,0,-9,3, 0.003)

for i in bissection_solver.apply_bissection(bissection_solver.get_intervals(grau)):
    st.table(mk_table(i))

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")