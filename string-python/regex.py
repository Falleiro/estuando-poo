endereco = "Rua da Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

import re

padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-][0123456789][0123456789]")
busca = padra.search(endereco) #retorna o objeto match caso encontre o padrao no parametro

if busca:
    print(busca.group())