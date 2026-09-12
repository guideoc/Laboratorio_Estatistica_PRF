"""
test_minhastats.py

Arquivo responsável pelos testes automatizados da nossa
biblioteca estatística própria: minhastats.py.

IMPORTANTE:
O NumPy é utilizado SOMENTE para validar os resultados
calculados pelas nossas próprias funções.

As estatísticas apresentadas pela aplicação serão calculadas
pelo minhastats.py e não pelo NumPy.

Tolerância numérica utilizada nas comparações:
    rtol = 1e-9
    atol = 1e-12
"""

# Importa a biblioteca NumPy.
# Neste arquivo ela será usada somente como referência para
# verificar se nossos cálculos estão corretos.
import numpy as np

# Importa o pytest.
# Ele é responsável por localizar e executar automaticamente
# as funções de teste deste arquivo.
import pytest

# Importa todas as funções da nossa biblioteca que serão
# verificadas pelos testes automatizados.
from minhastats import (
    media,
    mediana,
    moda,
    regressao_linear,
    amplitude,
    variancia_populacional,
    variancia_amostral,
    desvio_padrao_populacional,
    desvio_padrao_amostral,
    percentil,
    quartis,
    coeficiente_variacao,
    covariancia_populacional,
    covariancia_amostral,
    correlacao_pearson,
)

# ============================================================
# CONFIGURAÇÃO DA TOLERÂNCIA NUMÉRICA
# ============================================================

# RTOL significa "Relative Tolerance" (tolerância relativa).
#
# 1e-9 significa:
# 1 x 10 elevado a -9
#
# ou seja:
# 0.000000001
#
# Essa tolerância é utilizada porque cálculos com números
# decimais podem apresentar pequenas diferenças devido à
# representação de ponto flutuante do computador.
RTOL = 1e-9

# ATOL significa "Absolute Tolerance" (tolerância absoluta).
#
# 1e-12 significa:
# 1 x 10 elevado a -12
#
# ou:
# 0.000000000001
ATOL = 1e-12

# ============================================================
# TESTES DA MÉDIA
# ============================================================

# "def" significa: definir uma função. Nesse caso estamos criando uma função
def test_media_valores_inteiros():
    """
    Verifica a média utilizando números inteiros.
    """

    # Cria os dados que serão utilizados no teste.
    dados = [10, 20, 20, 30, 40]

    # Calcula a média utilizando NOSSA função.
    # o "= "significa que estamos armazenando na variável, resultado aquilo que nossa função media() devolveu.
    resultado = media(dados)

    # Calcula a média utilizando NumPy.
    #
    # Este valor serve apenas como referência para sabermos
    # qual deveria ser o resultado correto.
    esperado = np.mean(dados)

    # np.isclose verifica se os dois números são suficientemente
    # próximos considerando as tolerâncias RTOL e ATOL.
    #
    # assert exige que essa condição seja verdadeira.
    # "assert" pode ser entendido como: "Eu afirmo que esta condição precisa ser verdadeira."
    # Se for verdadeira -> teste PASSED.
    # Se for falsa     -> teste FAILED.
        
    assert np.isclose(
        resultado,
        esperado,
        rtol=RTOL,
        atol=ATOL
    )


def test_media_valores_decimais():
    """
    Verifica se nossa média funciona também com números decimais.
    """

    # Dados contendo valores do tipo float (decimal).
    dados = [1.5, 2.7, 3.2, 4.8, 5.1]

    # Resultado calculado pela nossa biblioteca.
    resultado = media(dados)

    # Resultado de referência calculado pelo NumPy.
    esperado = np.mean(dados)

    # Compara os dois resultados respeitando a tolerância.
    assert np.isclose(
        resultado,
        esperado,
        rtol=RTOL,
        atol=ATOL
    )


def test_media_valores_negativos():
    """
    Verifica se a média funciona corretamente com
    números negativos.
    """

    # Dados contendo números negativos, zero e positivos.
    dados = [-10, -5, 0, 5, 10]

    # Nossa implementação.
    resultado = media(dados)

    # Referência NumPy.
    esperado = np.mean(dados)

    # Compara os resultados.
    assert np.isclose(
        resultado,
        esperado,
        rtol=RTOL,
        atol=ATOL
    )


# ============================================================
# TESTES DA MEDIANA
# ============================================================


def test_mediana_quantidade_impar():
    """
    Testa a mediana quando temos uma quantidade ímpar
    de elementos.
    """

    # Existem cinco elementos.
    dados = [10, 20, 20, 30, 40]

    # Calcula usando nossa função.
    resultado = mediana(dados)

    # Calcula usando NumPy somente como referência.
    esperado = np.median(dados)

    # Verifica se os resultados são equivalentes.
    assert np.isclose(
        resultado,
        esperado,
        rtol=RTOL,
        atol=ATOL
    )


def test_mediana_quantidade_par():
    """
    Testa a mediana quando temos uma quantidade par
    de elementos.
    """

    # Existem quatro elementos.
    dados = [10, 20, 30, 40]

    # Nossa função deverá calcular a média dos dois
    # valores centrais: 20 e 30.
    #
    # Portanto:
    # (20 + 30) / 2 = 25
    resultado = mediana(dados)

    # NumPy fornece o valor de referência.
    esperado = np.median(dados)

    # Compara os resultados.
    assert np.isclose(
        resultado,
        esperado,
        rtol=RTOL,
        atol=ATOL
    )


def test_mediana_dados_desordenados():
    """
    Confirma que a função consegue calcular a mediana
    mesmo quando os dados não estão ordenados.
    """

    # Observe que os números estão fora de ordem.
    dados = [50, 10, 40, 20, 30]

    # Nossa função mediana cria internamente uma versão
    # ordenada desses valores.
    resultado = mediana(dados)

    # Resultado de referência.
    esperado = np.median(dados)

    # Compara os dois resultados.
    assert np.isclose(
        resultado,
        esperado,
        rtol=RTOL,
        atol=ATOL
    )


# ============================================================
# TESTES DA MODA
# ============================================================


def test_moda_unica():
    """
    Testa um conjunto que possui somente uma moda.
    """

    # O número 20 aparece duas vezes.
    # Todos os demais aparecem apenas uma vez.
    dados = [10, 20, 20, 30, 40]

    # Executa nossa função.
    resultado = moda(dados)

    # Esperamos receber uma lista contendo somente 20.
    assert resultado == [20]


def test_moda_multimodal():
    """
    Testa um conjunto que possui mais de uma moda.
    """

    # 10 aparece duas vezes.
    # 20 também aparece duas vezes.
    #
    # Portanto temos duas modas.
    dados = [10, 10, 20, 20, 30]

    # Executa nossa função.
    resultado = moda(dados)

    # A função deve retornar as duas modas.
    assert resultado == [10, 20]


def test_moda_amodal():
    """
    Testa nossa convenção para um conjunto sem moda.

    Neste projeto consideramos amodal o conjunto em que
    nenhum valor se repete.
    """

    # Cada número aparece exatamente uma vez.
    dados = [10, 20, 30, 40]

    # Executa nossa função.
    resultado = moda(dados)

    # Nossa convenção é retornar uma lista vazia.
    assert resultado == []


# ============================================================
# TESTES DA AMPLITUDE
# ============================================================


