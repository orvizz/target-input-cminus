allExpr = ['a', 'b', 'c', "'a'", 1, 1.5, 'd']

with open('target/l9-unary-minus.cminus', 'w') as f:
    f.write("void main() {\n")
    f.write("\tint a;\n\tdouble b;\n\tchar c;\n")
    f.write("\n")
    line = 5
    for expr in allExpr:
        assign = 'a = -' + str(expr) + ';'
        line+=1
        if expr == 'd':
            assign += f" // Error in line {line}"
        assign+= "\n"
        f.write(f"\t{assign}")
    f.write("}\n")