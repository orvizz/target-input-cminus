import random
allExpr = ['a', 'b', 'c', "'a'", 1, 1.5, 'd']
types = ["int", "char", "double"]

with open('target/l9-cast.cminus', 'w') as f:
    f.write("void main() {\n")
    f.write("\tint a;\n\tdouble b;\n\tchar c;\n")
    f.write("\n")
    line = 5
    for expr in allExpr:
        assign = f'a = ({types[random.randint(0,2)]}) ' + str(expr) + ';'
        line+=1
        if expr == 'd':
            assign += f" // Error in line {line}"
        assign+= "\n"
        f.write(f"\t{assign}")
    f.write("}\n")