def test_amplitude_valores_positivos():
    """
    Testa a amplitude utilizando números positivos.
    """

    dados = [10, 20, 20, 30, 40]

    # Nossa função calcula:
    #
    # maior valor - menor valor
    #
    # 40 - 10 = 30
    resultado = amplitude(dados)

    # NumPy é usado para encontrar o resultado de referência.
    esperado = np.max(dados) - np.min(dados)

    # Compara os resultados.
    assert np.isclose(
        resultado,
        esperado,
        rtol=RTOL,
        atol=ATOL
    )


def test_amplitude_com_valores_negativos():
    """
    Verifica se a amplitude funciona quando existem
    números negativos.
    """

    dados = [-20, -10, 0, 15, 30]

    # Nossa função deverá calcular:
    #
    # 30 - (-20)
    #
    # que resulta em 50.
    resultado = amplitude(dados)

    # Resultado de referência calculado com NumPy.
    esperado = np.max(dados) - np.min(dados)

    # Compara os resultados.
    assert np.isclose(
        resultado,
        esperado,
        rtol=RTOL,
        atol=ATOL
    )


def test_amplitude_valores_iguais():
    """
    Verifica a amplitude quando todos os valores
    são iguais.
    """

    dados = [5, 5, 5, 5]

    # Como:
    #
    # maior = 5
    # menor = 5
    #
    # amplitude = 5 - 5 = 0
    resultado = amplitude(dados)

    # Verifica diretamente se o resultado é zero.
    assert resultado == 0


# ============================================================
# TESTES DAS VALIDAÇÕES
# ============================================================


def test_lista_vazia_media():
    """
    Verifica se nossa biblioteca rejeita uma lista vazia.
    """

    # pytest.raises informa que ESPERAMOS que determinada
    # exceção aconteça.
    #
    # Nossa função _validar_dados deve gerar ValueError
    # quando receber uma coleção vazia.
    
    # Execute media([]) e o teste somente será considerado correto se essa operação produzir um ValueError.
    with pytest.raises(ValueError):

        # Esta chamada deve provocar ValueError.
        media([])


def test_none_media():
    """
    Verifica o comportamento quando None é informado
    no lugar dos dados.
    """

    # Esperamos que nossa validação gere ValueError.
    with pytest.raises(ValueError):

        # None significa ausência de um valor/objeto.
        media(None)


def test_valor_nao_numerico():
    """
    Verifica se nossa biblioteca rejeita valores
    que não sejam numéricos.
    """

    # O valor "30" está entre aspas.
    #
    # Portanto ele é uma string (texto), e não o número 30.
    dados = [10, 20, "30", 40]

    # Nossa função de validação deve detectar isso
    # e gerar TypeError.
    with pytest.raises(TypeError):

        # Esta chamada deve provocar TypeError.
        media(dados)

# ============================================================
# TESTES DA VARIÂNCIA POPULACIONAL
# ============================================================

def test_variancia_populacional():
    """
    Compara nossa variância populacional com a implementação
    de referência do NumPy.
    """

    # Conjunto de dados utilizado no teste.
    dados = [10, 20, 30, 40, 50]

    # Calcula a variância usando NOSSA implementação.
    resultado = variancia_populacional(dados)

    # Calcula o valor de referência usando NumPy.
    #
    # ddof=0 significa que o divisor utilizado pelo NumPy
    # será N, correspondendo à variância populacional.
    esperado = np.var(dados, ddof=0)

    # Compara os resultados respeitando nossa tolerância
    # numérica definida no início do arquivo.
    assert np.isclose(
        resultado,
        esperado,
        rtol=RTOL,
        atol=ATOL
    )


def test_variancia_populacional_decimais():
    """
    Verifica a variância populacional com números decimais.
    """

    # Valores decimais para verificar se nossa função
    # também trabalha corretamente com float.
    dados = [1.5, 2.7, 3.2, 4.8, 5.1]

    # Resultado produzido pelo minhastats.py.
    resultado = variancia_populacional(dados)

    # Resultado utilizado como referência.
    esperado = np.var(dados, ddof=0)

    # Compara os dois resultados.
    assert np.isclose(
        resultado,
        esperado,
        rtol=RTOL,
        atol=ATOL
    )


# ============================================================
# TESTES DA VARIÂNCIA AMOSTRAL
# ============================================================

def test_variancia_amostral():
    """
    Compara nossa variância amostral com NumPy.
    """

    dados = [10, 20, 30, 40, 50]

    # Calcula usando nossa função.
    resultado = variancia_amostral(dados)

    # ddof=1 faz o NumPy utilizar n - 1 no denominador.
    #
    # Portanto, corresponde à variância AMOSTRAL.
    esperado = np.var(dados, ddof=1)

    # Compara os resultados.
    assert np.isclose(
        resultado,
        esperado,
        rtol=RTOL,
        atol=ATOL
    )


def test_variancia_amostral_negativos():
    """
    Verifica se a variância amostral funciona corretamente
    com números negativos.
    """

    dados = [-20, -10, 0, 10, 20]

    # Nossa implementação.
    resultado = variancia_amostral(dados)

    # Referência NumPy.
    esperado = np.var(dados, ddof=1)

    # Faz a comparação.
    assert np.isclose(
        resultado,
        esperado,
        rtol=RTOL,
        atol=ATOL
    )


def test_variancia_amostral_um_elemento():
    """
    Verifica a regra de que a variância amostral precisa
    possuir pelo menos dois valores.
    """

    # Esperamos que nossa função gere ValueError.
    #
    # Com apenas um elemento teríamos:
    #
    # n - 1 = 1 - 1 = 0
    #
    # e não podemos realizar divisão por zero.
    with pytest.raises(ValueError):

        # Esta chamada DEVE gerar o erro.
        variancia_amostral([10])


# ============================================================
# TESTES DO DESVIO PADRÃO POPULACIONAL
# ============================================================

def test_desvio_padrao_populacional():
    """
    Compara nosso desvio padrão populacional com NumPy.
    """

    dados = [10, 20, 30, 40, 50]

    # Resultado da nossa biblioteca.
    resultado = desvio_padrao_populacional(dados)

    # np.std calcula o desvio padrão.
    #
    # ddof=0 indica cálculo populacional.
    esperado = np.std(dados, ddof=0)

    # Compara os resultados.
    assert np.isclose(
        resultado,
        esperado,
        rtol=RTOL,
        atol=ATOL
    )


def test_desvio_padrao_populacional_decimais():
    """
    Testa o desvio padrão populacional com números decimais.
    """

    dados = [1.5, 2.7, 3.2, 4.8, 5.1]

    # Nossa implementação.
    resultado = desvio_padrao_populacional(dados)

    # Referência NumPy.
    esperado = np.std(dados, ddof=0)

    # Compara os resultados.
    assert np.isclose(
        resultado,
        esperado,
        rtol=RTOL,
        atol=ATOL
    )


# ============================================================
# TESTES DO DESVIO PADRÃO AMOSTRAL
# ============================================================

def test_desvio_padrao_amostral():
    """
    Compara nosso desvio padrão amostral com NumPy.
    """

    dados = [10, 20, 30, 40, 50]

    # Resultado produzido pela nossa função.
    resultado = desvio_padrao_amostral(dados)

    # ddof=1 representa o cálculo amostral.
    esperado = np.std(dados, ddof=1)

    # Compara os resultados.
    assert np.isclose(
        resultado,
        esperado,
        rtol=RTOL,
        atol=ATOL
    )


