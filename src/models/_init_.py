class Motocicleta:
    def __int__(self, codigo_identificador, placa, modelo, ano):  
        self.codigo_identificador = codigo_identificador
        self.placa = placa  # Identificador único
        self.modelo = modelo
        self.ano = ano


class Entregador:
    def __init__(self, codigo_identificador, nome, data_nascimento, cnpj, numero_cnh, categoria_cnh, imagem_cnh):
        self.codigo_identificador = codigo_identificador 
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cnpj = cnpj  # Identificador único
        self.numero_cnh = numero_cnh  # Identificador único
        self.categoria_cnh = categoria_cnh  # (A, B ou A+B)
        self.imagem_cnh = imagem_cnh  # Formato png, bmp


class Plano :
    def __init__(self, identificador, tipo_plano, valor_diaria, quantidade_dias):
        self.identificador = identificador
        self.tipo_plano = tipo_plano
        self.valor_diaria = valor_diaria
        self.quantidade_dias = quantidade_dias


class Locação:
    Id
    data_inicio,
    data_fim,
    data_devolucao,
    data_previsao_fim,
    valor_adicional,
    percentual_multa,
    valor_total
