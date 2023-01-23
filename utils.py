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