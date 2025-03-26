variables = ['a', 'b', 'c']
literals = ["'a'", 1, 1.5]
undeclaredVar = 'd'
allExpr = ['a', 'b', 'c', "'a'", '1', '1.5', 'd']

with open('target/l9-arithmetic.cminus', 'w') as f:
    f.write("void main() {\n")
    f.write("\tint a;\n\tdouble b;\n\tchar c;\n")
    for expr in allExpr:
        f.write("\n")
        assign = 'a = ' + expr
        for expr2 in allExpr:
            finalAssign = assign + ' + ' + expr2 + ';\n'
            f.write(f"\t{finalAssign}")
    f.write("}\n")


