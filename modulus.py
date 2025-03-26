allExpr = ['a', 'b', 'c', "'a'", 1, 1.5, 'd']

with open('target/l9-modulus.cminus', 'w') as f:
    f.write("void main() {\n")
    f.write("\tint a;\n\tdouble b;\n\tchar c;\n")
    line = 4
    for expr in allExpr:
        f.write("\n")
        assign = 'a = ' + str(expr)
        line+=1
        for expr2 in allExpr:
            line+=1
            finalAssign = assign + ' % ' + str(expr2) + ';'
            if not(((expr == "'a'" or expr == 'c')  and (expr2 == "'a'" or expr2 == 'c')) or ((expr == 1 or expr == 'a')  and (expr2 == 1 or expr2 == 'a'))):
                finalAssign += f" // Error in line {line}"
            finalAssign+= "\n"
            f.write(f"\t{finalAssign}")
    f.write("}\n")
