"""
minhastats.py

Núcleo estatístico próprio do Laboratório de Estatística.

As funções deste módulo implementam manualmente as principais
medidas estatísticas utilizadas pela aplicação.

Regra do projeto:
Não utilizar funções estatísticas prontas do NumPy, SciPy,
Pandas ou módulo statistics para realizar os cálculos.
"""


def _validar_dados(dados):
    """
    Valida uma coleção de dados numéricos.

    Parâmetros
    ----------
    dados : sequência
        Valores que serão utilizados no cálculo.

    Raises
    ------
    ValueError
        Quando a coleção estiver vazia.

    TypeError
        Quando algum elemento não for numérico.
    """

    if dados is None:
        raise ValueError("Os dados não podem ser None.")

    if len(dados) == 0:
        raise ValueError("A coleção de dados não pode estar vazia.")

    for valor in dados:
        if not isinstance(valor, (int, float)):
            raise TypeError(
                "Todos os valores devem ser numéricos."
            )


def media(dados):
    """
    Calcula a média aritmética dos valores.

    Fórmula:
        média = soma dos valores / número de valores
    """

    _validar_dados(dados)

    soma = 0.0

    for valor in dados:
        soma += valor

    return soma / len(dados)


def mediana(dados):
    """
    Calcula a mediana dos valores.
    """

    _validar_dados(dados)

    valores = sorted(dados)
    n = len(valores)
    meio = n // 2

    # Quantidade ímpar de elementos
    if n % 2 != 0:
        return valores[meio]

    # Quantidade par de elementos
    return (valores[meio - 1] + valores[meio]) / 2


def moda(dados):
    """
    Retorna uma lista contendo o(s) valor(es) de maior frequência.

    Em caso de distribuição amodal, quando todos os valores
    aparecem com a mesma frequência, retorna uma lista vazia.
    """

    _validar_dados(dados)

    frequencias = {}

    for valor in dados:
        if valor in frequencias:
            frequencias[valor] += 1
        else:
            frequencias[valor] = 1

    maior_frequencia = 0

    for frequencia in frequencias.values():
        if frequencia > maior_frequencia:
            maior_frequencia = frequencia

    # Todos aparecem com a mesma frequência.
    if maior_frequencia == 1:
        return []

    modas = []

    for valor, frequencia in frequencias.items():
        if frequencia == maior_frequencia:
            modas.append(valor)

    return sorted(modas)


def amplitude(dados):
    """
    Calcula a amplitude total dos dados.

    Fórmula:
        amplitude = maior valor - menor valor
    """

    _validar_dados(dados)

    menor = dados[0]
    maior = dados[0]

    for valor in dados[1:]:
        if valor < menor:
            menor = valor

        if valor > maior:
            maior = valor

    return maior - menor
    

# ============================================================
# VARIÂNCIA POPULACIONAL
# ============================================================

def variancia_populacional(dados):
    """
    Calcula a variância populacional.

    A variância mede o quanto os valores estão dispersos
    em relação à média.

    Fórmula:

        σ² = Σ(x - μ)² / N

    Onde:
        x = cada valor do conjunto
        μ = média populacional
        N = quantidade de valores
    """

    # Primeiro verificamos se os dados recebidos são válidos.
    _validar_dados(dados)

    # Calculamos a média utilizando NOSSA própria função.
    # Não utilizamos np.mean(), statistics.mean() etc.
    valor_media = media(dados)

    # Esta variável acumulará a soma dos quadrados
    # das diferenças entre cada valor e a média.
    soma_quadrados = 0.0

    # Percorremos cada valor existente nos dados.
    for valor in dados:

        # Calculamos a distância entre o valor e a média.
        diferenca = valor - valor_media

        # Elevamos essa diferença ao quadrado.
        quadrado_diferenca = diferenca ** 2

        # Acrescentamos o resultado ao acumulador.
        soma_quadrados += quadrado_diferenca

    # Na variância POPULACIONAL dividimos por N,
    # ou seja, pela quantidade total de elementos.
    return soma_quadrados / len(dados)


# ============================================================
# VARIÂNCIA AMOSTRAL
# ============================================================