def test_desvio_padrao_amostral_negativos():
    """
    Verifica o desvio padrão amostral com valores negativos.
    """

    dados = [-20, -10, 0, 10, 20]

    # Nossa implementação.
    resultado = desvio_padrao_amostral(dados)

    # Referência NumPy.
    esperado = np.std(dados, ddof=1)

    # Compara os resultados.
    assert np.isclose(
        resultado,
        esperado,
        rtol=RTOL,
        atol=ATOL
    )


def test_desvio_padrao_amostral_um_elemento():
    """
    Verifica se o desvio padrão amostral também rejeita
    conjuntos contendo somente um elemento.
    """

    # Nossa função desvio_padrao_amostral chama internamente
    # variancia_amostral.
    #
    # Portanto, ela também deverá gerar ValueError.
    with pytest.raises(ValueError):

        desvio_padrao_amostral([10])

# ============================================================
# TESTES DE PERCENTIL
# ============================================================

def test_percentil_25():
    """
    Compara o percentil 25 calculado por nossa biblioteca
    com o resultado de referência do NumPy.
    """

    dados = [10, 20, 30, 40, 50]

    # Calcula utilizando NOSSA implementação.
    resultado = percentil(dados, 25)

    # NumPy é utilizado SOMENTE como referência para o teste.
    #
    # method="linear" é importante porque nossa função
    # percentil() implementa manualmente esse mesmo método
    # de interpolação.
    esperado = np.percentile(dados, 25, method="linear")

    # Compara os valores considerando nossa tolerância numérica.
    assert np.isclose(
        resultado,
        esperado,
        rtol=RTOL,
        atol=ATOL
    )


def test_percentil_50():
    """
    Verifica o percentil 50.

    O percentil 50 corresponde também à mediana.
    """

    dados = [10, 20, 30, 40, 50]

    resultado = percentil(dados, 50)

    esperado = np.percentile(
        dados,
        50,
        method="linear"
    )

    assert np.isclose(
        resultado,
        esperado,
        rtol=RTOL,
        atol=ATOL
    )


def test_percentil_75():
    """
    Verifica o percentil 75.
    """

    dados = [10, 20, 30, 40, 50]

    resultado = percentil(dados, 75)

    esperado = np.percentile(
        dados,
        75,
        method="linear"
    )

    assert np.isclose(
        resultado,
        esperado,
        rtol=RTOL,
        atol=ATOL
    )


def test_percentil_com_interpolacao():
    """
    Testa um caso em que a posição do percentil não é inteira.

    Para:
        dados = [10, 20, 30, 40]

    o percentil 25 deverá resultar em 17.5.
    """

    dados = [10, 20, 30, 40]

    resultado = percentil(dados, 25)

    esperado = np.percentile(
        dados,
        25,
        method="linear"
    )

    assert np.isclose(
        resultado,
        esperado,
        rtol=RTOL,
        atol=ATOL
    )


def test_percentil_dados_desordenados():
    """
    Verifica se nossa função funciona quando os valores
    recebidos não estão previamente ordenados.

    A própria função percentil() deve ordenar os dados.
    """

    dados = [50, 10, 40, 20, 30]

    resultado = percentil(dados, 25)

    esperado = np.percentile(
        dados,
        25,
        method="linear"
    )

    assert np.isclose(
        resultado,
        esperado,
        rtol=RTOL,
        atol=ATOL
    )


def test_percentil_zero():
    """
    O percentil zero deve corresponder ao menor valor
    do conjunto de dados.
    """

    dados = [30, 10, 50, 20, 40]

    resultado = percentil(dados, 0)

    esperado = np.percentile(
        dados,
        0,
        method="linear"
    )

    assert np.isclose(
        resultado,
        esperado,
        rtol=RTOL,
        atol=ATOL
    )


def test_percentil_cem():
    """
    O percentil 100 deve corresponder ao maior valor
    do conjunto de dados.
    """

    dados = [30, 10, 50, 20, 40]

    resultado = percentil(dados, 100)

    esperado = np.percentile(
        dados,
        100,
        method="linear"
    )

    assert np.isclose(
        resultado,
        esperado,
        rtol=RTOL,
        atol=ATOL
    )


def test_percentil_abaixo_de_zero():
    """
    Percentis menores que zero são inválidos.

    Nossa função deverá gerar ValueError.
    """

    dados = [10, 20, 30, 40, 50]

    with pytest.raises(ValueError):
        percentil(dados, -1)


def test_percentil_acima_de_cem():
    """
    Percentis maiores que 100 também são inválidos.
    """

    dados = [10, 20, 30, 40, 50]

    with pytest.raises(ValueError):
        percentil(dados, 101)


def test_percentil_nao_numerico():
    """
    O percentual precisa ser um número.

    Portanto, passar uma string deverá gerar TypeError.
    """

    dados = [10, 20, 30, 40, 50]

    with pytest.raises(TypeError):
        percentil(dados, "25")

# ============================================================
# TESTES DOS QUARTIS
# ============================================================

def test_quartis():
    """
    Compara Q1, Q2 e Q3 calculados pela nossa biblioteca
    com os percentis 25, 50 e 75 do NumPy.
    """

    dados = [10, 20, 30, 40, 50]

    # Nossa função retorna uma tupla:
    #
    # (Q1, Q2, Q3)
    q1, q2, q3 = quartis(dados)

    # NumPy é usado apenas para obter os valores
    # de referência dos três quartis.
    esperado_q1 = np.percentile(
        dados,
        25,
        method="linear"
    )

    esperado_q2 = np.percentile(
        dados,
        50,
        method="linear"
    )

    esperado_q3 = np.percentile(
        dados,
        75,
        method="linear"
    )

    # Compara Q1.
    assert np.isclose(
        q1,
        esperado_q1,
        rtol=RTOL,
        atol=ATOL
    )

    # Compara Q2.
    assert np.isclose(
        q2,
        esperado_q2,
        rtol=RTOL,
        atol=ATOL
    )

    # Compara Q3.
    assert np.isclose(
        q3,
        esperado_q3,
        rtol=RTOL,
        atol=ATOL
    )


def test_quartis_com_interpolacao():
    """
    Verifica os quartis em um conjunto que exige
    interpolação linear.
    """

    dados = [10, 20, 30, 40]

    q1, q2, q3 = quartis(dados)

    esperado_q1 = np.percentile(
        dados,
        25,
        method="linear"
    )

    esperado_q2 = np.percentile(
        dados,
        50,
        method="linear"
    )

    esperado_q3 = np.percentile(
        dados,
        75,
        method="linear"
    )

    assert np.isclose(q1, esperado_q1, rtol=RTOL, atol=ATOL)
    assert np.isclose(q2, esperado_q2, rtol=RTOL, atol=ATOL)
    assert np.isclose(q3, esperado_q3, rtol=RTOL, atol=ATOL)


def test_quartis_dados_desordenados():
    """
    Confirma que os quartis também funcionam com
    dados fornecidos fora de ordem.
    """

    dados = [50, 10, 40, 20, 30]

    q1, q2, q3 = quartis(dados)

    esperado_q1 = np.percentile(dados, 25, method="linear")
    esperado_q2 = np.percentile(dados, 50, method="linear")
    esperado_q3 = np.percentile(dados, 75, method="linear")

    assert np.isclose(q1, esperado_q1, rtol=RTOL, atol=ATOL)
    assert np.isclose(q2, esperado_q2, rtol=RTOL, atol=ATOL)
    assert np.isclose(q3, esperado_q3, rtol=RTOL, atol=ATOL)

