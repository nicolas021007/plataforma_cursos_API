
class Curso:
    def __init__(self, codigo: int, titulo: str, preco: float, tipo: int, desconto_percentual: float = 0):
        if desconto_percentual > 100 or desconto_percentual < 0:
            raise ValueError("Desconto deve estar entre 0 e 100")
        if preco <0:
            raise ValueError("Preço não pode ser negativo")
        
        self.codigo=codigo,
        self.titulo=titulo,
        self.preco=preco,
        self.tipo=tipo,
        self.desconto_percentual=desconto_percentual
        
    def preco_final(self)->float:
        if self.tipo==1:
            return 0.0
        desconto = self.preco*(self.desconto_percentual/100)
        return round(self.preco-desconto, 2)
    

    


                