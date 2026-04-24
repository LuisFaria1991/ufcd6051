config = {
    "produtos": {
        "cafe_longo" : {
            "preço" : 0.5,
            "tem_palheta" : True,
            "tem_copo" : True,
            "nivel_acucar" : 2,
            "botao_cafe_longo" : "periferico_2"
        },
        "café_comprido" :{
            "preço" : 0.5,
        },
        "cha" :{
            "preço" : 0.2,
        },
        "cappucino" :{
            "preço" : 0.6,
        }
    }
}


config["produtos"]
config["produtos"]["cha"]
preco_do_cha = config["produtos"]["cha"]["preço"]

config["produtos"]["cafe_longo"][nivel_de_acucar] +=1

config_da_maquina = {
    "velocidade"
}

botao_cafe_lomgo = config["produtos"]["cafe_longo"]["botao_cafe_longo"]

# ciclo principal
while True:
    # dados de entrada
    velocidade_da_maquina = config_da_maquina["velocidade"]

    # processamento
    if botao_cafe_longo and dinheiro_certo:
        if config["produtos"]["cafe longo"]["tem copo"]:
            colocar_copo()
        else:
            nao_colocar_copo()

botao_tirar_acucar:
if config["produtos"]["cafe longo"][nivel_de_acucar] > 0:
    config["produtos"]["cafe longo"][nivel_de_acucar] -= 1


    def colocar_copo():
        """Codigo para pedir à maquina para tira copo"""
        print("Tirar copo")