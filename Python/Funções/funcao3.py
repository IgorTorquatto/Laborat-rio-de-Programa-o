def media_notas(notas):
    media= sum(notas) / len(notas)
    return media


if __name__ == '__main__':
    lista=[4.5,8,7,3,10]
    media_turma=media_notas(lista)
    print(f"A média da turma foi de : {media_turma}")
