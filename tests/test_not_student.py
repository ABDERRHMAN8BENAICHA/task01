from src.not_student import not_student


def test_not_student_sup_10_returns_unsseccfull():
    assert not_student(9) == "غير ناجح"
