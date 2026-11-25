# 🎬 CineTrack — Sistema de Gerenciamento, Busca e Classificação de Filmes

O **CineTrack** é uma aplicação desenvolvida em Python para gerenciamento, consulta e classificação de filmes por meio de uma interface interativa no terminal. O projeto utiliza o dataset **MovieLens Latest Small**, disponibilizado pelo GroupLens Research, e tem como principal objetivo demonstrar a aplicação prática de estruturas de dados na organização e no processamento de informações cinematográficas.

Desenvolvido no contexto da disciplina de **Estruturas de Dados**, o sistema implementa manualmente uma **Tabela Hash com tratamento de colisões por sondagem linear** e uma **Fila Encadeada baseada no princípio FIFO**. Essas estruturas são empregadas para atender a diferentes requisitos de consulta e gerenciamento do catálogo.

O projeto prioriza a modularização do código, a compreensão dos algoritmos utilizados e a análise de suas respectivas complexidades computacionais.

---

## 📌 Objetivos do Projeto

O CineTrack foi desenvolvido para atender às seguintes necessidades:

- Organizar e armazenar informações sobre filmes.
- Localizar produções cinematográficas por identificador.
- Pesquisar filmes por título.
- Consultar filmes pertencentes a determinado gênero.
- Classificar produções de acordo com suas avaliações.
- Gerenciar uma lista de filmes para assistir.
- Demonstrar a aplicação de estruturas de dados em um sistema funcional.

## 👥 Integrantes

| Integrante | 
|---|
| Jhony Wictor do Nascimento Santos |
| Karleandro Santos da Silva |

---

## 🎯 Funcionalidades

O sistema disponibiliza as seguintes operações:

| Funcionalidade | Descrição |
|---|---|
| Busca por identificador | Localiza filmes utilizando o campo `movieId`, armazenado na Tabela Hash. |
| Busca por título | Permite pesquisar produções cinematográficas pelo nome ou por trechos do título. |
| Consulta por gênero | Filtra o catálogo de acordo com os gêneros associados aos filmes. |
| Classificação por avaliação | Calcula e apresenta os filmes com maiores médias de avaliação, utilizando os registros de `ratings.csv`. |
| Adição à fila | Insere filmes na lista de produções que o usuário deseja assistir. |
| Consulta à fila | Apresenta a sequência de filmes armazenados na lista de acompanhamento. |
| Marcação de filme assistido | Remove o primeiro elemento da fila, respeitando a ordem de inserção. |

---

## 🗃️ Dataset

