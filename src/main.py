from bissection import Bissection
if __name__ == '__main__':
    bissection_solver = Bissection(0,0,0,2,-22,-12, 0.003)
    bissection_solver.get_intervals(0)
    for interval in bissection_solver.intervals:
        print(str(interval.left_extreme) + "," + str(interval.right_extreme))
    
    print(len(bissection_solver.intervals))
