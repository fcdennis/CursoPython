from random import shuffle
nome1 = input("Primeiro aluno: ")
nome2 = input("Segundo aluno: ")
nome3 = input("Terceiro aluno: ")
nome4 = input("Quarto aluno: ")
turma = [nome1, nome2, nome3, nome4]
shuffle(turma)
print(f"A ordem de apresentação será {(turma)}")
