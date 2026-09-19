# Relatório — Laboratório de Estatística Interativa

## Análise de Acidentes nas Rodovias Federais Brasileiras — PRF 2025

---

## 1. Introdução

Este projeto foi desenvolvido como um Laboratório de Estatística Interativa utilizando Python e dados públicos reais.

O conjunto de dados escolhido contém registros de acidentes ocorridos em rodovias federais brasileiras durante o ano de 2025, disponibilizados pela Polícia Rodoviária Federal (PRF). A escolha foi feita em virtude da ampla quantidade de dados e variáveis à disposição, o que permite uma análise ampla na estatística.

O projeto busca aplicar, de forma prática, conceitos de Estatística Descritiva, Probabilidade, Simulação, Distribuições de Probabilidade, Correlação e Regressão Linear.

Além dos cálculos estatísticos, foi desenvolvida uma aplicação interativa utilizando Streamlit, permitindo que o usuário selecione variáveis, visualize gráficos, execute simulações e interprete os resultados.

Uma característica central do projeto é a implementação de uma biblioteca estatística própria, denominada `minhastats.py`. As principais medidas estatísticas exigidas pelo trabalho foram implementadas manualmente, sem utilizar funções estatísticas prontas para produzir os resultados apresentados pela aplicação.

---

## 2. Objetivos

### 2.1 Objetivo geral

Desenvolver uma aplicação interativa para análise estatística de dados reais de acidentes rodoviários registrados pela PRF em 2025.

### 2.2 Objetivos específicos

Os principais objetivos foram:

- selecionar e analisar um conjunto de dados público e real;
- implementar manualmente medidas estatísticas fundamentais;
- validar as funções próprias utilizando testes automatizados;
- realizar análises estatísticas descritivas;
- construir tabelas de frequência e gráficos;
- identificar possíveis outliers;
- demonstrar conceitos probabilísticos por simulação;
- demonstrar a Lei dos Grandes Números;
- demonstrar o Teorema Central do Limite;
- comparar dados observados com distribuições teóricas;
- calcular correlação linear;
- implementar regressão linear simples por mínimos quadrados;
- realizar previsões utilizando o modelo ajustado;
- identificar descobertas relevantes presentes no conjunto de dados.

---

## 3. Conjunto de dados

O conjunto de dados utilizado foi disponibilizado publicamente pela Polícia Rodoviária Federal.

A base utilizada corresponde aos acidentes de 2025 agrupados por ocorrência.

Arquivo:

```text
datatran2025.csv
```

A base possui:

```text
72.529 registros
30 variáveis
```

O período observado é:

```text
01/01/2025 a 31/12/2025
```

Cada registro representa uma ocorrência de trânsito.

O arquivo original foi mantido no projeto em:

```text
data/datatran2025.csv
```

O arquivo utiliza:

```text
Separador: ;
Codificação: latin1
Separador decimal original: vírgula
```

A leitura é realizada pelo Pandas durante a execução da aplicação.

---

## 4. Características das variáveis

A base apresenta variáveis numéricas e categóricas suficientes para as análises propostas.

Entre as variáveis numéricas utilizadas estão:

- pessoas;
- mortos;
- feridos leves;
- feridos graves;
- ilesos;
- ignorados;
- feridos;
- veículos;
- km.

Entre as variáveis categóricas estão:

- UF;
- dia da semana;
- causa do acidente;
- tipo do acidente;
- classificação do acidente;
- fase do dia;
- sentido da via;
- condição meteorológica;
- tipo de pista;
- traçado da via;
- uso do solo.

Colunas que representam identificadores ou códigos não são consideradas automaticamente como medidas quantitativas apenas por possuírem representação numérica.

---

## 5. Tecnologias utilizadas

O projeto foi desenvolvido utilizando:

- Python 3.12;
- Streamlit;
- Pandas;
- NumPy;
- SciPy;
- Matplotlib;
- Pytest.

Durante o desenvolvimento foi utilizado Python 3.12.7.

A aplicação foi construída utilizando Streamlit para disponibilizar uma interface interativa para as análises.

