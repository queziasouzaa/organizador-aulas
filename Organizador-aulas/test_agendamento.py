import pytest
from agendamento import ler_aulas, obter_grade_formatada, Aula

def test_leitura_aulas(tmp_path):
    conteudo = """Introdução à IA - Prof. Ana 60min
Machine Learning - Prof. João 45min
Deep Learning - Prof. Ana lightning
"""
    arquivo = tmp_path / "aulas.txt"
    arquivo.write_text(conteudo, encoding="utf-8")
    
    aulas = ler_aulas(arquivo)
    
    assert len(aulas) == 3
    assert aulas[0].titulo == "Introdução à IA"
    assert aulas[0].professor == "Ana"
    assert aulas[0].duracao == 60
    assert aulas[2].duracao == 5  # lightning

def test_geracao_grade():
    aulas = [
        Aula("Aula 1", "Prof. Ana", "60min"),
        Aula("Aula 2", "Prof. João", "45min"),
        Aula("Aula 3", "Prof. Ana", "lightning"),
        Aula("Aula 4", "Prof. Maria", "30min"),
    ]
    grade = obter_grade_formatada(aulas)
    assert "Prof. Ana" in grade
    assert "Aula 1" in grade
    assert "17:00 Reunião de Professores" in grade

