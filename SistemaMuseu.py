import getpass

# Abaixo fica os Dados de login (usuário e gestor).
usuarios = {
    "bran": "01",
    "usuario2": "2"
}

gestores = {
    "gestor1": "gestor1",
    "gestor2": "gestor2"
}
administradores = {
    "brayan": "123",
    "gioliano": "99"
}

# Abaixo está a Lista de obras, artistas, estilos artísticos e empréstimos.
obras = [
    {
        "titulo": "A Noite Estrelada",
        "data_criacao": "1889",
        "tema": "Paisagem",
        "estilo": "Pós-Impressionismo",
        "descricao": "Uma das pinturas mais famosas de Vincent van Gogh.",
        "tecnica": "Óleo sobre tela",
        "autor": "Vincent van Gogh",
        "localizacao": "Sala 1",
        "documentos": ["Carta ao irmão Theo", "Fotografia de Van Gogh"],
        "figura_retratada": None
    },
    {
        "titulo": "Monalisa",
        "data_criacao": "1503",
        "tema": "Retrato",
        "estilo": "Renascimento",
        "descricao": "Pintura icônica de Leonardo da Vinci, famosa por seu enigmático sorriso.",
        "tecnica": "Óleo sobre madeira",
        "autor": "Leonardo da Vinci",
        "localizacao": "Sala 2",
        "documentos": ["Estudo sobre proporções", "Entrevista sobre a Monalisa"],
        "figura_retratada": {
            "nome": "Lisa Gherardini",
            "descricao": "Nobre italiana, modelo para o retrato."
        }
    },
    {
        "titulo": "O Grito",
        "data_criacao": "1893",
        "tema": "Expressão",
        "estilo": "Expressionismo",
        "descricao": "Obra expressiva de Edvard Munch que representa a ansiedade humana.",
        "tecnica": "Óleo, têmpera e pastel sobre papelão",
        "autor": "Edvard Munch",
        "localizacao": "Sala 3",
        "documentos": ["Carta de Munch sobre a obra"],
        "figura_retratada": None
    },
    {
        "titulo": "A Persistência da Memória",
        "data_criacao": "1931",
        "tema": "Surrealismo",
        "estilo": "Surrealismo",
        "descricao": "Pintura surrealista de Salvador Dalí que representa relógios derretendo.",
        "tecnica": "Óleo sobre tela",
        "autor": "Salvador Dalí",
        "localizacao": "Sala 4",
        "documentos": ["Fotografia de Dalí", "Entrevista sobre a obra"],
        "figura_retratada": None
    },
    {
        "titulo": "Guernica",
        "data_criacao": "1937",
        "tema": "Guerra",
        "estilo": "Cubismo",
        "descricao": "Pintura de Pablo Picasso que retrata os horrores da Guerra Civil Espanhola.",
        "tecnica": "Óleo sobre tela",
        "autor": "Pablo Picasso",
        "localizacao": "Sala 5",
        "documentos": ["Carta sobre Guernica", "Fotografia de Picasso"],
        "figura_retratada": None
    },
    
]

# Abaixo está a Lista de artistas, estilos artísticos e empréstimos
artistas = [
     {
        "nome": "Vincent van Gogh",
        "data_nascimento": "1853-03-30",
        "local_nascimento": "Zundert, Países Baixos",
        "biografia": "Van Gogh foi um pintor pós-impressionista holandês que é um dos mais famosos e influentes figuras na história da arte ocidental.",
        "estilos": ["Pós-Impressionismo"]
    },
    {
        "nome": "Leonardo da Vinci",
        "data_nascimento": "1452-04-15",
        "local_nascimento": "Vinci, Itália",
        "biografia": "Leonardo da Vinci foi um polímata italiano do Renascimento cujas áreas de interesse incluíam invenção, pintura, escultura, arquitetura, ciência, música, matemática, engenharia, literatura, anatomia, geologia, astronomia, botânica, escrita, história e cartografia.",
        "estilos": ["Renascimento"]
    },
    {
        "nome": "Edvard Munch",
        "data_nascimento": "1863-12-12",
        "local_nascimento": "Loten, Noruega",
        "biografia": "Edvard Munch foi um pintor norueguês, cuja obra altamente simbólica é vista como precursora do expressionismo.",
        "estilos": ["Expressionismo"]
    },
    {
        "nome": "Salvador Dalí",
        "data_nascimento": "1904-05-11",
        "local_nascimento": "Figueres, Espanha",
        "biografia": "Salvador Dalí foi um pintor surrealista espanhol, conhecido pelo seu trabalho meticulosamente executado e onírico, bem como pela sua personalidade excêntrica.",
        "estilos": ["Surrealismo"]
    },
    {
        "nome": "Pablo Picasso",
        "data_nascimento": "1881-10-25",
        "local_nascimento": "Málaga, Espanha",
        "biografia": "Pablo Picasso foi um pintor, escultor, ceramista, cenógrafo, poeta e dramaturgo espanhol que passou a maior parte da sua vida na França.",
        "estilos": ["Cubismo"]
    },
    
]