Pandas foi utilizado principalmente para leitura, organização, filtragem e manipulação do conjunto de dados.

NumPy e SciPy foram utilizados principalmente como referências independentes para validação das implementações estatísticas próprias.

Matplotlib foi utilizado para a geração dos gráficos.

Pytest foi utilizado para automatizar os testes.

---

# 6. Módulo 0 — Dados Reais

O primeiro módulo consistiu na escolha e auditoria do conjunto de dados.

Os requisitos mínimos foram atendidos:

| Requisito | Resultado |
|---|---|
| Dataset público e real | Atendido |
| Pelo menos 1.000 registros | 72.529 |
| Pelo menos 4 variáveis numéricas | Atendido |
| Pelo menos 2 variáveis categóricas | Atendido |

Também foi realizada uma auditoria inicial da base para compreender sua estrutura e verificar possíveis problemas.

Foram identificados poucos valores ausentes em algumas colunas, principalmente:

```text
classificacao_acidente
regional
delegacia
uop
```

As principais variáveis utilizadas nas análises não apresentaram problemas que impedissem o desenvolvimento do projeto.

Também foi verificada a unicidade do identificador das ocorrências.

---

# 7. Módulo 1 — Núcleo Estatístico Próprio

Uma das principais exigências do projeto foi a implementação de funções estatísticas próprias.

Para isso foi criado:

```text
minhastats.py
```

Foram implementadas as seguintes funções:

```python
media()
mediana()
moda()
amplitude()

variancia_populacional()
variancia_amostral()

desvio_padrao_populacional()
desvio_padrao_amostral()

percentil()
quartis()

coeficiente_variacao()

covariancia_populacional()
covariancia_amostral()

correlacao_pearson()

regressao_linear()
```

Também foi criada uma rotina interna para validação dos dados recebidos pelas funções.

---

## 7.1 Média

A média aritmética é calculada por:

```text
média = soma dos valores / número de valores
```

No Python, temos:

```text
média = soma / len(dados)
```

A implementação própria percorre os valores e realiza o cálculo sem utilizar uma função estatística pronta.



---

## 7.2 Mediana

A mediana é determinada após ordenar os dados.

Quando o número de elementos é ímpar, utiliza-se o elemento central.

Quando o número de elementos é par, calcula-se a média dos dois elementos centrais.

Assim, calcula-se

```text
    n = len(valores)
    meio = n // 2
```

---

## 7.3 Moda

A moda corresponde ao valor ou aos valores de maior frequência.

A implementação permite a existência de múltiplas modas.

Quando todos os valores apresentam a mesma frequência unitária, o conjunto é considerado amodal pela regra adotada no projeto.

Calcula-se, então:

```text
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
```

---

## 7.4 Variância e desvio padrão

Foram implementadas separadamente:

- variância populacional (σ² = Σ(x - μ)² / N);
- variância amostral (s² = Σ(x - x̄)² / (n - 1));
- desvio padrão populacional (σ = √σ²);
- desvio padrão amostral (s = √s²).

Na variância populacional é utilizado o divisor:

```text
N
```

Na variância amostral:

```text
N - 1
```

O desvio padrão é calculado como a raiz quadrada da respectiva variância.

---

## 7.5 Percentis e quartis

Foi implementado o cálculo de percentis utilizando interpolação linear.

Os quartis são calculados como:

```text
Q1 = P25
Q2 = P50
Q3 = P75
```

---

## 7.6 Coeficiente de variação

O coeficiente de variação utiliza:

```text
CV = desvio padrão amostral / média × 100
```

Ele permite avaliar a dispersão dos valores relativamente à média.

---

## 7.7 Covariância e correlação

Foram implementadas:

- covariância populacional;
- covariância amostral;
- correlação de Pearson.

A correlação de Pearson permite avaliar a direção e a intensidade da associação linear entre duas variáveis quantitativas.

---

# 8. Testes automatizados

Para validar o núcleo estatístico próprio foi utilizado Pytest.

Os resultados das funções próprias foram comparados, quando aplicável, com resultados obtidos por NumPy e SciPy.