# ============================================================
# TESTES DO COEFICIENTE DE VARIAÇÃO
# ============================================================

def test_coeficiente_variacao():
    """
    Compara o coeficiente de variação calculado pela nossa
    biblioteca com um resultado de referência do NumPy.
    """

    # Conjunto de dados utilizado no teste.
    dados = [10, 20, 30, 40, 50]

    # Calcula o CV utilizando NOSSA função.
    resultado = coeficiente_variacao(dados)

    # NumPy é utilizado somente como referência.
    media_numpy = np.mean(dados)

    # ddof=1 indica desvio padrão amostral.
    desvio_numpy = np.std(dados, ddof=1)

    # Calcula o CV esperado.
    esperado = (desvio_numpy / abs(media_numpy)) * 100

    # Compara nosso resultado com o valor de referência.
    assert np.isclose(
        resultado,
        esperado,
        rtol=RTOL,
        atol=ATOL
    )


def test_coeficiente_variacao_baixa_dispersao():
    """
    Testa valores muito próximos da média.

    Neste caso esperamos um coeficiente de variação baixo.
    """

    dados = [98, 99, 100, 101, 102]

    # Resultado da nossa biblioteca.
    resultado = coeficiente_variacao(dados)

    # Valores de referência calculados pelo NumPy.
    media_numpy = np.mean(dados)
    desvio_numpy = np.std(dados, ddof=1)

    # CV utilizado como referência.
    esperado = (desvio_numpy / abs(media_numpy)) * 100

    # Compara os resultados.
    assert np.isclose(
        resultado,
        esperado,
        rtol=RTOL,
        atol=ATOL
    )


def test_coeficiente_variacao_media_zero():
    """
    Verifica o comportamento quando a média é zero.

    Como não podemos dividir por zero, nossa função deverá
    gerar ValueError.
    """

    dados = [-10, 0, 10]

    # Esperamos propositalmente um ValueError.
    with pytest.raises(ValueError):
        coeficiente_variacao(dados)


def test_coeficiente_variacao_um_elemento():
    """
    Verifica o comportamento com apenas um elemento.

    Como utilizamos desvio padrão amostral, precisamos
    de pelo menos dois valores.
    """

    dados = [10]

    # A função deverá gerar ValueError.
    with pytest.raises(ValueError):
        coeficiente_variacao(dados)


def test_coeficiente_variacao_dados_decimais():
    """
    Verifica o cálculo do CV utilizando valores decimais.
    """

    dados = [10.5, 12.7, 15.2, 17.8, 20.1]

    # Calcula utilizando nossa biblioteca.
    resultado = coeficiente_variacao(dados)

    # Calcula os valores de referência utilizando NumPy.
    media_numpy = np.mean(dados)
    desvio_numpy = np.std(dados, ddof=1)

    # Calcula o resultado esperado.
    esperado = (desvio_numpy / abs(media_numpy)) * 100

    # Compara os resultados considerando nossa
    # tolerância numérica.
    assert np.isclose(
        resultado,
        esperado,
        rtol=RTOL,
        atol=ATOL
    )

    # ============================================================
# TESTES DA COVARIÂNCIA
# ============================================================
#
# Estes testes verificam as funções:
#
#   covariancia_populacional()
#   covariancia_amostral()
#
# implementadas no arquivo minhastats.py.
#
# IMPORTANTE:
# O NumPy será utilizado SOMENTE como referência para validar
# os resultados da nossa implementação.
#
# O cálculo apresentado pela aplicação continuará sendo feito
# pela nossa biblioteca minhastats.py.
# ============================================================


def test_covariancia_populacional():
    """
    Verifica a covariância populacional utilizando dados
    com relação positiva perfeita.
    """

    # Importamos nossa função.
    from minhastats import covariancia_populacional

    # Primeira variável.
    dados_x = [10, 20, 30, 40, 50]

    # Segunda variável.
    # Observe que Y é exatamente duas vezes X.
    dados_y = [20, 40, 60, 80, 100]

    # Calculamos usando nossa implementação.
    resultado = covariancia_populacional(dados_x, dados_y)

    # Calculamos o valor de referência usando NumPy.
    #
    # np.cov() retorna uma matriz de covariância:
    #
    #          X       Y
    # X      var(X)  cov(X,Y)
    # Y      cov(Y,X) var(Y)
    #
    # Por isso usamos [0, 1] para obter a covariância
    # entre X e Y.
    #
    # ddof=0 determina o cálculo POPULACIONAL.
    esperado = np.cov(dados_x, dados_y, ddof=0)[0, 1]

    # np.isclose compara números decimais considerando
    # uma pequena tolerância numérica.
    assert np.isclose(resultado, esperado)


def test_covariancia_amostral():
    """
    Verifica a covariância amostral.
    """

    from minhastats import covariancia_amostral

    dados_x = [10, 20, 30, 40, 50]
    dados_y = [20, 40, 60, 80, 100]

    # Resultado produzido por nossa função.
    resultado = covariancia_amostral(dados_x, dados_y)

    # ddof=1 corresponde à covariância AMOSTRAL,
    # ou seja, utiliza n - 1 no denominador.
    esperado = np.cov(dados_x, dados_y, ddof=1)[0, 1]

    assert np.isclose(resultado, esperado)


def test_covariancia_negativa():
    """
    Verifica se nossa função identifica corretamente
    uma covariância negativa.
    """

    from minhastats import covariancia_populacional

    # X cresce...
    dados_x = [1, 2, 3, 4, 5]

    # ...enquanto Y diminui.
    dados_y = [10, 8, 6, 4, 2]

    resultado = covariancia_populacional(dados_x, dados_y)

    esperado = np.cov(dados_x, dados_y, ddof=0)[0, 1]

    # Compara com NumPy.
    assert np.isclose(resultado, esperado)

    # Além disso, confirmamos que o resultado é negativo.
    assert resultado < 0


def test_covariancia_zero():
    """
    Verifica um caso em que a covariância é zero.
    """

    from minhastats import covariancia_populacional

    dados_x = [1, 2, 3, 4, 5]

    # Y é constante.
    #
    # Como todos os valores de Y são iguais à sua média,
    # todos os desvios de Y serão zero.
    dados_y = [10, 10, 10, 10, 10]

    resultado = covariancia_populacional(dados_x, dados_y)

    esperado = np.cov(dados_x, dados_y, ddof=0)[0, 1]

    assert np.isclose(resultado, esperado)

    # Neste exemplo esperamos exatamente zero.
    assert np.isclose(resultado, 0.0)


def test_covariancia_dados_decimais():
    """
    Verifica se a função trabalha corretamente
    com números decimais.
    """

    from minhastats import covariancia_populacional

    dados_x = [1.5, 2.7, 3.2, 4.8, 5.1]
    dados_y = [2.2, 3.1, 4.6, 5.3, 6.7]

    resultado = covariancia_populacional(dados_x, dados_y)

    esperado = np.cov(dados_x, dados_y, ddof=0)[0, 1]

    assert np.isclose(resultado, esperado)


