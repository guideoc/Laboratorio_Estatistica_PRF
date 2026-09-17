# ============================================================
# LABORATÓRIO DE ESTATÍSTICA INTERATIVA
# Dataset: Acidentes PRF - 2025
# ============================================================

# Streamlit será responsável pela interface da aplicação.
import streamlit as st

# Pandas será utilizado para carregar e manipular o arquivo CSV.
# IMPORTANTE:
# Os cálculos estatísticos exibidos ao usuário NÃO serão feitos
# pelo Pandas. Posteriormente utilizaremos nosso minhastats.py.
import pandas as pd

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm


# ============================================================
# IMPORTAÇÃO DO NOSSO NÚCLEO ESTATÍSTICO
# ============================================================

# Estas funções foram implementadas por nós no Módulo 1.
# Elas serão responsáveis pelos valores estatísticos mostrados
# na aplicação.
#
# Portanto, NÃO utilizaremos comandos como:
# df["pessoas"].mean()
# df["pessoas"].median()
#
# para calcular as estatísticas apresentadas ao usuário.

from minhastats import (
    media,
    mediana,
    moda,
    amplitude,
    variancia_amostral,
    desvio_padrao_amostral,
    quartis,
    coeficiente_variacao,
    desvio_padrao_populacional,
    correlacao_pearson,
    regressao_linear
)


# ============================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================

st.set_page_config(
    page_title="Laboratório de Estatística - PRF 2025",
    layout="wide"
)


# ============================================================
# FUNÇÃO PARA CARREGAR O DATASET
# ============================================================

# @st.cache_data faz o Streamlit guardar o resultado da leitura
# do CSV em memória.
#
# Assim, sempre que o usuário mudar uma opção da tela,
# não será necessário ler novamente as 72 mil ocorrências.
@st.cache_data
def carregar_dados():

    # O arquivo da PRF possui algumas características:
    #
    # sep=";"
    # As colunas são separadas por ponto e vírgula.
    #
    # encoding="latin1"
    # Codificação utilizada no arquivo.
    #
    # decimal=","
    # Números decimais utilizam vírgula.
    dados = pd.read_csv(
        "data/datatran2025.csv",
        sep=";",
        encoding="latin1",
        decimal=","
    )

    return dados


# ============================================================
# CARREGAMENTO DOS DADOS
# ============================================================

df = carregar_dados()



# ============================================================
# NAVEGAÇÃO PRINCIPAL EM ABAS
# ============================================================
# A aplicação foi organizada em seis abas para facilitar a
# navegação, sem alterar os cálculos estatísticos existentes.

aba_inicio, aba_modulo2, aba_modulo3, aba_modulo4, aba_modulo5, aba_modulo6 = st.tabs(
    [
        "🏠 Início",
        "📊 Módulo 2 — Estatística Descritiva",
        "🎲 Módulo 3 — Probabilidade e Simulação",
        "🔔 Módulo 4 — Distribuições Teóricas",
        "📈 Módulo 5 — Correlação e Regressão",
        "🔎 Módulo 6 — Descobertas"
    ]
)

with aba_inicio:
    st.title("Laboratório de Estatística — PRF 2025")
    st.write(
        "Análise estatística interativa dos acidentes registrados nas "
        "rodovias federais brasileiras em 2025."
    )

    st.subheader("Sobre o projeto")
    st.write(
        "O projeto utiliza o dataset público de acidentes da Polícia Rodoviária "
        "Federal (PRF) referente ao ano de 2025. As análises foram organizadas "
        "por módulos para facilitar a navegação e a apresentação dos resultados."
    )

    col_inicio1, col_inicio2 = st.columns(2)
    col_inicio1.metric(
        "Quantidade de ocorrências",
        f"{len(df):,}".replace(",", ".")
    )
    col_inicio2.metric(
        "Quantidade de variáveis",
        len(df.columns)
    )

    st.subheader("Módulo 1 — Núcleo Estatístico")
    st.write(
        "As funções estatísticas utilizadas nos cálculos apresentados pela "
        "aplicação foram implementadas no arquivo `minhastats.py`. Esse núcleo "
        "inclui medidas de tendência central, dispersão, quartis, correlação de "
        "Pearson e regressão linear simples."
    )

    st.info(
        "Utilize as abas acima para acessar a Estatística Descritiva, as "
        "simulações, as distribuições teóricas, a correlação e regressão e "
        "as três descobertas obtidas a partir dos dados da PRF 2025."
    )

