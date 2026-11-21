import csv
import os
from filme import Filme
from tabelaHash import TabelaHashFilmes

def carregarMovielens(caminhoMovies="movies.csv", caminhoRatings="ratings.csv"):
    tabelaHash = TabelaHashFilmes(tamanho=15007)

    # caso os arquivos CSV não estejam no diretório
    if not os.path.exists(caminhoMovies) or not os.path.exists(caminhoRatings):
        print("⚠️ Arquivos movies.csv ou ratings.csv não encontrados no diretório! ⚠️")

        return tabelaHash

    print("⏳ Carregando dados do MovieLens... ⏳")
    try:
        # lê movies.csv (movieId, title, genres)
        with open(caminhoMovies, mode='r', encoding='utf-8') as arq:
            leitor = csv.reader(arq)
            next(leitor)  # pula o cabeçalho
            for linha in leitor:
                if len(linha) >= 3:
                    novoFilme = Filme(linha[0], linha[1], linha[2])
                    tabelaHash.inserir(novoFilme)

        # lê ratings.csv (userId, movieId, rating, timestamp)
        with open(caminhoRatings, mode='r', encoding='utf-8') as arq:
            leitor = csv.reader(arq)
            next(leitor)  # pula o cabeçalho
            for linha in leitor:
                if len(linha) >= 3:
                    idFilme = int(linha[1])
                    nota = float(linha[2])
                    filme = tabelaHash.buscar(idFilme)
                    if filme:
                        filme.adicionarAvaliacao(nota)

        print("✅ Dados carregados com sucesso!")

    except Exception as e:
        print(f"Erro no carregamento: {e}")

    return tabelaHash