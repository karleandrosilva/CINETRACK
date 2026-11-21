class TabelaHashFilmes:
    tamanho = 0
    tabela = None
    quantidadeElementos = 0

    def __init__(self, tamanho=10007): # inicializa a tabela hash com um tamanho preferencialmente primo para reduzir colisões iniciais
        
        self.tamanho = tamanho
        self.tabela = [None] * self.tamanho
        self.quantidadeElementos = 0

    def _funcaoHash(self, idFilme): # método privado para calcular a posição inicial baseada no ID do filme na tabela hash.
        
        return idFilme % self.tamanho

    def inserir(self, filme): # insere um objeto Filme na tabela hash, tratando colisões com sondagem linear (Linear Probing).
        
        pos = self._funcaoHash(filme.idFilme)

        # sondagem linear: procura a próxima posição livre ou atualiza se já existir
        for i in range(self.tamanho):
            indice = (pos + i) % self.tamanho

            # posição livre encontrada
            if self.tabela[indice] is None:
                self.tabela[indice] = filme
                self.quantidadeElementos += 1
                return True

            # se o filme já existe na tabela (mesmo ID), substitui/atualiza
            if self.tabela[indice].idFilme == filme.idFilme:
                self.tabela[indice] = filme
                return True

        print("❌ Erro: Tabela Hash cheia! ❌")
        return False

    def buscar(self, idFilme): # busca um filme pelo ID (movieId) com complexidade média O(1). Retorna o objeto Filme ou None se não encontrado.
        
        pos = self._funcaoHash(int(idFilme))

        for i in range(self.tamanho):
            indice = (pos + i) % self.tamanho

            # se encontrar posição vazia, o filme não está na tabela
            if self.tabela[indice] is None:
                return None

            # filme encontrado
            if self.tabela[indice].idFilme == int(idFilme):
                return self.tabela[indice]

        return None

    def obterTodosFilmes(self): 
        filmes = [] 
        for item in self.tabela: 
            if item is not None: 
                filmes.append(item) 
        return filmes