Foi utilizada tolerância numérica rigorosa:

Para lidar com pequenas diferenças decorrentes da representação
de números em ponto flutuante, os testes automatizados utilizam
tolerâncias numéricas documentadas.

Nos testes iniciais são utilizadas comparações com NumPy por meio
de np.isclose(), adotando:

rtol = 1e-9
atol = 1e-12

Nos blocos de validação acrescentados posteriormente é utilizado
pytest.approx(), com tolerância absoluta:

abs = 1e-10

NumPy e SciPy são utilizados exclusivamente como referências para
validação dos resultados produzidos pelas funções implementadas
manualmente em minhastats.py.

A última execução consolidada apresentou:

```text
80 passed
0 failed
```

Portanto, 80 testes automatizados foram executados com sucesso.

Os testes também incluem a regressão linear própria, comparada com resultados obtidos por `numpy.polyfit`.

NumPy e SciPy são utilizados para validação e não para substituir os cálculos próprios exibidos pela aplicação.

---

# 9. Módulo 2 — Estatística Descritiva Interativa

O Módulo 2 integrou o núcleo estatístico próprio à aplicação Streamlit.

O usuário pode selecionar uma variável numérica e obter automaticamente diferentes medidas estatísticas.

São apresentadas medidas como:

- média;
- mediana;
- moda;
- amplitude;
- variância;
- desvio padrão;
- quartis;
- coeficiente de variação.

Também são apresentadas tabelas de frequência e visualizações gráficas.

---

## 9.1 Histograma

O histograma permite observar a distribuição dos valores de uma variável numérica.

Ele auxilia na identificação de:

- concentração dos dados;
- dispersão;
- assimetria;
- caudas;
- possíveis valores extremos.

---

## 9.2 Boxplot e outliers

O boxplot permite visualizar quartis e possíveis valores extremos.

O método utilizado para identificar possíveis outliers é o intervalo interquartil:

```text
IQR = Q3 - Q1
```

Os limites são:

```text
Limite inferior = Q1 - 1,5 × IQR
Limite superior = Q3 + 1,5 × IQR
```

Valores fora desses limites são classificados como possíveis outliers.

A aplicação alerta que um outlier estatístico não significa necessariamente erro.

Em algumas variáveis de contagem, Q1 e Q3 podem ser iguais a zero, produzindo IQR igual a zero. Nesses casos, o resultado exige interpretação cuidadosa.

---

## 9.3 Variáveis categóricas

Também foi implementada análise para variáveis categóricas.

São apresentados:

- tabela de frequências;
- gráfico de barras;
- gráfico de setores.

Essas visualizações permitem identificar as categorias mais frequentes.

---

# 10. Módulo 3 — Probabilidade e Simulação

O Módulo 3 utiliza simulações de Monte Carlo para demonstrar conceitos de probabilidade.

Foram desenvolvidas duas experiências principais:

- Lei dos Grandes Números;
- Teorema Central do Limite.

---

## 10.1 Lei dos Grandes Números

Foi simulado o lançamento de um dado justo de seis faces.

A média teórica é:

```text
3,5
```

Em uma simulação com 1.000 lançamentos foi obtido, por exemplo:

```text
Média observada = 3,4880
Média teórica   = 3,5000
Diferença       = 0,0120
```

A aplicação apresenta um gráfico da média acumulada.

Nos primeiros lançamentos a média apresenta maiores oscilações.

À medida que a quantidade de observações cresce, a média acumulada tende a se aproximar do valor teórico.

Esse comportamento ilustra a Lei dos Grandes Números.

Posteriormente, o mesmo experimento foi aplicado diante dos dados obtidos pela PRF. Enquanto o comportamento observado difere, em certos aspectos, do "ideal" da Lei dos Grandes Números, visto que não há exatamente uma média teórica para esses casos, observa-se que os números tendem a se estabilizar a partir de um certo ponto, tal como a Lei propõe.

---

## 10.2 Teorema Central do Limite

