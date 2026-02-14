class Professor: 
    def __init__(self, nome, endereco, admissao, area_atuacao, chd, chs, valor_hora_aula, trabalhado_semana, trabalhado_mes, custo_semanal, custo_mensal):
        self.nome = nome
        self.endereco = endereco
        self.admissao = admissao
        self.area_atuacao = area_atuacao
        self.chd = chd
        self.chs = chs
        self.valor_hora_aula = valor_hora_aula
        self.trabalhado_semana = trabalhado_semana
        self.trabalhado_mes = trabalhado_mes
        self.custo_semanal = custo_semanal
        self.custo_mensal = custo_mensal


    def getNome(self):
        return self.nome
    
    def setNome(self, novo_nome):
        self.nome = novo_nome
        return novo_nome
    
    def getEndereco(self):
        return self.endereco

    def setEndereco(self, novo_endereco):
        self.endereco = novo_endereco
        return novo_endereco

    def getAdmissao(self):
        return self.admissao

    def setAdmissao(self, nova_admissao):
        self.admissao = nova_admissao
        return nova_admissao

    def getAreaAtuacao(self):
        return self.area_atuacao

    def setAreaAtuacao(self, nova_area_atuacao):
        self.area_atuacao = nova_area_atuacao
        return nova_area_atuacao

    def getChd(self):
        return self.chd

    def setChd(self, nova_chd):
        self.chd = nova_chd
        return nova_chd

    def getChs(self):
        return self.chs

    def setChs(self, nova_chs):
        self.chs = nova_chs
        return nova_chs

    def getValorHoraAula(self):
        return self.valor_hora_aula

    def setValorHoraAula(self, novo_valor_hora_aula):
        self.valor_hora_aula = novo_valor_hora_aula
        return novo_valor_hora_aula

    def getTrabalhadoSemana(self):
        return self.trabalhado_semana

    def setTrabalhadoSemana(self, novo_trabalhado_semana):
        self.trabalhado_semana = novo_trabalhado_semana
        return novo_trabalhado_semana

    def getTrabalhadoMes(self):
        return self.trabalhado_mes

    def setTrabalhadoMes(self, novo_trabalhado_mes):
        self.trabalhado_mes = novo_trabalhado_mes
        return novo_trabalhado_mes

    def getCustoSemanal(self):
        return self.custo_semanal

    def setCustoSemanal(self, novo_custo_semanal):
        self.custo_semanal = novo_custo_semanal
        return novo_custo_semanal

    def getCustoMensal(self):
        return self.custo_mensal

    def setCustoMensal(self, novo_custo_mensal):
        self.custo_mensal = novo_custo_mensal
        return novo_custo_mensal
