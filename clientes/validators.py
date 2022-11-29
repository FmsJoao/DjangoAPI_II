def cpf_valido(numero_do_cpf):
    return len(numero_do_cpf) == 11


def nome_valido(nome):
    return nome.isalpha()


def rg_valido (rg):
    return len(rg) != 9
