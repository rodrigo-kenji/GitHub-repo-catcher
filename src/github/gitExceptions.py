# Usa a classe Exception para criar uma exceção personalizada
class requestException(Exception):
    def __init__(self, message: str = 'Erro na requisição'):
        self.message = message
        super().__init__(message)