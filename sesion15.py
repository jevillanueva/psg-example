class NoAlfabeticoError(Exception):
    pass

palabras = []
while True:
    try:
        palabra = input("Ingrese una palabra: ")
        if palabra == "salir":
            break
        if not palabra.isalpha():
            raise NoAlfabeticoError("Solo se permiten letras")
        palabras.append(palabra)
    except NoAlfabeticoError as e:
        print("🚫 Error:", e)
    except Exception as e:
        print("💀 Error:", e)
    else:
        print("🎉 Palabra agregada")
    finally:
        print("Lista:", palabras)