O projeto utiliza o **MovieLens Latest Small**, um conjunto de dados disponibilizado pelo [GroupLens Research](https://grouplens.org/datasets/movielens/), vinculado à Universidade de Minnesota.

O dataset contém informações sobre filmes, avaliações realizadas por usuários e etiquetas textuais associadas às produções. Sua estrutura permite explorar operações de busca, classificação e relacionamento entre registros.

### Fonte dos dados

- **Dataset no Kaggle:** [MovieLens Latest Small](https://www.kaggle.com/datasets/grouplens/movielens-latest-small?resource=download)
- **Projeto original:** [GroupLens — MovieLens](https://grouplens.org/datasets/movielens/)

### Características da versão utilizada

De acordo com a versão apresentada no projeto, o conjunto de dados possui:

| Informação | Quantidade |
|---|---:|
| Filmes | 9.742 |
| Avaliações | 100.836 |
| Usuários | 610 |
| Tags | 3.683 |

Esses valores correspondem à versão utilizada durante o desenvolvimento e a apresentação do CineTrack. Como o MovieLens Latest é uma coleção destinada à educação e ao desenvolvimento e pode sofrer atualizações, as quantidades podem variar conforme a versão baixada.

### Arquivos utilizados

O dataset é distribuído em arquivos CSV, que são processados pelo sistema durante a inicialização.

| Arquivo | Descrição |
|---|---|
| `movies.csv` | Contém os identificadores dos filmes (`movieId`), seus títulos (`title`) e os gêneros associados (`genres`). |
| `ratings.csv` | Armazena os identificadores dos usuários e filmes, as notas atribuídas e os respectivos registros temporais. |
| `tags.csv` | Contém etiquetas textuais associadas aos filmes por usuários. É um arquivo complementar e opcional para a execução das funcionalidades principais. |
| `links.csv` | Disponibiliza identificadores externos relacionados aos filmes, como referências ao IMDb e ao TMDb. |

O CineTrack utiliza principalmente `movies.csv` e `ratings.csv` para carregar o catálogo e calcular as médias de avaliação.

---

## 🏗️ Arquitetura do Sistema

A arquitetura do CineTrack foi organizada de forma modular, separando o processamento dos dados, as estruturas de armazenamento e a interação com o usuário.

O fluxo geral de funcionamento pode ser representado da seguinte maneira:

```text
Dataset MovieLens
       │
       ▼
Arquivos CSV
       │
       ▼
Leitura e processamento
       │
       ├── movies.csv
       │      │
       │      ▼
       │  Tabela Hash
       │      │
       │      └── Busca e consulta de filmes
       │
       └── ratings.csv
              │
              ▼
       Associação das avaliações
              │
              └── Classificação por média

       Interface de terminal
              │
              ▼
       Fila Encadeada
              │
              └── Gerenciamento da lista de filmes
```

O sistema é executado localmente, por meio do terminal, sem depender de uma interface gráfica ou de um banco de dados externo. As estruturas de dados são implementadas manualmente, utilizando os recursos fundamentais da linguagem Python.

---

## 🧠 Estruturas de Dados Aplicadas

### 1. Tabela Hash

A Tabela Hash é utilizada para armazenar e localizar filmes por meio de seus identificadores (`movieId`).

Uma função hash transforma o identificador em uma posição inicial da tabela. Quando ocorre uma colisão — isto é, quando dois identificadores são direcionados à mesma posição — o sistema utiliza **sondagem linear (Linear Probing)** para procurar uma posição disponível.

A estrutura permite realizar operações de inserção, busca e remoção de registros.

| Operação | Complexidade média esperada | Pior caso |
|---|---|---|
| Busca | O(1) | O(n) |
| Inserção | O(1) | O(n) |
| Remoção | O(1) | O(n) |

A eficiência da Tabela Hash depende de fatores como o fator de carga, a distribuição dos valores hash e a quantidade de colisões. Portanto, as complexidades constantes representam o comportamento médio esperado, não uma garantia absoluta.

**Aplicação no CineTrack:**

- Armazenamento do catálogo de filmes.
- Busca por identificador.
- Recuperação de informações cinematográficas.
- Tratamento de colisões por sondagem linear.

### 2. Fila Encadeada

A Fila Encadeada é utilizada para gerenciar os filmes que o usuário deseja assistir.

Sua implementação segue o princípio **FIFO (First In, First Out)**, segundo o qual o primeiro elemento inserido é o primeiro a ser removido.

A estrutura utiliza células encadeadas por referências, mantendo ponteiros para o início e o final da fila. Essa organização permite inserir elementos no final e removê-los do início sem a necessidade de percorrer toda a estrutura.

| Operação | Complexidade |
|---|---|
| Inserção no final | O(1) |
| Remoção no início | O(1) |
| Consulta ao primeiro elemento | O(1) |

**Aplicação no CineTrack:**

- Adição de filmes à lista de acompanhamento.
- Consulta ao próximo filme da sequência.
- Visualização dos filmes armazenados.
- Remoção de filmes após serem marcados como assistidos.

---

## 📂 Estrutura do Projeto

O projeto segue uma organização modular, com arquivos responsáveis por diferentes componentes da aplicação.

```text
CineTrack/
│
├── filme.py
│   └── Modelo de dados e representação dos filmes
│
├── tabela_hash.py
│   └── Implementação da Tabela Hash com sondagem linear
│
├── fila.py
│   └── Implementação da Fila Encadeada para a lista de filmes
│
├── leitor.py
│   └── Leitura e processamento dos arquivos CSV do MovieLens
│
├── main.py
│   └── Menu interativo e fluxo principal da aplicação
│
├── movies.csv
│   └── Catálogo de filmes
│
├── ratings.csv
│   └── Registros de avaliações
│
├── tags.csv
│   └── Etiquetas textuais associadas aos filmes (opcional)
│
├── links.csv
│   └── Identificadores externos dos filmes (opcional)
│
└── README.md
    └── Documentação do projeto
```

> A organização acima representa a estrutura de referência utilizada na documentação. Os nomes dos arquivos de código e a disposição dos diretórios devem corresponder à versão efetivamente presente no repositório.

---

## 🛠️ Tecnologias e Ferramentas

| Tecnologia / Ferramenta | Aplicação |
|---|---|
| Python 3 | Implementação da lógica e das estruturas de dados. |
| CSV | Formato de armazenamento e leitura dos dados do MovieLens. |
| VS Code | Ambiente de desenvolvimento e edição do código. |
| Git | Controle de versão do projeto. |
| GitHub | Hospedagem do código-fonte e colaboração entre os integrantes. |
| MovieLens | Fonte dos dados cinematográficos e das avaliações. |

O projeto não exige bibliotecas externas para a implementação das estruturas de dados descritas, uma vez que elas são desenvolvidas manualmente pela equipe.

---

## 💻 Como Executar

### Pré-requisitos

Antes de executar o CineTrack, certifique-se de possuir:

- Python 3.8 ou superior instalado.
- Git instalado, caso opte por clonar o repositório.
- Os arquivos CSV necessários para carregar o dataset.
- Um terminal compatível com a execução de scripts Python.

### 1. Clonar o repositório

Clone o repositório utilizando o endereço correspondente ao projeto no GitHub:

```bash
git clone <URL_DO_REPOSITORIO>
```

Em seguida, acesse o diretório do projeto:

```bash
cd CineTrack
```

### 2. Obter o dataset

Faça o download do conjunto de dados no Kaggle:

[MovieLens Latest Small — Kaggle](https://www.kaggle.com/datasets/grouplens/movielens-latest-small?resource=download)

Extraia o arquivo compactado e localize os arquivos CSV.

Para a execução das funcionalidades principais, disponibilize os seguintes arquivos no diretório esperado pelo leitor de dados:

```text
movies.csv
ratings.csv
```

Caso o projeto utilize caminhos relativos, mantenha os arquivos na localização definida pelo código-fonte.

### 3. Executar a aplicação

No terminal, dentro do diretório do projeto, execute:

```bash
python main.py
```

Em ambientes nos quais o comando `python` não esteja associado à instalação correta, utilize:

```bash
py main.py
```

Após a execução, o sistema apresentará o menu interativo no terminal, permitindo selecionar as operações disponíveis.

---

## 🧪 Testes e Validação

Durante o desenvolvimento, foram considerados cenários para verificar o comportamento das estruturas de dados e a integridade das operações realizadas pelo sistema.

| Componente | Cenários de validação |
|---|---|
| Tabela Hash | Busca de registros, tratamento de colisões e remoção de elementos. |
| Fila Encadeada | Ordem FIFO, inserção, remoção e comportamento da fila vazia. |
| Sistema | Consulta de filmes inexistentes e tratamento de produções sem avaliações. |

Esses testes têm como finalidade verificar se as operações são executadas corretamente e se as estruturas preservam suas propriedades fundamentais.

---

## 📚 Fundamentação Acadêmica

O CineTrack demonstra a importância da escolha de estruturas de dados adequadas às operações exigidas por uma aplicação.

A Tabela Hash favorece a recuperação de registros por identificador, enquanto a Fila Encadeada permite organizar uma sequência de elementos de acordo com a ordem de entrada.

A implementação manual dessas estruturas contribui para a compreensão de seus mecanismos internos, incluindo funções hash, tratamento de colisões, encadeamento de nós, manipulação de ponteiros e análise de complexidade.

O projeto também evidencia a relação entre estruturas de dados e aplicações práticas, utilizando um conjunto de informações cinematográficas para contextualizar os conceitos estudados.

---

## 📄 Referências

**GROUPLENS RESEARCH.** MovieLens Latest Small. University of Minnesota. Disponível em: [https://www.grouplens.org/datasets/movielens/](https://www.grouplens.org/datasets/movielens/). Acesso em: 20 nov. 2026.

**KAGGLE.** MovieLens Latest Small Dataset. Disponível em: [https://www.kaggle.com/datasets/grouplens/movielens-latest-small](https://www.kaggle.com/datasets/grouplens/movielens-latest-small). Acesso em: 22 nov. 2026.

---

## 📌 Considerações Finais

O CineTrack constitui uma aplicação acadêmica voltada à demonstração prática de conceitos fundamentais de Estruturas de Dados.

A utilização de uma Tabela Hash e de uma Fila Encadeada permite atender a diferentes necessidades de armazenamento, consulta e gerenciamento de informações, evidenciando como a escolha de uma estrutura influencia o desempenho e a organização de um sistema.

Por meio da integração entre Python e o dataset MovieLens, o projeto transforma conceitos teóricos em funcionalidades concretas, contribuindo para o desenvolvimento de competências relacionadas à implementação de algoritmos, modularização de software e análise de complexidade computacional.