Para demonstrar o Teorema Central do Limite foram geradas diversas amostras da população representada pelos valores de um dado.

Em um dos experimentos foram utilizadas:

```text
1.000 amostras
tamanho da amostra = 30
```

Foi obtido aproximadamente:

```text
Média das médias amostrais = 3,4937
Média teórica               = 3,5000
Diferença                   = 0,0063
```

O histograma das médias amostrais apresentou comportamento aproximadamente Normal.

Também foi sobreposta uma curva Normal teórica.

Foram comparados diferentes tamanhos de amostra:

```text
n = 2
n = 10
n = 30
n = 100
```

À medida que o tamanho da amostra aumenta, a distribuição das médias fica mais concentrada ao redor da média populacional.

Isso demonstra também a redução do erro padrão com o aumento do tamanho da amostra.

---

# 11. Módulo 4 — Distribuições Teóricas

O Módulo 4 compara distribuições observadas com modelos teóricos.

Foram utilizadas:

- Distribuição Normal;
- Distribuição de Poisson.

---

## 11.1 Exemplo com a variável pessoas

Durante os testes foi utilizada a variável:

```text
pessoas
```

Foram encontrados aproximadamente:

```text
Média = 2,5968
Mediana = 2,0000
Desvio padrão populacional = 2,2551
Número de ocorrências = 72.529
```

A média superior à mediana indica assimetria à direita.

---

## 11.2 Comparação com a Normal

Foi sobreposta uma curva Normal ao histograma dos dados.

A comparação mostrou que a Normal não apresenta um ajuste visual adequado para toda a distribuição da variável `pessoas`.

Isso ocorre principalmente porque:

- a variável representa uma contagem;
- os valores são discretos;
- existe concentração nos valores baixos;
- existe assimetria à direita.

---

## 11.3 Comparação com Poisson

Como segunda distribuição foi utilizada a Poisson.

Para a variável analisada foi utilizado:

```text
λ = média observada
```

ou aproximadamente:

```text
λ = 2,5968
```

A distribuição de Poisson representa melhor algumas características de uma variável de contagem, especialmente a concentração nos valores menores.

Entretanto, ela também não representa perfeitamente toda a distribuição observada.

A conclusão é que distribuições teóricas devem ser interpretadas como modelos aproximados e não como prova de que os dados seguem exatamente determinada distribuição.

---

# 12. Módulo 5 — Correlação e Regressão Linear

O Módulo 5 investiga a relação entre duas variáveis quantitativas.

A aplicação permite selecionar:

```text
Variável X
Variável Y
```

São apresentados:

- diagrama de dispersão;
- coeficiente de Pearson;
- regressão linear;
- equação da reta;
- R²;
- reta ajustada;
- previsão interativa;
- interpretação.

---

## 12.1 Exemplo: veículos e pessoas

Durante o desenvolvimento foram utilizadas:

```text
X = veiculos
Y = pessoas
```

Foram utilizadas 72.529 observações válidas.

A correlação obtida foi:

```text
r = 0,3953
```

O resultado indica associação linear positiva, porém limitada, entre as duas variáveis.

---

## 12.2 Regressão linear

A regressão foi implementada manualmente pelo método dos mínimos quadrados.

A equação obtida foi:

```text
pessoas = 1,0149 + 0,7917 × veiculos
```

O intercepto é:

```text
1,0149
```

O coeficiente angular é:

```text
0,7917
```

Segundo o modelo ajustado, o aumento de uma unidade em `veiculos` está associado a um aumento estimado de aproximadamente 0,7917 na variável `pessoas`.

---

## 12.3 Coeficiente de determinação

Foi calculado:

```text
R² = 0,1563
```

ou:

```text
15,63%
```

Isso indica que aproximadamente 15,63% da variação observada em `pessoas` está associada linearmente à variável `veiculos` dentro do modelo simples utilizado.

O restante da variação depende de fatores não considerados pelo modelo.

---

## 12.4 Previsão

A aplicação permite realizar previsões interativas.

Por exemplo:

```text
veiculos = 1
```

produziu:

