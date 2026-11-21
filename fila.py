class Celula:
    item = None
    proximo = None

    def __init__(self, item): # representa um nó na memória que armazena um objeto Filme e uma referência para a próxima célula.
        
        self.item = item
        self.proximo = None

    def imprimir(self): # retorna a representação textual da célula, mostrando o item armazenado e a referência para a próxima célula.
        
        return f'[{self.item} | {self.proximo}]'


class FilaFilmes: # atributos de classe no topo (estilo utilizado nas aulas)

    ini = None
    fim = None
    tamanho = 0

    def __init__(self): # construtor da classe FilaFilmes, inicializando os atributos da fila.
        
        self.ini = None
        self.fim = None
        self.tamanho = 0

    def estaVazia(self): # verifica se a fila está vazia 
        
        return self.ini is None

    def enfileirar(self, filme): # adiciona um filme ao final da fila (Watchlist). Complexidade: O(1)
        
        c = Celula(filme)
        if self.estaVazia():
            self.ini = c
            self.fim = c
        else:
            self.fim.proximo = c
            self.fim = c
        self.tamanho += 1
        print(f"Filme '{filme.titulo}' adicionado à fila de reprodução!")

    def desenfileirar(self): # remove e retorna o próximo filme a ser assistido (do início da fila). Complexidade: O(1)
        
        if self.estaVazia():
            print('Fila vazia! Nenhum filme para assistir.')
            return None

        aux = self.ini
        self.ini = self.ini.proximo

        # se a fila ficou vazia após a remoção, atualiza o ponteiro fim
        if self.ini is None:
            self.fim = None

        item = aux.item
        del aux
        self.tamanho -= 1
        return item

    def marcarComoAssistido(self): # marca o próximo filme da fila como assistido, removendo-o do início da fila. Complexidade: O(1)
        
        filme = self.desenfileirar()
        if filme:
            print(f"🍿 Você assistiu: {filme.titulo}")
        return filme

    def proximoFilme(self): # consulta o próximo filme a ser assistido sem removê-lo da fila. Complexidade: O(1)
        
        if self.estaVazia():
            print('Fila vazia! Nenhum filme pendente.')
            return None
        return self.ini.item

    def imprimirFila(self): # exibe a sequência de filmes a serem assistidos na ordem (FIFO).
        
        print('\n--- FILA DE FILMES PARA ASSISTIR ---')
        if self.estaVazia():
            print('Fila vazia.')
        else:
            aux = self.ini
            posicao = 1
            while aux is not None:
                print(f"{posicao}º -> {aux.item.titulo} (ID: {aux.item.idFilme} | Média: {aux.item.mediaAvaliacoes:.2f})")
                aux = aux.proximo
                posicao += 1
        print('-------------------------------------\n')