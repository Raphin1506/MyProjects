import random

def roletagem():
    roletasRaças = [
        (f"Humano", 70),
        (f"Kuja", 10),
        (f"Mink", 30),
        (f"Skypiean/Shandian", 30),
        (f"Oni", 5),
        (f"Lunariano", 1),
        (f"Tontatta", 30),
        (f"Homem-peixe", 20),
        (f"Sereiano", 30),
        (f"Gigante", 10)
    ]

    roletaRaça = []
    for item, prob in roletasRaças:
        roletaRaça.extend([item] * prob)
#METODO DE CONDIÇÃO "Poder":
######################################        

    def Akuma_no_mi():
        roletasPoder = [
            ("Com fruta", 50),
            ("Sem fruta", 50)
        ]

        roletaPoder = []
        for item, prob in roletasPoder:
            roletaPoder.extend([item] * prob)
        resultadoPoder = random.choice(roletaPoder)

        if resultadoPoder == "Com fruta":
            roleta_Tipo_AkumaNoMi = [
                ("Logia", 25),
                ("Zoan", 25),
                ("Paramecia", 40),
                ("Zoan Mitica", 5),
                ("Zoan Ancestral", 10)
            ]
            roleta_Tipo = []
            for item, prob in roleta_Tipo_AkumaNoMi:
                roleta_Tipo.extend([item] * prob)

            tipo_akuma = random.choice(roleta_Tipo)
            if tipo_akuma == "Logia":
                roleta_Logia = ["Moku Moku no mi", "Suna Suna no mi", "Mera Mera no mi", "Goro Goro no mi", 
                "Hie Hie no mi", "Yami Yami no mi", "Pika Pika no mi", "Magu Magu no mi", "Susu Susu no mi", 
                "Numa Numa no mi", "Gasu Gasu no mi", "Yuki Yuki no mi", "Mori Mori no mi"]
                return random.choice(roleta_Logia)
            elif tipo_akuma == "Zoan":
                roleta_Zoan = ["Ushi Ushi No mi - Bison", "Ushi Ushi No mi - Giraffe", "Hito Hito No mi",  
                "Tori Tori No mi - Falcon","Inu Inu No mi - Dachshund", "Inu Inu No mi - Jackal", "Inu Inu No mi - Wolf", 
                "Inu Inu No mi - Tanuki", "Neko Neko No mi - Leopard", "Zou Zou No mi - elephant", "Hebi Hebi No mi - King Cobra", 
                "Hebi Hebi No mi - Anaconda",  "Mushi Mushi No mi - Beetle", "Mushi Mushi No mi - Suzumebachi","mole", "Uma Uma no mi",
                "Kame Kame no mi", "tama tama no mi - egg", "koala", "Ushi ushi no mi - rhino", "Uma Uma no mi - zebra", "Kumo Kumo no mi - Aranha-marrom", 
                "Inu Inu no mi - dalmatian", "Sara Sara no mi - Lagarta", "Inu Inu no mi - chihuahua"]
                return random.choice(roleta_Zoan)
            elif tipo_akuma == "Paramecia":
                roleta_Paramecia = ["Bara Bara no mi", "Sube Sube no mi", "Bomu Bomu no mi", "Kilo Kilo no mi", 
                "Hana Hana no mi", "Doru Doru no mi", "Baku Baku no mi", "Toge Toge no mi", "Mane Mane no mi", 
                "Supa Supa no mi", "Ori Ori no mi", "Bane Bane no mi", "Ito Ito no mi", "Doa Doa no mi", 
                "Noro Noro no mi", "Awa Awa no mi", "Beri Beri no mi", "Sabi Sabi no mi", "Shari Shari no mi", 
                "Horo Horo no mi", "Yomi Yomi no mi", "Kage Kage no mi", "Suke Suke no mi", "Nikyu Nikyu no mi", 
                "Jiki Jiki no mi", "Ope Ope no mi", "Shiro Shiro no mi", "Wara Wara no mi", "Oto Oto no mi", 
                "Mero Mero no mi", "Doku Doku no mi", "Horu Horu no mi", "Choki Choki no mi", "Gura Gura no mi", 
                "Kira Kira no mi", "Meco Meco no mi", "Woshu Woshu no mi", "Fuwa Fuwa no mi", "Mato Mato no mi", 
                "Fuku Fuku no mi", "Hobi Hobi no mi", "Buki Buki no mi", "Guru Guru no mi", "Beta Beta no mi", 
                "Zushi Zushi no mi", "Bari Bari no mi", "Nui Nui no mi", "Giro Giro no mi", "Ato Ato no mi", 
                "Jake Jake no mi", "Pamu Pamu no mi", "Sui Sui no mi", "Ton Ton no mi", "Hira Hira no mi", 
                "Ishi Ishi no mi", "Fude Fude no mi", "Nagi Nagi no mi", "Chiyu Chiyu no mi", "Soru Soru no mi", 
                "Mira Mira no mi", "Pero Pero no mi", "Bisu Bisu no mi", "Bata Bata no mi", "Buku Buku no mi", 
                "Kuri Kuri no mi", "Shibo Shibo no mi", "Memo Memo no mi", "Mochi Mochi no mi", "Hoya Hoya no mi", 
                "Netsu Netsu no mi", "Kuku Kuku no mi", "Yuuguu Yuuguu no mi", "Pusshu Pusshu no mi", 
                "Kobu Kobu no mi", "Kibi Kibi no mi", "Toki Toki no mi", "Juku Juku no mi", "Maki Maki no mi", 
                "Riki Riki no mi","Wapu Wapu no mi","Shiku Shiku no mi","Nomi Nomi no mi",
                "Deka Deka no mi","Uta Uta no mi"]
                return random.choice(roleta_Paramecia)
            elif tipo_akuma == "Zoan Mitica":
                roleta_ZoanMitica = [ "Hito Hito No mi - Buddha", "Hito Hito No mi - Onyudo", "Hito Hito No mi - Nika",
                "Tori Tori No mi - Phoenix", "Uo Uo No mi - Seiryu","Inu Inu No mi- Kitsune", "Inu Inu No mi - Okuchi no Makami", 
                "Uma Uma no mi - pegasus", "Hebi Hebi No mi - Orochi"]
                return random.choice(roleta_ZoanMitica)
            elif tipo_akuma == "Zoan Ancestral":
                roleta_ZoanAncestral = ["Tori Tori No mi - Albatross", "Neko Neko No mi - Saber Tooth", "Zou Zou No mi - Mammoth", 
                "Ryu Ryu No mi - Allosaurus", "Ryu Ryu No mi - Spinosaurus", "Ryu Ryu No mi - Pteranodon", "Ryu Ryu No mi - Brachiosaurus", 
                "Ryu Ryu No mi - Pachycephalosaurus", "Ryu Ryu No mi - Triceratops","Kumo Kumo No mi - Rosamygale Grauvogeli",
                "Sara Sara No mi - Axolotl"]
                return random.choice(roleta_ZoanAncestral)
        
        return "Sem fruta"

