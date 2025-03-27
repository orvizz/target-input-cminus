variables = ['a', 'b', 'c']
literals = ["'a'", 1, 1.5]
undeclaredVar = 'd'
allExpr = ['a', 'b', 'c', "'a'", 1, 1.5, 'd', 'iArr', 'pair']


with open('target/l9-square-brackets.cminus', 'w') as f:
    f.write("void main() {\n")
    f.write("\tint a;\n\tdouble b;\n\tchar c;\n\tint[10] iArr;\n\tstruct {\n\t\tint a;\n\t\tint b;\n\t} pair;\n")
    line = 9
    for expr in allExpr:
        f.write("\n")
        assign = 'a = ' + str(expr)
        line+=1
        for expr2 in allExpr:
            line+=1
            finalAssign = assign + f'[{str(expr2)}];'
            if not(expr=='iArr' and (expr2 == 1 or expr2 == 'a')):
                finalAssign += f" // Error in line {line}"
            finalAssign+= "\n"
            f.write(f"\t{finalAssign}")
    f.write("}\n")