# Laboratório de Estatística Interativa — PRF 2025

## Análise de Acidentes nas Rodovias Federais Brasileiras

Projeto acadêmico desenvolvido em **Python** com o objetivo de aplicar conceitos de Estatística Descritiva, Probabilidade, Simulação, Distribuições de Probabilidade, Correlação e Regressão Linear sobre uma base pública real.

A aplicação utiliza dados de acidentes registrados pela **Polícia Rodoviária Federal (PRF) no ano de 2025** e possui uma interface interativa desenvolvida com **Streamlit**.

Um dos principais objetivos do projeto é implementar um **núcleo estatístico próprio**, no arquivo `minhastats.py`, evitando o uso de funções estatísticas prontas para os cálculos exigidos pelo trabalho.

---

# 1. Objetivo do projeto

O projeto tem como objetivo construir um laboratório interativo de Estatística capaz de:

- trabalhar com um conjunto de dados público e real;
- calcular medidas estatísticas por meio de funções próprias;
- apresentar estatísticas descritivas;
- gerar tabelas e gráficos;
- identificar possíveis outliers;
- realizar simulações de Monte Carlo;
- demonstrar a Lei dos Grandes Números;
- demonstrar o Teorema Central do Limite;
- comparar dados observados com distribuições teóricas;
- calcular correlação de Pearson;
- realizar regressão linear simples;
- realizar previsões utilizando o modelo de regressão;
- apresentar descobertas relevantes encontradas na base de dados.

---

# 2. Dataset utilizado

Foi utilizado o conjunto de dados de acidentes rodoviários disponibilizado pela **Polícia Rodoviária Federal (PRF)**.

Dados utilizados:

- Ano: **2025**
- Arquivo: `datatran2025.csv`
- Tipo: acidentes agrupados por ocorrência
- Quantidade de registros: **72.529**
- Quantidade de variáveis: **30**
- Período: **01/01/2025 a 31/12/2025**
- Unidade de análise: ocorrência de trânsito

O arquivo original é mantido sem alterações dentro da pasta:

```text
data/datatran2025.csv
```

Os tratamentos necessários são realizados pelo código Python durante a execução da aplicação.

---

# 3. Principais variáveis

Entre as variáveis numéricas utilizadas no projeto estão:

```text
pessoas
mortos
feridos_leves
feridos_graves
ilesos
ignorados
feridos
veiculos
km
```

Entre as variáveis categóricas estão:

```text
uf
dia_semana
causa_acidente
tipo_acidente
classificacao_acidente
fase_dia
sentido_via
condicao_metereologica
tipo_pista
tracado_via
uso_solo
```

Colunas que representam identificadores ou códigos, como `id` e `br`, não são tratadas automaticamente como medidas quantitativas apenas por possuírem representação numérica.

---

# 4. Tecnologias utilizadas

O projeto foi desenvolvido utilizando:

- Python 3.12
- Streamlit
- Pandas
- NumPy
- SciPy
- Matplotlib
- Pytest

O ambiente utilizado durante o desenvolvimento foi validado com:

```text
Python 3.12.7
Streamlit 1.63.0
pytest 9.1.1
```

---

# 5. Estrutura do projeto

A estrutura principal é:

```text
Laboratorio_Estatistica_PRF/
│
├── app.py
├── minhastats.py
├── README.md
├── RELATORIO.md
├── requirements.txt
│
├── data/
│   └── datatran2025.csv
│
└── tests/
    └── test_minhastats.py
```

## Descrição dos principais arquivos

### `app.py`

Aplicação principal desenvolvida com Streamlit.

Responsável pela interface, seleção de variáveis, apresentação dos cálculos, tabelas, gráficos, simulações e interpretações.

### `minhastats.py`

Biblioteca estatística própria desenvolvida para o projeto.

Contém as implementações manuais das principais medidas estatísticas exigidas.

### `tests/test_minhastats.py`

Contém os testes automatizados das funções implementadas em `minhastats.py`.

### `requirements.txt`

Lista as bibliotecas necessárias para executar o projeto.

### `data/datatran2025.csv`

Dataset original da PRF utilizado nas análises.

### `RELATORIO.md`

Arquivo destinado ao relatório textual do projeto.

---

# 6. Núcleo estatístico próprio

O arquivo `minhastats.py` contém implementações próprias das medidas estatísticas utilizadas pela aplicação.

Foram implementadas:

- média;
- mediana;
- moda;
- amplitude;
- variância populacional;
- variância amostral;
- desvio padrão populacional;
- desvio padrão amostral;
- percentis;
- quartis;
- coeficiente de variação;
- covariância populacional;
- covariância amostral;
- coeficiente de correlação de Pearson;
- regressão linear simples por mínimos quadrados.

As principais funções são:

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

---

# 7. Regra para os cálculos estatísticos

