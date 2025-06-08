import re
from datetime import datetime, timedelta

# Tempo das sessões
HORARIO_MANHA = ("09:00", "12:00")
HORARIO_TARDE = ("13:00", "17:00")

MINUTOS_MANHA = 180
MINUTOS_TARDE = 240

def minutos_para_hora(base_time, minutos):
    return (datetime.strptime(base_time, "%H:%M") + timedelta(minutes=minutos)).strftime("%H:%M")

class Aula:
    def __init__(self, titulo, professor, duracao):
        self.titulo = titulo
        self.professor = professor
        self.duracao = 5 if duracao.lower() == "lightning" else int(re.sub(r"\D", "", duracao))

    def __repr__(self):
        return f"{self.titulo} - {self.professor} {self.duracao}min"

class Sessao:
    def __init__(self, tipo, hora_inicio, duracao_max):
        self.tipo = tipo
        self.hora_inicio = hora_inicio
        self.duracao_max = duracao_max
        self.horario_atual = 0
        self.aulas = []
        self.professores_ocupados = set()

    def pode_alocar(self, aula):
        if self.horario_atual + aula.duracao > self.duracao_max:
            return False
        if aula.professor in self.professores_ocupados:
            return False
        return True

    def alocar(self, aula):
        if self.pode_alocar(aula):
            hora_formatada = minutos_para_hora(self.hora_inicio, self.horario_atual)
            self.aulas.append((hora_formatada, aula))
            self.professores_ocupados.add(aula.professor)
            self.horario_atual += aula.duracao
            return True
        return False

class Dia:
    def __init__(self, nome_dia):
        self.nome = nome_dia
        self.manha = Sessao("Manhã", HORARIO_MANHA[0], MINUTOS_MANHA)
        self.tarde = Sessao("Tarde", HORARIO_TARDE[0], MINUTOS_TARDE)

    def tentar_alocar(self, aula):
        return self.manha.alocar(aula) or self.tarde.alocar(aula)

    def imprimir(self):
        print(self.formatar())

    def formatar(self):
        linhas = [f"\n{self.nome}:"]
        for sessao in [self.manha, self.tarde]:
            linhas.append("")
            if not sessao.aulas:
                linhas.append(f"{sessao.hora_inicio} (sem aulas disponíveis)")
            else:
                for hora, aula in sessao.aulas:
                    linhas.append(f"{hora} {aula.titulo} - {aula.professor} {aula.duracao}min")
            if sessao.tipo == "Manhã":
                linhas.append("12:00 Intervalo para Almoço")
        linhas.append("17:00 Reunião de Professores")
        return "\n".join(linhas)

def ler_aulas(arquivo):
    aulas = []
    with open(arquivo, "r", encoding="utf-8") as f:
        for linha in f:
            if linha.strip():
                match = re.match(r"(.+?) - Prof\. (.+?) (\d+min|lightning)", linha.strip())
                if match:
                    titulo, professor, duracao = match.groups()
                    aulas.append(Aula(titulo.strip(), professor.strip(), duracao.strip()))
    return aulas

def obter_grade_formatada(aulas):
    dias_da_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira"]
    aulas_ordenadas = sorted(aulas, key=lambda x: -x.duracao)
    dias = [Dia(nome) for nome in dias_da_semana]

    dia_index = 0
    for aula in aulas_ordenadas:
        alocada = False
        tentativas = 0
        while not alocada and tentativas < len(dias):
            dia = dias[dia_index % len(dias)]
            if dia.tentar_alocar(aula):
                alocada = True
            else:
                dia_index += 1
                tentativas += 1
        if not alocada:
            novo_nome = f"Dia Extra {len(dias) + 1}"
            novo_dia = Dia(novo_nome)
            novo_dia.tentar_alocar(aula)
            dias.append(novo_dia)

    return "\n".join([dia.formatar() for dia in dias])

def organizar_aulas(arquivo="aulas.txt"):
    aulas = ler_aulas(arquivo)
    resultado = obter_grade_formatada(aulas)
    print(resultado)

if __name__ == "__main__":
    organizar_aulas()