with aba_modulo2:
    # ============================================================
    # TÍTULO DA APLICAÇÃO
    # ============================================================

    st.title("Laboratório de Estatística — PRF 2025")

    st.write(
        "Análise estatística dos acidentes registrados nas "
        "rodovias federais brasileiras em 2025."
    )


    # ============================================================
    # INFORMAÇÕES GERAIS DO DATASET
    # ============================================================

    st.subheader("Visão geral da base de dados")

    # Criamos duas colunas visuais na tela.
    coluna1, coluna2 = st.columns(2)

    # len(df) informa a quantidade de linhas do dataset.
    coluna1.metric(
        "Quantidade de ocorrências",
        f"{len(df):,}".replace(",", ".")
    )

    # len(df.columns) informa a quantidade de colunas.
    coluna2.metric(
        "Quantidade de variáveis",
        len(df.columns)
    )


    # ============================================================
    # VARIÁVEIS NUMÉRICAS QUE UTILIZAREMOS
    # ============================================================

    # Não colocamos "id" ou "br", por exemplo, porque apesar de
    # serem números, funcionam principalmente como identificadores.
    variaveis_numericas = [
        "pessoas",
        "mortos",
        "feridos_leves",
        "feridos_graves",
        "ilesos",
        "ignorados",
        "feridos",
        "veiculos"
    ]


    # ============================================================
    # SELEÇÃO INTERATIVA DA VARIÁVEL
    # ============================================================

    st.subheader("Seleção da variável")

    variavel = st.selectbox(
        "Escolha uma variável numérica para analisar:",
        variaveis_numericas
    )

    st.write(
        f"Variável selecionada: **{variavel}**"
    )


    # ============================================================
    # PRÉVIA DOS DADOS
    # ============================================================

    st.subheader("Prévia da base de dados")

    st.caption(
        #"São exibidas abaixo apenas as 10 primeiras ocorrências. "
        "Os cálculos estatísticos utilizam todos os registros disponíveis."
    )

    # Mostramos somente algumas colunas para a tabela não ficar
    # excessivamente grande.
    #
    # head(10) limita a visualização às primeiras 10 ocorrências.
    st.dataframe(
        df[
            [
                "id",
                "uf",
                "municipio",
                variavel
            ]
        ],
        use_container_width=True
    )

    # ============================================================
    # PREPARAÇÃO DOS DADOS PARA O NOSSO NÚCLEO ESTATÍSTICO
    # ============================================================

    # Selecionamos somente a coluna escolhida pelo usuário.
    #
    # dropna()
    # Remove eventuais valores ausentes.
    #
    # tolist()
    # Converte a coluna do Pandas para uma lista Python comum.
    #
    # Exemplo:
    # [1, 2, 1, 0, 3, 1, ...]
    #
    # Essa lista será enviada para as funções do minhastats.py.

    dados_variavel = df[variavel].dropna().tolist()


    # ============================================================
    # CÁLCULOS REALIZADOS PELO minhastats.py
    # ============================================================

    # A partir deste ponto, as medidas estatísticas são calculadas
    # pelas funções que implementamos manualmente no Módulo 1.

    valor_media = media(dados_variavel)

    valor_mediana = mediana(dados_variavel)

    valor_moda = moda(dados_variavel)

    valor_amplitude = amplitude(dados_variavel)

    valor_variancia = variancia_amostral(dados_variavel)

    valor_desvio = desvio_padrao_amostral(dados_variavel)

    q1, q2, q3 = quartis(dados_variavel)

    valor_cv = coeficiente_variacao(dados_variavel)


    # ============================================================
    # EXIBIÇÃO DAS MEDIDAS ESTATÍSTICAS
    # ============================================================

    st.subheader("Medidas estatísticas")

    st.caption(
        "Os valores abaixo são calculados pelas funções próprias "
        "implementadas no arquivo minhastats.py."
    )


    # ------------------------------------------------------------
    # PRIMEIRA LINHA
    # Média, Mediana, Moda e Amplitude
    # ------------------------------------------------------------

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Média",
        f"{valor_media:.2f}"
    )

    col2.metric(
        "Mediana",
        f"{valor_mediana:.2f}"
    )


    # A função moda() retorna uma lista porque uma distribuição
    # pode possuir mais de uma moda.
    #
    # Exemplo:
    # [1]
    # [1, 2]
    #
    # Caso a lista esteja vazia, consideramos a distribuição
    # amodal.

    if len(valor_moda) == 0:
        texto_moda = "Amodal"
    else:
        texto_moda = ", ".join(
            str(valor) for valor in valor_moda
        )

    col3.metric(
        "Moda",
        texto_moda
    )

    col4.metric(
        "Amplitude",
        f"{valor_amplitude:.2f}"
    )


    # ------------------------------------------------------------
    # SEGUNDA LINHA
    # Variância, Desvio padrão e Coeficiente de variação
    # ------------------------------------------------------------

    col5, col6, col7 = st.columns(3)

    col5.metric(
        "Variância amostral",
        f"{valor_variancia:.4f}"
    )

    col6.metric(
        "Desvio padrão amostral",
        f"{valor_desvio:.4f}"
    )

    col7.metric(
        "Coeficiente de variação",
        f"{valor_cv:.2f}%"
    )


    # ------------------------------------------------------------
    # TERCEIRA LINHA
    # Quartis
    # ------------------------------------------------------------

    st.subheader("Quartis")

    col8, col9, col10 = st.columns(3)

    col8.metric(
        "Q1 — 25%",
        f"{q1:.2f}"
    )

    col9.metric(
        "Q2 — 50%",
        f"{q2:.2f}"
    )

    col10.metric(
        "Q3 — 75%",
        f"{q3:.2f}"
    )

    # ============================================================
    # TABELA DE FREQUÊNCIAS
    # ============================================================

    st.subheader("Tabela de frequências")

    st.write(
        "A tabela abaixo apresenta quantas vezes cada valor da "
        "variável selecionada aparece no conjunto de dados."
    )


    # ============================================================
    # CONTAGEM DAS FREQUÊNCIAS
    # ============================================================

    # Criamos um dicionário Python vazio.
    #
    # Exemplo do resultado que queremos construir:
    #
    # {
    #     0: 30000,
    #     1: 25000,
    #     2: 10000,
    #     3: 5000
    # }
    #
    # A chave representa o valor observado.
    # O número associado representa quantas vezes ele apareceu.
    #
    # A contagem é feita manualmente para deixar o procedimento
    # transparente e didático.

    frequencias = {}

    for valor in dados_variavel:

        if valor in frequencias:
            frequencias[valor] += 1

        else:
            frequencias[valor] = 1


    # ============================================================
    # ORGANIZAÇÃO DOS VALORES
    # ============================================================

    # Ordenamos os valores do menor para o maior.
    #
    # Exemplo:
    # 0, 1, 2, 3, 4, ...

    valores_ordenados = sorted(frequencias.keys())


    # ============================================================
    # CONSTRUÇÃO DA TABELA
    # ============================================================

    # A tabela terá:
    #
    # Valor
    # Frequência absoluta
    # Frequência relativa (%)
    # Frequência acumulada
    # Frequência relativa acumulada (%)

    tabela_frequencia = []

    total = len(dados_variavel)

    frequencia_acumulada = 0


    for valor in valores_ordenados:

        # Frequência absoluta:
        # quantidade de vezes que o valor apareceu.
        frequencia_absoluta = frequencias[valor]


        # Somamos à frequência acumulada.
        frequencia_acumulada += frequencia_absoluta


        # Frequência relativa em percentual.
        frequencia_relativa = (
            frequencia_absoluta / total
        ) * 100


        # Frequência relativa acumulada.
        frequencia_relativa_acumulada = (
            frequencia_acumulada / total
        ) * 100


        # Adicionamos uma linha à tabela.
        tabela_frequencia.append(
            {
                "Valor": valor,

                "Frequência absoluta": frequencia_absoluta,

                "Frequência relativa (%)":
                    frequencia_relativa,

                "Frequência acumulada":
                    frequencia_acumulada,

                "Frequência relativa acumulada (%)":
                    frequencia_relativa_acumulada
            }
        )


    # ============================================================
    # CONVERSÃO PARA DATAFRAME
    # ============================================================

    # Aqui o Pandas NÃO está calculando uma medida estatística.
    #
    # Ele está sendo utilizado apenas para transformar nossa lista
    # em uma tabela que o Streamlit consegue apresentar de maneira
    # organizada.

    df_frequencia = pd.DataFrame(
        tabela_frequencia
    )


    # ============================================================
    # FORMATAÇÃO DOS PERCENTUAIS
    # ============================================================

    # Arredondamos somente para facilitar a leitura na tela.

    df_frequencia["Frequência relativa (%)"] = (
        df_frequencia["Frequência relativa (%)"].round(2)
    )

    df_frequencia["Frequência relativa acumulada (%)"] = (
        df_frequencia[
            "Frequência relativa acumulada (%)"
        ].round(2)
    )


    # ============================================================
    # EXIBIÇÃO
    # ============================================================

    st.dataframe(
        df_frequencia,
        use_container_width=True,
        hide_index=True
    )

    # ============================================================
    # GRÁFICOS DA VARIÁVEL NUMÉRICA
    # ============================================================

    st.subheader("Visualização gráfica")

    st.write(
        "Os gráficos abaixo permitem observar visualmente a "
        "distribuição da variável selecionada."
    )


    # ============================================================
    # HISTOGRAMA
    # ============================================================

    st.markdown("### Histograma")

    # Criamos uma nova figura para o gráfico.
    fig_hist, ax_hist = plt.subplots(figsize=(9, 4))


    # ------------------------------------------------------------
    # DEFINIÇÃO DAS CLASSES DO HISTOGRAMA
    # ------------------------------------------------------------
    #
    # As variáveis que estamos analisando neste momento são
    # contagens discretas:
    #
    # mortos = 0, 1, 2, 3...
    # pessoas = 1, 2, 3...
    # veículos = 1, 2, 3...
    #
    # Por isso, criamos intervalos centralizados nos números
    # inteiros.
    #
    # Exemplo:
    #
    # valor 0 -> intervalo -0.5 até 0.5
    # valor 1 -> intervalo  0.5 até 1.5
    # valor 2 -> intervalo  1.5 até 2.5
    #
    # Dessa maneira cada barra representa corretamente um valor
    # inteiro da variável.

    valor_minimo = int(min(dados_variavel))
    valor_maximo = int(max(dados_variavel))

    classes = [
        valor - 0.5
        for valor in range(
            valor_minimo,
            valor_maximo + 2
        )
    ]


    # ------------------------------------------------------------
    # CONSTRUÇÃO DO HISTOGRAMA
    # ------------------------------------------------------------

    ax_hist.hist(
        dados_variavel,
        bins=classes,
        edgecolor="black"
    )


    # ------------------------------------------------------------
    # TÍTULO E IDENTIFICAÇÃO DOS EIXOS
    # ------------------------------------------------------------

    ax_hist.set_title(
        f"Distribuição da variável: {variavel}"
    )

    ax_hist.set_xlabel(
        variavel
    )

    ax_hist.set_ylabel(
        "Frequência"
    )


    # Adicionamos uma grade horizontal suave para facilitar
    # a leitura das frequências.

    ax_hist.grid(
        axis="y",
        alpha=0.3
    )


    # Ajustamos automaticamente os elementos dentro da figura.

    fig_hist.tight_layout()


    # Mostramos o gráfico dentro da aplicação Streamlit.

    st.pyplot(fig_hist)


    # Fechamos a figura depois de apresentá-la.
    # Isso evita que figuras antigas permaneçam ocupando memória.

    plt.close(fig_hist)

    # ============================================================
    # BOXPLOT
    # ============================================================

    st.markdown("### Boxplot")

    # Criamos uma nova figura exclusivamente para o boxplot.

    fig_box, ax_box = plt.subplots(figsize=(9, 4))


    # ------------------------------------------------------------
    # CONSTRUÇÃO DO BOXPLOT
    # ------------------------------------------------------------
    #
    # O boxplot permite visualizar:
    #
    # - mediana;
    # - região central dos dados;
    # - dispersão;
    # - possíveis valores discrepantes (outliers).
    #
    # Posteriormente nós mesmos calcularemos os limites dos
    # outliers utilizando Q1, Q3 e IQR.

    ax_box.boxplot(
        dados_variavel,
        vert=False
    )


    # ------------------------------------------------------------
    # TÍTULO E EIXO
    # ------------------------------------------------------------

    ax_box.set_title(
        f"Boxplot da variável: {variavel}"
    )

    ax_box.set_xlabel(
        variavel
    )

    ax_box.grid(
        axis="x",
        alpha=0.3
    )

    fig_box.tight_layout()


    # Apresentamos o boxplot no Streamlit.

    st.pyplot(fig_box)


    # Liberamos a figura da memória.

    plt.close(fig_box)

    # ============================================================
    # DETECÇÃO DE OUTLIERS PELO MÉTODO IQR
    # ============================================================

    st.subheader("Análise de outliers — Método IQR")

    st.write(
        "A identificação de possíveis valores discrepantes é feita "
        "utilizando o intervalo interquartil (IQR)."
    )


    # ============================================================
    # CÁLCULO DO IQR
    # ============================================================
    #
    # Os valores q1 e q3 já foram calculados anteriormente pela
    # nossa função quartis(), localizada no minhastats.py.
    #
    # IQR significa Intervalo Interquartil.
    #
    # Ele mede a distância entre o primeiro quartil (Q1)
    # e o terceiro quartil (Q3).
    #
    # Fórmula:
    #
    # IQR = Q3 - Q1

    iqr = q3 - q1


    # ============================================================
    # CÁLCULO DOS LIMITES
    # ============================================================
    #
    # Pela regra tradicional do IQR:
    #
    # Limite inferior = Q1 - 1,5 * IQR
    #
    # Limite superior = Q3 + 1,5 * IQR
    #
    # Valores abaixo do limite inferior ou acima do limite
    # superior serão classificados como possíveis outliers.

    limite_inferior = q1 - (1.5 * iqr)

    limite_superior = q3 + (1.5 * iqr)


    # ============================================================
    # IDENTIFICAÇÃO DOS OUTLIERS
    # ============================================================
    #
    # Percorremos todos os valores da variável selecionada.
    #
    # Se o valor estiver:
    #
    # abaixo do limite inferior
    #
    # OU
    #
    # acima do limite superior
    #
    # ele será colocado na lista de possíveis outliers.

    outliers = []

    for valor in dados_variavel:

        if (
            valor < limite_inferior
            or
            valor > limite_superior
        ):
            outliers.append(valor)


    # ============================================================
    # QUANTIDADE E PERCENTUAL DE OUTLIERS
    # ============================================================

    quantidade_outliers = len(outliers)

    percentual_outliers = (
        quantidade_outliers / len(dados_variavel)
    ) * 100


    # ============================================================
    # APRESENTAÇÃO DOS RESULTADOS
    # ============================================================

    col_out1, col_out2, col_out3 = st.columns(3)

    col_out1.metric(
        "Q1",
        f"{q1:.2f}"
    )

    col_out2.metric(
        "Q3",
        f"{q3:.2f}"
    )

    col_out3.metric(
        "IQR",
        f"{iqr:.2f}"
    )


    col_out4, col_out5 = st.columns(2)

    col_out4.metric(
        "Limite inferior",
        f"{limite_inferior:.2f}"
    )

    col_out5.metric(
        "Limite superior",
        f"{limite_superior:.2f}"
    )


    col_out6, col_out7 = st.columns(2)

    col_out6.metric(
        "Quantidade de possíveis outliers",
        f"{quantidade_outliers:,}".replace(",", ".")
    )

    col_out7.metric(
        "Percentual de possíveis outliers",
        f"{percentual_outliers:.2f}%"
    )

    # ============================================================
    # INTERPRETAÇÃO DO RESULTADO
    # ============================================================

    if quantidade_outliers == 0:

        st.success(
            "Pelo critério de 1,5 × IQR, não foram identificados "
            "possíveis outliers nesta variável."
        )

    else:

        st.info(
            f"Foram identificadas {quantidade_outliers:,} observações "
            f"({percentual_outliers:.2f}% dos dados) fora dos limites "
            "definidos pelo critério de 1,5 × IQR."
            .replace(",", ".")
        )


    # ============================================================
    # CASO ESPECIAL: IQR IGUAL A ZERO
    # ============================================================
    #
    # Algumas variáveis da base possuem uma concentração muito
    # grande em determinado valor.
    #
    # Por exemplo, na variável "mortos":
    #
    # Q1 = 0
    # Q3 = 0
    #
    # Consequentemente:
    #
    # IQR = 0
    #
    # Nesse caso, a regra do IQR fica extremamente restritiva.
    # É importante explicar ao usuário que um valor identificado
    # como outlier não significa necessariamente que seja um erro.

    if iqr == 0:

        st.warning(
            "Atenção: o IQR desta variável é igual a zero. "
            "Isso ocorre quando pelo menos a região entre Q1 e Q3 "
            "está concentrada no mesmo valor. Nesse caso, o critério "
            "de 1,5 × IQR pode classificar muitos valores diferentes "
            "como possíveis outliers. Um outlier estatístico não "
            "significa necessariamente um dado incorreto."
        )

    # ============================================================
    # INTERPRETAÇÃO TEXTUAL DA DISTRIBUIÇÃO
    # ============================================================

    st.subheader("Interpretação da distribuição")

    st.write(
        "A interpretação abaixo utiliza as medidas calculadas "
        "pelo nosso núcleo estatístico e as características "
        "observadas na distribuição."
    )


    # ============================================================
    # COMPARAÇÃO ENTRE MÉDIA E MEDIANA
    # ============================================================
    #
    # Uma maneira simples de obter uma indicação sobre a forma
    # da distribuição é comparar a média com a mediana.
    #
    # Em termos gerais:
    #
    # média > mediana
    #     pode indicar assimetria à direita.
    #
    # média < mediana
    #     pode indicar assimetria à esquerda.
    #
    # média aproximadamente igual à mediana
    #     pode indicar maior equilíbrio entre os dois lados.
    #
    # IMPORTANTE:
    #
    # Essa comparação é apenas uma indicação descritiva.
    # Ela não constitui, sozinha, uma prova matemática
    # da forma da distribuição.


    # ============================================================
    # DEFINIÇÃO DE UMA TOLERÂNCIA
    # ============================================================
    #
    # Não devemos comparar números decimais usando apenas:
    #
    # valor_media == valor_mediana
    #
    # porque pequenas diferenças numéricas podem existir.
    #
    # Por isso utilizamos uma pequena tolerância relativa.
    #
    # Aqui consideraremos como "próximos" valores cuja diferença
    # seja de até 1% da escala da média/mediana.
    #
    # O max(..., 1.0) impede que a tolerância fique igual a zero
    # quando média e mediana forem zero.

    tolerancia_assimetria = (
        max(
            abs(valor_media),
            abs(valor_mediana),
            1.0
        )
        * 0.01
    )


    # ============================================================
    # IDENTIFICAÇÃO DESCRITIVA DA ASSIMETRIA
    # ============================================================

    diferenca_media_mediana = (
        valor_media - valor_mediana
    )


    if abs(diferenca_media_mediana) <= tolerancia_assimetria:

        tipo_distribuicao = (
            "aproximadamente equilibrada em relação "
            "à média e à mediana"
        )

        explicacao_assimetria = (
            "A média e a mediana apresentam valores próximos. "
            "Essa proximidade sugere maior equilíbrio da "
            "distribuição, embora essa comparação isoladamente "
            "não seja suficiente para afirmar que a distribuição "
            "é perfeitamente simétrica."
        )


    elif valor_media > valor_mediana:

        tipo_distribuicao = (
            "com indicação de assimetria à direita"
        )

        explicacao_assimetria = (
            "A média é maior que a mediana. Isso indica que "
            "valores mais elevados podem estar puxando a média "
            "para a direita, formando uma cauda em direção aos "
            "valores maiores."
        )


    else:

        tipo_distribuicao = (
            "com indicação de assimetria à esquerda"
        )

        explicacao_assimetria = (
            "A média é menor que a mediana. Isso indica que "
            "valores mais baixos podem estar puxando a média "
            "para a esquerda, formando uma cauda em direção aos "
            "valores menores."
        )


    # ============================================================
    # APRESENTAÇÃO DA INTERPRETAÇÃO
    # ============================================================

    st.markdown(
        f"**Comportamento da distribuição:** "
        f"{tipo_distribuicao}."
    )

    st.write(explicacao_assimetria)

    # ============================================================
    # INTERPRETAÇÃO DOS QUARTIS
    # ============================================================

    st.markdown("#### Interpretação dos quartis")

    st.write(
        f"Q1 = {q1:.2f}, Q2 (mediana) = {q2:.2f} "
        f"e Q3 = {q3:.2f}."
    )

    st.write(
        f"Isso significa que aproximadamente 25% das observações "
        f"estão até {q1:.2f}, 50% estão até {q2:.2f} "
        f"e 75% estão até {q3:.2f}."
    )


    # ============================================================
    # INTERPRETAÇÃO DOS POSSÍVEIS OUTLIERS
    # ============================================================

    st.markdown("#### Interpretação dos possíveis outliers")

    if quantidade_outliers == 0:

        st.write(
            "Não foram identificadas observações fora dos limites "
            "definidos pela regra de 1,5 × IQR."
        )

    else:

        st.write(
            f"O critério de 1,5 × IQR identificou "
            f"{quantidade_outliers:,} possíveis outliers, "
            f"correspondentes a {percentual_outliers:.2f}% "
            f"das observações."
            .replace(",", ".")
        )

        st.write(
            "Esses valores devem ser interpretados como "
            "estatisticamente discrepantes segundo esse critério, "
            "e não automaticamente como erros na base de dados."
        )

        # ============================================================
    # OBSERVAÇÃO PARA DISTRIBUIÇÕES MUITO CONCENTRADAS
    # ============================================================

    if iqr == 0:

        st.info(
            "Como Q1 e Q3 possuem o mesmo valor, o intervalo "
            "interquartil é zero. Isso mostra uma forte "
            "concentração das observações em uma mesma região "
            "da distribuição. Nesse cenário, a regra de outliers "
            "por IQR deve ser interpretada com cautela."
        )

    # ============================================================
    # ANÁLISE DE VARIÁVEIS CATEGÓRICAS
    # ============================================================
    #
    # Até este ponto trabalhamos com variáveis numéricas:
    #
    # pessoas, mortos, feridos, veículos etc.
    #
    # Agora iniciaremos a análise das variáveis categóricas.
    #
    # Variáveis categóricas representam grupos ou categorias,
    # e não quantidades numéricas.
    #
    # Exemplos:
    #
    # uf                -> SP, MG, PR, GO...
    # dia_semana        -> segunda-feira, terça-feira...
    # tipo_acidente     -> colisão traseira, saída de leito...
    # fase_dia          -> pleno dia, plena noite...
    #
    # Para essas variáveis, medidas como média e desvio padrão
    # não fazem sentido.
    #
    # O mais adequado é analisar suas frequências.

    st.divider()

    st.header("Análise de variável categórica")


    # ============================================================
    # LISTA DE VARIÁVEIS CATEGÓRICAS
    # ============================================================

    variaveis_categoricas = [
        "uf",
        "dia_semana",
        "causa_acidente",
        "tipo_acidente",
        "classificacao_acidente",
        "fase_dia",
        "sentido_via",
        "condicao_metereologica",
        "tipo_pista",
        "tracado_via",
        "uso_solo"
    ]


    # ============================================================
    # SELEÇÃO DA VARIÁVEL CATEGÓRICA
    # ============================================================

    variavel_categorica = st.selectbox(
        "Escolha uma variável categórica para analisar:",
        variaveis_categoricas
    )

    st.write(
        f"Variável categórica selecionada: "
        f"**{variavel_categorica}**"
    )

    # ============================================================
    # PREPARAÇÃO DOS DADOS CATEGÓRICOS
    # ============================================================

    # Selecionamos a coluna escolhida.
    #
    # dropna()
    # remove eventuais valores ausentes.
    #
    # tolist()
    # transforma a coluna em uma lista Python comum.

    dados_categoria = (
        df[variavel_categorica]
        .dropna()
        .tolist()
    )


    # ============================================================
    # CONTAGEM MANUAL DAS CATEGORIAS
    # ============================================================
    #
    # Novamente faremos a contagem explicitamente.
    #
    # Exemplo para UF:
    #
    # {
    #     "MG": 9570,
    #     "SC": 8186,
    #     "PR": 7630,
    #     ...
    # }
    #
    # O Pandas poderia fazer essa operação com value_counts(),
    # mas aqui deixamos o algoritmo visível e didático.

    frequencias_categoria = {}

    for categoria in dados_categoria:

        if categoria in frequencias_categoria:

            frequencias_categoria[categoria] += 1

        else:

            frequencias_categoria[categoria] = 1

    # ============================================================
    # ORDENAÇÃO DAS CATEGORIAS
    # ============================================================
    #
    # Ordenamos pela frequência, da maior para a menor.
    #
    # Isso facilita bastante a interpretação da tabela e,
    # posteriormente, do gráfico de barras.

    categorias_ordenadas = sorted(
        frequencias_categoria.items(),
        key=lambda item: item[1],
        reverse=True
    )

    # ============================================================
    # CONSTRUÇÃO DA TABELA DE FREQUÊNCIAS CATEGÓRICAS
    # ============================================================

    tabela_categoria = []

    total_categorias = len(dados_categoria)

    for categoria, frequencia in categorias_ordenadas:

        # Calculamos o percentual que essa categoria representa
        # em relação ao total de observações válidas.

        percentual = (
            frequencia / total_categorias
        ) * 100


        # Guardamos os resultados em uma lista.

        tabela_categoria.append(
            {
                "Categoria": categoria,

                "Frequência absoluta":
                    frequencia,

                "Frequência relativa (%)":
                    percentual
            }
        )

        # ============================================================
    # TRANSFORMAÇÃO EM DATAFRAME
    # ============================================================
    #
    # Novamente o Pandas está sendo utilizado apenas para
    # organizar e apresentar a tabela.
    #
    # A contagem das frequências foi feita pelo nosso código.

    df_categoria = pd.DataFrame(
        tabela_categoria
    )


    # Arredondamos os percentuais para duas casas decimais.

    df_categoria["Frequência relativa (%)"] = (
        df_categoria[
            "Frequência relativa (%)"
        ].round(2)
    )


    # ============================================================
    # EXIBIÇÃO DA TABELA
    # ============================================================

    st.subheader("Tabela de frequências — variável categórica")

    st.dataframe(
        df_categoria,
        use_container_width=True,
        hide_index=True
    )

    # ============================================================
    # GRÁFICOS DAS VARIÁVEIS CATEGÓRICAS
    # ============================================================

    st.subheader("Visualização gráfica — variável categórica")

    st.write(
        "Os gráficos abaixo representam a distribuição das "
        "categorias da variável selecionada."
    )


    # ============================================================
    # GRÁFICO DE BARRAS
    # ============================================================

    st.markdown("### Gráfico de barras")


    # ------------------------------------------------------------
    # PREPARAÇÃO DOS DADOS
    # ------------------------------------------------------------
    #
    # categorias_ordenadas já foi construída anteriormente.
    #
    # Sua estrutura é semelhante a:
    #
    # [
    #     ("MG", 9570),
    #     ("SC", 8186),
    #     ("PR", 7630),
    #     ...
    # ]
    #
    # Para o gráfico, vamos separar as categorias das frequências.

    nomes_categorias = [
        item[0]
        for item in categorias_ordenadas
    ]

    frequencias_grafico = [
        item[1]
        for item in categorias_ordenadas
    ]


    # ------------------------------------------------------------
    # CRIAÇÃO DO GRÁFICO
    # ------------------------------------------------------------

    fig_barras, ax_barras = plt.subplots(
        figsize=(12, 6)
    )

    ax_barras.bar(
        nomes_categorias,
        frequencias_grafico
    )


    # ------------------------------------------------------------
    # TÍTULO E EIXOS
    # ------------------------------------------------------------

    ax_barras.set_title(
        f"Frequência por categoria — {variavel_categorica}"
    )

    ax_barras.set_xlabel(
        variavel_categorica
    )

    ax_barras.set_ylabel(
        "Frequência"
    )


    # ------------------------------------------------------------
    # ROTAÇÃO DOS NOMES
    # ------------------------------------------------------------
    #
    # Algumas categorias possuem nomes grandes.
    #
    # Giramos os textos para evitar que eles fiquem
    # sobrepostos.

    ax_barras.tick_params(
        axis="x",
        labelrotation=45
    )


    # Alinhamos os textos à direita.

    for rotulo in ax_barras.get_xticklabels():
        rotulo.set_horizontalalignment("right")


    # Grade horizontal para facilitar a leitura.

    ax_barras.grid(
        axis="y",
        alpha=0.3
    )


    # Ajustamos automaticamente o espaço da figura.

    fig_barras.tight_layout()


    # Apresentamos no Streamlit.

    st.pyplot(fig_barras)


    # Liberamos a figura da memória.

    plt.close(fig_barras)

    # ============================================================
    # GRÁFICO DE SETORES (PIZZA)
    # ============================================================

    st.markdown("### Gráfico de setores")


    # ============================================================
    # QUANTIDADE DE CATEGORIAS PRINCIPAIS
    # ============================================================
    #
    # Para manter o gráfico legível, mostraremos somente
    # as 7 categorias mais frequentes.
    #
    # As demais serão agrupadas em "Outros".

    quantidade_principais = 7


    # Pegamos as primeiras categorias da lista já ordenada.

    categorias_principais = (
        categorias_ordenadas[:quantidade_principais]
    )


    # Pegamos todas as categorias restantes.

    categorias_restantes = (
        categorias_ordenadas[quantidade_principais:]
    )


    # ============================================================
    # PREPARAÇÃO DOS DADOS DA PIZZA
    # ============================================================

    nomes_pizza = []

    frequencias_pizza = []


    # Adicionamos as categorias principais.

    for categoria, frequencia in categorias_principais:

        nomes_pizza.append(categoria)

        frequencias_pizza.append(frequencia)


    # ============================================================
    # AGRUPAMENTO DAS DEMAIS CATEGORIAS
    # ============================================================
    #
    # Somamos as frequências de todas as categorias que ficaram
    # fora das sete primeiras.

    frequencia_outros = 0

    for categoria, frequencia in categorias_restantes:

        frequencia_outros += frequencia


    # Somente adicionamos "Outros" quando realmente existirem
    # categorias além das sete primeiras.

    if frequencia_outros > 0:

        nomes_pizza.append("Outros")

        frequencias_pizza.append(
            frequencia_outros
        )


    # ============================================================
    # CRIAÇÃO DO GRÁFICO
    # ============================================================

    fig_pizza, ax_pizza = plt.subplots(
        figsize=(6, 6)
    )

    ax_pizza.pie(
        frequencias_pizza,
        labels=nomes_pizza,
        autopct="%1.1f%%",
        startangle=90
    )


    # ------------------------------------------------------------
    # TÍTULO
    # ------------------------------------------------------------

    ax_pizza.set_title(
        f"Distribuição percentual — {variavel_categorica}"
    )


    # ------------------------------------------------------------
    # FORMATO CIRCULAR
    # ------------------------------------------------------------
    #
    # Isso evita que o gráfico fique visualmente oval.

    ax_pizza.axis("equal")


    fig_pizza.tight_layout()


    # Mostramos o gráfico no Streamlit.

    st.pyplot(fig_pizza)


    # Liberamos a figura da memória.

    plt.close(fig_pizza)

    # ============================================================

