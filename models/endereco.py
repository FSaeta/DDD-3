import re
import requests


class CepInvalidoException(Exception):
    def __init__(self, message=""):
        msg = "CEP inválido"
        if message:
            msg += f": {message}"
        self.message = msg
        super().__init__(self.message)


class Endereco:
    def __init__(self, cep, rua, numero, complemento, pais, cidade, estado):
        self.rua = rua
        self.zipCode = self.validar_e_corrigir_cep(cep)
        self.numero = numero
        self.complemento = complemento
        self.pais = pais
        self.cidade = cidade
        self.estado = estado

    def validar_e_corrigir_cep(self, cep):
        if not cep:
            raise CepInvalidoException("CEP inválido: não pode ser vazio.")

        cep_limpo = re.sub(r"[^0-9]", "", cep)
        if len(cep_limpo) != 8:
            raise CepInvalidoException("CEP inválido: deve ter 8 dígitos.")

        cep_formatado = f"{cep_limpo[:5]}-{cep_limpo[5:]}"
        pattern = r"^\d{5}-\d{3}$"
        if not re.match(pattern, cep_formatado):
            raise CepInvalidoException("CEP inválido: formato incorreto (xxxxx-xxx).")

        return cep_formatado
    
    def getCoordenadas(self):
        endereco = f"{self.rua}, {self.numero}, {self.bairro}, {self.cidade}, {self.estado}, {self.cep}, {self.pais}"
        # url = f"https://nominatim.openstreetmap.org/search?q={endereco}&format=json"
        url = f"https://example-coordinates.getter.com/get?addrs={endereco}&format=json"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data:
                return data[0]['lat'], data[0]['lon']
        return None, None