estilos_artistico = [
     {
        "denominacao": "Pós-Impressionismo",
        "periodo": "1886-1905",
        "descricao": "Estilo artístico que surgiu na França e caracteriza-se pelo uso de cores vivas, uso de formas geométricas e uma abordagem subjetiva à pintura.",
        "escola_principal": "França"
    },
    {
        "denominacao": "Renascimento",
        "periodo": "Século XIV - XVII",
        "descricao": "Período da história europeia marcado pelo 'renascimento' da cultura clássica e pelo desenvolvimento das artes, da literatura e das ciências.",
        "escola_principal": "Itália"
    },
    {
        "denominacao": "Expressionismo",
        "periodo": "Início do século XX",
        "descricao": "Movimento artístico que surgiu na Alemanha e é caracterizado pela distorção da realidade para expressar emoções e sentimentos subjetivos.",
        "escola_principal": "Alemanha"
    },
    {
        "denominacao": "Surrealismo",
        "periodo": "Década de 1920 - 1940",
        "descricao": "Movimento artístico e literário que buscava libertar a mente das convenções da lógica e da razão, explorando o inconsciente e os sonhos.",
        "escola_principal": "França"
    },
    {
        "denominacao": "Cubismo",
        "periodo": "1907-1914",
        "descricao": "Movimento artístico que desafia as convenções da perspectiva tradicional através do uso de formas geométricas e fragmentação de objetos.",
        "escola_principal": "França"
    },
    
]

emprestimos = [
     {
        "titulo_obra": "Monalisa",
        "periodo_emprestimo": "01/01/2024 - 31/01/2024",
        "nome_evento": "Exposição Renascimento",
        "responsavel": "Maria Silva",
        "tema": "Renascimento"
    }
    
]

# Abaixo está a função para salvar log
def registrar_log(acao, item, tipo):
    with open("log.txt", "a") as log_file:
        log_file.write(f"Ação: {acao} | Tipo: {tipo} | Item: {item}\n")

# Abaixo está a função de ordenação por (título)
def ordenar_obras(obras):
    return sorted(obras, key=lambda x: x['titulo'])

# Abaixo está a função para listar (todas as obras)
def listar_obras():
    obras_ordenadas = ordenar_obras(obras)
    for obra in obras_ordenadas:
        estilo = next((estilo for estilo in estilos_artistico if estilo['denominacao'] == obra['estilo']), None)
        estilo_descr = estilo['descricao'] if estilo else "Estilo desconhecido"
        documentos = ", ".join(obra['documentos']) if obra['documentos'] else "Nenhum documento"
        figura_retratada = obra['figura_retratada']['nome'] if obra['figura_retratada'] else "Nenhuma"
        print(f"Título: {obra['titulo']}, Autor: {obra['autor']}, Estilo: {obra['estilo']}, Descrição do Estilo: {estilo_descr}, Localização: {obra['localizacao']}, Documentos: {documentos}, Figura Retratada: {figura_retratada}")

# Abaixo está a função para buscar obra por (título)
def buscar_obra(titulo):
    for obra in obras:
        if obra['titulo'].lower() == titulo.lower():
            return obra
    return None