def test_covariancia_tamanhos_diferentes():
    """
    Verifica se a função impede o cálculo quando X e Y
    possuem quantidades diferentes de elementos.
    """

    from minhastats import covariancia_populacional

    dados_x = [10, 20, 30]
    dados_y = [10, 20]

    # pytest.raises informa ao pytest que esperamos
    # propositalmente uma exceção ValueError.
    with pytest.raises(ValueError):
        covariancia_populacional(dados_x, dados_y)


def test_covariancia_amostral_um_elemento():
    """
    A covariância amostral precisa de pelo menos
    dois pares de observações, pois divide por n - 1.
    """

    from minhastats import covariancia_amostral

    dados_x = [10]
    dados_y = [20]

    # Nossa função deve rejeitar esse cálculo.
    with pytest.raises(ValueError):
        covariancia_amostral(dados_x, dados_y)

# ============================================================
# TESTES - COEFICIENTE DE CORRELACAO DE PEARSON
# ============================================================
#
# O coeficiente de correlacao de Pearson mede a intensidade
# e a direcao da relacao LINEAR entre duas variaveis.
#
# Seu valor varia entre -1 e +1:
#
#   r = +1  -> correlacao positiva perfeita
#   r =  0  -> ausencia de correlacao linear
#   r = -1  -> correlacao negativa perfeita
#
# IMPORTANTE:
# Correlacao nao implica causalidade.
#
# Nestes testes utilizamos pytest.approx() porque calculos com
# numeros de ponto flutuante podem apresentar pequenas diferencas.
# ============================================================


def test_correlacao_pearson_positiva_perfeita():
    """
    Testa duas variaveis com correlacao positiva perfeita.
    """

    # Primeira variavel.
    dados_x = [10, 20, 30, 40, 50]

    # Segunda variavel.
    # Y cresce proporcionalmente a X.
    dados_y = [20, 40, 60, 80, 100]

    # Calcula a correlacao usando NOSSA biblioteca.
    resultado = correlacao_pearson(dados_x, dados_y)

    # Uma relacao linear positiva perfeita deve produzir r = 1.
    assert resultado == pytest.approx(1.0, abs=1e-10)


def test_correlacao_pearson_negativa_perfeita():
    """
    Testa duas variaveis com correlacao negativa perfeita.
    """

    dados_x = [1, 2, 3, 4, 5]

    # Enquanto X aumenta, Y diminui linearmente.
    dados_y = [10, 8, 6, 4, 2]

    resultado = correlacao_pearson(dados_x, dados_y)

    # Esperamos r = -1.
    assert resultado == pytest.approx(-1.0, abs=1e-10)


def test_correlacao_pearson_positiva_nao_perfeita():
    """
    Testa uma correlacao positiva que nao e perfeita.
    """

    # Conjunto de valores da primeira variavel.
    dados_x = [1, 2, 3, 4, 5]

    # Conjunto de valores da segunda variavel.
    # Existe uma tendencia de crescimento,
    # mas ela nao e perfeitamente linear.
    dados_y = [2, 3, 5, 4, 8]

    # Calcula o coeficiente de correlacao de Pearson
    # utilizando nossa funcao.
    resultado = correlacao_pearson(dados_x, dados_y)

    # Valor correto esperado para esses dois conjuntos.
    esperado = 0.8928436656664787

    # Compara o resultado calculado com o esperado.
    assert resultado == pytest.approx(
        esperado,
        abs=1e-10
    )


def test_correlacao_pearson_tamanhos_diferentes():
    """
    Verifica se a funcao rejeita conjuntos de tamanhos diferentes.
    """

    dados_x = [10, 20, 30]
    dados_y = [10, 20]

    # Nossa funcao deve gerar ValueError.
    with pytest.raises(ValueError):
        correlacao_pearson(dados_x, dados_y)


def test_correlacao_pearson_desvio_zero():
    """
    Verifica o comportamento quando uma variavel e constante.

    Uma variavel constante possui desvio padrao igual a zero.
    Nesse caso, a correlacao de Pearson nao pode ser calculada.
    """

    # Todos os valores de X sao iguais.
    dados_x = [10, 10, 10, 10, 10]

    dados_y = [1, 2, 3, 4, 5]

    with pytest.raises(ValueError):
        correlacao_pearson(dados_x, dados_y)


def test_correlacao_pearson_dados_decimais():
    """
    Verifica se a funcao trabalha corretamente com numeros decimais.
    """

    dados_x = [1.5, 2.5, 3.5, 4.5, 5.5]
    dados_y = [3.0, 5.0, 7.0, 9.0, 11.0]

    resultado = correlacao_pearson(dados_x, dados_y)

    # Y = 2X, portanto existe correlacao positiva perfeita.
    assert resultado == pytest.approx(1.0, abs=1e-10)


# ============================================================
# TESTE DE VALIDACAO COM NUMPY
# ============================================================

def test_correlacao_pearson_comparacao_numpy():
    """
    Compara nossa implementacao da correlacao de Pearson
    com o resultado produzido pelo NumPy.

    O NumPy e usado SOMENTE como referencia para validacao.
    """

    # Importamos o NumPy para calcular o valor de referencia.
    import numpy as np

    # Dados utilizados na comparacao.
    dados_x = [12, 15, 18, 22, 25, 30, 35]
    dados_y = [20, 24, 27, 31, 36, 40, 48]

    # Calcula a correlacao usando NOSSA implementacao.
    resultado_nosso = correlacao_pearson(dados_x, dados_y)

    # Calcula o mesmo valor utilizando NumPy.
    # [0, 1] representa a correlacao entre X e Y.
    resultado_numpy = np.corrcoef(dados_x, dados_y)[0, 1]

    # Compara os dois resultados.
    #
    # abs=1e-10 significa que aceitamos apenas uma diferenca
    # numerica extremamente pequena entre os resultados.
    assert resultado_nosso == pytest.approx(
        resultado_numpy,
        abs=1e-10
    )

# ============================================================
# VALIDACAO DO NUCLEO ESTATISTICO CONTRA NUMPY
# ============================================================
#
# Estes testes existem para atender diretamente ao requisito:
#
# "Cada funcao deve ser validada com testes automatizados
# comparando o resultado com NumPy/SciPy."
#
# IMPORTANTE:
#
# NumPy e utilizado SOMENTE como referencia nos testes.
# A aplicacao utiliza as funcoes implementadas em minhastats.py.
#
# TOLERANCIA NUMERICA:
#
# Para resultados de ponto flutuante adotamos:
#
#     abs = 1e-10
#
# Ou seja, aceitamos diferencas absolutas menores ou iguais
# a 0.0000000001, decorrentes da representacao de numeros
# reais em ponto flutuante.
# ============================================================


def test_validacao_media_numpy():
    """Compara nossa media com numpy.mean()."""

    dados = [10, 15, 22, 30, 41, 53]

    resultado_nosso = media(dados)
    resultado_numpy = np.mean(dados)

    assert resultado_nosso == pytest.approx(
        resultado_numpy,
        abs=1e-10
    )


def test_validacao_mediana_numpy():
    """Compara nossa mediana com numpy.median()."""

    dados = [7, 15, 3, 22, 11, 19]

    resultado_nosso = mediana(dados)
    resultado_numpy = np.median(dados)

    assert resultado_nosso == pytest.approx(
        resultado_numpy,
        abs=1e-10
    )


