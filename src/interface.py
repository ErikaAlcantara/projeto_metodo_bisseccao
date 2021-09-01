import streamlit as st
import time
import numpy as np
import pandas as pd
from bokeh.plotting import figure
from bissection import Bissection

st.sidebar.title('Método da Bissecção')
st.sidebar.write('Dada a função: ')
st.sidebar.latex(r'''axˆ5 + bxˆ4 + cxˆ3 + dxˆ2 + ex + k''')
st.sidebar.write('Insira os valores para as variáveis: ')


x5 = st.sidebar.number_input("a: ", min_value = -100, max_value=100, value=0, step=1) 
x4 = st.sidebar.number_input("b: ", min_value = -100, max_value=100, value=0, step=1) 
x3 = st.sidebar.number_input("c: ", min_value = -100, max_value=100, value=0, step=1) 
x2 = st.sidebar.number_input("d: ", min_value = -100, max_value=100, value=0, step=1) 
x1 = st.sidebar.number_input("e: ", min_value = -100, max_value=100, value=0, step=1) 
k= st.sidebar.number_input("k: ", min_value = -100, max_value=100, value=0, step=1)
st.sidebar.latex(r'''10^e''') 
ep = st.sidebar.number_input("Epsilon: ", min_value=-100, max_value=100, value=0, step=1) 
ep = 10**ep

bissection_solver = Bissection(x5, x4, x3, x2, x1, k, ep)

degree = 0
if x1!=0: degree = 1
if x2!=0: degree = 2
if x3!=0: degree = 3
if x4!=0: degree = 4
if x5!=0: degree = 5

y = -100
# define os resultados da função
f = []
fg = []
fh = []
# define o escopo do chart VV
s = []
# abre espaço dentro do escopo e grava os resultados da função dentro do chart


while y <= 100:
    function_sum = (x5 * (y**5)) + (x4 * (y**4)) + (x3 * (y**3)) + (x2 * (y**2)) + (x1 * y) + k
    
    f.append(bissection_solver.solve_function(y))
    fg.append(bissection_solver.g_of_x(bissection_solver.get_degree(),y))
    fh.append(bissection_solver.h_of_x(bissection_solver.get_degree(),y))
    s.append(y)
    y += 1

# inserção do chart

p = figure(
    title='grafo',
    x_axis_label='x',
    y_axis_label='y'
)
# inserção da linha

p.line(s, f, legend_label=' f(x)', line_color="blue", line_width=2)
p.line(s, fg, legend_label='g(x)', line_color="red", line_width=2)
p.line(s, fh, legend_label='h(x)', line_color="green", line_width=2)


progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
chart = st.bokeh_chart(p, use_container_width=2)

# progress_bar.empty()

def mk_table(x):
    # print(x)
    a = []
    b = []
    c = []
    Fa = []
    Fb = []
    Fc = []
    b_a = []
    for i in x: 
        a.append(i[0])
        b.append(i[1])
        c.append((i[0]+i[1])/2)
        Fa.append(bissection_solver.solve_function(i[0]))
        Fb.append(bissection_solver.solve_function(i[1]))
        Fc.append(bissection_solver.solve_function((i[0] + i[1]) / 2))
        b_a.append(i[0] - i[1])


    return pd.DataFrame(data = {'A':a, 'B':b, 'F(a)':Fa, 'F(b)':Fb,'C=(a+b)/2':c,'F(c)':Fc, 'B-A':b_a})
# essa linha abaixo vai fazer uma tabela de qualquer coisa que vc por dentro, por isso q eu preciso saber como vc vai me passar os dados
# bissection_solver = Bissection(x5,x4,x3,x2,x1,k, ep)

for i in bissection_solver.apply_bissection(bissection_solver.get_intervals(bissection_solver.get_degree())):
    for j in i :
        st.table(mk_table(j))

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")