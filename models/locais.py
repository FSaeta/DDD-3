import re


class Endereco:

    def __init__(self, rua, cep, numero):
        self.rua = rua
        self.cep = self.validar_e_corrigir_cep(cep)
        self.numero = numero

    def validar_e_corrigir_cep(self, cep):
        if not cep:
            raise ValueError("CEP inválido: não pode ser vazio.")

        cep_limpo = re.sub(r"[^0-9]", "", cep)
        if len(cep_limpo) != 8:
            raise ValueError("CEP inválido: deve ter 8 dígitos.")

        cep_formatado = f"{cep_limpo[:5]}-{cep_limpo[5:]}"
        pattern = r"^\d{5}-\d{3}$"
        if not re.match(pattern, cep_formatado):
            raise ValueError("CEP inválido: formato incorreto (xxxxx-xxx).")

        return cep_formatado


class Local:

    def __init__(self, endereco, nome):
        self.endereco = endereco
        self.nome = nome


# Exemplo de uso
if __name__ == "__main__":
    print("Hello, World!")

    endereco = Endereco("Rua Exemplo", "12345678", "100")
    local = Local(endereco, "Meu Local")

    print(local.endereco.cep)  # Imprime o CEP formatado ou a mensagem de erro