Uma regra central do projeto é que as medidas estatísticas apresentadas pela aplicação sejam calculadas pelo núcleo próprio.

Por exemplo, em vez de utilizar diretamente:

```python
np.mean(dados)
```

a aplicação utiliza:

```python
media(dados)
```

implementada em:

```text
minhastats.py
```

NumPy e SciPy podem ser utilizados como referências independentes nos testes automatizados, mas não substituem as implementações próprias exigidas pelo projeto.

---

# 8. Testes automatizados

As funções estatísticas foram verificadas utilizando **Pytest**.

Os resultados das implementações próprias são comparados, quando aplicável, com resultados de referência obtidos com NumPy/SciPy.

Foi adotada uma tolerância numérica rigorosa nas comparações de ponto flutuante.

Exemplo:

```python
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
```

A última execução consolidada registrada durante o desenvolvimento apresentou:

```text
80 passed
```

Portanto:

```text
80 testes aprovados
0 falhas
```

Os testes incluem também a função de regressão linear própria, validada em diferentes cenários e comparada com `numpy.polyfit`.

---

# 9. Como instalar o projeto

## 9.1 Criar o ambiente virtual

Na pasta do projeto, executar:

```bash
python -m venv .venv
```

---

## 9.2 Ativar o ambiente virtual

No Windows:

```bash
.venv\Scripts\activate
```

Quando o ambiente estiver ativo, normalmente aparecerá:

```text
(.venv)
```

antes do caminho no Prompt de Comando.

---

## 9.3 Instalar as dependências

Com o ambiente virtual ativo:

```bash
python -m pip install -r requirements.txt
```

O arquivo `requirements.txt` contém as principais dependências:

```text
streamlit
pandas
numpy
scipy
matplotlib
pytest
```

---

# 10. Como executar a aplicação

Primeiro, ativar o ambiente virtual:

```bash
.venv\Scripts\activate
```

Depois executar:

```bash
streamlit run app.py
```

O Streamlit iniciará o servidor local e disponibilizará a aplicação no navegador.

---

# 11. Como executar os testes

Na raiz do projeto e com o ambiente virtual ativo:

```bash
python -m pytest -v
```

O Pytest localizará os testes existentes na pasta:

```text
tests/
```

---

# 12. Módulo 0 — Dados Reais

O primeiro módulo corresponde à seleção e auditoria do conjunto de dados.

O dataset escolhido atende aos requisitos do projeto:

| Critério | Resultado |
|---|---|
| Dataset público real | Atendido |
| Mínimo de 1.000 registros | 72.529 registros |
| Mínimo de 4 variáveis numéricas | Atendido |
| Mínimo de 2 variáveis categóricas | Atendido |
| Formato apropriado | CSV |
| Período analisado | Ano de 2025 |

Também foi realizada uma auditoria inicial para identificar valores ausentes e verificar a consistência de variáveis importantes.

---

# 13. Módulo 1 — Núcleo Estatístico Próprio

Neste módulo foi criada a biblioteca:

```text
minhastats.py
```

As principais medidas estatísticas foram implementadas manualmente.

O módulo inclui:

- medidas de tendência central;
- medidas de dispersão;
- quartis;
- percentis;
- coeficiente de variação;
- covariância;
- correlação de Pearson;
- validação de entradas;
- testes automatizados.

NumPy/SciPy são utilizados como referência para validação dos resultados.

---

# 14. Módulo 2 — Estatística Descritiva Interativa

O Módulo 2 conecta o núcleo estatístico próprio à interface Streamlit.

O usuário pode selecionar variáveis e visualizar automaticamente diferentes análises.

Foram implementados:

- seleção interativa de variável numérica;
- medidas de tendência central;
- medidas de dispersão;
- quartis;
- coeficiente de variação;
- tabela de frequências;
- histograma;
- boxplot;
- identificação de possíveis outliers pelo IQR;
- interpretação textual da distribuição;
- seleção de variáveis categóricas;
- tabela de frequência categórica;
- gráfico de barras;
- gráfico de setores.

## Outliers

O método utilizado é o intervalo interquartil:

```text
IQR = Q3 - Q1
```

Limite inferior:

```text
Q1 - 1,5 × IQR
```

Limite superior:

```text
Q3 + 1,5 × IQR
```

Valores fora desses limites são apresentados como possíveis outliers.

A aplicação também alerta que um possível outlier estatístico não significa necessariamente um erro no dataset.

---

# 15. Módulo 3 — Probabilidade e Simulação

O Módulo 3 utiliza simulações de Monte Carlo para demonstrar dois conceitos fundamentais.

## 15.1 Lei dos Grandes Números

Foi simulada uma sequência de lançamentos de um dado justo de seis faces.

A média teórica é:

```text
3,5
```

À medida que a quantidade de lançamentos aumenta, a média observada tende a se aproximar da média teórica.

