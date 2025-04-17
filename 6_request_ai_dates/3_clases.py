# Son plantillas para cerar objetos.
# Un objeto es una instancia de la clase.
#  Permite crear objetos con atributos y métodos.

# Ejemplo basico de una clase
class Coche:
    # Atributo de clase (comparten todas las instancias)
    tipo = "vehículo de cuatro ruedas"
    # Constructor (método especial que se llama al crear un objeto)
    def __init__(self, marca, modelo, color):
        # Atributos de instancia (cada objeto tiene sus propios valores)
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def arrancar(self):
        print(f"El {self.marca} {self.modelo} de color {self.color} arrancó.")


mi_coche = Coche("Ford", "Mustang", "Rojo")
mi_coche.arrancar()

coche_juan = Coche("Toyota", "Corolla", "Azul")
coche_juan.arrancar()

# Encapsulamiento: ocultar atributos y métodos internos de la clase y exponer solo la interfaz pública.


# Crear una clase para llamar a la AI de OpenAI, DeepSeek o cualquier otra API.

import requests

OPENAI_KEY = ""
DEEPSEEK_KEY = ""

class AI_API:
    def __init__(self, api_key, url, model):
        self.api_key = api_key
        self.url = url
        self.model = model

    def call(self, prompt):
        header = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }
        data = {
            "model": self.model,
            "message": [
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        }
        response = requests.post(self.url, headers=header, json=data)
        res_json = response.json()
        print(res_json["choices"][0]["message"]["content"])
        
print("\nOPEN_AI: ")
open_ai = AI_API(OPENAI_KEY, "https://api.openai.com/v1/chat/completions", "gpt-3.5-turbo")

open_ai.call("¿Cuántos días tiene un año?")

print("\nDEEPSEEK: ")
deepseek_ai = AI_API(DEEPSEEK_KEY, "https://api.deepseek.ai/v1/chat/completions", "gpt-3.5-turbo")

deepseek_ai.call("¿Cuántos días tiene un año?")