def variancia_amostral(dados):
    """
    Calcula a variância amostral.

    Fórmula:

        s² = Σ(x - x̄)² / (n - 1)

    A diferença principal em relação à variância populacional
    é que dividimos por (n - 1).
    """

    # Valida os dados recebidos.
    _validar_dados(dados)

    # Para calcular variância amostral precisamos de
    # pelo menos dois elementos.
    #
    # Isso ocorre porque o denominador será n - 1.
    if len(dados) < 2:
        raise ValueError(
            "A variância amostral exige pelo menos dois valores."
        )

    # Calculamos a média através da nossa própria função.
    valor_media = media(dados)

    # Inicializa o acumulador.
    soma_quadrados = 0.0

    # Percorre todos os valores.
    for valor in dados:

        # Calcula a diferença em relação à média.
        diferenca = valor - valor_media

        # Soma o quadrado dessa diferença.
        soma_quadrados += diferenca ** 2

    # Na variância AMOSTRAL utilizamos n - 1.
    return soma_quadrados / (len(dados) - 1)


# ============================================================
# DESVIO PADRÃO POPULACIONAL
# ============================================================

def desvio_padrao_populacional(dados):
    """
    Calcula o desvio padrão populacional.

    O desvio padrão é a raiz quadrada da variância.

    Fórmula:

        σ = √σ²
    """

    # Utilizamos nossa própria função de variância.
    variancia = variancia_populacional(dados)

    # A raiz quadrada de um número pode ser calculada
    # elevando esse número a 1/2 (0.5).
    #
    # Dessa forma não precisamos utilizar np.sqrt().
    return variancia ** 0.5


# ============================================================
# DESVIO PADRÃO AMOSTRAL
# ============================================================

def desvio_padrao_amostral(dados):
    """
    Calcula o desvio padrão amostral.

    Fórmula:

        s = √s²
    """

    # Calculamos primeiro a variância amostral utilizando
    # nossa própria implementação.
    variancia = variancia_amostral(dados)

    # Retornamos a raiz quadrada da variância.
    return variancia ** 0.5

# ============================================================
# PERCENTIL
# ============================================================

def percentil(dados, percentual):
    """
    Calcula um percentil utilizando interpolação linear.

    O percentil indica o valor abaixo do qual está uma
    determinada porcentagem dos dados.

    Exemplos:
        percentil(dados, 25) -> percentil 25 (P25)
        percentil(dados, 50) -> percentil 50 (P50)
        percentil(dados, 75) -> percentil 75 (P75)

    O método utilizado é a interpolação linear.

    Fórmula da posição:

        posição = (n - 1) * (percentual / 100)

    Onde:
        n = quantidade de elementos
        percentual = percentil desejado entre 0 e 100

    IMPORTANTE:
    Esta função NÃO utiliza np.percentile(), statistics
    ou qualquer função estatística pronta.
    """

    # Verifica se a coleção recebida possui dados válidos.
    # Estamos reutilizando nossa função de validação já existente.
    _validar_dados(dados)

    # Verifica se o percentual informado é numérico.
    #
    # int   -> número inteiro, como 25
    # float -> número decimal, como 25.5
    if not isinstance(percentual, (int, float)):
        raise TypeError("O percentual deve ser um valor numérico.")

    # Um percentil somente pode estar entre 0 e 100.
    #
    # Portanto:
    # 0   é permitido.
    # 50  é permitido.
    # 100 é permitido.
    #
    # -1 ou 101, por exemplo, não são permitidos.
    if percentual < 0 or percentual > 100:
        raise ValueError(
            "O percentual deve estar entre 0 e 100."
        )

    # Cria uma NOVA lista contendo os dados ordenados.
    #
    # sorted() não calcula nenhuma estatística.
    # Ela apenas coloca os valores em ordem crescente.
    #
    # Também não modificamos a lista original recebida.
    dados_ordenados = sorted(dados)

    # Descobre quantos elementos existem.
    n = len(dados_ordenados)

    # Calcula a posição teórica do percentil.
    #
    # Exemplo:
    #
    # dados = [10, 20, 30, 40, 50]
    # percentual = 25
    #
    # posição = (5 - 1) * (25 / 100)
    # posição = 4 * 0.25
    # posição = 1.0
    posicao = (n - 1) * (percentual / 100)

    # int() remove a parte decimal positiva.
    #
    # Exemplo:
    # int(1.75) -> 1
    #
    # Esse será o índice inferior da interpolação.
    indice_inferior = int(posicao)

    # Calcula o índice imediatamente superior.
    indice_superior = indice_inferior + 1

    # Se a posição corresponder ao último elemento,
    # não existe um próximo índice.
    #
    # Nesse caso simplesmente retornamos o valor encontrado.
    if indice_superior >= n:
        return dados_ordenados[indice_inferior]

    # Descobrimos quanto da posição está depois
    # do índice inferior.
    #
    # Exemplo:
    #
    # posição = 1.75
    #
    # parte_decimal = 1.75 - 1
    # parte_decimal = 0.75
    parte_decimal = posicao - indice_inferior

    # Obtém o valor localizado no índice inferior.
    valor_inferior = dados_ordenados[indice_inferior]

    # Obtém o valor localizado no índice superior.
    valor_superior = dados_ordenados[indice_superior]

    # Faz manualmente a interpolação linear.
    #
    # Fórmula:
    #
    # valor_inferior +
    # (valor_superior - valor_inferior) * parte_decimal
    #
    # Se a posição for exatamente inteira,
    # parte_decimal será zero e o resultado será
    # simplesmente valor_inferior.
    resultado = (
        valor_inferior
        + (valor_superior - valor_inferior) * parte_decimal
    )

    # Devolve o percentil calculado.
    return resultado

