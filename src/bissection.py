from interval import Interval
import math
class Bissection:
    def __init__(self, a, b, c, d, e, constant, epsilon):
        self.x_value = 0
        self.epsilon = epsilon
        self.iterations = 100
        self.epsilon = epsilon
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.constant = constant
        self.function_roots = []
        self.intervals = []
    
    
    def solve_function (self, x_value):
        return (self.a*x_value**5 + self.b*x_value**4 + self.c*x_value**3 + self.d*x_value**2 + self.e*x_value + self.constant)

    def get_intervals(self, x_value):
        interval = Interval()
        f_a = self.solve_function(x_value)
        a = x_value
        interval.set_left_extreme(a)
        # interval.apped(a)
        
        
        for _ in range(self.iterations):
            x_value += 1
            f_b = self.solve_function(x_value)
            if not f_a * f_b < 0:
                b = x_value
                interval.set_right_extreme(b)
                # interval.append(b)
                break
            else:
                x_value = 0
                for _ in range(self.iterations):
                    x_value -= 1
                    f_b = self.solve_function(x_value)
                    if not f_a * f_b < 0:
                        b = x_value
                        interval.set_right_extreme(b)
                        # interval.append(b)
                        break
        
        self.intervals.append(interval)
        # return interval


    def apply_bissection(self, interval):
        a = interval[0]
        b = interval[1]
        
        while not b-a < self.epsilon:
            midpoint = (a+b)/2
            if midpoint < 0:
                a = midpoint
            elif midpoint > 0:
                b = midpoint
            else:
                exact_root = midpoint
                self.function_roots.append(exact_root)
                # return exact_root

        self.function_roots.append(midpoint)
        
        # return midpoint

                

            
            
            





        