```text
pessoas estimadas = 1,8066
```

A previsão representa uma estimativa matemática e não necessariamente um valor que será observado em uma ocorrência real.

---

## 12.5 Correlação e causalidade

O projeto destaca que:

```text
Correlação não implica causalidade.
```

Uma associação estatística entre duas variáveis não demonstra que uma delas cause diretamente a outra.

---

# 13. Módulo 6 — Descobertas nos Dados

O último módulo apresenta três descobertas obtidas a partir da análise do conjunto de dados.

---

## 13.1 Descoberta 1 — Estados com maior número de ocorrências

As dez UFs com maior número de ocorrências foram:

| Posição | UF | Ocorrências |
|---|---|---:|
| 1 | MG | 9.570 |
| 2 | SC | 8.186 |
| 3 | PR | 7.630 |
| 4 | RJ | 6.428 |
| 5 | RS | 4.899 |
| 6 | SP | 4.683 |
| 7 | BA | 4.108 |
| 8 | GO | 3.196 |
| 9 | PE | 3.013 |
| 10 | ES | 2.642 |

Minas Gerais apresentou:

```text
9.570 ocorrências
```

equivalentes a aproximadamente:

```text
13,19%
```

do total analisado.

Esse resultado representa frequência absoluta e não significa, isoladamente, que Minas Gerais apresente maior risco.

Uma comparação de risco exigiria informações adicionais, como extensão das rodovias, volume de tráfego e exposição.

---

## 13.2 Descoberta 2 — Causas mais frequentes

As três causas mais frequentes foram:

### 1º — Ausência de reação do condutor

```text
11.469 ocorrências
```

### 2º — Reação tardia ou ineficiente do condutor

```text
10.799 ocorrências
```

### 3º — Acessar a via sem observar a presença dos outros veículos

```text
7.097 ocorrências
```

A causa mais frequente correspondeu a aproximadamente:

```text
15,81%
```

das ocorrências.

Esses resultados representam as classificações registradas na base e não significam que uma única causa explique todos os fatores envolvidos em cada acidente.

---

## 13.3 Descoberta 3 — Consequências dos acidentes

Foram encontrados:

```text
Mortos:           6.043
Feridos graves:  20.018
Feridos leves:   63.532
Total de feridos: 83.550
```

Foi realizada também uma verificação de consistência:

```text
63.532 + 20.018 = 83.550
```

Portanto, na base analisada:

```text
feridos = feridos_leves + feridos_graves
```

Entre as pessoas classificadas como feridas:

```text
aproximadamente 76,04% foram feridos leves
aproximadamente 23,96% foram feridos graves
```

Também foram registradas:

```text
6.043 mortes
```

Os números representam totais registrados e não taxas de risco.

---

# 14. Outros resultados gerais

A auditoria da base encontrou os seguintes totais:

| Informação | Total |
|---|---:|
| Ocorrências | 72.529 |
| Pessoas envolvidas | 188.346 |
| Mortos | 6.043 |
| Feridos leves | 63.532 |
| Feridos graves | 20.018 |
| Total de feridos | 83.550 |
| Ilesos | 76.406 |
| Ignorados | 28.630 |
| Veículos | 144.922 |

Esses valores ajudam a dimensionar o conjunto de dados analisado.

---

# 15. Cuidados e limitações da análise

Os resultados devem ser interpretados considerando as características e limitações do conjunto de dados.

Alguns cuidados são fundamentais.

## 15.1 Frequência não é risco

Um estado possuir maior quantidade de ocorrências não significa necessariamente que suas rodovias sejam mais perigosas.

Seriam necessárias informações sobre exposição ao risco.

---

## 15.2 Correlação não é causalidade

Uma correlação estatística não demonstra uma relação causal.

---

## 15.3 Outliers

Um valor identificado pelo método do IQR não é necessariamente incorreto.

Pode representar uma ocorrência real e excepcional.

---

## 15.4 Distribuições teóricas

A aproximação visual entre uma distribuição observada e uma distribuição teórica não prova que os dados seguem exatamente aquele modelo probabilístico.

