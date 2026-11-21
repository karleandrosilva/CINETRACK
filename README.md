# 🎬 CineTrack - Sistema de Gerenciamento de Filmes

O **CineTrack** é uma aplicação interativa via terminal desenvolvida em Python para gerenciamento e consulta de filmes utilizando o dataset **MovieLens**. O projeto foi estruturado com foco em **Estruturas de Dados**, aplicando conceitos de **Tabela Hash com Sondagem Linear** e **Fila Encadeada (FIFO)** para garantir alta performance e eficiência nas operações.

---

## 🚀 Funcionalidades

- **🔍 Busca `O(1)` por ID:** Localização instantânea de filmes na Tabela Hash a partir do `movieId`.
- **🔎 Busca por Título:** Pesquisa flexível por nome ou trecho do título do filme.
- **🎭 Filtro por Gênero:** Listagem de filmes por categoria (ex: *Action, Comedy, Drama*).
- **⭐ Ranking dos Mais Bem Avaliados:** Cálculo da média das notas a partir do `ratings.csv` para listar os filmes no topo.
- **🍿 Fila de Assistir (Watchlist FIFO):** Adição de filmes ao final da fila em `O(1)`.
- **✔️ Marcar como Assistido:** Remoção do próximo filme a ser assistido (início da fila) em `O(1)`.

---

## 🛠️ Estruturas de Dados Aplicadas

| Estrutura | Função no Sistema | Tratamento / Regra | Complexidade |
| :--- | :--- | :--- | :--- |
| **Tabela Hash** | Armazenamento e busca de filmes por ID | Sondagem Linear (*Linear Probing*) | Inserção `O(1)` / Busca `O(1)` |
| **Fila Encadeada** | Gerenciamento da Watchlist | FIFO (*First In, First Out*) com ponteiros `ini` e `fim` | Enfileirar `O(1)` / Desenfileirar `O(1)` |

---

## 📂 Estrutura do Projeto

A arquitetura do projeto segue o padrão **modular**, separando as responsabilidades em arquivos independentes:

```text
cinetrack/
├── filme.py          # Modelo de dados (Classe Filme)
├── tabela_hash.py    # Tabela Hash com Sondagem Linear para busca por ID
├── fila.py           # Fila Encadeada (FIFO) para a Watchlist
├── leitor.py         # Leitor dos arquivos CSV (movies.csv e ratings.csv)
├── main.py           # Menu interativo do terminal e fluxo de controle
├── movies.csv        # Base de dados de filmes (MovieLens)
└── ratings.csv       # Base de dados de avaliações (MovieLens)
```

---

## 🖥️ Como Executar

### Pré-requisitos
- **Python 3.8+** instalado.
- Arquivos `movies.csv` e `ratings.csv` salvos no mesmo diretório dos scripts *(caso não sejam encontrados, o sistema inicia automaticamente com filmes de teste)*.

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/cinetrack.git](https://github.com/seu-usuario/cinetrack.git)
   ```

2. **Acesse a pasta do projeto:**
   ```bash
   cd cinetrack
   ```

3. **Execute o programa:**
   ```bash
   python main.py
   ```