# Abaixo está a função para adicionar (nova obra)
def adicionar_obra():
  try:
    titulo = input("Título: ")
    data_criacao = input("Data de Criação: ")
    tema = input("Tema: ")
    estilo = input("Estilo Artístico: ")
    descricao = input("Descrição: ")
    tecnica = input("Técnica Utilizada: ")
    autor = input("Autor: ")
    localizacao = input("Localização na Sala de Exposição: ")
    documentos = input("Documentos Relacionados (separados por vírgula): ").split(',')
    figura_retratada_nome = input("Nome da Figura Retratada (se houver): ")
    figura_retratada_desc = input("Descrição da Figura Retratada (se houver): ") if figura_retratada_nome else None

    nova_obra = {
        "titulo": titulo,
        "data_criacao": data_criacao,
        "tema": tema,
        "estilo": estilo,
        "descricao": descricao,
        "tecnica": tecnica,
        "autor": autor,
        "localizacao": localizacao,
        "documentos": [doc.strip() for doc in documentos],
        "figura_retratada": {
            "nome": figura_retratada_nome,
            "descricao": figura_retratada_desc
        } if figura_retratada_nome else None
    }

    obras.append(nova_obra)
    registrar_log("Adicionar", nova_obra['titulo'], "Obra")
    print("Obra adicionada com sucesso!")
    print()
  except Exception as e:
        print(f"Erro: {e}")
        print("A obra não pôde ser adicionada. Por favor, verifique os dados e tente novamente.")
        print("Obrigado")
  finally:
        print("Operação está sendo finalizada.")
        print()

# Abaixo está a função de remover obra.
def remover_obra():
    titulo = input("Título da obra a remover: ")
    obra = buscar_obra(titulo)

    if obra:
        obras.remove(obra)
        registrar_log("Remover", obra['titulo'], "Obra")
        print("Obra removida com sucesso!")
    else:
        print("Obra não encontrada.")

# Abaixo está a função para editar obra.
def editar_obra():
    titulo = input("Título da obra a editar: ")
    obra = buscar_obra(titulo)

    if obra:
        print("Deixe em branco para manter o valor atual.")
        obra['data_criacao'] = input(f"Data de Criação [{obra['data_criacao']}]: ") or obra['data_criacao']
        obra['tema'] = input(f"Tema [{obra['tema']}]: ") or obra['tema']
        obra['estilo'] = input(f"Estilo Artístico [{obra['estilo']}]: ") or obra['estilo']
        obra['descricao'] = input(f"Descrição [{obra['descricao']}]: ") or obra['descricao']
        obra['tecnica'] = input(f"Técnica Utilizada [{obra['tecnica']}]: ") or obra['tecnica']
        obra['autor'] = input(f"Autor [{obra['autor']}]: ") or obra['autor']
        obra['localizacao'] = input(f"Localização na Sala de Exposição [{obra['localizacao']}]: ") or obra['localizacao']
        documentos = input(f"Documentos Relacionados [{', '.join(obra['documentos'])}]: ")
        if documentos:
            obra['documentos'] = [doc.strip() for doc in documentos.split(',')]
        figura_retratada_nome = input(f"Nome da Figura Retratada [{obra['figura_retratada']['nome'] if obra['figura_retratada'] else 'Nenhuma'}]: ") or (obra['figura_retratada']['nome'] if obra['figura_retratada'] else None)
        figura_retratada_desc = input(f"Descrição da Figura Retratada [{obra['figura_retratada']['descricao'] if obra['figura_retratada'] else 'Nenhuma'}]: ") if figura_retratada_nome else None
        obra['figura_retratada'] = {
            "nome": figura_retratada_nome,
            "descricao": figura_retratada_desc
        } if figura_retratada_nome else None

        registrar_log("Editar", obra['titulo'], "Obra")
        print("Obra editada com sucesso!")
        print()
    else:
        print("Obra não encontrada.")
        print()

# Abaixo está a função para listar (todos) os artistas.
def listar_artistas():
    for artista in artistas:
        print(f"Nome: {artista['nome']}, Data de Nascimento: {artista['data_nascimento']}, Local de Nascimento: {artista['local_nascimento']}, Estilos: {', '.join(artista['estilos'])}")

# Abaixo está a função para buscar artista por (nome).
def buscar_artista(nome):
    for artista in artistas:
        if artista['nome'].lower() == nome.lower():
            return artista
    return None