with aba_modulo3:
    # ============================================================
    # MÓDULO 3 - PROBABILIDADE E SIMULAÇÃO
    # ============================================================
    # Este módulo permite trabalhar com duas fontes:
    # 1) dados reais da PRF 2025 (opção padrão);
    # 2) exemplo didático de um dado equilibrado de seis faces.
    #
    # O NumPy é utilizado somente para realizar os sorteios.
    # As médias apresentadas são calculadas pela função media(),
    # implementada no nosso arquivo minhastats.py.

    st.header("Módulo 3 — Probabilidade e Simulação")

    st.write(
        "Nesta seção utilizamos simulações computacionais para observar "
        "a Lei dos Grandes Números (LGN) e o Teorema Central do Limite (TCL). "
        "Por padrão, as simulações utilizam os dados reais da PRF 2025."
    )

    fonte_simulacao = st.radio(
        "Fonte dos dados da simulação:",
        [
            "Dados reais da PRF 2025",
            "Exemplo didático — dado de 6 faces"
        ],
        index=0,
        key="m3_fonte_simulacao"
    )

    # ------------------------------------------------------------
    # PREPARAÇÃO DA POPULAÇÃO
    # ------------------------------------------------------------
    if fonte_simulacao == "Dados reais da PRF 2025":

        variaveis_simulacao = [
            "pessoas",
            "mortos",
            "feridos_leves",
            "feridos_graves",
            "ilesos",
            "ignorados",
            "feridos",
            "veiculos"
        ]

        variavel_simulacao = st.selectbox(
            "Escolha a variável da PRF para a simulação:",
            variaveis_simulacao,
            index=0,
            key="m3_variavel_simulacao"
        )

        dados_populacao = (
            df[variavel_simulacao]
            .dropna()
            .tolist()
        )

        media_populacional = media(dados_populacao)
        desvio_populacional = desvio_padrao_populacional(dados_populacao)

        st.caption(
            "A base completa é tratada como a população de referência. "
            "Os sorteios são feitos a partir das ocorrências disponíveis no CSV."
        )

        col_m3_1, col_m3_2, col_m3_3 = st.columns(3)

        col_m3_1.metric(
            "Variável selecionada",
            variavel_simulacao
        )

        col_m3_2.metric(
            "Observações válidas",
            f"{len(dados_populacao):,}".replace(",", ".")
        )

        col_m3_3.metric(
            "Média da população",
            f"{media_populacional:.4f}"
        )

        nome_populacao = "PRF 2025 — " + variavel_simulacao

    else:
        # População teórica do dado: 1, 2, 3, 4, 5 e 6.
        dados_populacao = [1, 2, 3, 4, 5, 6]
        media_populacional = media(dados_populacao)
        desvio_populacional = desvio_padrao_populacional(dados_populacao)
        nome_populacao = "dado equilibrado de 6 faces"

        st.info(
            "Nesta opção mantemos o exemplo clássico do dado de seis faces. "
            "A média populacional teórica é 3,5."
        )

    # ============================================================
    # 3.1 - LEI DOS GRANDES NÚMEROS
    # ============================================================
    st.divider()
    st.subheader("Lei dos Grandes Números")

    st.write(
        "A LGN indica que, conforme aumenta a quantidade de observações "
        "aleatórias, a média acumulada tende a se aproximar da média "
        "da população de referência."
    )

    quantidade_observacoes = st.slider(
        "Quantidade de observações sorteadas:",
        min_value=10,
        max_value=10000,
        value=1000,
        step=10,
        key="m3_quantidade_lgn"
    )

    gerador_lgn = np.random.default_rng(seed=42)

    # replace=True representa amostragem com reposição.
    # O NumPy faz apenas o sorteio dos valores.
    amostra_lgn = gerador_lgn.choice(
        dados_populacao,
        size=quantidade_observacoes,
        replace=True
    )

    # Cálculo explícito da média acumulada.
    medias_acumuladas = []
    soma_acumulada = 0.0

    for indice, valor in enumerate(amostra_lgn, start=1):
        soma_acumulada += float(valor)
        medias_acumuladas.append(soma_acumulada / indice)

    # A média final também é conferida pela nossa função própria.
    media_final_lgn = media(amostra_lgn.tolist())
    diferenca_lgn = abs(media_final_lgn - media_populacional)

    col_lgn1, col_lgn2, col_lgn3 = st.columns(3)

    col_lgn1.metric(
        "Quantidade de sorteios",
        f"{quantidade_observacoes:,}".replace(",", ".")
    )

    col_lgn2.metric(
        "Média da população",
        f"{media_populacional:.4f}"
    )

    col_lgn3.metric(
        "Média observada",
        f"{media_final_lgn:.4f}"
    )

    numero_observacoes = list(range(1, quantidade_observacoes + 1))

    fig_lgn, ax_lgn = plt.subplots(figsize=(9, 4))

    ax_lgn.plot(
        numero_observacoes,
        medias_acumuladas,
        label="Média acumulada"
    )

    ax_lgn.axhline(
        y=media_populacional,
        linestyle="--",
        label="Média da população"
    )

    ax_lgn.set_title(
        "Lei dos Grandes Números — " + nome_populacao
    )
    ax_lgn.set_xlabel("Quantidade de observações")
    ax_lgn.set_ylabel("Média acumulada")
    ax_lgn.legend()
    ax_lgn.grid(alpha=0.3)
    fig_lgn.tight_layout()

    st.pyplot(fig_lgn)
    plt.close(fig_lgn)

    st.write(
        f"Após **{quantidade_observacoes:,} sorteios**, a média observada foi "
        f"**{media_final_lgn:.4f}**, enquanto a média da população de referência "
        f"é **{media_populacional:.4f}**. A diferença absoluta foi "
        f"**{diferenca_lgn:.4f}**."
        .replace(",", ".")
    )

    st.info(
        "No início a média acumulada pode oscilar bastante. Conforme o número "
        "de observações aumenta, ela tende a se estabilizar em torno da média "
        "da população, ilustrando a Lei dos Grandes Números."
    )

    # ============================================================
    # 3.2 - TEOREMA CENTRAL DO LIMITE
    # ============================================================
    st.divider()
    st.subheader("Teorema Central do Limite")

    st.write(
        "Agora retiramos várias amostras independentes da população escolhida. "
        "Para cada amostra calculamos a média com a função própria media(). "
        "Em seguida analisamos a distribuição dessas médias amostrais."
    )

    col_controle1, col_controle2 = st.columns(2)

    quantidade_amostras = col_controle1.slider(
        "Quantidade de amostras:",
        min_value=100,
        max_value=5000,
        value=1000,
        step=100,
        key="m3_quantidade_amostras"
    )

    tamanho_amostra = col_controle2.slider(
        "Tamanho de cada amostra:",
        min_value=2,
        max_value=100,
        value=30,
        step=1,
        key="m3_tamanho_amostra"
    )

    gerador_tcl = np.random.default_rng(seed=42)
    medias_amostrais = []

    for _ in range(quantidade_amostras):
        amostra = gerador_tcl.choice(
            dados_populacao,
            size=tamanho_amostra,
            replace=True
        )

        media_da_amostra = media(amostra.tolist())
        medias_amostrais.append(media_da_amostra)

    media_das_medias = media(medias_amostrais)
    diferenca_tcl = abs(media_das_medias - media_populacional)

    col_tcl1, col_tcl2, col_tcl3 = st.columns(3)

    col_tcl1.metric(
        "Quantidade de amostras",
        f"{quantidade_amostras:,}".replace(",", ".")
    )

    col_tcl2.metric(
        "Tamanho da amostra",
        tamanho_amostra
    )

    col_tcl3.metric(
        "Média das médias",
        f"{media_das_medias:.4f}"
    )

    # Erro padrão teórico da média.
    erro_padrao = desvio_populacional / np.sqrt(tamanho_amostra)

    fig_tcl, ax_tcl = plt.subplots(figsize=(9, 4))

    ax_tcl.hist(
        medias_amostrais,
        bins=30,
        density=True,
        edgecolor="black",
        alpha=0.7,
        label="Médias amostrais simuladas"
    )

    if erro_padrao > 0:
        x_normal = np.linspace(
            min(medias_amostrais),
            max(medias_amostrais),
            300
        )

        y_normal = norm.pdf(
            x_normal,
            loc=media_populacional,
            scale=erro_padrao
        )

        ax_tcl.plot(
            x_normal,
            y_normal,
            linewidth=2,
            label="Normal teórica"
        )

    ax_tcl.axvline(
        x=media_populacional,
        linestyle="--",
        linewidth=2,
        label="Média da população"
    )

    ax_tcl.set_title(
        "TCL — distribuição das médias amostrais — " + nome_populacao
    )
    ax_tcl.set_xlabel("Média da amostra")
    ax_tcl.set_ylabel("Densidade")
    ax_tcl.legend()
    ax_tcl.grid(axis="y", alpha=0.3)
    fig_tcl.tight_layout()

    st.pyplot(fig_tcl)
    plt.close(fig_tcl)

    st.write(
        f"A média das **{quantidade_amostras:,} médias amostrais** foi "
        f"**{media_das_medias:.4f}**. A média da população é "
        f"**{media_populacional:.4f}**, resultando em diferença absoluta "
        f"de **{diferenca_tcl:.4f}**."
        .replace(",", ".")
    )

    st.info(
        "O histograma representa as médias obtidas nas várias amostras. "
        "A curva sobreposta representa a distribuição Normal teórica esperada. "
        "À medida que o tamanho das amostras aumenta, a distribuição das médias "
        "amostrais tende a apresentar comportamento aproximadamente Normal e "
        "a se concentrar em torno da média da população."
    )

    # ============================================================
    # 3.3 - COMPARAÇÃO ENTRE TAMANHOS DE AMOSTRA
    # ============================================================
    st.divider()
    st.subheader("Comparação entre tamanhos de amostra")

    st.write(
        "Para observar o efeito do tamanho da amostra, repetimos a simulação "
        "com amostras de tamanhos 2, 10, 30 e 100."
    )

    tamanhos_comparacao = [2, 10, 30, 100]
    quantidade_comparacao = 1000
    gerador_comparacao = np.random.default_rng(seed=123)

    fig_comparacao, ax_comparacao = plt.subplots(figsize=(9, 5))

    for tamanho in tamanhos_comparacao:
        medias_comparacao = []

        for _ in range(quantidade_comparacao):
            amostra = gerador_comparacao.choice(
                dados_populacao,
                size=tamanho,
                replace=True
            )

            medias_comparacao.append(
                media(amostra.tolist())
            )

        ax_comparacao.hist(
            medias_comparacao,
            bins=30,
            density=True,
            histtype="step",
            linewidth=1.5,
            label=f"n = {tamanho}"
        )

    ax_comparacao.axvline(
        x=media_populacional,
        linestyle="--",
        linewidth=2,
        label="Média da população"
    )

    ax_comparacao.set_title(
        "TCL — efeito do tamanho da amostra — " + nome_populacao
    )
    ax_comparacao.set_xlabel("Média da amostra")
    ax_comparacao.set_ylabel("Densidade")
    ax_comparacao.legend()
    ax_comparacao.grid(axis="y", alpha=0.3)
    fig_comparacao.tight_layout()

    st.pyplot(fig_comparacao)
    plt.close(fig_comparacao)

    st.success(
        "A comparação mostra que, conforme o tamanho da amostra aumenta, "
        "as médias amostrais tendem a ficar mais concentradas em torno da "
        "média da população. Isso corresponde à redução do erro padrão da média."
    )

    # ============================================================
    # CONCLUSÃO DO MÓDULO 3
    # ============================================================
    st.markdown("### Conclusão do Módulo 3")

    if fonte_simulacao == "Dados reais da PRF 2025":
        st.write(
            f"Nesta execução, a LGN e o TCL foram demonstrados utilizando "
            f"a variável real **{variavel_simulacao}** do arquivo "
            f"**datatran2025.csv**. Dessa forma, os conceitos probabilísticos "
            f"são relacionados diretamente ao conjunto de dados estudado no projeto."
        )
    else:
        st.write(
            "Nesta execução foi utilizado o exemplo didático do dado de seis faces, "
            "mantido como referência clássica para a LGN e o TCL."
        )

    st.markdown(
        """
        **Lei dos Grandes Números:** conforme aumentamos a quantidade de
        observações, a média observada tende a se aproximar da média da população.

        **Teorema Central do Limite:** ao retirarmos repetidas amostras e
        calcularmos suas médias, a distribuição dessas médias tende a apresentar
        comportamento aproximadamente Normal e a se concentrar em torno da média
        da população.
        """
    )