A aplicação apresenta:

- quantidade de lançamentos controlável;
- média observada;
- média teórica;
- diferença absoluta;
- gráfico da média acumulada;
- interpretação do comportamento observado.

---

## 15.2 Teorema Central do Limite

Também foram simuladas diversas amostras retiradas da população representada pelos resultados de um dado.

A aplicação permite controlar:

- quantidade de amostras;
- tamanho de cada amostra.

São calculadas as médias das amostras e apresentado um histograma da distribuição dessas médias.

Uma curva Normal teórica é sobreposta ao histograma para facilitar a visualização do comportamento previsto pelo Teorema Central do Limite.

Também foi realizada uma comparação entre diferentes tamanhos de amostra, por exemplo:

```text
n = 2
n = 10
n = 30
n = 100
```

A visualização mostra que a distribuição das médias amostrais tende a ficar mais concentrada ao redor da média populacional à medida que o tamanho das amostras aumenta.

---

# 16. Módulo 4 — Distribuições Teóricas

O Módulo 4 compara a distribuição observada nos dados com modelos probabilísticos teóricos.

Foram utilizadas:

- Distribuição Normal;
- Distribuição de Poisson.

Uma variável numérica pode ser selecionada para a análise.

Em um dos testes foi utilizada:

```text
pessoas
```

Para essa variável foram observados aproximadamente:

```text
Média = 2,5968
Mediana = 2,0000
Desvio padrão populacional = 2,2551
```

A média superior à mediana é compatível com uma distribuição assimétrica à direita.

## Distribuição Normal

A curva Normal é sobreposta ao histograma observado.

Para a variável `pessoas`, a comparação visual mostrou limitações no ajuste, pois os dados são discretos e apresentam assimetria à direita.

## Distribuição de Poisson

Por se tratar de uma variável de contagem, a distribuição de Poisson foi utilizada como segunda candidata.

O parâmetro utilizado é baseado na média observada:

```text
λ = média
```

A Poisson representa melhor algumas características da concentração dos valores baixos, embora também não represente perfeitamente toda a distribuição observada.

As distribuições teóricas são utilizadas como modelos aproximados e a comparação visual não significa que os dados necessariamente sigam exatamente determinada distribuição.

---

# 17. Módulo 5 — Correlação e Regressão Linear

O Módulo 5 permite selecionar duas variáveis numéricas para investigar sua relação.

A aplicação apresenta:

- seleção de variável X;
- seleção de variável Y;
- diagrama de dispersão;
- correlação de Pearson;
- regressão linear simples;
- equação da reta;
- coeficiente de determinação R²;
- reta de regressão;
- previsão interativa;
- interpretação dos resultados;
- alerta sobre causalidade.

---

## 17.1 Exemplo analisado

Durante o desenvolvimento foram utilizadas:

```text
X = veiculos
Y = pessoas
```

O coeficiente de Pearson obtido foi aproximadamente:

```text
r = 0,3953
```

Esse resultado representa uma associação linear positiva de intensidade relativamente limitada entre as duas variáveis.

---

## 17.2 Regressão linear

A regressão linear foi implementada manualmente utilizando o método dos mínimos quadrados.

A equação obtida no exemplo foi:

```text
pessoas = 1,0149 + 0,7917 × veiculos
```

O coeficiente angular indica que, segundo o modelo linear ajustado, o acréscimo de um veículo está associado a um aumento estimado de aproximadamente:

```text
0,7917 pessoa
```

na variável resposta.

---

## 17.3 Coeficiente de determinação

Foi obtido:

```text
R² = 0,1563
```

ou aproximadamente:

```text
15,63%
```

Isso indica que aproximadamente 15,63% da variação observada em `pessoas` é explicada linearmente pela variável `veiculos` dentro desse modelo simples.

Grande parte da variação permanece relacionada a outros fatores não considerados nesse modelo.

---

## 17.4 Previsão interativa

A aplicação permite informar um valor de X e calcular uma estimativa de Y utilizando a equação da regressão.

Por exemplo, para:

```text
veiculos = 1
```

o modelo produz aproximadamente:

```text
pessoas = 1,8066
```

Essa previsão representa uma estimativa matemática do modelo e não significa que o valor necessariamente ocorrerá em uma observação real.

---

## 17.5 Correlação não implica causalidade

Uma correlação estatística entre duas variáveis não demonstra, por si só, uma relação de causa e efeito.

Por esse motivo, a aplicação apresenta explicitamente um alerta sobre essa limitação.

---

# 18. Módulo 6 — Descobertas nos Dados

O módulo final apresenta três descobertas obtidas a partir da análise da base PRF 2025.

---

## 18.1 Descoberta 1 — Estados com maior número de ocorrências

As Unidades da Federação com maior quantidade de ocorrências na base foram:

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

