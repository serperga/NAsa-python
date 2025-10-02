from src.indexing.build_index import build_index
from src.config.settings import DEFAULT_IMAGE_COUNT

def run_cli():
    print("🔭 Bienvenido al explorador de imágenes NASA APOD con ChatGPT")

    try:
        user_count = input(f"Ingrese el número de imágenes a indexar (default={DEFAULT_IMAGE_COUNT}): ").strip()
        image_count = int(user_count) if user_count else DEFAULT_IMAGE_COUNT
    except ValueError:
        print(f"⚠️ Valor inválido, se usará el valor por defecto: {DEFAULT_IMAGE_COUNT}")
        image_count = DEFAULT_IMAGE_COUNT

    print(f"\n📥 Descargando {image_count} imágenes de NASA APOD y creando índice...")
    index = build_index(image_count=image_count)

    # Query engine usa LLM de Settings automáticamente
    query_engine = index.as_query_engine()

    print("\n💬 Haz preguntas sobre las imágenes indexadas (escribe 'salir' para terminar).\n")
    while True:
        pregunta = input("Tu pregunta: ").strip()
        if pregunta.lower() in ("salir", "exit", "quit"):
            print("👋 ¡Hasta luego!")
            break
        if not pregunta:
            print("⚠️ Ingresa una pregunta válida.\n")
            continue

        respuesta = query_engine.query(pregunta)
        print("\nRespuesta:\n", respuesta, "\n")