# Abaixo está a função para adicionar um novo artista.
def adicionar_artista():
    nome = input("Nome: ")
    data_nascimento = input("Data de Nascimento: ")
    local_nascimento = input("Local de Nascimento: ")
    biografia = input("Biografia: ")
    estilos = input("Estilos Artísticos (separados por vírgula): ").split(',')

    novo_artista = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "local_nascimento": local_nascimento,
        "biografia": biografia,
        "estilos": [estilo.strip() for estilo in estilos]
    }

    artistas.append(novo_artista)
    registrar_log("Adicionar", novo_artista['nome'], "Artista")
    print("Artista adicionado com sucesso!")
    print()

# Abaixo está a função para remover artista.
def remover_artista():
    nome = input("Nome do artista a remover: ")
    artista = buscar_artista(nome)

    if artista:
        artistas.remove(artista)
        registrar_log("Remover", artista['nome'], "Artista")
        print("Artista removido com sucesso!")
        print()
    else:
        print("Artista não encontrado.")

# Abaixo está a função para editar artista.
def editar_artista():
    nome = input("Nome do artista a editar: ")
    artista = buscar_artista(nome)

    if artista:
        print("Deixe em branco para manter o valor atual.")
        artista['data_nascimento'] = input(f"Data de Nascimento [{artista['data_nascimento']}]: ") or artista['data_nascimento']
        artista['local_nascimento'] = input(f"Local de Nascimento [{artista['local_nascimento']}]: ") or artista['local_nascimento']
        artista['biografia'] = input(f"Biografia [{artista['biografia']}]: ") or artista['biografia']
        estilos = input(f"Estilos Artísticos [{', '.join(artista['estilos'])}]: ")
        if estilos:
            artista['estilos'] = [estilo.strip() for estilo in estilos.split(',')]

        registrar_log("Editar", artista['nome'], "Artista")
        print("Artista editado com sucesso!")
        print()
    else:
        print("Artista não encontrado.")

# Abaixo está a função para listar todos os estilos artísticos.
def listar_estilos():
    for estilo in estilos_artistico:
        print(f"Denominação: {estilo['denominacao']}, Período: {estilo['periodo']}, Descrição: {estilo['descricao']}, Escola Principal: {estilo['escola_principal']}")

# Abaixo está a função para buscar estilo artístico por (denominação).
def buscar_estilo(denominacao):
    for estilo in estilos_artistico:
        if estilo['denominacao'].lower() == denominacao.lower():
            return estilo
    return None

# Abaixo está a função para adicionar novo estilo artístico.
def adicionar_estilo():
    denominacao = input("Denominação: ")
    periodo = input("Período de Influência: ")
    descricao = input("Descrição das Características: ")
    escola_principal = input("Principal Escola Representativa: ")

    novo_estilo = {
        "denominacao": denominacao,
        "periodo": periodo,
        "descricao": descricao,
        "escola_principal": escola_principal
    }

    estilos_artistico.append(novo_estilo)
    registrar_log("Adicionar", novo_estilo['denominacao'], "Estilo")
    print("Estilo artístico adicionado com sucesso!")
    print()

# Abaixo está a função para remover estilo artístico.
def remover_estilo():
    denominacao = input("Denominação do estilo a remover: ")
    estilo = buscar_estilo(denominacao)

    if estilo:
        estilos_artistico.remove(estilo)
        registrar_log("Remover", estilo['denominacao'], "Estilo")
        print("Estilo artístico removido com sucesso!")
        print()
    else:
        print("Estilo artístico não encontrado.")

# Abaixo está a função para editar estilo artístico.
def editar_estilo():
    denominacao = input("Denominação do estilo a editar: ")
    estilo = buscar_estilo(denominacao)

    if estilo:
        print("Deixe em branco para manter o valor atual.")
        estilo['periodo'] = input(f"Período de Influência [{estilo['periodo']}]: ") or estilo['periodo']
        estilo['descricao'] = input(f"Descrição das Características [{estilo['descricao']}]: ") or estilo['descricao']
        estilo['escola_principal'] = input(f"Principal Escola Representativa [{estilo['escola_principal']}]: ") or estilo['escola_principal']

        registrar_log("Editar", estilo['denominacao'], "Estilo")
        print("Estilo artístico editado com sucesso!")
        print()
    else:
        print("Estilo artístico não encontrado.")