with aba_modulo4:
    # MÓDULO 4 — DISTRIBUIÇÕES TEÓRICAS
    # ============================================================

    st.divider()

    st.header("Módulo 4 — Distribuições Teóricas")

    st.write(
        "Nesta seção comparamos a distribuição observada nos dados "
        "reais da PRF 2025 com distribuições teóricas de probabilidade."
    )

    st.write(
        "O objetivo é verificar visualmente como determinados modelos "
        "probabilísticos se aproximam do comportamento observado nos dados."
    )


    # ============================================================
    # SELEÇÃO DA VARIÁVEL
    # ============================================================

    st.subheader("Seleção da variável numérica")

    st.write(
        "Escolha uma variável numérica da base de acidentes para "
        "comparar sua distribuição com modelos teóricos."
    )

    variaveis_modulo4 = [
        "pessoas",
        "mortos",
        "feridos_leves",
        "feridos_graves",
        "ilesos",
        "ignorados",
        "feridos",
        "veiculos"
    ]

    variavel_modulo4 = st.selectbox(
        "Variável para análise:",
        variaveis_modulo4,
        key="variavel_modulo4"
    )


    # ============================================================
    # PREPARAÇÃO DOS DADOS
    # ============================================================

    # Retiramos possíveis valores ausentes e transformamos
    # os dados em uma lista Python.
    #
    # A manipulação dos dados pode ser feita com Pandas.
    # As medidas estatísticas exibidas continuarão sendo
    # calculadas pelo nosso núcleo minhastats.py.

    dados_modulo4 = (
        df[variavel_modulo4]
        .dropna()
        .tolist()
    )


    # ============================================================
    # INFORMAÇÕES BÁSICAS
    # ============================================================

    st.subheader("Informações da variável selecionada")

    media_modulo4 = media(dados_modulo4)
    mediana_modulo4 = mediana(dados_modulo4)
    desvio_modulo4 = desvio_padrao_populacional(dados_modulo4)

    col1_m4, col2_m4, col3_m4 = st.columns(3)

    col1_m4.metric(
        "Média",
        f"{media_modulo4:.4f}"
    )

    col2_m4.metric(
        "Mediana",
        f"{mediana_modulo4:.4f}"
    )

    col3_m4.metric(
        "Desvio padrão populacional",
        f"{desvio_modulo4:.4f}"
    )

    st.write(
        f"Quantidade de observações analisadas: "
        f"**{len(dados_modulo4):,}**".replace(",", ".")
    )

    # ============================================================
    # MÓDULO 4.2
    # HISTOGRAMA DOS DADOS REAIS + DISTRIBUIÇÃO NORMAL TEÓRICA
    # ============================================================

    st.subheader("Comparação com a Distribuição Normal")

    st.write(
        "O histograma representa a distribuição observada nos dados reais. "
        "Sobre ele será desenhada uma curva Normal teórica utilizando a "
        "média e o desvio padrão da variável selecionada."
    )

    # ------------------------------------------------------------
    # Importação da distribuição Normal
    # ------------------------------------------------------------
    # A biblioteca scipy será utilizada apenas para obter a função
    # de densidade da distribuição Normal teórica.
    #
    # IMPORTANTE:
    # A média e o desvio padrão utilizados na curva continuam sendo
    # calculados pelo nosso próprio núcleo estatístico (minhastats.py).
    # ------------------------------------------------------------

    from scipy.stats import norm


    # ------------------------------------------------------------
    # PREPARAÇÃO DO EIXO X
    # ------------------------------------------------------------
    # Criamos vários valores igualmente espaçados entre o menor e
    # o maior valor observado na variável.
    #
    # Esses pontos serão usados para desenhar a curva Normal.
    # ------------------------------------------------------------

    valor_minimo = min(dados_modulo4)
    valor_maximo = max(dados_modulo4)

    eixo_x_normal = np.linspace(
        valor_minimo,
        valor_maximo,
        500
    )


    # ------------------------------------------------------------
    # CÁLCULO DA DENSIDADE DA DISTRIBUIÇÃO NORMAL
    # ------------------------------------------------------------
    # A curva Normal será construída usando:
    #
    # loc   = média da variável
    # scale = desvio padrão populacional
    #
    # Os dois valores foram calculados anteriormente utilizando
    # funções próprias do arquivo minhastats.py.
    # ------------------------------------------------------------

    densidade_normal = norm.pdf(
        eixo_x_normal,
        loc=media_modulo4,
        scale=desvio_modulo4
    )


    # ------------------------------------------------------------
    # CRIAÇÃO DO GRÁFICO
    # ------------------------------------------------------------

    fig_normal, ax_normal = plt.subplots(
        figsize=(9, 4.5)
    )


    # ------------------------------------------------------------
    # HISTOGRAMA DOS DADOS REAIS
    # ------------------------------------------------------------
    # density=True transforma as frequências em densidade.
    #
    # Isso é necessário para que o histograma e a curva Normal
    # possam ser comparados na mesma escala.
    # ------------------------------------------------------------

    ax_normal.hist(
        dados_modulo4,
        bins=30,
        density=True,
        alpha=0.65,
        edgecolor="black",
        label="Dados observados"
    )


    # ------------------------------------------------------------
    # CURVA NORMAL TEÓRICA
    # ------------------------------------------------------------

    ax_normal.plot(
        eixo_x_normal,
        densidade_normal,
        linewidth=3,
        label="Distribuição Normal teórica"
    )


    # ------------------------------------------------------------
    # LINHA VERTICAL REPRESENTANDO A MÉDIA
    # ------------------------------------------------------------

    ax_normal.axvline(
        media_modulo4,
        linestyle="--",
        linewidth=2,
        label=f"Média = {media_modulo4:.2f}"
    )


    # ------------------------------------------------------------
    # TÍTULO E IDENTIFICAÇÃO DOS EIXOS
    # ------------------------------------------------------------

    ax_normal.set_title(
        f"Dados observados × Distribuição Normal — {variavel_modulo4}"
    )

    ax_normal.set_xlabel(variavel_modulo4)

    ax_normal.set_ylabel("Densidade")

    ax_normal.legend()

    ax_normal.grid(
        alpha=0.20
    )

    fig_normal.tight_layout()


    # ------------------------------------------------------------
    # EXIBIÇÃO NO STREAMLIT
    # ------------------------------------------------------------

    st.pyplot(
        fig_normal,
        use_container_width=True
    )

    plt.close(fig_normal)

    # ============================================================
    # MÓDULO 4.3
    # COMPARAÇÃO COM A DISTRIBUIÇÃO DE POISSON
    # ============================================================

    st.subheader("Comparação com a Distribuição de Poisson")

    st.write(
        "Como a variável selecionada representa uma contagem, "
        "também podemos compará-la com a Distribuição de Poisson. "
        "Na distribuição de Poisson, o parâmetro λ (lambda) "
        "corresponde à média esperada da variável."
    )


    # ------------------------------------------------------------
    # IMPORTAÇÃO DA DISTRIBUIÇÃO DE POISSON
    # ------------------------------------------------------------

    from scipy.stats import poisson


    # ------------------------------------------------------------
    # PARÂMETRO LAMBDA
    # ------------------------------------------------------------
    # Na distribuição de Poisson:
    #
    # lambda = média da distribuição
    #
    # Utilizamos a média calculada anteriormente pelo nosso
    # próprio núcleo estatístico minhastats.py.
    # ------------------------------------------------------------

    lambda_poisson = media_modulo4


    # ------------------------------------------------------------
    # VALORES INTEIROS PARA A DISTRIBUIÇÃO DE POISSON
    # ------------------------------------------------------------
    # Diferentemente da Normal, a Poisson é uma distribuição
    # discreta. Por isso trabalhamos com valores inteiros:
    #
    # 0, 1, 2, 3, 4, ...
    # ------------------------------------------------------------

    valor_maximo_poisson = int(max(dados_modulo4))

    eixo_x_poisson = np.arange(
        0,
        valor_maximo_poisson + 1
    )


    # ------------------------------------------------------------
    # PROBABILIDADES TEÓRICAS DA POISSON
    # ------------------------------------------------------------
    # pmf significa Probability Mass Function.
    #
    # Ela fornece a probabilidade teórica correspondente
    # a cada valor inteiro da distribuição.
    # ------------------------------------------------------------

    probabilidade_poisson = poisson.pmf(
        eixo_x_poisson,
        mu=lambda_poisson
    )


    # ------------------------------------------------------------
    # CRIAÇÃO DO GRÁFICO
    # ------------------------------------------------------------

    fig_poisson, ax_poisson = plt.subplots(
        figsize=(9, 4.5)
    )


    # ------------------------------------------------------------
    # HISTOGRAMA DOS DADOS OBSERVADOS
    # ------------------------------------------------------------

    ax_poisson.hist(
        dados_modulo4,
        bins=np.arange(
            -0.5,
            valor_maximo_poisson + 1.5,
            1
        ),
        density=True,
        alpha=0.60,
        edgecolor="black",
        label="Dados observados"
    )


    # ------------------------------------------------------------
    # DISTRIBUIÇÃO DE POISSON TEÓRICA
    # ------------------------------------------------------------
    # Como a Poisson é discreta, utilizamos pontos e hastes
    # em vez de uma curva contínua.
    # ------------------------------------------------------------

    ax_poisson.stem(
        eixo_x_poisson,
        probabilidade_poisson,
        linefmt="C1-",
        markerfmt="C1o",
        basefmt=" ",
        label="Distribuição de Poisson"
    )


    # ------------------------------------------------------------
    # CONFIGURAÇÃO DO GRÁFICO
    # ------------------------------------------------------------

    ax_poisson.set_title(
        f"Dados observados × Distribuição de Poisson — "
        f"{variavel_modulo4}"
    )

    ax_poisson.set_xlabel(
        variavel_modulo4
    )

    ax_poisson.set_ylabel(
        "Probabilidade / densidade"
    )

    ax_poisson.legend()

    ax_poisson.grid(
        alpha=0.20
    )

    fig_poisson.tight_layout()


    # ------------------------------------------------------------
    # EXIBIÇÃO NO STREAMLIT
    # ------------------------------------------------------------

    st.pyplot(
        fig_poisson,
        use_container_width=True
    )

    plt.close(fig_poisson)


    # ------------------------------------------------------------
    # INFORMAÇÃO SOBRE O PARÂMETRO DA POISSON
    # ------------------------------------------------------------

    st.write(
        f"Parâmetro da Distribuição de Poisson: "
        f"**λ = {lambda_poisson:.4f}**"
    )

    # ============================================================
    # MÓDULO 4.4
    # INTERPRETAÇÃO DAS DISTRIBUIÇÕES TEÓRICAS
    # ============================================================

    st.subheader("Interpretação das distribuições teóricas")

    st.write(
        f"A variável analisada é **{variavel_modulo4}**, "
        f"com média igual a **{media_modulo4:.4f}** e "
        f"mediana igual a **{mediana_modulo4:.4f}**."
    )


    # ------------------------------------------------------------
    # COMPARAÇÃO ENTRE MÉDIA E MEDIANA
    # ------------------------------------------------------------
    # A relação entre média e mediana ajuda a observar
    # a assimetria da distribuição.
    #
    # Média > mediana:
    #     indicação de assimetria à direita.
    #
    # Média < mediana:
    #     indicação de assimetria à esquerda.
    #
    # Média aproximadamente igual à mediana:
    #     distribuição mais próxima da simetria.
    # ------------------------------------------------------------

    if media_modulo4 > mediana_modulo4:

        st.info(
            "A média é maior que a mediana. Isso indica uma "
            "assimetria à direita: existem valores elevados que "
            "estendem a cauda da distribuição e aumentam a média."
        )

    elif media_modulo4 < mediana_modulo4:

        st.info(
            "A média é menor que a mediana. Isso indica uma "
            "possível assimetria à esquerda."
        )

    else:

        st.info(
            "A média e a mediana são iguais, indicando uma "
            "distribuição mais próxima da simetria."
        )


    # ------------------------------------------------------------
    # INTERPRETAÇÃO DA DISTRIBUIÇÃO NORMAL
    # ------------------------------------------------------------

    st.markdown("### Distribuição Normal")

    st.write(
        "A Distribuição Normal é contínua e simétrica em torno "
        "da média. No gráfico, entretanto, os dados observados "
        "apresentam forte concentração nos valores menores e "
        "uma cauda em direção aos valores maiores."
    )

    st.warning(
        "Portanto, para a variável selecionada, a Distribuição "
        "Normal não apresenta um ajuste visual muito adequado "
        "aos dados observados."
    )


    # ------------------------------------------------------------
    # INTERPRETAÇÃO DA DISTRIBUIÇÃO DE POISSON
    # ------------------------------------------------------------

    st.markdown("### Distribuição de Poisson")

    st.write(
        "A Distribuição de Poisson é uma distribuição discreta "
        "utilizada para representar contagens. Por esse motivo, "
        "ela é uma candidata mais natural para variáveis que "
        "representam quantidades inteiras."
    )

    st.write(
        f"Para esta comparação foi utilizado "
        f"**λ = {lambda_poisson:.4f}**, correspondente à média "
        f"observada da variável."
    )

    st.info(
        "Visualmente, a Distribuição de Poisson consegue representar "
        "parte da concentração existente nos valores menores. "
        "Entretanto, também existem diferenças entre o modelo "
        "teórico e os dados reais, principalmente na cauda da "
        "distribuição."
    )


    # ------------------------------------------------------------
    # CONCLUSÃO DA COMPARAÇÃO
    # ------------------------------------------------------------

    st.markdown("### Conclusão da comparação")

    st.success(
        "A comparação mostra que uma distribuição teórica é um "
        "modelo aproximado do comportamento dos dados. Para a "
        "variável analisada, a Distribuição Normal apresenta "
        "limitações devido à assimetria dos dados. A Distribuição "
        "de Poisson é conceitualmente mais apropriada para uma "
        "variável de contagem, mas também não reproduz perfeitamente "
        "todos os valores observados."
    )

    st.write(
        "Assim, os gráficos não devem ser interpretados como prova "
        "de que os dados seguem exatamente uma determinada "
        "distribuição, mas como uma comparação entre os dados reais "
        "e modelos probabilísticos teóricos."
    )

    # ============================================================

