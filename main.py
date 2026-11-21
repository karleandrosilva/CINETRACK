# IMPORTAÇÃO DOS MÓDULOS DO PROJETO
from lerCsv import carregarMovielens
from fila import FilaFilmes

def menu(): # inicializa os dados carregando a Tabela Hash e instanciando a Fila

    tabelaFilmes = carregarMovielens("movies.csv", "ratings.csv")
    watchlist = FilaFilmes()

    # loop principal da interface de terminal
    while True:
        print("\n" + "=" * 45)
        print("            🎬 CINETRACK - MENU 🎬           ")
        print("=" * 45)
        print("1. Buscar filme por ID (Tabela Hash)")
        print("2. Buscar filme por título")
        print("3. Consultar filmes por gênero")
        print("4. Exibir filmes mais bem avaliados")
        print("5. Adicionar filme à Fila de Assistir")
        print("6. Consultar Fila de Assistir (Watchlist)")
        print("7. Marcar próximo filme como assistido (FIFO)")
        print("0. Sair")
        print("=" * 45)

        opcao = input("Escolha uma opção: ").strip()

        # --- OPÇÃO 1: busca O(1) na Tabela Hash ---
        if opcao == "1":
            try:
                idFilme = int(input("Digite o ID do filme: "))
                filme = tabelaFilmes.buscar(idFilme)
                if filme:
                    print("\n--- Filme Encontrado ---")
                    filme.imprimir()
                else:
                    print(f"\n❌ Filme com ID {idFilme} não foi encontrado. ❌")
            except ValueError:
                print("\n⚠️ Por favor, digite um número de ID válido. ⚠️")

        # --- OPÇÃO 2: busca por Título ---
        elif opcao == "2":
            termo = input("Digite o título (ou parte dele): ").lower()
            encontrados = 0
            print("\n--- Resultados da Busca por Título ---")
            for f in tabelaFilmes.obterTodosFilmes():
                if termo in f.titulo.lower():
                    f.imprimir()
                    encontrados += 1
                    if encontrados >= 10:
                        print("... (Exibindo até 10 resultados para evitar excesso de dados)")
                        break
            if encontrados == 0:
                print("Nenhum filme encontrado com o termo informado.")

        # --- OPÇÃO 3: filtro por Gênero ---
        elif opcao == "3":
            genero = input("Digite o gênero desejado (ex: Comedy, Action): ").lower()
            encontrados = 0
            print(f"\n--- Filmes do Gênero '{genero.capitalize()}' ---")
            for f in tabelaFilmes.obterTodosFilmes():
                if genero in f.generos.lower():
                    f.imprimir()
                    encontrados += 1
                    if encontrados >= 10:
                        break
            if encontrados == 0:
                print("Nenhum filme encontrado para o gênero informado.")

        # --- OPÇÃO 4: ranking por Média de Notas ---
        elif opcao == "4":
            todos = tabelaFilmes.obterTodosFilmes()
            # considerando apenas filmes com ao menos 5 avaliações
            relevantes = [f for f in todos if f.quantidadeAvaliacoes >= 5]
            relevantes.sort(key=lambda x: x.mediaAvaliacoes, reverse=True)

            print("\n--- Top 10 Filmes Mais Bem Avaliados ---")
            for f in relevantes[:10]:
                f.imprimir()

        # --- OPÇÃO 5: adicionar à Watchlist (Enfileirar) ---
        elif opcao == "5":
            try:
                idFilme = int(input("Digite o ID do filme para adicionar à Fila: "))
                filme = tabelaFilmes.buscar(idFilme)
                if filme:
                    watchlist.enfileirar(filme)
                else:
                    print(f"\n❌ Filme com ID {idFilme} não encontrado. ❌")
            except ValueError:
                print("\n⚠️ Digite um ID numérico válido. ⚠️")

        # --- OPÇÃO 6: consultar Fila ---
        elif opcao == "6":
            watchlist.imprimirFila()

        # --- OPÇÃO 7: assistir Filme (Desenfileirar FIFO) ---
        elif opcao == "7":
            watchlist.marcarComoAssistido()

        # --- OPÇÃO 0: encerrar Programa ---
        elif opcao == "0":
            print("\n🍿 Obrigado por usar o CineTrack! Até a próxima. 🍿")
            break

        else:
            print("\n⚠️ Opção inválida! Tente novamente. ⚠️")


if __name__ == "__main__":
    menu() 