# Abaixo está a função para listar (todos) os empréstimos.
def listar_emprestimos():
    for emprestimo in emprestimos:
        print(f"Obra: {emprestimo['titulo_obra']}, Período: {emprestimo['periodo_emprestimo']}, Evento: {emprestimo['nome_evento']}, Responsável: {emprestimo['responsavel']}, Tema: {emprestimo['tema']}")
        print()
# Abaixo está a função para buscar empréstimo por (título da obra).
def buscar_emprestimo(titulo_obra):
    for emprestimo in emprestimos:
        if emprestimo['titulo_obra'].lower() == titulo_obra.lower():
            return emprestimo
    return None

# Abaixo está a função para adicionar um novo empréstimo.
def adicionar_emprestimo():
    titulo_obra = input("Título da Obra: ")
    periodo_emprestimo = input("Período de Empréstimo: ")
    nome_evento = input("Nome do Evento: ")
    responsavel = input("Responsável: ")
    tema = input("Tema: ")

    novo_emprestimo = {
        "titulo_obra": titulo_obra,
        "periodo_emprestimo": periodo_emprestimo,
        "nome_evento": nome_evento,
        "responsavel": responsavel,
        "tema": tema
    }

    emprestimos.append(novo_emprestimo)
    registrar_log("Adicionar", novo_emprestimo['titulo_obra'], "Empréstimo")
    print("Empréstimo adicionado com sucesso!")
    print()

# Abaixo está a função para remover empréstimo.
def remover_emprestimo():
    titulo_obra = input("Título da Obra a remover do empréstimo: ")
    emprestimo = buscar_emprestimo(titulo_obra)

    if emprestimo:
        emprestimos.remove(emprestimo)
        registrar_log("Remover", emprestimo['titulo_obra'], "Empréstimo")
        print("Empréstimo removido com sucesso!")
        print()
    else:
        print("Empréstimo não encontrado.")

# Abaixo está a função para editar empréstimo.
def editar_emprestimo():
    titulo_obra = input("Título da Obra do empréstimo a editar: ")
    emprestimo = buscar_emprestimo(titulo_obra)

    if emprestimo:
        print("Deixe em branco para manter o valor atual.")
        emprestimo['periodo_emprestimo'] = input(f"Período de Empréstimo [{emprestimo['periodo_emprestimo']}]: ") or emprestimo['periodo_emprestimo']
        emprestimo['nome_evento'] = input(f"Nome do Evento [{emprestimo['nome_evento']}]: ") or emprestimo['nome_evento']
        emprestimo['responsavel'] = input(f"Responsável [{emprestimo['responsavel']}]: ") or emprestimo['responsavel']
        emprestimo['tema'] = input(f"Tema [{emprestimo['tema']}]: ") or emprestimo['tema']

        registrar_log("Editar", emprestimo['titulo_obra'], "Empréstimo")
        print("Empréstimo editado com sucesso!")
        print()
    else:
        print("Empréstimo não encontrado.")


def pedir_emprestimo():
    titulo_obra = input("Título da Obra: ")
    obra = buscar_obra(titulo_obra)

    if obra:
        periodo_emprestimo = input("Período de Empréstimo (ex: 01/01/2024 - 31/01/2024): ")
        nome_evento = input("Nome do Evento: ")
        responsavel = input("Responsável: ")
        tema = input("Tema: ")

        novo_emprestimo = {
            "titulo_obra": titulo_obra,
            "periodo_emprestimo": periodo_emprestimo,
            "nome_evento": nome_evento,
            "responsavel": responsavel,
            "tema": tema
        }

        emprestimos.append(novo_emprestimo)
        registrar_log("Adicionar", novo_emprestimo['titulo_obra'], "Empréstimo")
        print("Pedido de empréstimo realizado com sucesso!")
    else:
        print("Obra não encontrada.")

