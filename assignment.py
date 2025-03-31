import random
allExpr = ['a', 'b', 'c', "'a'", 1, 1.5, 'd', 'iArr', 'pair', 'f()', 'p()', 'iArr[0]']
fields = ['a', 'b', 'c', 'd']
variables = ['a', 'b', 'c']

with open('target/l9-assignment.cminus', 'w') as f:
    f.write("int f(){\n\treturn 2;\n}\n\n")
    f.write("void p(){}\n\n")
    f.write("void main() {\n")
    f.write("\tint a;\n\tdouble b;\n\tchar c;\n\tint[10] iArr;\n\tstruct {\n\t\tint a;\n\t\tdouble b;\n\t\tchar c;\n\t} pair;\n\n")
    line = 16
    for var in variables:
        assign = f'{var} = '
        line += 1
        for expr in allExpr:
            finalAssign = assign + str(expr)
            if expr == 'pair':
                for field in fields:
                    line+=1
                    finalAssign2 = finalAssign + f'.{field};'
                    if field == 'd':
                        finalAssign2 += f" // Error in line {line}"
                    finalAssign2+= "\n"
                    f.write(f"\t{finalAssign2}")
            else:
                line+=1
                finalAssign+= ";\n"
                f.write(f"\t{finalAssign}")
        f.write("\n")
    f.write("}\n")