allExpr = ['a', 'b', 'c', "'a'", 1, 1.5, 'd', 'iArr', 'pair', 'f()', 'p()', 'iArr[0]']
fields = ['a', 'b', 'c', 'd']
variables = ['a', 'b', 'c']
valid_assignments = {
    'a': {'a', 1, 'iArr[0]', 'f()', 'pair.a'},
    'b': {'b', 1.5, 'pair.b'},
    'c': {'c', "'a'", 'pair.c'}
}

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
            error_comment = ""
            
            if expr == 'pair':
                for field in fields:
                    error_comment = ""
                    line += 1
                    finalAssign2 = finalAssign + f'.{field};'
                    if f'pair.{field}' not in valid_assignments[var]:
                        error_comment = f" // Error in line {line}"
                    if field == 'd':
                        finalAssign2 += f" // Error in line {line}"
                    finalAssign2 += f"{error_comment}\n"
                    f.write(f"\t{finalAssign2}")
            else:
                if expr not in valid_assignments[var]:
                    error_comment = f" // Error in line {line}"
                line += 1
                finalAssign += f";{error_comment}\n"
                f.write(f"\t{finalAssign}")
        f.write("\n")
    f.write("}\n")