# Abaixo estão as funções específicas do menu do usuário.
def menu_usuario():
    while True:
        print("--- Menu de Usuário ---")
        print("1. Visitar Museu")
        print("2. Pedir Empréstimo de Obra")
        print("3. Visita Guiada com Roteiro")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")
        print()

        if opcao == '1':
          print("O Usuário escolheu a opção: Visitar Museu")
          print("1. Listar obras")
          print("2. Listar Artistas")
          print("3. Listar estilo artistico")
          opcao_visitar = input("Escolha uma opção: ")
          if opcao_visitar == "1":
            print("O Usuário escolheu a opção: Listar obras")
            listar_obras()
            print()
          elif opcao_visitar == "2":
            print("O Usuário escolheu a opção: Listar Artistas")
            listar_artistas()
            print()
          elif opcao_visitar == "3":
            print("O Usuário escolheu a opção: Listar estilo artistico")
            listar_estilos()
            print()
          else:
            print("Opção inválida. Tente novamente.")
        elif opcao == '2':
            print("O Usuário escolheu a opção: Pedir Empréstimo de Obra")
            pedir_emprestimo()
            print()
        elif opcao == '3':
            print("--- Roteiro da Visita Guiada ---")
            print("1. Sala 1: A Noite Estrelada")
            print("2. Sala 2: Monalisa")
            print("3. Sala 3: O Grito")
            print("4. Sala 4: A Persistência da Memória")
            print("5. Sala 5: Guernica")
            print()
        elif opcao == '4':
            break
            print()
        else:
            print("Opção inválida.")

# Abaixo estão as funções específicas do menu do gestor.
def menu_gestor():
    while True:
        print("--- Menu de Gestor ---")
        print("1. Visitar Museu")
        print("2. Gerenciar Acervo")
        print("3. Gerenciar Artistas")
        print("4. Gerenciar Estilos Artísticos")
        print("5. Gerenciar Empréstimos de Obras")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")
        print()

        if opcao == '1':
            print("O Gestor escolheu a opção: Visitar Museu")
            print("1. Listar obras")
            print("2. Listar artistas")
            print("3. Listar estilos artísticos")
            opcao_visitar = input("Escolha uma opção: ")
            if opcao_visitar == "1":
                print("O Gestor escolheu a opção: Listar obras ")
                listar_obras()
                print()
            elif opcao_visitar == "2":
                print("O Gestor escolheu a opção: Listar artistas")
                listar_artistas()
                print()
            elif opcao_visitar == "3":
                print("O Gestor escolheu a opção: Listar Estilos")
                listar_estilos()
                print()
            else:
                print("Opção inválida. Tente novamente.")
        elif opcao == '2':
            print("--- Gerenciar Acervo ---")
            print("1. Adicionar nova obra")
            print("2. Remover obra")
            print("3. Editar obra")
            print("4. Voltar")

            opcao_acervo = input("Escolha uma opção: ")

            if opcao_acervo == '1':
                print("Opção escolhida: Adicionar obra")
                adicionar_obra()
                print()
            elif opcao_acervo == '2':
                print("Opção escolhida: Remover obra")
                remover_obra()
                print()
            elif opcao_acervo == '3':
                print("Opção escolhida: Editar obra")
                editar_obra()
                print()
            elif opcao_acervo == '4':
                print()
                continue
            else:
                print("Opção inválida.")

        elif opcao == '3':
            print("--- Gerenciar Artistas ---")
            print("1. Listar todos os artistas")
            print("2. Adicionar novo artista")
            print("3. Remover artista")
            print("4. Editar artista")
            print("5. Voltar")

            opcao_artista = input("Escolha uma opção: ")

            if opcao_artista == '1':
                print("A opção escolhida foi: Listar Artistas")
                listar_artistas()
                print()
            elif opcao_artista == '2':
                print("A opção escolhida foi: Adicionar Artista")
                adicionar_artista()
                print()
            elif opcao_artista == '3':
                print("A opção escolhida foi: Remover Artista")
                remover_artista()
                print()
            elif opcao_artista == '4':
                print("A opção escolhida foi: Editar Artista")
                editar_artista()
                print()
            elif opcao_artista == '5':
                print()
                continue
            else:
                print("Opção inválida.")

        elif opcao == '4':
            print("--- Gerenciar Estilos Artísticos ---")
            print("1. Listar todos os estilos artísticos")
            print("2. Adicionar novo estilo artístico")
            print("3. Remover estilo artístico")
            print("4. Editar estilo artístico")
            print("5. Voltar")

            opcao_estilo = input("Escolha uma opção: ")

            if opcao_estilo == '1':
                print("A opção escolhida foi: Listar Estilo Artistico")
                listar_estilos()
                print()
            elif opcao_estilo == '2':
                print("A opção escolhida foi: Adicionar Novo Estilo Artistisco")
                adicionar_estilo()
                print()
            elif opcao_estilo == '3':
                print("A opção escolhida foi: Remover Estilo Artistico")
                remover_estilo()
                print()
            elif opcao_estilo == '4':
                print("A opção escolhida foi: Editar Estilo Artistico")
                editar_estilo()
                print()
            elif opcao_estilo == '5':
                print()
                continue
            else:
                print("Opção inválida.")

        elif opcao == '5':
            print("--- Gerenciar Empréstimos de Obras ---")
            print("1. Listar todos os empréstimos")
            print("2. Adicionar novo empréstimo")
            print("3. Remover empréstimo")
            print("4. Editar empréstimo")
            print("5. Voltar")

            opcao_emprestimo = input("Escolha uma opção: ")

            if opcao_emprestimo == '1':
                print("A opção escolhida foi: Listar Empréstimo")
                listar_emprestimos()
                print()
            elif opcao_emprestimo == '2':
                print("A opção escolhida foi: Adicionar Empréstimo")
                adicionar_emprestimo()
                print()
            elif opcao_emprestimo == '3':
                print("A opção escolhida foi: Remover Empréstimo")
                remover_emprestimo()
                print()
            elif opcao_emprestimo == '4':
                print("A opção escolhida foi: Editar Empréstimo")
                editar_emprestimo()
                print()
            elif opcao_emprestimo == '5':
                continue
            else:
                print("Opção inválida.")

        elif opcao == '6':
            break
            
        else:
            print("Opção inválida.")