# ============================================================
# QUARTIS
# ============================================================

def quartis(dados):
    """
    Calcula os três quartis principais de um conjunto de dados.

    Os quartis dividem os dados ordenados em quatro partes.

        Q1 = percentil 25
        Q2 = percentil 50
        Q3 = percentil 75

    Q2 corresponde também à mediana.

    Esta função utiliza NOSSA própria função percentil().
    """

    # Valida os dados antes de realizar os cálculos.
    _validar_dados(dados)

    # Calcula o primeiro quartil.
    #
    # Q1 representa o percentil 25.
    q1 = percentil(dados, 25)

    # Calcula o segundo quartil.
    #
    # Q2 representa o percentil 50 e corresponde
    # à mediana do conjunto.
    q2 = percentil(dados, 50)

    # Calcula o terceiro quartil.
    #
    # Q3 representa o percentil 75.
    q3 = percentil(dados, 75)

    # Retornamos os três resultados.
    #
    # Isso é uma "tupla" Python.
    #
    # Por exemplo:
    # (20.0, 30.0, 40.0)
    return q1, q2, q3

# ============================================================
# COEFICIENTE DE VARIAÇÃO
# ============================================================

def coeficiente_variacao(dados):
    """
    Calcula o coeficiente de variação amostral de um
    conjunto de dados.

    O coeficiente de variação (CV) mede a dispersão dos
    dados em relação à média e é expresso em porcentagem.

    Fórmula:

        CV = (s / |media|) * 100

    Onde:

        s     = desvio padrão amostral
        media = média aritmética dos dados

    IMPORTANTE:
    O cálculo utiliza as funções media() e
    desvio_padrao_amostral() implementadas nesta própria
    biblioteca.

    Nenhuma função estatística pronta do NumPy, SciPy
    ou statistics é utilizada neste cálculo.
    """

    # --------------------------------------------------------
    # 1. Validação dos dados
    # --------------------------------------------------------

    # Utilizamos novamente nossa função interna de validação.
    #
    # Ela verifica situações como:
    # - lista vazia;
    # - valores não numéricos.
    _validar_dados(dados)

    # --------------------------------------------------------
    # 2. Calcula a média
    # --------------------------------------------------------

    # Chamamos NOSSA função media(), implementada anteriormente.
    media_dados = media(dados)

    # --------------------------------------------------------
    # 3. Verifica se a média é zero
    # --------------------------------------------------------

    # Pela fórmula:
    #
    # CV = desvio_padrao / media
    #
    # não podemos dividir por zero.
    #
    # Portanto, quando a média for zero, o coeficiente
    # de variação não poderá ser calculado.
    if media_dados == 0:
        raise ValueError(
            "O coeficiente de variacao nao pode ser calculado "
            "quando a media e igual a zero."
        )

    # --------------------------------------------------------
    # 4. Calcula o desvio padrão amostral
    # --------------------------------------------------------

    # Novamente utilizamos NOSSA própria implementação.
    desvio = desvio_padrao_amostral(dados)

    # --------------------------------------------------------
    # 5. Calcula o coeficiente de variação
    # --------------------------------------------------------

    # abs() retorna o valor absoluto da média.
    #
    # Exemplo:
    #
    # abs(30)  -> 30
    # abs(-30) -> 30
    #
    # Assim, o denominador utilizado no CV permanece positivo.
    resultado = (desvio / abs(media_dados)) * 100

    # --------------------------------------------------------
    # 6. Retorna o resultado
    # --------------------------------------------------------

    return resultado


