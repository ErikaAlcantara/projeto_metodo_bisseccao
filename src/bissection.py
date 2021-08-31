from interval import Interval
import math
class Bissection:
    def __init__(self, a, b, c, d, e, constant, epsilon):
        self.epsilon = epsilon
        self.epsilon = epsilon
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.constant = constant
        
    def get_grau(self):
        grau = 0
        if self.e!=0: grau = 1
        if self.d!=0: grau = 2
        if self.c!=0: grau = 3
        if self.b!=0: grau = 4
        if self.a!=0: grau = 5
        return grau

    def solve_function (self, x_value):
        return (self.a*x_value**5 + self.b*x_value**4 + self.c*x_value**3 + self.d*x_value**2 + self.e*x_value + self.constant)

    def g_of_x(self, degree, x_value):
        if degree == 5:
            return self.a*x_value**5
        elif degree == 4:
            return self.b*x_value**4
        elif degree == 3:
            return self.c*x_value**3
        elif degree == 2:
            return self.d*x_value**2
        else:
            return self.e*x_value + self.constant
    
    def h_of_x (self, x_value, degree):
        if degree == 5:
            return self.b*x_value**4 + self.c*x_value**3 + self.d*x_value**2 + self.e*x_value + self.constant
        elif degree == 4:
            return self.c*x_value**3 + self.d*x_value**2 + self.e*x_value + self.constant
        elif degree == 3:
            return self.d*x_value**2 + self.e*x_value + self.constant
        else:
            return self.e*x_value + self.constant
    
        

    def get_intervals(self, grau):
        all_intervalls = []
        a = -100
        while len(all_intervalls) <= grau:
            for b in range(-99, 101):
                if self.solve_function(a) * self.solve_function(b) < 0:       
                    all_intervalls.append([a,b])
                a +=1
            break   
        return all_intervalls
            
    def apply_bissection(self, all_intervalls):
        
        all_tables = []
        for i in all_intervalls:
            table = []
            midpoints = []
            a = i[0]
            b = i[1]
            while not b-a < self.epsilon:
                midpoint = (a+b)/2
                if self.solve_function(midpoint) < 0:
                    a = midpoint
                elif self.solve_function(midpoint) > 0:
                    b = midpoint
                else:
                    a = midpoint
                    b = midpoint
                midpoints.append([a, b])
            table.append(midpoints)
            all_tables.append(table)    
        return all_tables
        

        
    

                

            
            
            





        
