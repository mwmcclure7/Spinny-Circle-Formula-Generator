import math

def make_formula(num_instances=3):
    x_part = "x"
    y_part = "y"
    for i in range(num_instances):
        x_part += f"-(r\u221Am^{i}+r\u221Am^({i}+1))cos((s^{i})t)"
        y_part += f"-(r\u221Am^{i}+r\u221Am^({i}+1))sin((s^{i})t)"

    return f"({x_part})^2+({y_part})^2=(r^2)m^{num_instances}"
0
print(make_formula(int(input("How many circles? "))))