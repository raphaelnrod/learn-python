def format_number():
    formatado = "R$ {:7.2f}".format(24.541)
    print(formatado)
    formatado2 = "R$ {:7.2f}".format(1114.54)
    print(formatado2)
    formatado3 = "R$ {:7.2f}".format(4.54)
    print(formatado3)


def print_date(dia, mes, ano):
    print(dia, mes, ano, sep="/")


def print_type(var, var_name):
    print('The', var_name, "is a type of:", type(var))


def replacer(s, newstring, index):
    # if not erroring, but the index is still not in the correct range..
    if index < 0:  # add it to the beginning
        return newstring + s
    if index > len(s):  # add it to the end
        return s + newstring

    # insert the new string between "slices" of the original
    return s[:index] + newstring + s[index + 1:]


def remove_duplicates(l):
    return list(set(l))
