from .add_qna_model import add_qna_model

def add_multiple_qna_model(subject, list_of_qna):
  if not len(list_of_qna):
    raise ValueError("--INVALID INPUT: Q & A list are empty.")
  
  for qna in list_of_qna:
    try:
      if not qna["question"] and not qna["answer"]:
        continue
      if not qna["question"] or not qna["answer"]:
        continue
      
      add_qna_model(subject, qna)
    except ValueError as e:
      raise ValueError(e)