import requests

# URL de la API de DuckDuckGo
url = "https://api.duckduckgo.com/"

# Parámetros de la consulta
params = {
    "q": "Toledo",
    "format": "json"
}

# Realizar la llamada GET
response = requests.get(url, params=params)

# Validar que el estado de la respuesta sea 200
assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

# Parsear la respuesta JSON
data = response.json()

# Validar que el parámetro AbstractSource contenga Wikipedia
assert data["AbstractSource"] == "Wikipedia", f"Expected AbstractSource to be 'Wikipedia' but got {data['AbstractSource']}"

# Crear una estructura de datos para almacenar los registros de RelatedTopics
related_topics = []

# Extraer los datos de RelatedTopics
for topic in data["RelatedTopics"]:
    if "FirstURL" in topic and "Text" in topic:
        related_topics.append({
            "FirstURL": topic["FirstURL"],
            "Text": topic["Text"]
        })

# Imprimir FirstURL y Text de cada registro
for topic in related_topics:
    print(f"FirstURL: {topic['FirstURL']}, Text: {topic['Text']}")