# ============================================================
# COVARIÂNCIA
# ============================================================

def covariancia_populacional(dados_x, dados_y):
    """
    Calcula a covariância populacional entre dois conjuntos
    de dados numéricos.

    A covariância indica como duas variáveis variam em conjunto.

    Interpretação geral:
        covariância > 0:
            as duas variáveis tendem a variar na mesma direção.

        covariância < 0:
            as duas variáveis tendem a variar em direções opostas.

        covariância próxima de 0:
            não há evidência forte de relação linear pela
            covariância.

    Fórmula da covariância populacional:

        Cov(X,Y) =
        soma((xi - media_x) * (yi - media_y)) / N

    Parâmetros:
        dados_x:
            Lista contendo os valores da primeira variável.

        dados_y:
            Lista contendo os valores da segunda variável.

    Retorno:
        Valor da covariância populacional.

    Exemplo:
        >>> covariancia_populacional(
        ...     [10, 20, 30, 40, 50],
        ...     [20, 40, 60, 80, 100]
        ... )
        400.0
    """

    # --------------------------------------------------------
    # Validação 1:
    # Os dois conjuntos precisam possuir valores.
    # --------------------------------------------------------

    if dados_x is None or dados_y is None:
        raise ValueError(
            "Os conjuntos de dados nao podem ser None."
        )

    # --------------------------------------------------------
    # Validação 2:
    # Os conjuntos não podem estar vazios.
    # --------------------------------------------------------

    if len(dados_x) == 0 or len(dados_y) == 0:
        raise ValueError(
            "Os conjuntos de dados nao podem estar vazios."
        )

    # --------------------------------------------------------
    # Validação 3:
    # Precisamos ter um valor de Y correspondente para
    # cada valor de X.
    #
    # Exemplo válido:
    #
    # X = [10, 20, 30]
    # Y = [15, 25, 35]
    #
    # Ambos possuem três elementos.
    # --------------------------------------------------------

    if len(dados_x) != len(dados_y):
        raise ValueError(
            "Os conjuntos de dados devem possuir "
            "a mesma quantidade de elementos."
        )

    # --------------------------------------------------------
    # Calculamos a média da variável X.
    #
    # IMPORTANTE:
    # Estamos utilizando nossa própria função media(),
    # implementada anteriormente no minhastats.py.
    # --------------------------------------------------------

    media_x = media(dados_x)

    # --------------------------------------------------------
    # Agora calculamos a média da variável Y.
    # --------------------------------------------------------

    media_y = media(dados_y)

    # --------------------------------------------------------
    # Criamos uma variável que armazenará a soma dos
    # produtos dos desvios em relação às médias.
    # --------------------------------------------------------

    soma_produtos = 0.0

    # --------------------------------------------------------
    # Percorremos os elementos utilizando seus índices.
    #
    # range(len(dados_x)) produzirá:
    #
    # 0, 1, 2, 3, ...
    #
    # Assim conseguimos acessar simultaneamente:
    #
    # dados_x[i]
    # dados_y[i]
    # --------------------------------------------------------

    for i in range(len(dados_x)):

        # Obtém o valor atual da variável X.
        valor_x = dados_x[i]

        # Obtém o valor correspondente da variável Y.
        valor_y = dados_y[i]

        # ----------------------------------------------------
        # Calcula quanto X está distante de sua média.
        # ----------------------------------------------------

        desvio_x = valor_x - media_x

        # ----------------------------------------------------
        # Calcula quanto Y está distante de sua média.
        # ----------------------------------------------------

        desvio_y = valor_y - media_y

        # ----------------------------------------------------
        # Multiplicamos os dois desvios.
        #
        # Quando os dois possuem o mesmo sinal,
        # o produto é positivo.
        #
        # Quando possuem sinais diferentes,
        # o produto é negativo.
        # ----------------------------------------------------

        produto = desvio_x * desvio_y

        # ----------------------------------------------------
        # Acumulamos o resultado.
        # ----------------------------------------------------

        soma_produtos += produto

    # --------------------------------------------------------
    # Na covariância POPULACIONAL dividimos por N.
    #
    # N corresponde à quantidade total de elementos.
    # --------------------------------------------------------

    resultado = soma_produtos / len(dados_x)

    # Retorna a covariância calculada.
    return resultado