with aba_modulo5:
    # MÓDULO 5
    # CORRELAÇÃO E REGRESSÃO LINEAR
    # ============================================================

    st.divider()

    st.header("Módulo 5 — Correlação e Regressão Linear")

    st.write(
        "Nesta seção analisamos a relação entre duas variáveis "
        "numéricas da base de acidentes da PRF 2025."
    )

    st.write(
        "O objetivo é verificar se existe associação linear entre "
        "as variáveis e construir um modelo de regressão linear simples."
    )


    # ============================================================
    # MÓDULO 5.1
    # SELEÇÃO DAS VARIÁVEIS
    # ============================================================

    st.subheader("Seleção das variáveis")

    st.write(
        "Escolha duas variáveis numéricas para realizar a análise."
    )


    # ------------------------------------------------------------
    # VARIÁVEIS DISPONÍVEIS
    # ------------------------------------------------------------
    # Estamos utilizando variáveis numéricas que representam
    # quantidades registradas em cada ocorrência da PRF.
    # ------------------------------------------------------------

    variaveis_modulo5 = [
        "pessoas",
        "mortos",
        "feridos_leves",
        "feridos_graves",
        "ilesos",
        "ignorados",
        "feridos",
        "veiculos"
    ]


    # ------------------------------------------------------------
    # SELEÇÃO DA VARIÁVEL X
    # ------------------------------------------------------------
    # X será considerada a variável explicativa na regressão.
    # ------------------------------------------------------------

    variavel_x = st.selectbox(
        "Variável X:",
        variaveis_modulo5,
        index=7,
        key="variavel_x_modulo5"
    )


    # ------------------------------------------------------------
    # SELEÇÃO DA VARIÁVEL Y
    # ------------------------------------------------------------
    # Y será considerada a variável resposta.
    #
    # Começamos com "pessoas" para que a tela inicialmente
    # apresente a relação entre veículos e pessoas.
    # ------------------------------------------------------------

    variavel_y = st.selectbox(
        "Variável Y:",
        variaveis_modulo5,
        index=0,
        key="variavel_y_modulo5"
    )


    # ------------------------------------------------------------
    # VERIFICAÇÃO DAS VARIÁVEIS
    # ------------------------------------------------------------
    # Não faz muito sentido calcular a correlação de uma variável
    # com ela mesma. Por isso mostramos um aviso caso X e Y sejam
    # iguais.
    # ------------------------------------------------------------

    if variavel_x == variavel_y:

        st.warning(
            "Selecione duas variáveis diferentes para realizar "
            "a análise de correlação e regressão."
        )

    else:

        st.write(
            f"Variável explicativa **X:** {variavel_x}"
        )

        st.write(
            f"Variável resposta **Y:** {variavel_y}"
        )


        # --------------------------------------------------------
        # PREPARAÇÃO DOS DADOS
        # --------------------------------------------------------
        # Selecionamos somente as duas colunas escolhidas.
        #
        # O dropna() remove registros que eventualmente possuam
        # valor ausente em uma das duas variáveis.
        #
        # É importante fazer isso em conjunto para manter cada
        # valor de X associado ao Y da MESMA ocorrência.
        # --------------------------------------------------------

        dados_regressao = (
            df[[variavel_x, variavel_y]]
            .dropna()
        )


        # --------------------------------------------------------
        # CONVERSÃO PARA LISTAS
        # --------------------------------------------------------
        # As nossas funções do minhastats.py trabalham com
        # sequências numéricas. Por isso transformamos as colunas
        # do Pandas em listas.
        # --------------------------------------------------------

        dados_x = dados_regressao[variavel_x].tolist()

        dados_y = dados_regressao[variavel_y].tolist()


        # --------------------------------------------------------
        # INFORMAÇÕES DA ANÁLISE
        # --------------------------------------------------------

        st.subheader("Dados utilizados na análise")

        coluna_x, coluna_y, coluna_total = st.columns(3)

        coluna_x.metric(
            "Variável X",
            variavel_x
        )

        coluna_y.metric(
            "Variável Y",
            variavel_y
        )

        coluna_total.metric(
            "Quantidade de pares",
            f"{len(dados_regressao):,}".replace(",", ".")
        )


        # --------------------------------------------------------
        # PRÉVIA DOS PARES X E Y
        # --------------------------------------------------------
        # Aqui mostramos somente as 10 primeiras ocorrências.
        #
        # IMPORTANTE:
        # assim como fizemos no Módulo 2, isso é apenas uma
        # visualização. Os cálculos posteriores utilizarão TODOS
        # os registros disponíveis.
        # --------------------------------------------------------

        st.write(
            "Prévia dos primeiros pares de valores utilizados "
            "na análise:"
        )

        st.dataframe(
            dados_regressao.head(10),
            use_container_width=True
        )

        st.caption(
            "A tabela apresenta somente os 10 primeiros registros. "
            "Os cálculos de correlação e regressão utilizarão todos "
            "os pares de dados disponíveis."
        )

            # ========================================================
        # MÓDULO 5.2
        # GRÁFICO DE DISPERSÃO
        # ========================================================

        st.subheader("Gráfico de dispersão")

        st.write(
            "O gráfico de dispersão permite observar visualmente "
            "como os valores das duas variáveis se relacionam."
        )

        st.write(
            f"Cada ponto representa uma ocorrência da PRF, onde "
            f"o eixo X representa **{variavel_x}** e o eixo Y "
            f"representa **{variavel_y}**."
        )


        # --------------------------------------------------------
        # CRIAÇÃO DO GRÁFICO
        # --------------------------------------------------------
        # O gráfico de dispersão utiliza um ponto para representar
        # cada par de valores X e Y.
        #
        # Como a base possui mais de 72 mil ocorrências, muitos
        # pontos podem ficar exatamente sobrepostos.
        #
        # Por isso usamos:
        #
        # alpha = 0.20
        #
        # Esse parâmetro deixa os pontos parcialmente transparentes.
        # Regiões onde existem muitos registros sobrepostos ficam
        # visualmente mais intensas.
        # --------------------------------------------------------

        fig_disp, ax_disp = plt.subplots(
            figsize=(9, 4.5)
        )

        ax_disp.scatter(
            dados_x,
            dados_y,
            alpha=0.20,
            s=15
        )


        # --------------------------------------------------------
        # TÍTULO E IDENTIFICAÇÃO DOS EIXOS
        # --------------------------------------------------------

        ax_disp.set_title(
            f"Dispersão entre {variavel_x} e {variavel_y}"
        )

        ax_disp.set_xlabel(
            variavel_x
        )

        ax_disp.set_ylabel(
            variavel_y
        )


        # --------------------------------------------------------
        # GRADE
        # --------------------------------------------------------
        # A grade facilita a leitura aproximada dos valores.
        # --------------------------------------------------------

        ax_disp.grid(
            alpha=0.25
        )


        # --------------------------------------------------------
        # AJUSTE DO LAYOUT
        # --------------------------------------------------------

        fig_disp.tight_layout()


        # --------------------------------------------------------
        # EXIBIÇÃO NO STREAMLIT
        # --------------------------------------------------------

        st.pyplot(
            fig_disp,
            use_container_width=True
        )

        plt.close(fig_disp)


        # --------------------------------------------------------
        # EXPLICAÇÃO
        # --------------------------------------------------------

        st.info(
            "Cada ponto do gráfico corresponde a uma ocorrência. "
            "Quando vários registros possuem os mesmos valores de "
            "X e Y, os pontos ficam sobrepostos. A transparência "
            "ajuda a identificar as regiões com maior concentração "
            "de ocorrências."
        )

        # ========================================================
        # MÓDULO 5.3
        # CORRELAÇÃO DE PEARSON
        # ========================================================

        st.subheader("Correlação de Pearson")

        st.write(
            "O coeficiente de correlação de Pearson mede a "
            "intensidade e a direção da relação linear entre "
            "duas variáveis numéricas."
        )


        # --------------------------------------------------------
        # CÁLCULO DA CORRELAÇÃO
        # --------------------------------------------------------
        # IMPORTANTE:
        #
        # O cálculo abaixo NÃO utiliza a função pronta do Pandas,
        # NumPy ou SciPy.
        #
        # Estamos utilizando a função correlacao_pearson()
        # desenvolvida por nós no arquivo minhastats.py.
        #
        # Isso atende ao requisito do trabalho de utilizar
        # o nosso próprio núcleo estatístico.
        # --------------------------------------------------------

        valor_correlacao = correlacao_pearson(
            dados_x,
            dados_y
        )


        # --------------------------------------------------------
        # EXIBIÇÃO DO RESULTADO
        # --------------------------------------------------------

        st.metric(
            "Coeficiente de correlação de Pearson (r)",
            f"{valor_correlacao:.4f}"
        )


        # --------------------------------------------------------
        # CLASSIFICAÇÃO DIDÁTICA DA INTENSIDADE DA CORRELAÇÃO
        #
        # Utilizamos o mesmo critério em todo o Módulo 5
        # para evitar interpretações diferentes do mesmo valor.
        # --------------------------------------------------------

        correlacao_absoluta = abs(valor_correlacao)

        if correlacao_absoluta < 0.20:
            intensidade = "muito fraca"

        elif correlacao_absoluta < 0.40:
            intensidade = "fraca"

        elif correlacao_absoluta < 0.60:
            intensidade = "moderada"

        elif correlacao_absoluta < 0.80:
            intensidade = "forte"

        else:
            intensidade = "muito forte"


        # --------------------------------------------------------
        # INTERPRETAÇÃO DA DIREÇÃO
        # --------------------------------------------------------

        if valor_correlacao > 0:
            direcao = "positiva"

        elif valor_correlacao < 0:
            direcao = "negativa"

        else:
            direcao = "nula"


        # --------------------------------------------------------
        # TEXTO AUTOMÁTICO DE INTERPRETAÇÃO
        # --------------------------------------------------------

        st.write(
            f"O coeficiente calculado foi **r = "
            f"{valor_correlacao:.4f}**."
        )

        st.info(
            f"Considerando a classificação didática utilizada "
            f"neste projeto, existe uma correlação linear "
            f"**{intensidade} e {direcao}** entre "
            f"**{variavel_x}** e **{variavel_y}**."
        )

        st.warning(
            "Correlação não implica causalidade. "
            "A existência de associação entre duas variáveis "
            "não permite concluir, por si só, que alterações "
            "em uma variável sejam a causa das alterações "
            "observadas na outra."
        )


        # --------------------------------------------------------
        # ALERTA IMPORTANTE
        # --------------------------------------------------------
        # Correlação não significa causalidade.
        #
        # Mesmo quando duas variáveis apresentam correlação,
        # isso não demonstra que uma delas seja a causa da outra.
        # --------------------------------------------------------

        st.warning(
            "Correlação não implica causalidade. "
            "A existência de associação entre duas variáveis "
            "não permite concluir, por si só, que alterações "
            "em uma variável sejam a causa das alterações "
            "observadas na outra."
        )

        # ========================================================
        # MÓDULO 5.4
        # REGRESSÃO LINEAR SIMPLES
        # ========================================================

        st.subheader("Regressão Linear Simples")

        st.write(
            "A regressão linear simples procura representar a "
            "relação entre as duas variáveis por meio de uma reta."
        )

        st.write(
            f"Nesta análise, **{variavel_x}** será utilizada como "
            f"variável explicativa (X) e **{variavel_y}** como "
            f"variável resposta (Y)."
        )


        # --------------------------------------------------------
        # CÁLCULO DOS COEFICIENTES DA RETA
        # --------------------------------------------------------
        # A função regressao_linear() foi desenvolvida por nós
        # no arquivo minhastats.py.
        #
        # Ela utiliza o método dos mínimos quadrados para calcular:
        #
        # intercepto  -> valor de "a"
        # inclinacao  -> valor de "b"
        #
        # A equação resultante é:
        #
        # Y = a + bX
        # --------------------------------------------------------

        intercepto, inclinacao = regressao_linear(
            dados_x,
            dados_y
        )


        # --------------------------------------------------------
        # EXIBIÇÃO DOS COEFICIENTES
        # --------------------------------------------------------

        coluna_reg1, coluna_reg2 = st.columns(2)

        coluna_reg1.metric(
            "Intercepto (a)",
            f"{intercepto:.4f}"
        )

        coluna_reg2.metric(
            "Inclinação (b)",
            f"{inclinacao:.4f}"
        )


        # --------------------------------------------------------
        # EQUAÇÃO DA RETA
        # --------------------------------------------------------

        st.write("**Equação estimada da regressão:**")

        if intercepto >= 0:

            st.code(
                f"{variavel_y} = {intercepto:.4f} "
                f"+ ({inclinacao:.4f} × {variavel_x})"
            )

        else:

            st.code(
                f"{variavel_y} = {intercepto:.4f} "
                f"+ ({inclinacao:.4f} × {variavel_x})"
            )


        # --------------------------------------------------------
        # INTERPRETAÇÃO DA INCLINAÇÃO
        # --------------------------------------------------------
        # O coeficiente b informa quanto Y tende a variar
        # quando X aumenta uma unidade.
        # --------------------------------------------------------

        if inclinacao > 0:

            st.info(
                f"A inclinação é positiva. Segundo o modelo linear, "
                f"quando **{variavel_x}** aumenta uma unidade, "
                f"**{variavel_y}** apresenta um aumento médio estimado "
                f"de aproximadamente **{inclinacao:.4f}** unidade(s)."
            )

        elif inclinacao < 0:

            st.info(
                f"A inclinação é negativa. Segundo o modelo linear, "
                f"quando **{variavel_x}** aumenta uma unidade, "
                f"**{variavel_y}** apresenta uma redução média estimada "
                f"de aproximadamente **{abs(inclinacao):.4f}** unidade(s)."
            )

        else:

            st.info(
                "A inclinação calculada foi igual a zero. "
                "Neste caso, o modelo linear não indica variação média "
                "da variável resposta em função da variável explicativa."
            )

        # ========================================================
        # MÓDULO 5.5
        # GRÁFICO DE DISPERSÃO COM RETA DE REGRESSÃO
        # ========================================================

        st.subheader("Reta de regressão sobre o gráfico de dispersão")

        st.write(
            "O gráfico abaixo apresenta novamente os dados observados, "
            "agora acompanhados pela reta estimada pelo modelo de "
            "regressão linear simples."
        )


        # --------------------------------------------------------
        # CRIAÇÃO DO GRÁFICO
        # --------------------------------------------------------

        fig_regressao, ax_regressao = plt.subplots(
            figsize=(10, 6)
        )


        # --------------------------------------------------------
        # PONTOS OBSERVADOS
        # --------------------------------------------------------
        # Cada ponto corresponde a uma ocorrência existente
        # na base de acidentes da PRF.
        # --------------------------------------------------------

        ax_regressao.scatter(
            dados_x,
            dados_y,
            alpha=0.25,
            label="Dados observados"
        )


        # --------------------------------------------------------
        # VALORES DE X PARA DESENHAR A RETA
        # --------------------------------------------------------
        # Para desenhar a reta precisamos apenas do menor
        # e do maior valor de X.
        # --------------------------------------------------------

        x_min = min(dados_x)
        x_max = max(dados_x)

        x_reta = [
            x_min,
            x_max
        ]


        # --------------------------------------------------------
        # CÁLCULO DOS VALORES DE Y DA RETA
        # --------------------------------------------------------
        # Utilizamos exatamente a equação calculada anteriormente:
        #
        # Y = intercepto + inclinacao * X
        # --------------------------------------------------------

        y_reta = [
            intercepto + inclinacao * x_min,
            intercepto + inclinacao * x_max
        ]


        # --------------------------------------------------------
        # DESENHO DA RETA DE REGRESSÃO
        # --------------------------------------------------------

        ax_regressao.plot(
            x_reta,
            y_reta,
            linewidth=2.5,
            label="Reta de regressão"
        )


        # --------------------------------------------------------
        # CONFIGURAÇÕES VISUAIS
        # --------------------------------------------------------

        ax_regressao.set_title(
            f"Regressão linear entre {variavel_x} e {variavel_y}"
        )

        ax_regressao.set_xlabel(
            variavel_x
        )

        ax_regressao.set_ylabel(
            variavel_y
        )

        ax_regressao.grid(
            alpha=0.25
        )

        ax_regressao.legend()


        # --------------------------------------------------------
        # EXIBIÇÃO NO STREAMLIT
        # --------------------------------------------------------

        st.pyplot(
            fig_regressao,
            use_container_width=True
        )

        plt.close(
            fig_regressao
        )


        # --------------------------------------------------------
        # INTERPRETAÇÃO DO GRÁFICO
        # --------------------------------------------------------
        # Calculamos novamente a correlação utilizando nossa própria
        # função do arquivo minhastats.py.
        #
        # Fazemos isso para que esta parte do código não dependa
        # do nome de uma variável criada anteriormente no app.py.
        # --------------------------------------------------------

        valor_correlacao_grafico = correlacao_pearson(
            dados_x,
            dados_y
        )

        st.info(
            f"A reta representa os valores médios estimados de "
            f"**{variavel_y}** pelo modelo para diferentes valores de "
            f"**{variavel_x}**. Os pontos afastados da reta mostram que "
            f"a relação não é perfeitamente linear, o que é compatível "
            f"com a correlação de Pearson calculada anteriormente "
            f"(r = {valor_correlacao_grafico:.4f})."
        )


    # ============================================================
    # 5.6 - COEFICIENTE DE DETERMINAÇÃO (R²)
    # ============================================================

    st.subheader("Coeficiente de Determinação — R²")

    st.write(
        "O coeficiente de determinação R² indica qual proporção da "
        "variação da variável resposta Y pode ser explicada pelo "
        "modelo de regressão linear simples."
    )

    # ------------------------------------------------------------
    # CÁLCULO DO R²
    #
    # No item 5.3 já calculamos a correlação de Pearson:
    #
    # valor_correlacao = correlacao_pearson(dados_x, dados_y)
    #
    # Na regressão linear simples com intercepto, o coeficiente
    # de determinação R² é igual ao quadrado da correlação de
    # Pearson.
    # ------------------------------------------------------------

    r_quadrado = valor_correlacao ** 2

    # ------------------------------------------------------------
    # EXIBIÇÃO DO RESULTADO
    # ------------------------------------------------------------

    st.metric(
        "Coeficiente de determinação (R²)",
        f"{r_quadrado:.4f}"
    )

    # Também mostramos em porcentagem para facilitar
    # a interpretação.
    percentual_explicado = r_quadrado * 100

    st.write(
        f"**R² = {r_quadrado:.4f}**, o que corresponde a "
        f"aproximadamente **{percentual_explicado:.2f}%**."
    )

    # ------------------------------------------------------------
    # INTERPRETAÇÃO
    # ------------------------------------------------------------

    st.info(
        f"No modelo de regressão linear simples entre "
        f"**{variavel_x}** e **{variavel_y}**, aproximadamente "
        f"**{percentual_explicado:.2f}%** da variação observada em "
        f"**{variavel_y}** pode ser explicada pela relação linear "
        f"com **{variavel_x}**."
    )

    st.warning(
        "O valor de R² não significa que a variável X causa as "
        "alterações observadas na variável Y. Ele mede apenas o "
        "quanto o modelo linear consegue explicar da variabilidade "
        "observada nos dados."
    )

    # ============================================================
    # 5.7 - PREVISÃO INTERATIVA
    # ============================================================

    st.subheader("Previsão Interativa")

    st.write(
        f"Utilizando a equação de regressão linear, podemos estimar "
        f"um valor de **{variavel_y}** a partir de um valor informado "
        f"para **{variavel_x}**."
    )

    # ------------------------------------------------------------
    # DEFINIÇÃO DOS LIMITES PARA O CAMPO DE ENTRADA
    #
    # Utilizamos os próprios valores observados da variável X
    # para determinar um intervalo adequado para a simulação.
    # ------------------------------------------------------------

    valor_minimo_x = float(min(dados_x))
    valor_maximo_x = float(max(dados_x))

    # ------------------------------------------------------------
    # CAMPO INTERATIVO
    #
    # O usuário informa um valor para a variável X.
    # ------------------------------------------------------------

    valor_x_previsao = st.number_input(
        f"Informe um valor para {variavel_x}:",
        min_value=valor_minimo_x,
        max_value=valor_maximo_x,
        value=valor_minimo_x,
        step=1.0
    )

    # ------------------------------------------------------------
    # CÁLCULO DA PREVISÃO
    #
    # Equação da regressão:
    #
    # Y = intercepto + inclinacao * X
    # ------------------------------------------------------------

    valor_y_previsto = (
        intercepto
        + inclinacao * valor_x_previsao
    )

    # ------------------------------------------------------------
    # EXIBIÇÃO DO RESULTADO
    # ------------------------------------------------------------

    st.metric(
        f"Valor estimado de {variavel_y}",
        f"{valor_y_previsto:.4f}"
    )

    st.write("**Cálculo realizado pelo modelo:**")

    st.code(
        f"{variavel_y} = "
        f"{intercepto:.4f} + "
        f"({inclinacao:.4f} × {valor_x_previsao:.2f})"
    )

    st.success(
        f"Para **{valor_x_previsao:.2f}** em **{variavel_x}**, "
        f"o modelo de regressão linear estima aproximadamente "
        f"**{valor_y_previsto:.4f}** para **{variavel_y}**."
    )

    st.info(
        "A previsão apresentada é uma estimativa produzida pelo "
        "modelo de regressão linear. Ela não representa necessariamente "
        "o valor que será observado em uma ocorrência real."
    )

    # ============================================================
    # 5.8 - INTERPRETAÇÃO E CONCLUSÃO DO MÓDULO 5
    # ============================================================

    st.subheader("Interpretação da análise")

    st.write(
        f"A análise investigou a relação entre **{variavel_x}** "
        f"e **{variavel_y}**, utilizando correlação de Pearson "
        f"e regressão linear simples."
    )

    # ------------------------------------------------------------
    # INTERPRETAÇÃO DA CORRELAÇÃO
    # ------------------------------------------------------------

    st.write(
        f"O coeficiente de correlação de Pearson encontrado foi "
        f"**r = {valor_correlacao:.4f}**."
    )

    if valor_correlacao > 0:
        direcao_relacao = "positiva"
    elif valor_correlacao < 0:
        direcao_relacao = "negativa"
    else:
        direcao_relacao = "nula"

    valor_absoluto_correlacao = abs(valor_correlacao)

    if valor_absoluto_correlacao < 0.20:
        intensidade_relacao = "muito fraca"
    elif valor_absoluto_correlacao < 0.40:
        intensidade_relacao = "fraca"
    elif valor_absoluto_correlacao < 0.60:
        intensidade_relacao = "moderada"
    elif valor_absoluto_correlacao < 0.80:
        intensidade_relacao = "forte"
    else:
        intensidade_relacao = "muito forte"

    st.info(
        f"A relação linear observada entre **{variavel_x}** e "
        f"**{variavel_y}** pode ser classificada, segundo o critério "
        f"didático utilizado neste projeto, como "
        f"**{intensidade_relacao} e {direcao_relacao}**."
    )

    # ------------------------------------------------------------
    # INTERPRETAÇÃO DA REGRESSÃO
    # ------------------------------------------------------------

    st.write("**Equação estimada pelo modelo:**")

    st.code(
        f"{variavel_y} = "
        f"{intercepto:.4f} + "
        f"({inclinacao:.4f} × {variavel_x})"
    )

    if inclinacao > 0:

        st.write(
            f"A inclinação positiva indica que, segundo o modelo, "
            f"quando **{variavel_x}** aumenta uma unidade, "
            f"o valor médio estimado de **{variavel_y}** aumenta "
            f"aproximadamente **{inclinacao:.4f}** unidade(s)."
        )

    elif inclinacao < 0:

        st.write(
            f"A inclinação negativa indica que, segundo o modelo, "
            f"quando **{variavel_x}** aumenta uma unidade, "
            f"o valor médio estimado de **{variavel_y}** diminui "
            f"aproximadamente **{abs(inclinacao):.4f}** unidade(s)."
        )

    else:

        st.write(
            "A inclinação calculada é igual a zero, indicando que "
            "o modelo linear não identifica alteração média em Y "
            "quando X aumenta."
        )

    # ------------------------------------------------------------
    # INTERPRETAÇÃO DO R²
    # ------------------------------------------------------------

    percentual_r2 = r_quadrado * 100

    st.write(
        f"O coeficiente de determinação encontrado foi "
        f"**R² = {r_quadrado:.4f}**, correspondente a "
        f"aproximadamente **{percentual_r2:.2f}%**."
    )

    st.write(
        f"Isso significa que, dentro deste modelo linear simples, "
        f"aproximadamente **{percentual_r2:.2f}% da variação de "
        f"{variavel_y}** está associada linearmente à variável "
        f"**{variavel_x}**."
    )

    # ------------------------------------------------------------
    # ALERTA SOBRE CAUSALIDADE
    # ------------------------------------------------------------

    st.warning(
        "Correlação não implica causalidade. Mesmo quando duas "
        "variáveis apresentam associação estatística, não podemos "
        "concluir apenas com esta análise que uma variável causa "
        "alterações na outra. Outros fatores podem influenciar "
        "os resultados observados."
    )

    # ------------------------------------------------------------
    # CONCLUSÃO DO MÓDULO
    # ------------------------------------------------------------

    st.subheader("Conclusão do Módulo 5")

    st.success(
        f"A análise entre **{variavel_x}** e **{variavel_y}** mostrou "
        f"uma correlação **{intensidade_relacao} e {direcao_relacao}**, "
        f"com r = {valor_correlacao:.4f}. "
        f"O modelo de regressão linear apresentou R² = "
        f"{r_quadrado:.4f}, indicando que aproximadamente "
        f"{percentual_r2:.2f}% da variação observada em "
        f"**{variavel_y}** está associada linearmente a "
        f"**{variavel_x}**."
    )

    st.write(
        "A regressão linear permite ainda realizar previsões com base "
        "na relação estimada entre as variáveis. Entretanto, os "
        "resultados devem ser interpretados como associações "
        "estatísticas e não como evidência de uma relação causal."
    )

    # ============================================================

