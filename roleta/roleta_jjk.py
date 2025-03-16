import random

class Roletagem:
    def __init__(self):
        self.racas = [
            ("Humano", 70),
            ("Feto Amaldiçoado", 5),
            ("Infernal", 10),
            ("Híbrido", 5)
        ]

        self.raridades = {
            "Comum": [
                "Técnica do boneco de palha", "Técnica da Razão", "Manipulação de Objetos",
                "Construção", "Técnica de clonagem", "Inverso", "Manipulação fotográfica",
                "Técnica de anestesia", "Técnica de imobilização", "Manipulação do céu"
            ],
            "Raro": [
                "Boogie Woogie", "Técnica do amplificamento de som", "Manipulação de marionetes",
                "Manipulação de corvos", "Milagres", "Mãos gigantes de Pedra", "Técnica das mãos gigantes",
                "Recriação Contratual", "Técnica da explosão", "Cajado de guerra G",
                "Descarga de energia amaldiçoada"
            ],
            "Épico": [
                "Gambito do apostador", "Fúria estelar", "Sistema Anti Gravitacional", "Manipulação de espíritos amaldiçoados",
                "Invocação das bestas Auspiciosas","Formação de Gelo", "Coragem flamejante",
                "Encontro do amor", "Julgamento", "Maldição Rainha: Rika", "Mythical Beast Amber",
                 "Extinção de Técnica"
            ],
        }
        self.infernais = [
            "do Sangue", "do Tubarão", "da Violência", "da Pistola", "da Guerra", "do Cosmos"
        ]
        self.hibridos = [
            "da Motoserra", "da Lança", "de Lança-Chamas", "da Espada Longa", "da Katana",
            "do Arco", "da Bomba", "do Chicote"
        ]

    def roletagem(self):
        raca = random.choices(*zip(*self.racas))[0]
        resultado = {
            "Raça": raca,
            "Clã": None,
            "Técnica": None,
            "EA": None,
            "Extra": None
        }

        if raca == "Humano":
            resultado["Clã"] = self.roletaCla()
            resultado["Técnica"] = self.roletaTecnica(resultado["Clã"])
            resultado['EA'] = self.roletaEnergiaAmaldicoada(resultado["Técnica"])
            resultado['Extra'] = self.roletaExtra(resultado["Clã"])
            resultado['Extra2'] = self.roletaExtra2()

        elif raca == "Feto Amaldiçoado":
            resultado["Técnica"] = self.roletaTecnica(cl="Maldição")
            resultado['EA'] = self.roletaEnergiaAmaldicoada(resultado["Técnica"])
            resultado['Extra'] = self.roletaExtrasComuns()

        elif raca == "Infernal":
            resultado['Infernal'] = self.roletaInfernal()
            resultado['EA'] = self.roletaEnergiaAmaldicoada(resultado["Técnica"])
            resultado['Extra'] = self.roletaExtrasComuns()

        elif raca == "Híbrido":
            resultado['Híbrido'] = self.roletaHibrido()
            resultado['EA'] = self.roletaEnergiaAmaldicoada(resultado["Técnica"])
            resultado['Extra'] = self.roletaExtrasComuns()

        return resultado

    def roletaCla(self):
        cl = random.choices(["Clã Kamo", "Clã Zenin", "Clã Inumaki", "Clã Gojo", "Sem Clã"], [25, 20, 25, 10, 70])[0]
        return cl

    def roletaInfernal(self):
        infernal = random.choice(self.infernais)
        return infernal

    def roletaHibrido(self):
        hibrido = random.choice(self.hibridos)
        return hibrido

    def roletaTecnica(self, cl=None):
        chance = random.randint(1, 100)

        if chance <= 10:
            return "Sem Técnica"

        elif cl == "Clã Gojo":
            return "Ilimitado" if chance <= 10 else random.choice(
                self.raridades["Comum"] + self.raridades["Raro"] + self.raridades["Épico"])

        elif cl == "Clã Zenin":
            return random.choice(["Dez Sombras", "Restrição Celestial","Feitiço de projeção"]) if chance <= 20 else random.choice(
                self.raridades["Comum"] + self.raridades["Raro"] + self.raridades["Épico"])

        elif cl == "Clã Kamo":
            return random.choice(
                ["Manipulação de Sangue", "Manipulação de Sangue(Podre)"]) if chance <= 40 else random.choice(
                self.raridades["Comum"] + self.raridades["Raro"] + self.raridades["Épico"])

        elif cl == "Clã Inumaki":
            return "Fala Amaldiçoada" if chance <= 50 else random.choice(
                self.raridades["Comum"] + self.raridades["Raro"] + self.raridades["Épico"])

        elif cl == "Sem Clã":
            return random.choice(self.raridades["Comum"] + self.raridades["Raro"] + self.raridades["Épico"])

        elif cl == "Maldição":
            return random.choice(
                ["Manipulação de Sangue", "Manipulação de Sangue(Podre)", "Chamas do Desastre","Plantas do desastre",
                 "Maré do desastre","Transfiguração Ociosa"]) if chance <= 50 else random.choice(
                self.raridades["Comum"] + self.raridades["Raro"] + self.raridades["Épico"])

    def roletaEnergiaAmaldicoada(self, tecnica):
        if tecnica == "Restrição Celestial":
            return "Sem Energia Amaldiçoada"

        roletaEA = [
            ("Energia Amaldiçoada Comum", 60),
            ("Grande Energia Amaldiçoada", 25),
            ("Imensa Energia Amaldiçoada", 15),
        ]

        roletaEAs = []
        for item, prob in roletaEA:
            roletaEAs.extend([item] * prob)

        return random.choice(roletaEAs)

    def roletaExtra(self, cl):
        if cl == "Clã Gojo":
            chance = random.randint(1, 100)
            return "Seis Olhos" if chance <= 1 else self.roletaExtrasComuns()
        else:
            return self.roletaExtrasComuns()

    def roletaExtrasComuns(self):
        roletaExtra = [
            ("Nada", 60),
            ("Fisico Divino", 10),
            ("Alto QI", 10),
            ("Mestre no Combate", 20)
        ]

        roletaExtras = []
        for item, prob in roletaExtra:
            roletaExtras.extend([item] * prob)

        return random.choice(roletaExtras)

    def roletaExtra2(self):
        chance = random.randint(1, 100)
        return "1 em 1 milhão" if chance <= 1 else "Nada"

    def exibirFicha(self, resultado):
        print(f"Raça: {resultado['Raça']}", end="")
        if resultado['Raça'] == "Humano" and resultado['Técnica'] != "Sem Técnica":
            print(f" | Clã: {resultado.get('Clã', '')}")
        elif resultado['Raça'] == "Infernal":
            print(f" | Infernal {resultado.get('Infernal', '')}")
        elif  resultado['Raça'] == "Híbrido":
            print(f" | Híbrido {resultado.get('Híbrido', '')}")
        else:
            print()
        if resultado['Raça'] == "Humano" or resultado['Raça'] == "Feto Amaldiçoado":
            print(f"Técnica: {resultado['Técnica']}")
        print(f"EA: {resultado['EA']}")
        print(f"Extra: {resultado['Extra']}")
        if "Extra2" in resultado and resultado["Extra2"] == "1 em 1 milhão":
            print(f"{resultado['Extra2']}")


roletagem = Roletagem()
resultado1 = roletagem.roletagem()
resultado2 = roletagem.roletagem()
resultado3 = roletagem.roletagem()

numero = int(input("\nDigite um número de três dígitos: "))
if 000 <= numero <= 999:
    roletagem.exibirFicha(resultado1)
numero = int(input("\nDigite um número de três dígitos: "))
if 000 <= numero <= 999:
    roletagem.exibirFicha(resultado2)
numero = int(input("\nDigite um número de três dígitos: "))
if 000 <= numero <= 999:
    roletagem.exibirFicha(resultado3)