# ============================================================
# COVARIÂNCIA AMOSTRAL
# ============================================================

def covariancia_amostral(dados_x, dados_y):
    """
    Calcula a covariância amostral entre dois conjuntos
    de dados numéricos.

    Fórmula:

        Cov(X,Y) =
        soma((xi - media_x) * (yi - media_y)) / (n - 1)

    A diferença para a covariância populacional está
    no denominador.

    Populacional:
        divide por N

    Amostral:
        divide por n - 1

    Parâmetros:
        dados_x:
            Lista contendo os valores da primeira variável.

        dados_y:
            Lista contendo os valores da segunda variável.

    Retorno:
        Valor da covariância amostral.
    """

    # --------------------------------------------------------
    # Validação 1:
    # Os conjuntos não podem ser None.
    # --------------------------------------------------------

    if dados_x is None or dados_y is None:
        raise ValueError(
            "Os conjuntos de dados nao podem ser None."
        )

    # --------------------------------------------------------
    # Validação 2:
    # Os conjuntos não podem estar vazios.
    # --------------------------------------------------------

    if len(dados_x) == 0 or len(dados_y) == 0:
        raise ValueError(
            "Os conjuntos de dados nao podem estar vazios."
        )

    # --------------------------------------------------------
    # Validação 3:
    # As duas listas precisam possuir a mesma quantidade
    # de elementos.
    # --------------------------------------------------------

    if len(dados_x) != len(dados_y):
        raise ValueError(
            "Os conjuntos de dados devem possuir "
            "a mesma quantidade de elementos."
        )

    # --------------------------------------------------------
    # Para calcular a covariância AMOSTRAL precisamos
    # de pelo menos dois pares de valores.
    #
    # Isso acontece porque o denominador é n - 1.
    #
    # Com apenas um elemento:
    #
    # n - 1 = 1 - 1 = 0
    #
    # e não podemos dividir por zero.
    # --------------------------------------------------------

    if len(dados_x) < 2:
        raise ValueError(
            "A covariancia amostral exige pelo menos "
            "dois pares de valores."
        )

    # --------------------------------------------------------
    # Calculamos as médias utilizando nossa própria
    # função media().
    # --------------------------------------------------------

    media_x = media(dados_x)
    media_y = media(dados_y)

    # Variável acumuladora.
    soma_produtos = 0.0

    # --------------------------------------------------------
    # Percorremos os dois conjuntos simultaneamente
    # através do índice.
    # --------------------------------------------------------

    for i in range(len(dados_x)):

        # Recupera os valores correspondentes.
        valor_x = dados_x[i]
        valor_y = dados_y[i]

        # Calcula os desvios em relação às médias.
        desvio_x = valor_x - media_x
        desvio_y = valor_y - media_y

        # Multiplica os desvios.
        produto = desvio_x * desvio_y

        # Adiciona o produto ao acumulador.
        soma_produtos += produto

    # --------------------------------------------------------
    # Aqui está a diferença fundamental:
    #
    # Covariância amostral divide por n - 1.
    # --------------------------------------------------------

    resultado = soma_produtos / (len(dados_x) - 1)

    # Retorna o resultado.
    return resultado