def test_validacao_amplitude_numpy():
    """
    Compara nossa amplitude com a diferenca entre
    o maior e o menor valor calculados pelo NumPy.
    """

    dados = [5, 12, 18, 27, 44, 61]

    resultado_nosso = amplitude(dados)

    resultado_numpy = np.max(dados) - np.min(dados)

    assert resultado_nosso == pytest.approx(
        resultado_numpy,
        abs=1e-10
    )


def test_validacao_variancia_populacional_numpy():
    """Compara nossa variancia populacional com numpy.var()."""

    dados = [12, 18, 25, 31, 42, 56]

    resultado_nosso = variancia_populacional(dados)

    # ddof=0 -> variancia populacional
    resultado_numpy = np.var(dados, ddof=0)

    assert resultado_nosso == pytest.approx(
        resultado_numpy,
        abs=1e-10
    )


def test_validacao_variancia_amostral_numpy():
    """Compara nossa variancia amostral com numpy.var()."""

    dados = [12, 18, 25, 31, 42, 56]

    resultado_nosso = variancia_amostral(dados)

    # ddof=1 -> variancia amostral
    resultado_numpy = np.var(dados, ddof=1)

    assert resultado_nosso == pytest.approx(
        resultado_numpy,
        abs=1e-10
    )


def test_validacao_desvio_padrao_populacional_numpy():
    """
    Compara nosso desvio padrao populacional
    com numpy.std().
    """

    dados = [8, 14, 21, 29, 38, 50]

    resultado_nosso = desvio_padrao_populacional(dados)

    # ddof=0 -> populacional
    resultado_numpy = np.std(dados, ddof=0)

    assert resultado_nosso == pytest.approx(
        resultado_numpy,
        abs=1e-10
    )


def test_validacao_desvio_padrao_amostral_numpy():
    """
    Compara nosso desvio padrao amostral
    com numpy.std().
    """

    dados = [8, 14, 21, 29, 38, 50]

    resultado_nosso = desvio_padrao_amostral(dados)

    # ddof=1 -> amostral
    resultado_numpy = np.std(dados, ddof=1)

    assert resultado_nosso == pytest.approx(
        resultado_numpy,
        abs=1e-10
    )

def test_validacao_moda_scipy():
    """
    Compara nossa moda com scipy.stats.mode().

    SciPy e utilizado somente como referencia de validacao.
    """

    from scipy import stats

    dados = [10, 20, 20, 20, 30, 40, 50]

    resultado_nosso = moda(dados)

    resultado_scipy = stats.mode(
        dados,
        keepdims=False
    ).mode

    # Nossa funcao moda retorna uma lista, pois pode existir
    # mais de uma moda.
    #
    # Neste conjunto existe somente uma moda: 20.
    assert resultado_nosso[0] == resultado_scipy

    # ============================================================
# SEGUNDO BLOCO DE VALIDACAO CONTRA NUMPY
# ============================================================
#
# Este bloco valida:
#
#   - Percentil
#   - Quartis
#   - Coeficiente de variacao
#   - Covariancia populacional
#   - Covariancia amostral
#
# O NumPy e utilizado SOMENTE como biblioteca de referencia.
#
# Os calculos da aplicacao continuam sendo realizados pelas
# funcoes implementadas em minhastats.py.
#
# Tolerancia numerica adotada:
#
#       abs = 1e-10
#
# Isso significa que pequenas diferencas provocadas pela
# representacao de numeros de ponto flutuante sao aceitas
# ate o limite de 0.0000000001.
# ============================================================


def test_validacao_percentil_25_numpy():
    """
    Compara nosso percentil de 25% com numpy.percentile().
    """

    dados = [10, 20, 30, 40, 50, 60, 70]

    # Resultado produzido pela nossa biblioteca.
    resultado_nosso = percentil(dados, 25)

    # Resultado de referencia produzido pelo NumPy.
    resultado_numpy = np.percentile(dados, 25)

    # Compara os dois resultados utilizando tolerancia numerica.
    assert resultado_nosso == pytest.approx(
        resultado_numpy,
        abs=1e-10
    )


def test_validacao_percentil_50_numpy():
    """
    Compara nosso percentil de 50% com NumPy.

    O percentil 50 corresponde tambem a mediana.
    """

    dados = [5, 12, 18, 25, 31, 44, 60, 75]

    resultado_nosso = percentil(dados, 50)

    resultado_numpy = np.percentile(dados, 50)

    assert resultado_nosso == pytest.approx(
        resultado_numpy,
        abs=1e-10
    )


def test_validacao_percentil_75_numpy():
    """
    Compara nosso percentil de 75% com NumPy.
    """

    dados = [3, 8, 15, 21, 29, 35, 42, 50]

    resultado_nosso = percentil(dados, 75)

    resultado_numpy = np.percentile(dados, 75)

    assert resultado_nosso == pytest.approx(
        resultado_numpy,
        abs=1e-10
    )


# ============================================================
# VALIDACAO DOS QUARTIS
# ============================================================

def test_validacao_quartis_numpy():
    """
    Compara Q1, Q2 e Q3 calculados pela nossa funcao quartis()
    com os percentis 25, 50 e 75 calculados pelo NumPy.
    """

    dados = [4, 9, 15, 20, 27, 33, 41, 48, 55]

    # Nossa funcao retorna tres valores:
    #
    # Q1 = primeiro quartil
    # Q2 = segundo quartil / mediana
    # Q3 = terceiro quartil
    q1_nosso, q2_nosso, q3_nosso = quartis(dados)

    # Calculamos os valores equivalentes utilizando NumPy.
    q1_numpy = np.percentile(dados, 25)
    q2_numpy = np.percentile(dados, 50)
    q3_numpy = np.percentile(dados, 75)

    # Validamos cada quartil separadamente.
    assert q1_nosso == pytest.approx(
        q1_numpy,
        abs=1e-10
    )

    assert q2_nosso == pytest.approx(
        q2_numpy,
        abs=1e-10
    )

    assert q3_nosso == pytest.approx(
        q3_numpy,
        abs=1e-10
    )


# ============================================================
# VALIDACAO DO COEFICIENTE DE VARIACAO
# ============================================================

def test_validacao_coeficiente_variacao_numpy():
    """
    Compara nosso coeficiente de variacao com um valor
    de referencia calculado a partir de NumPy.

    Formula:

        CV = (desvio padrao amostral / media) * 100
    """

    dados = [15, 22, 28, 35, 41, 50]

    # Resultado produzido por nossa biblioteca.
    resultado_nosso = coeficiente_variacao(dados)

    # Calculamos a media utilizando NumPy.
    media_numpy = np.mean(dados)

    # Calculamos o desvio padrao AMOSTRAL.
    #
    # ddof=1 significa que o denominador utilizado pelo NumPy
    # sera n - 1.
    desvio_numpy = np.std(dados, ddof=1)

    # Aplicamos a mesma formula do coeficiente de variacao.
    resultado_numpy = (
        desvio_numpy / media_numpy
    ) * 100

    # Comparamos nossa implementacao com a referencia.
    assert resultado_nosso == pytest.approx(
        resultado_numpy,
        abs=1e-10
    )


# ============================================================
# VALIDACAO DA COVARIANCIA POPULACIONAL
# ============================================================

