import re
from validate_docbr import CPF


def cpf_valido(numero_cpf):
    cpf = CPF()
    return cpf.validate(numero_cpf)


def nome_valido(nome):
    return nome.isalpha()


def rg_valido(rg):
    return len(rg) == 9


def celular_valido(celular):
    """Verifica se o celular está dentro do padrão válido
    Por exemplo: 51 91234-1234

    Args:
        celular (str): O número do celular

    Returns:
        bool: True se válido e False caso contrário
    """
    pattern = '\d{2} \d{5}-\d{4}'
    match = re.findall(pattern, celular)
    return match
