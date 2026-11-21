class Filme: # declaração dos atributos
    idFilme = None
    titulo = None
    generos = None
    somaAvaliacoes = 0.0
    quantidadeAvaliacoes = 0
    mediaAvaliacoes = 0.0

    def __init__(self, idFilme, titulo, generos): # construtor da classe Filme.
        
        self.idFilme = int(idFilme)
        self.titulo = titulo
        self.generos = generos  # pode ser mantido como string original ("Action|Adventure") ou lista
        self.somaAvaliacoes = 0.0
        self.quantidadeAvaliacoes = 0
        self.mediaAvaliacoes = 0.0

    def adicionarAvaliacao(self, nota): # adiciona uma nova avaliação recebida (ex: do ratings.csv) e atualiza a soma, a quantidade e a média das avaliações.
        
        self.somaAvaliacoes += float(nota)
        self.quantidadeAvaliacoes += 1
        self.calcularMedia()

    def calcularMedia(self): # calcula e atualiza a média das avaliações do filme

        if self.quantidadeAvaliacoes > 0:
            self.mediaAvaliacoes = self.somaAvaliacoes / self.quantidadeAvaliacoes
        else:
            self.mediaAvaliacoes = 0.0
        return self.mediaAvaliacoes

    def __str__(self): # retorna a representação em string do objeto Filme

        generosFormatados = self.generos.replace("|", ", ")
        return (
            f"🎬 [{self.idFilme}] {self.titulo}\n"
            f"   Gêneros  : {generosFormatados}\n"
            f"   Avaliação: ⭐ {self.mediaAvaliacoes:.2f} ({self.quantidadeAvaliacoes} notas)\n"
            f"{'-' * 55}"
        )

    def imprimir(self): # exibe os dados do filme
        
        print(self.__str__())