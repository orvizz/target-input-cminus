import random
allExpr = ['a', 'b', 'c', "'a'", 1, 1.5, 'd', 'iArr', 'pair']
types = ["int", "char", "double"]

with open('target/l9-cast.cminus', 'w') as f:
    f.write("void main() {\n")
    f.write("\tint a;\n\tdouble b;\n\tchar c;\n\tint[10] iArr;\n\tstruct {\n\t\tint a;\n\t\tint b;\n\t} pair;\n")
    f.write("\n")
    line = 10
    for expr in allExpr:
        assign = f'a = ({types[random.randint(0,2)]}) ' + str(expr) + ';'
        line+=1
        if expr == 'd' or expr == 'iArr' or expr == 'pair':
            assign += f" // Error in line {line}"
        assign+= "\n"
        f.write(f"\t{assign}")
    f.write(f"\ta = (int[10]) iArr; // Error in line {line+1}\n")
    f.write(f"\tiArr = (int[10]) 1; // Error in line {line+1}\n")
    f.write("}\n")