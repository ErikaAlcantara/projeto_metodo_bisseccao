from bissection import Bissection
import interface
if __name__ == '__main__':
    bissection_solver = Bissection(0,0,1,0,-9,3, 0.003)
    
    print(bissection_solver.get_intervals(3))
    # print(bissection_solver.apply_bissection(bissection_solver.get_intervals(3)))
    
    #TODO linkar os métodos com a interface