# ============================================================
# COEFICIENTE DE CORRELAÇÃO DE PEARSON
# ============================================================

def correlacao_pearson(dados_x, dados_y):
    """
    Calcula o coeficiente de correlação linear de Pearson
    entre dois conjuntos de dados numéricos.

    O coeficiente de Pearson mede a força e a direção
    da relação LINEAR entre duas variáveis.

    O resultado varia entre -1 e 1.

    Interpretação geral:

        r = 1
            Correlação linear positiva perfeita.

        r próximo de 1
            Correlação linear positiva forte.

        r próximo de 0
            Pouca ou nenhuma correlação linear.

        r próximo de -1
            Correlação linear negativa forte.

        r = -1
            Correlação linear negativa perfeita.

    Fórmula utilizada:

        r = cov(X,Y) / (sX * sY)

    Onde:

        cov(X,Y) = covariância amostral entre X e Y
        sX       = desvio padrão amostral de X
        sY       = desvio padrão amostral de Y

    IMPORTANTE:

    Esta função utiliza exclusivamente funções que já foram
    implementadas em nossa própria biblioteca minhastats.py.

    Não utilizamos numpy.corrcoef(), scipy.stats.pearsonr()
    ou qualquer outra função estatística pronta para realizar
    o cálculo apresentado pela aplicação.
    """

    # --------------------------------------------------------
    # 1. Validação: None
    # --------------------------------------------------------
    #
    # Precisamos receber os dois conjuntos de dados.
    #
    # Se algum deles for None, não existe informação
    # suficiente para calcular a correlação.
    # --------------------------------------------------------

    if dados_x is None or dados_y is None:
        raise ValueError(
            "Os conjuntos de dados nao podem ser None."
        )

    # --------------------------------------------------------
    # 2. Validação: listas vazias
    # --------------------------------------------------------

    if len(dados_x) == 0 or len(dados_y) == 0:
        raise ValueError(
            "Os conjuntos de dados nao podem estar vazios."
        )

    # --------------------------------------------------------
    # 3. Validação: tamanhos iguais
    # --------------------------------------------------------
    #
    # Cada observação de X precisa possuir uma observação
    # correspondente em Y.
    #
    # Exemplo:
    #
    # X = [10, 20, 30]
    # Y = [15, 25, 35]
    #
    # Temos os pares:
    #
    # (10, 15)
    # (20, 25)
    # (30, 35)
    # --------------------------------------------------------

    if len(dados_x) != len(dados_y):
        raise ValueError(
            "Os conjuntos de dados devem possuir "
            "a mesma quantidade de elementos."
        )

    # --------------------------------------------------------
    # 4. Validação: quantidade mínima
    # --------------------------------------------------------
    #
    # Como estamos trabalhando com covariância e
    # desvio padrão AMOSTRAIS, precisamos de pelo menos
    # dois pares de observações.
    # --------------------------------------------------------

    if len(dados_x) < 2:
        raise ValueError(
            "A correlacao de Pearson exige pelo menos "
            "dois pares de valores."
        )

    # --------------------------------------------------------
    # 5. Calcula a covariância amostral
    # --------------------------------------------------------
    #
    # Reutilizamos NOSSA função implementada anteriormente.
    # --------------------------------------------------------

    covariancia = covariancia_amostral(
        dados_x,
        dados_y
    )

    # --------------------------------------------------------
    # 6. Calcula o desvio padrão amostral de X
    # --------------------------------------------------------

    desvio_x = desvio_padrao_amostral(dados_x)

    # --------------------------------------------------------
    # 7. Calcula o desvio padrão amostral de Y
    # --------------------------------------------------------

    desvio_y = desvio_padrao_amostral(dados_y)

    # --------------------------------------------------------
    # 8. Verifica se existe variável constante
    # --------------------------------------------------------
    #
    # Se todos os valores de uma variável forem iguais,
    # seu desvio padrão será zero.
    #
    # Exemplo:
    #
    # X = [10, 10, 10, 10]
    #
    # Nesse caso:
    #
    # desvio_x = 0
    #
    # A fórmula de Pearson teria:
    #
    # covariancia / (0 * desvio_y)
    #
    # provocando divisão por zero.
    #
    # Além disso, a correlação de Pearson não é definida
    # quando uma das variáveis possui variância zero.
    # --------------------------------------------------------

    if desvio_x == 0 or desvio_y == 0:
        raise ValueError(
            "A correlacao de Pearson nao pode ser calculada "
            "quando uma das variaveis possui desvio padrao zero."
        )

    # --------------------------------------------------------
    # 9. Calcula o denominador
    # --------------------------------------------------------

    denominador = desvio_x * desvio_y

    # --------------------------------------------------------
    # 10. Calcula Pearson
    # --------------------------------------------------------

    resultado = covariancia / denominador

    # --------------------------------------------------------
    # 11. Retorna o resultado
    # --------------------------------------------------------

    return resultado

