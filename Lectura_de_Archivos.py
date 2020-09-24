import re
from Clases import Ruta
from Clases import Estacion
Reporte_Tokens = []
Reporte_Tokens.append(["No.", "Lexema", "Fila", "Columna", "Token"])
pattern_ruta_apertura = r"<[^/]*[R|r][U|u][T|t][A|a](.)*>"
pattern_ruta_lexema = r"[R|r][U|u][T|t][A|a]"
pattern_ruta_cerradura = r"</(.)*[R|r][U|u][T|t][A|a](.)*>"
pattern_ruta_nombre_apertura = r"<[^/]*[N|n][O|o][M|m][B|b][R|r][E|e](.)*>"
pattern_ruta_nombre_lexema = r"[N|n][O|o][M|m][B|b][R|r][E|e]"
pattern_ruta_nombre_cerradura = r"</(.)*[N|n][O|o][M|m][B|b][R|r][E|e](.)*>"
pattern_ruta_peso_apertura = r"<[^/]*[P|p][E|e][S|s][O|o](.)*>"
pattern_ruta_peso_lexema = r"[P|p][E|e][S|s][O|o]"
pattern_ruta_peso_cerradura = r"</(.)*[P|p][E|e][S|s][O|o](.)*>"
pattern_ruta_inicio_apertura = r"<[^/]*[I|i][N|n][I|i][C|c][I|i][O|o](.)*>"
pattern_ruta_inicio_lexema = r"[I|i][N|n][I|i][C|c][I|i][O|o]"
pattern_ruta_inicio_cerradura = r"</(.)*[I|i][N|n][I|i][C|c][I|i][O|o](.)*>"
pattern_ruta_fin_apertura = r"<[^/]*[F|f][I|i][N|n](.)*>"
pattern_ruta_fin_lexema = r"[F|f][I|i][N|n]"
pattern_ruta_fin_cerradura = r"</(.)*[F|f][I|i][N|n](.)*>"
pattern_estacion_apertura = r"<[^/]*[E|e][S|s][T|t][A|a][C|c][I|i][O|o][N|n](.)*>"
pattern_estacion_lexema = r"[E|e][S|s][T|t][A|a][C|c][I|i][O|o][N|n]"
pattern_estacion_cerradura = r"</(.)*[E|e][S|s][T|t][A|a][C|c][I|i][O|o][N|n](.)*>"
pattern_estacion_nombre_apertura = r"<[^/]*[N|n][O|o][M|m][B|b][R|r][E|e](.)*>"
pattern_estacion_nombre_lexema = r"[N|n][O|o][M|m][B|b][R|r][E|e]"
pattern_estacion_nombre_cerradura = r"</(.)*[N|n][O|o][M|m][B|b][R|r][E|e](.)*>"
pattern_estacion_estado_apertura = r"<[^/]*[E|e][S|s][T|t][A|a][D|d][O|o](.)*>"
pattern_estacion_estado_lexema = r"[E|e][S|s][T|t][A|a][D|d][O|o]"
pattern_estacion_estado_cerradura = r"</(.)*[E|e][S|s][T|t][A|a][D|d][O|o](.)*>"
pattern_estacion_color_apertura = r"<[^/]*[C|c][O|o][L|l][O|o][R|r](.)*>"
pattern_estacion_color_lexema = r"[C|c][O|o][L|l][O|o][R|r]"
pattern_estacion_color_cerradura = r"</(.)*[C|c][O|o][L|l][O|o][R|r](.)*>"
pattern_nombre_apertura = r"<[^/]*[N|n][O|o][M|m][B|b][R|r][E|e](.)*>"
pattern_nombre_lexema = r"[N|n][O|o][M|m][B|b][R|r][E|e]"
pattern_nombre_cerradura = r"</(.)*[N|n][O|o][M|m][B|b][R|r][E|e](.)*>"
def Lectura(ruta):
    file = open(ruta, "r")
    Estado_Padre = "ninguno"
    Estado_Hijo = "ninguno"
    cadena = ""
    filas = 0
    columnas = 0
    Numero_Tokens = 0
    NombreRuta = ""
    PesoRuta = 0
    InicioRuta = ""
    FinRuta = ""
    Lexema = ""
    EstacionNombre = ""
    EstacionEstado = ""
    EstacionColor = ""
    for line in file:
        filas += 1
        columnas = 0
        for char in line:
            columnas += 1
            if re.search(pattern_ruta_apertura, cadena) and Estado_Padre == "ninguno":
                Estado_Padre = "ruta"
                Numero_Tokens += 1
                Reporte_Tokens.append([Numero_Tokens, cadena[re.search(pattern_ruta_lexema, cadena).start(): re.search(pattern_ruta_lexema, cadena).end()], filas, (columnas-len(cadena)), Estado_Padre])
                cadena = ""
            elif Estado_Padre == "ruta":
                if re.search(pattern_ruta_nombre_apertura, cadena) and Estado_Hijo == "ninguno":
                    Estado_Hijo = "nombre"
                    Numero_Tokens += 1
                    Reporte_Tokens.append([Numero_Tokens, cadena[re.search(pattern_ruta_nombre_lexema, cadena).start(): re.search(pattern_ruta_nombre_lexema, cadena).end()],filas, (columnas - len(cadena)), Estado_Hijo])
                    cadena = ""
                elif Estado_Hijo == "nombre":
                    if char == "<":
                        NombreRuta = cadena
                        cadena = ""
                    elif re.search(pattern_ruta_nombre_cerradura, cadena):
                        Estado_Hijo = "ninguno"
                        cadena = ""
                elif re.search(pattern_ruta_peso_apertura, cadena) and Estado_Hijo == "ninguno":
                    Estado_Hijo = "peso"
                    Numero_Tokens += 1
                    Reporte_Tokens.append([Numero_Tokens, cadena[
                        re.search(pattern_ruta_peso_lexema, cadena).start(): re.search(pattern_ruta_peso_lexema, cadena).end()],
                                                     filas, (columnas - len(cadena)), Estado_Hijo])
                    cadena = ""
                elif Estado_Hijo == "peso":
                    if char == "<":
                        PesoRuta = float(cadena)
                        cadena = ""
                    elif re.search(pattern_ruta_peso_cerradura, cadena):
                        Estado_Hijo = "ninguno"
                        cadena = ""
                elif re.search(pattern_ruta_inicio_apertura, cadena) and Estado_Hijo == "ninguno":
                    Estado_Hijo = "inicio"
                    Numero_Tokens += 1
                    Reporte_Tokens.append([Numero_Tokens, cadena[
                        re.search(pattern_ruta_inicio_lexema, cadena).start(): re.search(pattern_ruta_inicio_lexema, cadena).end()],
                                                     filas, (columnas - len(cadena)), Estado_Hijo])
                    cadena = ""
                elif Estado_Hijo == "inicio":
                    if char == "<":
                        InicioRuta = cadena
                        cadena = ""
                    elif re.search(pattern_ruta_inicio_cerradura, cadena):
                        Estado_Hijo = "ninguno"
                        cadena = ""
                elif re.search(pattern_ruta_fin_apertura, cadena) and Estado_Hijo == "ninguno":
                    Estado_Hijo = "fin"
                    Numero_Tokens += 1
                    Reporte_Tokens.append([Numero_Tokens, cadena[
                        re.search(pattern_ruta_fin_lexema, cadena).start(): re.search(pattern_ruta_fin_lexema, cadena).end()],
                                                     filas, (columnas - len(cadena)), Estado_Hijo])
                    cadena = ""
                elif Estado_Hijo == "fin":
                    if char == "<":
                        FinRuta = cadena
                        cadena = ""
                    elif re.search(pattern_ruta_fin_cerradura, cadena):
                        Estado_Hijo = "ninguno"
                        cadena = ""
                elif re.search(pattern_ruta_cerradura, cadena):
                    RutaAux = Ruta(NombreRuta, PesoRuta, InicioRuta, FinRuta)
                    Estado_Padre = "ninguno"
                    cadena = ""
                    NombreRuta = ""
                    PesoRuta = ""
                    InicioRuta = ""
                    FinRuta = ""
            elif re.search(pattern_estacion_apertura, cadena) and Estado_Padre == "ninguno":
                Estado_Padre = "estacion"
                Numero_Tokens += 1
                Reporte_Tokens.append([Numero_Tokens, cadena[
                    re.search(pattern_estacion_lexema, cadena).start(): re.search(pattern_estacion_lexema, cadena).end()],
                                                 filas, (columnas - len(cadena)), Estado_Padre])
                cadena = ""
            elif Estado_Padre == "estacion":
                if re.search(pattern_estacion_nombre_apertura, cadena) and Estado_Hijo == "ninguno":
                    Estado_Hijo = "nombre"
                    Numero_Tokens += 1
                    Reporte_Tokens.append([Numero_Tokens, cadena[
                        re.search(pattern_estacion_nombre_lexema, cadena).start(): re.search(pattern_estacion_nombre_lexema, cadena).end()],
                                                     filas, (columnas - len(cadena)), Estado_Hijo])
                    cadena = ""
                elif Estado_Hijo == "nombre":
                    if char == "<":
                        cadena = ""
                    elif re.search(pattern_estacion_nombre_cerradura, cadena):
                        Estado_Hijo = "ninguno"
                        cadena = ""
                elif re.search(pattern_estacion_estado_apertura, cadena) and Estado_Hijo == "ninguno":
                    Estado_Hijo = "estado"
                    Numero_Tokens += 1
                    Reporte_Tokens.append([Numero_Tokens, cadena[
                        re.search(pattern_estacion_estado_lexema, cadena).start(): re.search(pattern_estacion_estado_lexema, cadena).end()],
                                                     filas, (columnas - len(cadena)), Estado_Hijo])
                    cadena = ""
                elif Estado_Hijo == "estado":
                    if char == "<":
                        cadena = ""
                    elif re.search(pattern_estacion_estado_cerradura, cadena):
                        Estado_Hijo = "ninguno"
                        cadena = ""
                elif re.search(pattern_estacion_color_apertura, cadena) and Estado_Hijo == "ninguno":
                    Estado_Hijo = "color"
                    Numero_Tokens += 1
                    Reporte_Tokens.append([Numero_Tokens, cadena[
                        re.search(pattern_estacion_color_lexema, cadena).start(): re.search(pattern_estacion_color_lexema, cadena).end()],
                                                     filas, (columnas - len(cadena)), Estado_Hijo])
                    cadena = ""
                elif Estado_Hijo == "color":
                    if char == "<":
                        cadena = ""
                    elif re.search(pattern_estacion_color_cerradura, cadena):
                        Estado_Hijo = "ninguno"
                        cadena = ""
                elif re.search(pattern_estacion_cerradura, cadena):
                    Estado_Padre = "ninguno"
                    cadena = ""
            elif re.search(pattern_nombre_apertura, cadena) and Estado_Padre == "ninguno":
                Estado_Padre = "nombre"
                Numero_Tokens += 1
                Reporte_Tokens.append([Numero_Tokens, cadena[
                    re.search(pattern_nombre_lexema, cadena).start(): re.search(pattern_nombre_lexema, cadena).end()],
                                                 filas, (columnas - len(cadena)), Estado_Padre])
                cadena = ""
            elif Estado_Padre == "nombre":
                if char == "<":
                    cadena = ""
                elif re.search(pattern_nombre_cerradura, cadena):
                    Estado_Padre = "ninguno"
                    cadena = ""
            if char == "\n" or char == " ":
                pass
            else:
                cadena += char
    print("-----------------------------------------------------\n")
    for celda in Reporte_Tokens:
        print(celda)
    print("\n-----------------------------------------------------")