Minas Gerais representou aproximadamente:

```text
13,19%
```

das 72.529 ocorrências analisadas.

Esse resultado representa frequência absoluta de registros e não permite concluir isoladamente que determinado estado seja mais perigoso.

Para uma comparação de risco seriam necessárias outras informações, como extensão das rodovias, fluxo de veículos e exposição ao trânsito.

---

## 18.2 Descoberta 2 — Causas mais frequentes dos acidentes

As três causas mais frequentes registradas foram:

```text
1º Ausência de reação do condutor
   11.469 ocorrências

2º Reação tardia ou ineficiente do condutor
   10.799 ocorrências

3º Acessar a via sem observar a presença dos outros veículos
   7.097 ocorrências
```

A causa mais frequente correspondeu a aproximadamente:

```text
15,81%
```

das ocorrências analisadas.

A frequência de uma classificação não significa, isoladamente, que ela explique todos os fatores envolvidos nos acidentes.

---

## 18.3 Descoberta 3 — Consequências dos acidentes

Os totais registrados na base foram:

| Consequência | Total |
|---|---:|
| Mortos | 6.043 |
| Feridos graves | 20.018 |
| Feridos leves | 63.532 |
| Total de feridos | 83.550 |

Também foi verificada a consistência:

```text
63.532 + 20.018 = 83.550
```

Portanto:

```text
feridos = feridos_leves + feridos_graves
```

na análise realizada.

Entre as pessoas classificadas como feridas, aproximadamente:

```text
76,04% foram registradas como feridos leves
23,96% foram registradas como feridos graves
```

Esses valores são totais observados na base e não representam, isoladamente, taxas de risco.

---

# 19. Principais resultados

A análise do dataset permitiu observar:

- 72.529 ocorrências durante 2025;
- 188.346 pessoas envolvidas;
- 6.043 mortos;
- 83.550 feridos;
- 63.532 feridos leves;
- 20.018 feridos graves;
- 76.406 ilesos;
- 144.922 veículos envolvidos.

Além disso:

- Minas Gerais apresentou a maior quantidade absoluta de ocorrências;
- ausência de reação do condutor foi a causa mais frequente registrada;
- as variáveis `veiculos` e `pessoas` apresentaram associação linear positiva, porém limitada;
- o modelo simples entre `veiculos` e `pessoas` apresentou R² de aproximadamente 15,63%.

---

# 20. Cuidados na interpretação

Os resultados apresentados são baseados nos registros existentes no dataset da PRF.

Alguns cuidados são importantes:

- frequência não significa necessariamente risco;
- associação não significa causalidade;
- outlier estatístico não significa necessariamente erro;
- uma distribuição teórica é uma aproximação matemática;
- uma regressão simples não explica todos os fatores envolvidos;
- comparações entre estados exigiriam medidas de exposição, como fluxo de veículos e extensão das rodovias;
- resultados observados devem ser interpretados dentro do contexto e das limitações da base utilizada.

---

# 21. Situação atual do projeto

Situação dos módulos:

```text
Módulo 0 — Dados Reais                         CONCLUÍDO
Módulo 1 — Núcleo Estatístico Próprio         CONCLUÍDO
Módulo 2 — Estatística Descritiva             CONCLUÍDO
Módulo 3 — Probabilidade e Simulação           CONCLUÍDO
Módulo 4 — Distribuições Teóricas              CONCLUÍDO
Módulo 5 — Correlação e Regressão Linear       CONCLUÍDO
Módulo 6 — Descobertas                         CONCLUÍDO
```

Testes automatizados registrados:

```text
80 passed
0 failed
```

---

# 22. Reprodutibilidade

Para reproduzir o projeto em outra máquina:

```bash
git clone <URL-DO-REPOSITORIO>
```

Entrar na pasta:

```bash
cd Laboratorio_Estatistica_PRF
```

Criar ambiente virtual:

```bash
python -m venv .venv
```

Ativar:

```bash
.venv\Scripts\activate
```

Instalar dependências:

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

> O endereço do repositório deverá substituir `<URL-DO-REPOSITORIO>` quando o projeto for publicado no GitHub ou GitLab.

---

# 23. Fonte dos dados

Dados públicos de acidentes rodoviários da:

**Polícia Rodoviária Federal — PRF**

Base utilizada:

```text
Acidentes 2025 — Agrupados por ocorrência
datatran2025.csv
```

Os dados utilizados neste trabalho pertencem à fonte pública responsável por sua disponibilização.

---

# 24. Observação acadêmica

Este projeto foi desenvolvido para fins acadêmicos como laboratório interativo de Estatística.

O foco do trabalho está na aplicação prática dos conceitos estudados, na implementação própria dos principais cálculos estatísticos e na interpretação responsável dos resultados obtidos a partir de dados reais.