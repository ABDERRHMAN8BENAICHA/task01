def note_student(note:float)->str:
    if note < 10:
        return "unsuccessful"
    if note >= 10 and note < 12 :
        return "better"
    if note >= 12 and note < 14 :
        return "good"