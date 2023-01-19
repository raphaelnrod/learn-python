def print_date(dia, mes, ano):
    print(dia, mes, ano, sep="/")

def print_type(var, var_name):
    print('The', var_name, "is a type of:", type(var))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dia = 15
    mes = 10
    ano = 2015
    print_date(dia, mes, ano)

    preco = 49.99
    print_type(preco, 'preco')
