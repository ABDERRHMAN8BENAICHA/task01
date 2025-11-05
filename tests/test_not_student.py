from src.not_student import note_student


def test_note_student_sup_10_returns_unsuccessful():
    assert note_student(9) == "unsuccessful"