with aba_modulo6:
    # MÓDULO 6 — DESCOBERTAS NOS DADOS
    # ============================================================

    st.divider()

    st.header("Módulo 6 — Descobertas nos Dados")

    st.write(
        "Nesta seção são apresentados três resultados considerados "
        "interessantes a partir das análises realizadas sobre os "
        "acidentes registrados pela PRF em 2025."
    )

    st.write(
        "As descobertas combinam análise descritiva, visualizações "
        "e resultados estatísticos obtidos nos módulos anteriores."
    )


    # ============================================================
    # DESCOBERTA 1
    # ACIDENTES POR UNIDADE DA FEDERAÇÃO
    # ============================================================

    st.subheader("Descoberta 1 — Estados com maior número de ocorrências")

    st.write(
        "A primeira análise procura identificar em quais Unidades da "
        "Federação foi registrada a maior quantidade de ocorrências "
        "de acidentes nas rodovias federais durante o ano de 2025."
    )


    # ------------------------------------------------------------
    # CONTAGEM DAS OCORRÊNCIAS POR UF
    # ------------------------------------------------------------
    # Cada linha do DataFrame representa uma ocorrência.
    # Portanto, contamos quantas linhas existem para cada UF.
    #
    # value_counts() é utilizado apenas para organizar e contar
    # os registros da base. Não estamos utilizando uma função
    # estatística pronta para substituir nossa biblioteca.
    # ------------------------------------------------------------

    ocorrencias_por_uf = (
        df["uf"]
        .value_counts()
        .sort_values(ascending=False)
    )


    # ------------------------------------------------------------
    # SELECIONAMOS AS 10 UFs COM MAIS OCORRÊNCIAS
    # ------------------------------------------------------------

    top_10_uf = ocorrencias_por_uf.head(10)


    # ------------------------------------------------------------
    # MOSTRAMOS AS TRÊS PRIMEIRAS POSIÇÕES
    # ------------------------------------------------------------

    primeira_uf = top_10_uf.index[0]
    primeiro_total = int(top_10_uf.iloc[0])

    segunda_uf = top_10_uf.index[1]
    segundo_total = int(top_10_uf.iloc[1])

    terceira_uf = top_10_uf.index[2]
    terceiro_total = int(top_10_uf.iloc[2])


    st.write("### As três UFs com mais ocorrências")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        f"1º — {primeira_uf}",
        f"{primeiro_total:,}".replace(",", ".")
    )

    col2.metric(
        f"2º — {segunda_uf}",
        f"{segundo_total:,}".replace(",", ".")
    )

    col3.metric(
        f"3º — {terceira_uf}",
        f"{terceiro_total:,}".replace(",", ".")
    )


    # ============================================================
    # GRÁFICO — 10 UFs COM MAIS OCORRÊNCIAS
    # ============================================================

    st.write("### Ranking das 10 UFs com mais ocorrências")

    st.write(
        "O gráfico abaixo apresenta as dez Unidades da Federação "
        "com maior quantidade de ocorrências registradas na base "
        "da PRF em 2025."
    )


    # ------------------------------------------------------------
    # CRIAÇÃO DO GRÁFICO
    # ------------------------------------------------------------
    # top_10_uf já contém as dez UFs com maior quantidade
    # de ocorrências, calculadas anteriormente.
    #
    # O eixo X representa as UFs.
    # O eixo Y representa a quantidade de ocorrências.
    # ------------------------------------------------------------

    fig_uf, ax_uf = plt.subplots(figsize=(12, 6))

    ax_uf.bar(
        top_10_uf.index,
        top_10_uf.values
    )

    ax_uf.set_title(
        "10 UFs com maior número de ocorrências — PRF 2025"
    )

    ax_uf.set_xlabel("Unidade da Federação")

    ax_uf.set_ylabel("Quantidade de ocorrências")

    ax_uf.grid(
        axis="y",
        alpha=0.3
    )


    # ------------------------------------------------------------
    # ADICIONAMOS O VALOR ACIMA DE CADA BARRA
    # ------------------------------------------------------------

    for indice, valor in enumerate(top_10_uf.values):

        ax_uf.text(
            indice,
            valor,
            f"{int(valor):,}".replace(",", "."),
            ha="center",
            va="bottom"
        )


    # ------------------------------------------------------------
    # EXIBIÇÃO DO GRÁFICO NO STREAMLIT
    # ------------------------------------------------------------

    st.pyplot(fig_uf)

    plt.close(fig_uf)

    # ============================================================
    # INTERPRETAÇÃO DA DESCOBERTA 1
    # ============================================================

    st.write("### Interpretação da descoberta")

    total_ocorrencias = len(df)

    percentual_primeira_uf = (
        primeiro_total / total_ocorrencias
    ) * 100


    st.info(
        f"A Unidade da Federação com maior número de ocorrências "
        f"registradas na base da PRF em 2025 foi {primeira_uf}, "
        f"com {primeiro_total:,} ocorrências, correspondendo a "
        f"aproximadamente {percentual_primeira_uf:.2f}% das "
        f"{total_ocorrencias:,} ocorrências analisadas."
        .replace(",", ".")
    )


    st.success(
        f"O ranking mostra que {primeira_uf}, {segunda_uf} e "
        f"{terceira_uf} ocupam as três primeiras posições em "
        f"quantidade de ocorrências registradas nas rodovias "
        f"federais presentes na base analisada."
    )


    st.warning(
        "É importante observar que uma maior quantidade de ocorrências "
        "não significa necessariamente que uma UF possua rodovias mais "
        "perigosas. Para fazer essa conclusão seriam necessárias outras "
        "informações, como extensão da malha rodoviária, fluxo de veículos "
        "e volume de tráfego de cada região."
    )

    # ============================================================
    # DESCOBERTA 2 — PRINCIPAIS CAUSAS DOS ACIDENTES
    # ============================================================

    st.write("---")

    st.header("Descoberta 2 — Causas mais frequentes dos acidentes")

    st.write(
        "Nesta segunda descoberta, analisamos quais causas de acidentes "
        "aparecem com maior frequência nos registros da PRF em 2025."
    )


    # ------------------------------------------------------------
    # CONTAGEM DAS CAUSAS
    # ------------------------------------------------------------
    # value_counts() conta quantas vezes cada causa aparece na coluna
    # causa_acidente.
    #
    # head(10) seleciona somente as dez causas mais frequentes.
    # ------------------------------------------------------------

    top_10_causas = (
        df["causa_acidente"]
        .dropna()
        .value_counts()
        .head(10)
    )


    # ------------------------------------------------------------
    # IDENTIFICAÇÃO DAS TRÊS PRINCIPAIS CAUSAS
    # ------------------------------------------------------------

    primeira_causa = top_10_causas.index[0]
    primeira_causa_total = int(top_10_causas.iloc[0])

    segunda_causa = top_10_causas.index[1]
    segunda_causa_total = int(top_10_causas.iloc[1])

    terceira_causa = top_10_causas.index[2]
    terceira_causa_total = int(top_10_causas.iloc[2])


    # ------------------------------------------------------------
    # EXIBIÇÃO DAS TRÊS PRINCIPAIS CAUSAS
    # ------------------------------------------------------------

    st.write("### As três causas mais frequentes")

    col_causa1, col_causa2, col_causa3 = st.columns(3)

    col_causa1.metric(
        f"1º — {primeira_causa}",
        f"{primeira_causa_total:,}".replace(",", ".")
    )

    col_causa2.metric(
        f"2º — {segunda_causa}",
        f"{segunda_causa_total:,}".replace(",", ".")
    )

    col_causa3.metric(
        f"3º — {terceira_causa}",
        f"{terceira_causa_total:,}".replace(",", ".")
    )

    # ------------------------------------------------------------
    # GRÁFICO DAS 10 CAUSAS MAIS FREQUENTES
    # ------------------------------------------------------------

    st.write(
        "O gráfico abaixo apresenta as dez causas de acidentes "
        "mais frequentes registradas na base da PRF em 2025."
    )

    # Criamos a figura do gráfico.
    # Como os nomes das causas são grandes, utilizamos barras
    # horizontais para facilitar a leitura.
    fig_causas, ax_causas = plt.subplots(figsize=(12, 7))

    # ------------------------------------------------------------
    # IMPORTANTE:
    # O gráfico de barras horizontais é construído de baixo para cima.
    # Por isso usamos [::-1] para inverter a ordem e deixar a causa
    # mais frequente aparecendo no topo do gráfico.
    # ------------------------------------------------------------

    causas_grafico = top_10_causas[::-1]

    ax_causas.barh(
        causas_grafico.index,
        causas_grafico.values
    )

    # Título e identificação dos eixos
    ax_causas.set_title(
        "10 causas de acidentes mais frequentes — PRF 2025",
        fontsize=16
    )

    ax_causas.set_xlabel("Quantidade de ocorrências")
    ax_causas.set_ylabel("Causa do acidente")

    # ------------------------------------------------------------
    # COLOCA O VALOR NUMÉRICO AO LADO DE CADA BARRA
    # ------------------------------------------------------------

    for indice, valor in enumerate(causas_grafico.values):

        ax_causas.text(
            valor,
            indice,
            f" {valor:,}".replace(",", "."),
            va="center"
        )

    # Grade apenas no eixo X para facilitar a comparação
    ax_causas.grid(
        axis="x",
        alpha=0.25
    )

    # Ajusta automaticamente os espaços do gráfico
    fig_causas.tight_layout()

    # Exibe o gráfico no Streamlit
    st.pyplot(fig_causas)

    # Fecha a figura depois da exibição
    plt.close(fig_causas)


    # ============================================================
    # INTERPRETAÇÃO DA DESCOBERTA 2
    # ============================================================

    st.subheader("Interpretação da descoberta")

    # Percentual representado pela principal causa
    percentual_primeira_causa = (
        primeira_causa_total / len(df)
    ) * 100


    st.info(
        f"A causa mais frequente registrada na base da PRF em 2025 foi "
        f"**{primeira_causa}**, com "
        f"**{primeira_causa_total:,} ocorrências** "
        f"({percentual_primeira_causa:.2f}% do total analisado)."
        .replace(",", ".")
    )


    st.success(
        f"As três causas mais frequentes foram **{primeira_causa}**, "
        f"**{segunda_causa}** e **{terceira_causa}**. "
        f"Esses resultados mostram a predominância dessas classificações "
        f"entre as causas registradas na base analisada."
    )


    st.warning(
        "As causas apresentadas correspondem às classificações registradas "
        "pela PRF para cada ocorrência. A frequência de uma determinada "
        "causa não significa, isoladamente, que ela explique todos os fatores "
        "envolvidos nos acidentes."
    )

    # ============================================================
    # DESCOBERTA 3 — CONSEQUÊNCIAS DOS ACIDENTES
    # ============================================================

    st.header(
        "Descoberta 3 — Consequências dos acidentes"
    )

    st.write(
        "Nesta terceira descoberta, analisamos as consequências "
        "dos acidentes registrados pela PRF em 2025, considerando "
        "a quantidade de mortos, feridos graves e feridos leves."
    )


    # ------------------------------------------------------------
    # SOMA DAS PRINCIPAIS CONSEQUÊNCIAS
    # ------------------------------------------------------------
    # Cada linha da base representa uma ocorrência.
    #
    # As colunas abaixo informam quantas pessoas tiveram cada
    # tipo de consequência naquela ocorrência.
    #
    # Portanto, somamos os valores das colunas para obter os
    # totais registrados em toda a base.
    # ------------------------------------------------------------

    total_mortos = int(df["mortos"].sum())

    total_feridos_graves = int(
        df["feridos_graves"].sum()
    )

    total_feridos_leves = int(
        df["feridos_leves"].sum()
    )

    total_feridos = int(
        df["feridos"].sum()
    )


    # ------------------------------------------------------------
    # APRESENTAÇÃO DOS RESULTADOS
    # ------------------------------------------------------------

    st.subheader(
        "Totais registrados na base"
    )

    coluna_mortos, coluna_graves, coluna_leves = st.columns(3)

    coluna_mortos.metric(
        "Mortos",
        f"{total_mortos:,}".replace(",", ".")
    )

    coluna_graves.metric(
        "Feridos graves",
        f"{total_feridos_graves:,}".replace(",", ".")
    )

    coluna_leves.metric(
        "Feridos leves",
        f"{total_feridos_leves:,}".replace(",", ".")
    )


    # ------------------------------------------------------------
    # TOTAL DE FERIDOS
    # ------------------------------------------------------------

    st.metric(
        "Total de feridos",
        f"{total_feridos:,}".replace(",", ".")
    )


    # ------------------------------------------------------------
    # VERIFICAÇÃO DOS DADOS
    # ------------------------------------------------------------
    # Na base da PRF, a coluna "feridos" corresponde à soma de:
    #
    #     feridos_leves + feridos_graves
    #
    # Vamos verificar isso também no resultado apresentado.
    # ------------------------------------------------------------

    soma_feridos = (
        total_feridos_leves
        + total_feridos_graves
    )

    if soma_feridos == total_feridos:

        st.success(
            "Verificação dos dados: o total de feridos corresponde "
            "à soma dos feridos leves com os feridos graves."
        )

    else:

        st.warning(
            "Foi encontrada diferença entre o total de feridos "
            "e a soma dos feridos leves com os feridos graves."
        )

    # ============================================================
    # GRÁFICO — CONSEQUÊNCIAS DOS ACIDENTES
    # ============================================================

    st.subheader(
        "Comparação das consequências registradas"
    )

    st.write(
        "O gráfico abaixo compara as quantidades totais de mortos, "
        "feridos graves e feridos leves registradas na base da PRF "
        "em 2025."
    )


    # ------------------------------------------------------------
    # PREPARAÇÃO DOS DADOS DO GRÁFICO
    # ------------------------------------------------------------
    # Criamos duas listas:
    #
    # categorias -> nomes que aparecerão no eixo X
    # valores    -> quantidade correspondente a cada categoria
    # ------------------------------------------------------------

    categorias_consequencias = [
        "Mortos",
        "Feridos graves",
        "Feridos leves"
    ]

    valores_consequencias = [
        total_mortos,
        total_feridos_graves,
        total_feridos_leves
    ]


    # ------------------------------------------------------------
    # CRIAÇÃO DO GRÁFICO
    # ------------------------------------------------------------

    fig_consequencias, ax_consequencias = plt.subplots(
        figsize=(10, 6)
    )

    barras_consequencias = ax_consequencias.bar(
        categorias_consequencias,
        valores_consequencias
    )

    ax_consequencias.set_title(
        "Consequências dos acidentes registrados — PRF 2025"
    )

    ax_consequencias.set_xlabel(
        "Consequência"
    )

    ax_consequencias.set_ylabel(
        "Quantidade de pessoas"
    )

    ax_consequencias.grid(
        axis="y",
        alpha=0.3
    )


    # ------------------------------------------------------------
    # VALORES ACIMA DAS BARRAS
    # ------------------------------------------------------------

    for barra, valor in zip(
        barras_consequencias,
        valores_consequencias
    ):

        ax_consequencias.text(
            barra.get_x() + barra.get_width() / 2,
            barra.get_height(),
            f"{valor:,}".replace(",", "."),
            ha="center",
            va="bottom",
            fontsize=11
        )


    # ------------------------------------------------------------
    # EXIBIÇÃO NO STREAMLIT
    # ------------------------------------------------------------

    st.pyplot(
        fig_consequencias,
        use_container_width=True
    )

    plt.close(fig_consequencias)


    # ============================================================
    # INTERPRETAÇÃO DA DESCOBERTA
    # ============================================================

    st.subheader(
        "Interpretação da descoberta"
    )


    # ------------------------------------------------------------
    # CÁLCULO DE PROPORÇÕES
    # ------------------------------------------------------------
    # Vamos calcular qual percentual dos feridos corresponde
    # a feridos leves e qual corresponde a feridos graves.
    # ------------------------------------------------------------

    percentual_leves = (
        total_feridos_leves
        / total_feridos
    ) * 100

    percentual_graves = (
        total_feridos_graves
        / total_feridos
    ) * 100


    st.info(
        f"A base da PRF registra {total_feridos:,} pessoas feridas "
        f"em 2025, sendo {total_feridos_leves:,} feridos leves e "
        f"{total_feridos_graves:,} feridos graves."
        .replace(",", ".")
    )


    st.success(
        f"Entre as pessoas classificadas como feridas, "
        f"aproximadamente {percentual_leves:.2f}% foram registradas "
        f"como feridos leves e {percentual_graves:.2f}% como "
        f"feridos graves."
    )


    st.warning(
        f"Além dos feridos, foram registradas "
        f"{total_mortos:,} mortes na base analisada. "
        f"Esses valores representam totais registrados nas "
        f"ocorrências e não devem ser interpretados como taxas de "
        f"risco sem considerar outras informações, como fluxo de "
        f"veículos, extensão das rodovias e exposição ao trânsito."
        .replace(",", ".")
    )


    # ============================================================
    # CONCLUSÃO DO MÓDULO 6
    # ============================================================

    st.subheader("Conclusão do Módulo 6")

    st.success(
        "As análises realizadas permitiram identificar três aspectos "
        "relevantes dos acidentes registrados pela PRF em 2025: "
        "a distribuição das ocorrências entre as Unidades da Federação, "
        "as causas de acidentes mais frequentemente registradas e as "
        "consequências observadas em relação a mortos e feridos."
    )

    st.write(
        "Na primeira descoberta, Minas Gerais apresentou a maior "
        "quantidade de ocorrências da base analisada, seguido por "
        "Santa Catarina e Paraná."
    )

    st.write(
        "Na segunda descoberta, as causas mais frequentes foram "
        "Ausência de reação do condutor, Reação tardia ou ineficiente "
        "do condutor e Acessar a via sem observar a presença dos "
        "outros veículos."
    )

    st.write(
        "Na terceira descoberta, observamos 6.043 mortos, "
        "20.018 feridos graves e 63.532 feridos leves. "
        "O total de pessoas feridas foi de 83.550."
    )

    st.info(
        "Essas descobertas são descritivas e representam os registros "
        "existentes na base da PRF utilizada neste projeto. "
        "Os resultados, isoladamente, não permitem estabelecer relações "
        "de causa e efeito nem comparar diretamente o risco entre regiões "
        "sem considerar outras informações."
    )
