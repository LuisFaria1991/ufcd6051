# estrutura de dados

# lista de mesas:
mesas = {
    "mesa_retangular":{
        "tamanho":{
        "comprimento" : 1200,
        "largura" : 600,
        "altura" : 700,
        },
        "cor":{
        "cor_tampo" : "branco com vira pinho",
        "cor_pernas" : "preta",
        },
    },
    "mesa_quadrada":{
        "tamanho":{
            "tamanho":{
        "comprimento" : 800,
        "largura" : 600,
        "altura" : 700,
        },
        "cor":{
        "cor_tampo" : "branco_com_vira_pinho",
        "cor_pernas" : "preta",
        }
    }
}
}

cadeiras = {
    "tipo":{
        "com_encosto" : "sem_almofadado"
        },
    "tamanho":{
        "altura_solo/assento" : 400,
        "altura_solo/encosto" : 750,
    },
    "cor":{
        "assento/encosto" : "cinza plaster",
        "pernas" : "pretas",
    }
}

computadores = {
    "caracteristicas_torres":{
        "processador" : "intel_core_duo",
        "memoria_ram" : 4,
        "memoria_interna" : 320,
        "placa_grafica" : "intel_grafics_3000",
    },
    "caracteristicas_monitor":{
        "tamanho" : "16_polegadas",
        "resoluçao" : "HD",
    }
}

lista_de_objetos = [
    mesas["mesa_retangular"] * 8, 
    mesas["mesa_quadrada"] *12,
    cadeiras * 28,
    computadores * 28,
]