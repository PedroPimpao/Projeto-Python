from itertools import cycle

toggle = cycle(['ON', 'OFF'])

class Forno:
    def __init__(self):
        self.UMID_INT = 0
        self.UMID_EXT = 0
        self.TEMP_INT = 0
        self.TEMP_EXT = 0
        self.conteudo = 0

    # Getters
    def get_umid_int(self):
        return self.UMID_INT
    
    def get_umid_ext(self):
        return self.UMID_EXT

    def get_temp_int(self):
        return self.TEMP_INT

    def get_temp_ext(self):
        return self.TEMP_EXT
    
    def get_conteudo(self):
        return self.conteudo

    # Setters
    def set_umid_int(self, UMID_INT):
        self.UMID_INT = UMID_INT

    def set_umid_ext(self, UMID_EXT):
        self.UMID_EXT = UMID_EXT

    def set_temp_int(self, TEMP_INT):
        self.TEMP_INT = TEMP_INT

    def set_temp_ext(self, TEMP_EXT):
        self.TEMP_EXT = TEMP_EXT

    def set_conteudo(self, conteudo):
        self.conteudo = conteudo



    def sensor(self, unidade):
        valor = 0
        if unidade == 'temp_ext':
            valor = self.get_temp_ext()
        elif unidade == 'temp_int':
            valor = self.get_temp_int()
        elif unidade == 'umid_ext':
            valor = self.get_umid_ext()
        elif unidade == 'umid_int':
            valor = self.get_umid_int()
        else:
            print('Leitura inválida')
            valor = 0

        return valor
    

    def acionar(self):
        temp_ext_input = int(input('Insira a temperatura externa: '))
        umid_ext_input = int(input('Insira a umidade do ar externa: '))

        self.set_temp_ext(temp_ext_input)
        self.set_umid_ext(umid_ext_input)

        umid_ext = self.sensor('umid_ext')
        temp_ext = self.sensor('temp_ext')
    
        if temp_ext <= 20 and umid_ext >= 40:
            print('É inverno')
            self.desumidificacao()
            self.coccao()
            return True
        
        print('NÃO é inverno')
        self.coccao()
        return False
    

    def desumidificacao(self):
        print('Início desumidificação')

        umid_int_input = int(input('Insira a umidade interna do forno: '))
        temp_int_input = int(input('Insira a temperatura interna do forno: '))

        self.set_umid_int(umid_int_input)
        self.set_temp_int(temp_int_input)

        umid_int = self.sensor('umid_int')
        temp_int = self.sensor('temp_int')

        if temp_int > 15 and umid_int >= 40:
            self.exaustor('ON')
        elif temp_int < 15  and umid_int >= 40: 
            self.aquecedor('ON', 100)
            self.exaustor('ON')

        umid_int = self.sensor('umid_int')
        if umid_int <= 5:
            self.exaustor('OFF')
            self.aquecedor('OFF', 0)
        
        print('Fim desumidificação')
        # pass


    def coccao(self):
        print('Início cocção')
        umid_int = self.sensor('umid_int')

        if umid_int > 15:
            self.exaustor('ON')
        
        temp_int = self.sensor('temp_int')

        if temp_int < 200:
            self.aquecedor('ON', 380)

        umid_int = self.sensor('umid_int')
        temp_int = self.sensor('temp_int')

        if umid_int <= 5:
            self.exaustor('OFF')
        elif umid_int <= 5 and temp_int == 380:
            print('Insira conteúdo para a Cocção')
            conteudo = int(input('Insira a quantidade de pães: '))
            self.set_conteudo(conteudo)
            
        # pass


    def aquecedor(self, estado, temperatura):
        if estado == 'ON':
            print('Aquecedor acionado')
            print(f'Aquecendo para {temperatura}°')
            self.set_temp_int(temperatura)
        elif estado == 'OFF':
            print('Aquecedor desativado')
        else: 
            print('Ação inválida')

    def exaustor(self, estado):
        umidade_config = 5
        if estado == 'ON':
            print('Exaustor acionado')
            print(f'Reduzindo a umidade para {umidade_config}%')
            self.set_umid_int(umidade_config)
        elif estado == 'OFF':
            print('Exaustor desativado')
        else: 
            print('Ação inválida')

    def timer(self, estado, tempo):
        if estado == 'set':
            tempo = 0
        pass

    def pronto(self):
        print(next(toggle))
        # print(next(toggle))






forno = Forno()

# forno.acionar()
forno.pronto()
forno.pronto()
forno.pronto()
# forno.pronto()