def test_validacao_covariancia_populacional_numpy():
    """
    Compara nossa covariancia populacional com numpy.cov().
    """

    dados_x = [10, 20, 30, 40, 50]
    dados_y = [15, 25, 38, 46, 62]

    # Resultado calculado pela nossa biblioteca.
    resultado_nosso = covariancia_populacional(
        dados_x,
        dados_y
    )

    # np.cov() devolve uma matriz.
    #
    # bias=True faz o calculo populacional, utilizando n
    # no denominador.
    #
    # [0, 1] recupera a covariancia entre X e Y.
    resultado_numpy = np.cov(
        dados_x,
        dados_y,
        bias=True
    )[0, 1]

    assert resultado_nosso == pytest.approx(
        resultado_numpy,
        abs=1e-10
    )


# ============================================================
# VALIDACAO DA COVARIANCIA AMOSTRAL
# ============================================================

def test_validacao_covariancia_amostral_numpy():
    """
    Compara nossa covariancia amostral com numpy.cov().
    """

    dados_x = [10, 20, 30, 40, 50]
    dados_y = [15, 25, 38, 46, 62]

    resultado_nosso = covariancia_amostral(
        dados_x,
        dados_y
    )

    # bias=False corresponde ao calculo amostral,
    # utilizando n - 1 no denominador.
    resultado_numpy = np.cov(
        dados_x,
        dados_y,
        bias=False
    )[0, 1]

    assert resultado_nosso == pytest.approx(
        resultado_numpy,
        abs=1e-10
    )

    # ============================================================
# SEGUNDO BLOCO DE VALIDACAO CONTRA NUMPY
# ============================================================
#
# Este bloco valida:
#
#   - Percentil
#   - Quartis
#   - Coeficiente de variacao
#   - Covariancia populacional
#   - Covariancia amostral
#
# O NumPy e utilizado SOMENTE como biblioteca de referencia.
#
# Os calculos da aplicacao continuam sendo realizados pelas
# funcoes implementadas em minhastats.py.
#
# Tolerancia numerica adotada:
#
#       abs = 1e-10
#
# Isso significa que pequenas diferencas provocadas pela
# representacao de numeros de ponto flutuante sao aceitas
# ate o limite de 0.0000000001.
# ============================================================


def test_validacao_percentil_25_numpy():
    """
    Compara nosso percentil de 25% com numpy.percentile().
    """

    dados = [10, 20, 30, 40, 50, 60, 70]

    # Resultado produzido pela nossa biblioteca.
    resultado_nosso = percentil(dados, 25)

    # Resultado de referencia produzido pelo NumPy.
    resultado_numpy = np.percentile(dados, 25)

    # Compara os dois resultados utilizando tolerancia numerica.
    assert resultado_nosso == pytest.approx(
        resultado_numpy,
        abs=1e-10
    )


def test_validacao_percentil_50_numpy():
    """
    Compara nosso percentil de 50% com NumPy.

    O percentil 50 corresponde tambem a mediana.
    """

    dados = [5, 12, 18, 25, 31, 44, 60, 75]

    resultado_nosso = percentil(dados, 50)

    resultado_numpy = np.percentile(dados, 50)

    assert resultado_nosso == pytest.approx(
        resultado_numpy,
        abs=1e-10
    )


def test_validacao_percentil_75_numpy():
    """
    Compara nosso percentil de 75% com NumPy.
    """

    dados = [3, 8, 15, 21, 29, 35, 42, 50]

    resultado_nosso = percentil(dados, 75)

    resultado_numpy = np.percentile(dados, 75)

    assert resultado_nosso == pytest.approx(
        resultado_numpy,
        abs=1e-10
    )


# ============================================================
# VALIDACAO DOS QUARTIS
# ============================================================

def test_validacao_quartis_numpy():
    """
    Compara Q1, Q2 e Q3 calculados pela nossa funcao quartis()
    com os percentis 25, 50 e 75 calculados pelo NumPy.
    """

    dados = [4, 9, 15, 20, 27, 33, 41, 48, 55]

    # Nossa funcao retorna tres valores:
    #
    # Q1 = primeiro quartil
    # Q2 = segundo quartil / mediana
    # Q3 = terceiro quartil
    q1_nosso, q2_nosso, q3_nosso = quartis(dados)

    # Calculamos os valores equivalentes utilizando NumPy.
    q1_numpy = np.percentile(dados, 25)
    q2_numpy = np.percentile(dados, 50)
    q3_numpy = np.percentile(dados, 75)

    # Validamos cada quartil separadamente.
    assert q1_nosso == pytest.approx(
        q1_numpy,
        abs=1e-10
    )

    assert q2_nosso == pytest.approx(
        q2_numpy,
        abs=1e-10
    )

    assert q3_nosso == pytest.approx(
        q3_numpy,
        abs=1e-10
    )


# ============================================================
# VALIDACAO DO COEFICIENTE DE VARIACAO
# ============================================================

def test_validacao_coeficiente_variacao_numpy():
    """
    Compara nosso coeficiente de variacao com um valor
    de referencia calculado a partir de NumPy.

    Formula:

        CV = (desvio padrao amostral / media) * 100
    """

    dados = [15, 22, 28, 35, 41, 50]

    # Resultado produzido por nossa biblioteca.
    resultado_nosso = coeficiente_variacao(dados)

    # Calculamos a media utilizando NumPy.
    media_numpy = np.mean(dados)

    # Calculamos o desvio padrao AMOSTRAL.
    #
    # ddof=1 significa que o denominador utilizado pelo NumPy
    # sera n - 1.
    desvio_numpy = np.std(dados, ddof=1)

    # Aplicamos a mesma formula do coeficiente de variacao.
    resultado_numpy = (
        desvio_numpy / media_numpy
    ) * 100

    # Comparamos nossa implementacao com a referencia.
    assert resultado_nosso == pytest.approx(
        resultado_numpy,
        abs=1e-10
    )


# ============================================================
# VALIDACAO DA COVARIANCIA POPULACIONAL
# ============================================================

def test_validacao_covariancia_populacional_numpy():
    """
    Compara nossa covariancia populacional com numpy.cov().
    """

    dados_x = [10, 20, 30, 40, 50]
    dados_y = [15, 25, 38, 46, 62]

    # Resultado calculado pela nossa biblioteca.
    resultado_nosso = covariancia_populacional(
        dados_x,
        dados_y
    )

    # np.cov() devolve uma matriz.
    #
    # bias=True faz o calculo populacional, utilizando n
    # no denominador.
    #
    # [0, 1] recupera a covariancia entre X e Y.
    resultado_numpy = np.cov(
        dados_x,
        dados_y,
        bias=True
    )[0, 1]

    assert resultado_nosso == pytest.approx(
        resultado_numpy,
        abs=1e-10
    )


# ============================================================
# VALIDACAO DA COVARIANCIA AMOSTRAL
# ============================================================

def test_validacao_covariancia_amostral_numpy():
    """
    Compara nossa covariancia amostral com numpy.cov().
    """

    dados_x = [10, 20, 30, 40, 50]
    dados_y = [15, 25, 38, 46, 62]

    resultado_nosso = covariancia_amostral(
        dados_x,
        dados_y
    )

    # bias=False corresponde ao calculo amostral,
    # utilizando n - 1 no denominador.
    resultado_numpy = np.cov(
        dados_x,
        dados_y,
        bias=False
    )[0, 1]

    assert resultado_nosso == pytest.approx(
        resultado_numpy,
        abs=1e-10
    )

    # ============================================================
