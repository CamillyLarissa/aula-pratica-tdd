import pytest
from unittest.mock import MagicMock
from aluno.aluno import Aluno, contar_aprovados


# =============================================================
# PARTE 1 — Encontre os bugs
# Escreva um teste para cada bug descrito no guia da atividade.
# =============================================================

def test_menor_nota_deve_retornar_valor_minimo():
    aluno = Aluno("Camilly", [5.0, 10.0, 2.0, 8.0])
    assert aluno.menor_nota() == 2.0

def test_media_arredondada_para_baixo():
    aluno = Aluno(nome="João", notas=[5, 6, 5, 6], faltas=1)
    assert aluno.calcular_media_arredondada() == 6

def test_calcular_media():
    aluno = Aluno("Teste", [10, 10])
    assert aluno.calcular_media() == 10.0

def test_situacao_aprovado():
    aluno = Aluno(nome="Larissa", notas=[6, 6, 6, 6], faltas=12)
    assert aluno.situacao() == "Aprovado"

def test_situacao_reprovado():
    aluno = Aluno(nome="Carlos", notas=[5, 5, 4, 4], faltas=2)
    assert aluno.situacao() == "Reprovado"

def test_maior_nota_deve_retornar_valor_maximo():
    aluno = Aluno("Ana", [5.0, 10.0, 2.0, 8.0])
    assert aluno.maior_nota() == 10.0
# =============================================================
# PARTE 2 — Implemente com TDD
# Siga o ciclo: 🔴 escreva o teste → 🟢 implemente → 🟡 refatore
# =============================================================

# Requisito 1 — contar_aprovados(lista_de_alunos) -> int
# Escreva os testes ANTES de implementar a função
def test_contar_aprovados_vazio():
    assert contar_aprovados([]) == 0

def test_contar_aprovados_mista():
    alunos = [Aluno("A", [10, 10, 10, 10]), Aluno("B", [2, 2, 2, 2])]
    assert contar_aprovados(alunos) == 1

# Requisito 2 — situacao_final(total_aulas) -> str
# Escreva os testes ANTES de implementar o método

def test_aprovado_limite_25_faltas():
    aluno = Aluno("Camilly", [8, 8, 8, 8], faltas=25)
    assert aluno.situacao_final(100) == "Aprovado"

def test_reprovado_por_faltas_acima_25():
    aluno = Aluno("Camilly", [8, 8, 8, 8], faltas=26)
    assert aluno.situacao_final(100) == "Reprovado por falta"

# Requisito 3 — enviar_boletim(email_service)
# Use MagicMock para simular o serviço de e-mail
# Escreva os testes ANTES de implementar o método

def test_enviar_boletim_reprovado():
    mock_servico = MagicMock()
    aluno = Aluno("Camilly", [2, 2, 2, 2])
    aluno.enviar_boletim(mock_servico)
    mock_servico.enviar.assert_called_once()