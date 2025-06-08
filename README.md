# 📚 Organizador de Aulas para Professores

Esta é  uma atividade de uma aplicação Python que organiza automaticamente a grade de aulas semanais para uma instituição de ensino, respeitando restrições de horário e conflitos de professores.

Também conta com uma **interface gráfica simples** usando Tkinter, além de testes automatizados com `pytest`.

---

## Funcionalidades

* Leitura de um arquivo `aulas.txt` contendo as propostas de aulas.
* Organização automática das aulas por dia e turno (manhã/tarde).
* Evita conflitos de horários entre professores.
* Interface gráfica com tema escuro para visualização da grade.
* Testes automatizados com `pytest`.

---

## Regras de alocação

* **Turno da manhã:** das 09h00 às 12h00 (180 minutos)
* **Turno da tarde:** das 13h00 às 17h00 (240 minutos)
* Aulas com duração definida em minutos ou como `"lightning"` (5 minutos).
* Um professor **não pode ter mais de uma aula ao mesmo tempo**.
* Todas as aulas devem terminar antes da reunião obrigatória às 17h00.
* Aulas são alocadas por prioridade de duração (mais longas primeiro).

---

## Exemplo do arquivo `aulas.txt`

Cada linha deve conter:

```text
Nome da Aula - Prof. NomeDoProfessor 60min
Outra Aula - Prof. Fulano lightning
```

Exemplo:

```
Inteligência Artificial - Prof. Ana 60min
Redes de Computadores - Prof. João 45min
Algoritmos Genéticos - Prof. Ana lightning
```

---

## Interface Gráfica

Execute com:

```bash
python gui.py
```

Permite carregar um arquivo de aulas e visualizar a grade organizada com um tema escuro.

---

## Rodando os Testes

Use `pytest` para executar os testes automatizados:

```bash
pytest test_agendamento.py
```

---

## Requisitos e Instalação

Este projeto usa apenas bibliotecas padrão do Python, então **não há necessidade de instalar pacotes externos**, a menos que você queira rodar os testes com `pytest`.

### Instalar o `pytest` (opcional, mas recomendado)

```bash
pip install pytest
```

---

## Estrutura do Projeto

```
organizador_de_aulas/
├── organizacaoDeAulas.py        # Lógica principal de organização
├── gui.py                       # Interface gráfica (Tkinter)
├── test_agendamento.py         # Testes automatizados com pytest
├── aulas.txt                   # Arquivo de entrada de exemplo
└── README.md                   # Este arquivo
```

---

## Autor

Desenvolvido por \Quézia Souza
Projeto para fins educacionais, com foco em organização de horários e estruturas de dados.

---