# TESTES - REGRESSAO LINEAR
# ============================================================
#
# Estes testes verificam a funcao regressao_linear().
#
# A regressao linear simples procura uma reta que represente
# a relacao entre duas variaveis X e Y.
#
# A equacao da reta possui a seguinte forma:
#
#     y = a + b*x
#
# onde:
#
#     a = intercepto da reta
#     b = coeficiente angular (inclinacao)
#
# Nossa funcao regressao_linear() retorna:
#
#     (intercepto, coeficiente_angular)
#
# ============================================================


def test_regressao_linear_positiva_perfeita():
    """
    Testa uma regressao linear positiva perfeita.

    Os valores de Y sao exatamente duas vezes os valores de X.

    Portanto:

        y = 2*x

    Logo:

        intercepto = 0
        coeficiente angular = 2
    """

    # Valores da variavel independente X.
    dados_x = [1, 2, 3, 4, 5]

    # Valores da variavel dependente Y.
    dados_y = [2, 4, 6, 8, 10]

    # Executamos nossa funcao de regressao linear.
    intercepto, coeficiente = regressao_linear(
        dados_x,
        dados_y
    )

    # O intercepto esperado e zero.
    assert intercepto == pytest.approx(
        0.0,
        abs=1e-10
    )

    # O coeficiente angular esperado e 2.
    assert coeficiente == pytest.approx(
        2.0,
        abs=1e-10
    )


def test_regressao_linear_com_intercepto():
    """
    Testa uma regressao linear cujo intercepto nao e zero.

    Os dados seguem exatamente:

        y = 1 + 2*x

    Portanto:

        intercepto = 1
        coeficiente angular = 2
    """

    # Valores de X.
    dados_x = [1, 2, 3, 4, 5]

    # Valores de Y.
    dados_y = [3, 5, 7, 9, 11]

    # Calculamos a regressao.
    intercepto, coeficiente = regressao_linear(
        dados_x,
        dados_y
    )

    # Verificamos o intercepto.
    assert intercepto == pytest.approx(
        1.0,
        abs=1e-10
    )

    # Verificamos a inclinacao da reta.
    assert coeficiente == pytest.approx(
        2.0,
        abs=1e-10
    )


def test_regressao_linear_negativa():
    """
    Testa uma regressao linear negativa.

    Neste exemplo, quando X aumenta, Y diminui.

    Os dados seguem:

        y = 6 - x

    Portanto:

        intercepto = 6
        coeficiente angular = -1
    """

    # Valores crescentes de X.
    dados_x = [1, 2, 3, 4, 5]

    # Valores decrescentes de Y.
    dados_y = [5, 4, 3, 2, 1]

    # Calculamos a regressao.
    intercepto, coeficiente = regressao_linear(
        dados_x,
        dados_y
    )

    # O intercepto esperado e 6.
    assert intercepto == pytest.approx(
        6.0,
        abs=1e-10
    )

    # O coeficiente negativo indica que Y diminui
    # quando X aumenta.
    assert coeficiente == pytest.approx(
        -1.0,
        abs=1e-10
    )


def test_regressao_linear_dados_decimais():
    """
    Testa a regressao linear utilizando valores decimais.

    Isso garante que nossa funcao nao funciona apenas
    com numeros inteiros.
    """

    # Valores decimais para X.
    dados_x = [1.5, 2.5, 3.5, 4.5, 5.5]

    # Utilizamos uma relacao linear exata:
    #
    #     y = 2*x + 1
    #
    dados_y = [4.0, 6.0, 8.0, 10.0, 12.0]

    # Calculamos a regressao.
    intercepto, coeficiente = regressao_linear(
        dados_x,
        dados_y
    )

    # O intercepto deve ser 1.
    assert intercepto == pytest.approx(
        1.0,
        abs=1e-10
    )

    # O coeficiente angular deve ser 2.
    assert coeficiente == pytest.approx(
        2.0,
        abs=1e-10
    )


def test_regressao_linear_tamanhos_diferentes():
    """
    Verifica se a funcao rejeita conjuntos X e Y
    que possuem quantidades diferentes de elementos.

    Cada valor X precisa possuir um valor Y correspondente.
    """

    # X possui cinco elementos.
    dados_x = [1, 2, 3, 4, 5]

    # Y possui somente quatro elementos.
    dados_y = [2, 4, 6, 8]

    # Esperamos que nossa funcao gere ValueError.
    with pytest.raises(ValueError):

        regressao_linear(
            dados_x,
            dados_y
        )


def test_regressao_linear_um_elemento():
    """
    Verifica o comportamento quando existe somente
    um par de observacoes.

    Uma regressao linear nao pode determinar a inclinacao
    de uma reta utilizando somente um ponto.
    """

    # Apenas uma observacao em X.
    dados_x = [10]

    # Apenas uma observacao correspondente em Y.
    dados_y = [20]

    # Esperamos ValueError.
    with pytest.raises(ValueError):

        regressao_linear(
            dados_x,
            dados_y
        )


def test_regressao_linear_x_sem_variacao():
    """
    Verifica o caso em que todos os valores de X sao iguais.

    Exemplo:

        X = [10, 10, 10, 10]

    Nesse caso nao existe variacao em X e, portanto,
    nao e possivel calcular corretamente a inclinacao
    da reta de regressao.
    """

    # Todos os valores de X sao iguais.
    dados_x = [10, 10, 10, 10]

    # Y possui valores diferentes.
    dados_y = [1, 2, 3, 4]

    # Nossa implementacao deve detectar esse problema
    # e gerar ValueError.
    with pytest.raises(ValueError):

        regressao_linear(
            dados_x,
            dados_y
        )


def test_regressao_linear_comparacao_numpy():
    """
    Valida nossa regressao linear comparando o resultado
    com uma implementacao de referencia do NumPy.

    O NumPy e utilizado SOMENTE para validacao.

    Nossa funcao continua realizando seus proprios
    calculos estatisticos.
    """

    # Importamos NumPy apenas dentro deste teste.
    import numpy as np

    # Dados utilizados para a comparacao.
    #
    # Desta vez propositalmente usamos dados que NAO
    # formam uma reta perfeita.
    dados_x = [10, 20, 30, 40, 50]

    dados_y = [15, 24, 38, 46, 62]

    # --------------------------------------------------------
    # Resultado da NOSSA biblioteca
    # --------------------------------------------------------

    # Calculamos intercepto e coeficiente utilizando
    # nossa propria funcao.
    intercepto_nosso, coeficiente_nosso = regressao_linear(
        dados_x,
        dados_y
    )

    # --------------------------------------------------------
    # Resultado de referencia utilizando NumPy
    # --------------------------------------------------------

    # np.polyfit(..., 1) calcula uma regressao
    # polinomial de grau 1, isto e, uma reta.
    #
    # O NumPy retorna:
    #
    #     coeficiente angular, intercepto
    #
    # Observe que a ordem e diferente da nossa funcao.
    coeficiente_numpy, intercepto_numpy = np.polyfit(
        dados_x,
        dados_y,
        1
    )

    # --------------------------------------------------------
    # Comparacao
    # --------------------------------------------------------

    # Comparamos nosso intercepto com o NumPy.
    assert intercepto_nosso == pytest.approx(
        intercepto_numpy,
        abs=1e-10
    )

    # Comparamos nosso coeficiente angular com o NumPy.
    assert coeficiente_nosso == pytest.approx(
        coeficiente_numpy,
        abs=1e-10
    )