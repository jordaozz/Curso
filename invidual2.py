
candidatos = [
    ("Thayane", 4, 3, 5, 4),
    ("Hanna", 3, 4, 4, 3),
    ("Cezar", 5, 5, 6, 5),
    ("Gabriel", 4, 3, 7, 3),
    ("Luis Felipe", 4, 4, 8, 8)
]


def buscarcand(notas_minimas):
    filtragem = []

    for candidato in candidatos:
        nome, nota_e, nota_t, nota_p, nota_s = candidato

        if nota_e >= notas_minimas[0] and nota_t >= notas_minimas[1] and nota_p >= notas_minimas[2] and nota_s >= notas_minimas[3]:
            filtragem.append(candidato)

    return filtragem


nota_e_minima = int(input("Digite a nota mínima em E: "))
nota_t_minima = int(input("Digite a nota mínima em T: "))
nota_p_minima = int(input("Digite a nota mínima em P: "))
nota_s_minima = int(input("Digite a nota mínima em S: "))

notas_minimas = [nota_e_minima, nota_t_minima, nota_p_minima, nota_s_minima]


candidatosencontrados = buscarcand(notas_minimas)


if candidatosencontrados:
    print("Candidatos encontrados:")
    for candidato in candidatosencontrados:
        print(f"Nome: {candidato[0]}, Notas (E, T, P, S): {candidato[1:]}")
else:
    print("Nenhum candidato encontrado com base nos critérios de notas mínimas fornecidos.")
