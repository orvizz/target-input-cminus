allExpr = ['a', 'b', 'c', "'a'", 1, 1.5, 'd']

with open('target/l9-not.cminus', 'w') as f:
    f.write("void main() {\n")
    f.write("\tint a;\n\tdouble b;\n\tchar c;\n")
    f.write("\n")
    line = 5
    for expr in allExpr:
        assign = 'a = !' + str(expr) + ';'
        line+=1
        if not(expr == 1 or expr == 'a'):
            assign += f" // Error in line {line}"
        assign+= "\n"
        f.write(f"\t{assign}")
    f.write("}\n")