######################################
#METODO DE CONDIÇÃO "Extra":
######################################   
    def roleta_extra():
        if resultadoRaça == "Humano":
            roleta_extra_Humano = [
                (f"Nenhum", 60),
                (f"Clã do D.", 5),
                (f"Clã Shimotsuki", 20),
                (f"Tenryubito", 1),
                (f"Haki do Rei", 1),
                (f"Tribo do Terceiro Olho", 20),
                (f"Fator linhagem germa", 10)
            ]
            roleta_Humano = []
            for item, prob in roleta_extra_Humano:
                roleta_Humano.extend([item] * prob)
            return random.choice(roleta_Humano)
        elif resultadoRaça == "Gigante":
            roleta_extra_Gigante = [
                (f"Nenhum", 70),
                (f"Clã do D.", 1),
                (f"Gigante Ancestral", 10),
                (f"Haki do Rei", 1),
            ]
            roleta_Gigante = []
            for item, prob in roleta_extra_Gigante:
                roleta_Gigante.extend([item] * prob)
            return random.choice(roleta_Gigante)
        elif resultadoRaça == "Gigante":
            roleta_extra_Skypiean= [
                (f"Nenhum", 70),
                (f"Clã do D.", 1),
                (f"Birkan", 10),
                (f"Haki do Rei", 1),
                (f"Mantra desperto", 5)
            ]
            roleta_Skypiean = []
            for item, prob in roleta_extra_Skypiean:
                roleta_Skypiean.extend([item] * prob)
            return random.choice(roleta_Skypiean)
        else:
            roleta_extra = [
                (f"Nenhum", 70),
                (f"Clã do D.", 1),
                (f"Haki do Rei", 1)
            ]
            roleta_Extra = []
            for item, prob in roleta_extra:
                roleta_Extra.extend([item] * prob)
            return random.choice(roleta_Extra)
###########################################

    resultadoRaça = random.choice(roletaRaça)
    resultadoPoder = Akuma_no_mi()
    resultadoExtra = roleta_extra()
    return resultadoRaça, resultadoPoder, resultadoExtra


numero = int(input("\nDigite um número de três dígitos: "))
if 000 <= numero <= 999:
    resultado_1 = roletagem()
    print(f"\nResultado da roletagem 1:")
    print(f"\nRaça: {resultado_1[0]}", "|", f"Poder: {resultado_1[1]}", "|", f"Extra: {resultado_1[2]}")
    print()
else:
    print("O número digitado não tem três dígitos.")
numero_2 = int(input("\nDigite um número de três dígitos: "))
if  000 <= numero_2 <= 999:
    resultado_2 = roletagem()
    print(f"\nResultado da roletagem 2:")
    print(f"\nRaça: {resultado_2[0]}", "|", f"Poder: {resultado_2[1]}", "|", f"Extra: {resultado_2[2]}")
    print()
else:
    print("O número digitado não tem três dígitos.")
numero_3 = int(input("\nDigite um número de três dígitos: "))
if 000 <= numero_3 <= 999:
    resultado_3 = roletagem()
    print(f"\nResultado da roletagem 3:")
    print(f"\nRaça: {resultado_3[0]}", "|", f"Poder: {resultado_3[1]}", "|", f"Extra: {resultado_3[2]}")
    print()
else:
    print("O número digitado não tem três dígitos.")