---

## 15.5 Regressão

A regressão linear simples considera apenas duas variáveis.

No exemplo entre veículos e pessoas, o R² de aproximadamente 15,63% demonstra que grande parte da variação depende de outros fatores.

---

# 16. Reprodutibilidade

O projeto possui um arquivo:

```text
requirements.txt
```

com as dependências necessárias.

Para preparar o ambiente:

```bash
python -m venv .venv
```

No Windows:

```bash
.venv\Scripts\activate
```

Instalar as dependências:

```bash
python -m pip install -r requirements.txt
```

Executar os testes:

```bash
python -m pytest -v
```

Executar a aplicação:

```bash
streamlit run app.py
```

---

# 17. Auditoria dos requisitos do trabalho

Após a implementação, foi realizada uma revisão dos módulos.

| Módulo | Situação |
|---|---|
| Módulo 0 — Dados Reais | Concluído |
| Módulo 1 — Núcleo Estatístico Próprio | Concluído |
| Módulo 2 — Estatística Descritiva | Concluído |
| Módulo 3 — Probabilidade e Simulação | Concluído |
| Módulo 4 — Distribuições Teóricas | Concluído |
| Módulo 5 — Correlação e Regressão | Concluído |
| Módulo 6 — Descobertas | Concluído |

O núcleo estatístico possui testes automatizados.

Última execução consolidada:

```text
80 passed
0 failed
```

O arquivo `README.md` também foi preparado com instruções para instalação, execução e compreensão da estrutura do projeto.

---

# 18. Conclusão

O desenvolvimento do Laboratório de Estatística Interativa permitiu aplicar conceitos estatísticos a um conjunto de dados público e real contendo 72.529 ocorrências registradas pela PRF em 2025.

A implementação de um núcleo estatístico próprio possibilitou compreender de forma prática como medidas como média, mediana, variância, desvio padrão, percentis, covariância e correlação são calculadas.

Os testes automatizados permitiram comparar as implementações próprias com referências consolidadas, aumentando a confiabilidade dos cálculos.

A aplicação Streamlit transformou os cálculos em uma ferramenta interativa, permitindo selecionar variáveis, gerar tabelas, visualizar distribuições, identificar possíveis outliers e interpretar resultados.

As simulações demonstraram de maneira prática a Lei dos Grandes Números e o Teorema Central do Limite.

A comparação com distribuições Normal e Poisson mostrou que modelos probabilísticos teóricos devem ser interpretados levando em consideração as características reais das variáveis.

A análise de correlação e regressão permitiu estudar a associação entre veículos e pessoas envolvidas, encontrando correlação positiva e um modelo com R² de aproximadamente 15,63%, reforçando a importância de não interpretar associação estatística como causalidade.

Por fim, as três descobertas apresentadas mostraram a distribuição geográfica das ocorrências, as causas mais frequentemente registradas e as consequências dos acidentes em termos de mortos e feridos.

O projeto demonstra, portanto, a utilização integrada de programação, estatística, testes automatizados, visualização de dados e interpretação crítica sobre um conjunto de dados real.

---

# 19. Situação final

No estágio atual:

```text
Dataset real                         CONCLUÍDO
Núcleo estatístico próprio           CONCLUÍDO
Testes automatizados                 CONCLUÍDO
Aplicação Streamlit                  CONCLUÍDA
Módulos 0 a 6                       CONCLUÍDOS
README.md                            CONCLUÍDO
RELATORIO.md                         CONCLUÍDO
requirements.txt                     CONCLUÍDO
```

Ainda devem ser verificados antes da entrega:

```text
Publicação no GitHub/GitLab
Histórico real de commits
Revisão final dos arquivos
Vídeo/apresentação do projeto
```

---

## Fonte dos dados

**Polícia Rodoviária Federal — PRF**

Base de acidentes de trânsito de 2025, agrupados por ocorrência.

Arquivo utilizado:

```text
datatran2025.csv
```

---

## Observação

Projeto desenvolvido para fins acadêmicos no contexto de um Laboratório de Estatística Interativa.