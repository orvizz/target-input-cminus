import random
variables = ['a', 'b', 'c']
literals = ["'a'", 1, 1.5]
undeclaredVar = 'd'
allExpr = ['a', 'b', 'c', "'a'", 1, 1.5, 'd', 'iArr', 'pair']
fields = ['a', 'b', 'c', 'd']


with open('target/l9-dot.cminus', 'w') as f:
    f.write("void main() {\n")
    f.write("\tint a;\n\tdouble b;\n\tchar c;\n\tint[10] iArr;\n\tstruct {\n\t\tint a;\n\t\tdouble b;\n\t\tchar c;\n\t} pair;\n")
    line = 10
    for expr in allExpr:
        f.write("\n")
        assign = 'a = ' + str(expr)
        line+=1
        if expr == 'pair':
            for field in fields:
                line+=1
                finalAssign = assign + f'.{field};'
                if field == 'd':
                    finalAssign += f" // Error in line {line}"
                finalAssign+= "\n"
                f.write(f"\t{finalAssign}")
        else:
            line+=1
            finalAssign = assign + f'.{fields[random.randint(0,3)]};'
            finalAssign += f" // Error in line {line}"
            finalAssign+= "\n"
            f.write(f"\t{finalAssign}")
    f.write("}\n")