# Abaixo está as funções de cadastrar usuáro e cadastrar gestor.
def cadastrar_usuario():
    nome = input("Nome de usuário: ")
    senha = getpass.getpass("Senha: ")
    usuarios[nome] = senha
    print("Usuário cadastrado com sucesso!")
    print()
    
def cadastrar_gestor():
    admin_nome = input("Nome de usuário do administrador: ")
    admin_senha = getpass.getpass("Senha do administrador: ")

    if admin_nome in administradores and administradores[admin_nome] == admin_senha:
        nome = input("Digite o nome do gestor: ")
        senha = getpass.getpass("Digite a senha do gestor: ")
        if nome not in gestores:
            gestores[nome] = senha
            print("Gestor cadastrado com sucesso.")
            registrar_log("Cadastro", nome, "Gestor")
        else:
            print("Gestor já existe.")
    else:
        print("Autenticação de administrador falhou.")
        print(" Você não pode cadastrar Gestor")
        
# Abaixo está a função de login.
def login():
    while True:
        print("--- Login ---")
        tipo_usuario = input("Você é (1) Usuário ou (2) Gestor? ")

        if tipo_usuario == '1':
            print("Lembre-se de colocar o mesmo nome e senha do cadastro!")
            nome = input("Nome de usuário: ")
            senha = getpass.getpass("Senha: ")

            if nome in usuarios and usuarios[nome] == senha:
                print("Login de usuário bem-sucedido!")
                print()
                menu_usuario()
            else:
                print("Nome de usuário ou senha incorretos.")
            break

        elif tipo_usuario == '2':
            print("Lembre-se de colocar o mesmo nome e senha do cadastro!")
            nome = input("Nome de gestor: ")
            senha = getpass.getpass("Senha: ")

            if nome in gestores and gestores[nome] == senha:
                print("Login de gestor bem-sucedido!")
                print()
                menu_gestor()
            else:
                print("Nome de gestor ou senha incorretos.")
            print()
            break

        else:
            print("Opção inválida.")

def main():
    while True:
        print("--- Menu ---")
        print("1. Cadastrar usuário")
        print("2. Cadastrar gestor")
        print("3. Login")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print("A opção escolhida foi: Cadastrar Usuário")
            cadastrar_usuario()
            print()
        elif opcao == '2':
            print("A opção escolhida foi: Cadastrar Gestor")
            cadastrar_gestor()
            print()
        elif opcao == '3':
            print("Opção escolhida: Login")
            login()
            print()
        elif opcao == '4':
            break
        else:
            print("Opção inválida.")




if __name__ == "__main__":
    main()