def regressao_linear(dados_x, dados_y):
    """
    Calcula uma regressao linear simples entre duas variaveis.

    A regressao linear procura encontrar uma reta que represente
    a relacao entre X e Y.

    A equacao da reta possui a forma:

        y = a + b * x

    onde:

        a = intercepto da reta
        b = coeficiente angular (inclinacao)

    Parametros
    ----------
    dados_x : lista
        Valores da variavel independente X.

    dados_y : lista
        Valores da variavel dependente Y.

    Retorno
    -------
    tuple
        Uma tupla contendo:

        (intercepto, inclinacao)

    Exemplo
    -------
    dados_x = [1, 2, 3, 4, 5]
    dados_y = [2, 4, 6, 8, 10]

    regressao_linear(dados_x, dados_y)

    Resultado:

        (0.0, 2.0)
    """

    # Verifica se os dois conjuntos possuem a mesma quantidade
    # de elementos.
    if len(dados_x) != len(dados_y):
        raise ValueError(
            "Os conjuntos de dados devem possuir a mesma quantidade de elementos."
        )

    # Para calcular uma regressao precisamos de pelo menos
    # dois pares de observacoes.
    if len(dados_x) < 2:
        raise ValueError(
            "A regressao linear exige pelo menos dois pares de valores."
        )

    # Calculamos a media dos valores de X.
    media_x = media(dados_x)

    # Calculamos a media dos valores de Y.
    media_y = media(dados_y)

    # Esta variavel armazenara a soma:
    #
    # (x - media_x) * (y - media_y)
    #
    # Esse valor representa a variacao conjunta de X e Y.
    soma_xy = 0.0

    # Esta variavel armazenara:
    #
    # (x - media_x) ** 2
    #
    # Ela representa a variacao existente nos valores de X.
    soma_x2 = 0.0

    # Percorremos os valores de X e Y simultaneamente.
    for x, y in zip(dados_x, dados_y):

        # Calculamos quanto X esta distante de sua media.
        diferenca_x = x - media_x

        # Calculamos quanto Y esta distante de sua media.
        diferenca_y = y - media_y

        # Acumulamos o produto das diferencas.
        soma_xy += diferenca_x * diferenca_y

        # Acumulamos o quadrado da diferenca de X.
        soma_x2 += diferenca_x ** 2

    # Se todos os valores de X forem iguais, soma_x2 sera zero.
    #
    # Nesse caso nao existe variacao em X e, portanto,
    # nao podemos calcular a inclinacao da reta.
    if soma_x2 == 0:
        raise ValueError(
            "A regressao linear nao pode ser calculada quando todos "
            "os valores de X sao iguais."
        )

    # Calculamos o coeficiente angular da reta.
    #
    # Ele informa quanto Y tende a variar quando X aumenta
    # uma unidade.
    inclinacao = soma_xy / soma_x2

    # Calculamos o intercepto.
    #
    # Pela equacao:
    #
    #     y = a + b*x
    #
    # temos:
    #
    #     a = media_y - b*media_x
    intercepto = media_y - inclinacao * media_x

    # Retornamos os dois coeficientes.
    return intercepto, inclinacao