import random

def obtener_pregunta():
    """Retorna una pregunta aleatoria de cultura general"""
    preguntas = [
        {
            "pregunta": "¿Cuál es la capital de Francia?",
            "respuesta": "paris"
        },
        {
            "pregunta": "¿En qué año comenzó la Segunda Guerra Mundial?",
            "respuesta": "1939"
        },
        {
            "pregunta": "¿Cuál es el río más largo del mundo?",
            "respuesta": "amazonas"
        },
        {
            "pregunta": "¿Quién pintó la Mona Lisa?",
            "respuesta": "leonardo da vinci"
        },
        {
            "pregunta": "¿Cuál es el planeta más grande del sistema solar?",
            "respuesta": "jupiter"
        },
        {
            "pregunta": "¿En qué continente se encuentra Egipto?",
            "respuesta": "africa"
        },
        {
            "pregunta": "¿Cuál es el metal más abundante en la corteza terrestre?",
            "respuesta": "aluminio"
        },
        {
            "pregunta": "¿Quién escribió 'Don Quijote de la Mancha'?",
            "respuesta": "miguel de cervantes"
        },
        {
            "pregunta": "¿Cuál es el océano más grande del mundo?",
            "respuesta": "pacifico"
        },
        {
            "pregunta": "¿En qué año llegó el hombre a la Luna?",
            "respuesta": "1969"
        }
    ]
    return random.choice(preguntas)

def jugar():
    print("¡Bienvenido al juego de preguntas y respuestas!")
    print("Por cada respuesta correcta ganarás premios en pesos argentinos.")
    print("¡Buena suerte!\n")
    
    premio_total = 0
    preguntas_usadas = []
    
    for i in range(5):
        print(f"\nPregunta {i + 1}:")
        pregunta_data = obtener_pregunta()
        while pregunta_data in preguntas_usadas:
            pregunta_data = obtener_pregunta()
        
        preguntas_usadas.append(pregunta_data)
        print(pregunta_data["pregunta"])
        respuesta_usuario = input("Tu respuesta: ").strip().lower()
        
        if respuesta_usuario == pregunta_data["respuesta"]:
            premio = 1000 * (i + 1)  # El premio aumenta con cada pregunta
            premio_total += premio
            print(f"¡Correcto! Has ganado {premio} pesos argentinos")
        else:
            print(f"Incorrecto. La respuesta correcta era: {pregunta_data['respuesta']}")
    
    print(f"\n¡Juego terminado! Has ganado un total de {premio_total} pesos argentinos")

if __name__ == "__main__":
    jugar()
