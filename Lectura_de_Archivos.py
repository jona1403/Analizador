import re
from Clases import Ruta
from Clases import Estacion
from GraficarReportes import Graficar_Reporte_Tokens_Y_Reporte_Errores
Reporte_Tokens = []
Reporte_Errores = []
Lista_Rutas = []
Lista_Estaciones = []
Reporte_Tokens.append(["No.", "Lexema", "Fila", "Columna", "Token"])
Reporte_Errores.append(["No.", "Fila", "Columna", "Caracter", "Descripción"])
pattern_ruta_apertura = r"<[^/]*[R|r][U|u][T|t][A|a](.)*>"
pattern_ruta_apertura_correcto = r"<[R|r][U|u][T|t][A|a]>"
pattern_ruta_lexema = r"[R|r][U|u][T|t][A|a]"
pattern_ruta_cerradura = r"</(.)*[R|r][U|u][T|t][A|a](.)*>"
pattern_ruta_cerradura_correcto = r"</[R|r][U|u][T|t][A|a]>"
pattern_ruta_nombre_apertura = r"<[^/]*[N|n][O|o][M|m][B|b][R|r][E|e](.)*>"
pattern_ruta_nombre_lexema = r"[N|n][O|o][M|m][B|b][R|r][E|e]"
pattern_ruta_nombre_contenido = r"[A-Za-z]+[_|A-Za-z0-9|@|#]*"
pattern_ruta_nombre_cerradura = r"</(.)*[N|n][O|o][M|m][B|b][R|r][E|e](.)*>"
pattern_ruta_peso_apertura = r"<[^/]*[P|p][E|e][S|s][O|o](.)*>"
pattern_ruta_peso_lexema = r"[P|p][E|e][S|s][O|o]"
pattern_ruta_peso_contenido = r"[0-9]+[.]?[0-9]*"
pattern_ruta_peso_cerradura = r"</(.)*[P|p][E|e][S|s][O|o](.)*>"
pattern_ruta_inicio_apertura = r"<[^/]*[I|i][N|n][I|i][C|c][I|i][O|o](.)*>"
pattern_ruta_inicio_lexema = r"[I|i][N|n][I|i][C|c][I|i][O|o]"
pattern_ruta_inicio_contenido = r"[A-Za-z]+[_|A-Za-z0-9|@|#]*"
pattern_ruta_inicio_cerradura = r"</(.)*[I|i][N|n][I|i][C|c][I|i][O|o](.)*>"
pattern_ruta_fin_apertura = r"<[^/]*[F|f][I|i][N|n](.)*>"
pattern_ruta_fin_lexema = r"[F|f][I|i][N|n]"
pattern_ruta_fin_contenido = r"[A-Za-z]+[_|A-Za-z0-9|@|#]*"
pattern_ruta_fin_cerradura = r"</(.)*[F|f][I|i][N|n](.)*>"
pattern_estacion_apertura = r"<[^/]*[E|e][S|s][T|t][A|a][C|c][I|i][O|o][N|n](.)*>"
pattern_estacion_lexema = r"[E|e][S|s][T|t][A|a][C|c][I|i][O|o][N|n]"
pattern_estacion_cerradura = r"</(.)*[E|e][S|s][T|t][A|a][C|c][I|i][O|o][N|n](.)*>"
pattern_estacion_nombre_apertura = r"<[^/]*[N|n][O|o][M|m][B|b][R|r][E|e](.)*>"
pattern_estacion_nombre_lexema = r"[N|n][O|o][M|m][B|b][R|r][E|e]"
pattern_estacion_nombre_contenido = r"[A-Za-z]+[_|A-Za-z0-9|@|#]*"
pattern_estacion_nombre_cerradura = r"</(.)*[N|n][O|o][M|m][B|b][R|r][E|e](.)*>"
pattern_estacion_estado_apertura = r"<[^/]*[E|e][S|s][T|t][A|a][D|d][O|o](.)*>"
pattern_estacion_estado_lexema = r"[E|e][S|s][T|t][A|a][D|d][O|o]"
pattern_estacion_estadodis_contenido = r"[D|d][I|i][S|s][P|p][O|o][N|n][I|i][B|b][L|l][E|e]"
pattern_estacion_estado_cerrado_contenido = r"[C|c][E|e][R|r][R|r][A|a][D|d][A|a|O|o]"
pattern_estacion_estado_cerradura = r"</(.)*[E|e][S|s][T|t][A|a][D|d][O|o](.)*>"
pattern_estacion_color_apertura = r"<[^/]*[C|c][O|o][L|l][O|o][R|r](.)*>"
pattern_estacion_color_lexema = r"[C|c][O|o][L|l][O|o][R|r]"
pattern_estacion_color_contenido = r"#[A-Z0-9]{6,6}"
pattern_estacion_color_cerradura = r"</(.)*[C|c][O|o][L|l][O|o][R|r](.)*>"
pattern_nombre_apertura = r"<[^/]*[N|n][O|o][M|m][B|b][R|r][E|e](.)*>"
pattern_nombre_lexema = r"[N|n][O|o][M|m][B|b][R|r][E|e]"
pattern_nombre_contenido = r"[A-Za-z]+[_|A-Za-z0-9|@|#|\s]*"
pattern_nombre_cerradura = r"</(.)*[N|n][O|o][M|m][B|b][R|r][E|e](.)*>"
identificador_esperado = r"(a-zA-Z)(\w)*"
def Lectura(ruta):
    file = open(ruta, "r")
    Estado_Padre = "ninguno"
    Estado_Hijo = "ninguno"
    Estado_Caracter = "ninguno"
    cadena = ""
    filas = 0
    columnas = 0
    Contador_Signos_de_Apertura = 0
    Numero_Tokens = 0
    Numero_Erores = 0
    NombreRuta = ""
    PesoRuta = 0
    InicioRuta = ""
    FinRuta = ""
    Lexema = ""
    EstacionNombre = ""
    EstacionEstado = ""
    EstacionColor = ""
    NombreMapa = ""
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
                    if re.match(pattern_ruta_nombre_contenido, NombreRuta) and re.match(pattern_ruta_peso_contenido, str(PesoRuta)) and re.match(pattern_ruta_inicio_contenido, InicioRuta) and re.match(pattern_ruta_fin_contenido, FinRuta):
                        RutaAux = Ruta(NombreRuta.lower(), PesoRuta, InicioRuta.lower(), FinRuta.lower())
                        Lista_Rutas.append(RutaAux)
                        Estado_Padre = "ninguno"
                        cadena = ""
                        NombreRuta = ""
                        PesoRuta = ""
                        InicioRuta = ""
                        FinRuta = ""
                    else:
                        print("Los Datos dentro de la ruta no poseen el formato adecuado")
                        break
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
                        EstacionNombre = cadena
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
                        EstacionEstado = cadena
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
                        EstacionColor = cadena
                        cadena = ""
                    elif re.search(pattern_estacion_color_cerradura, cadena):
                        Estado_Hijo = "ninguno"
                        cadena = ""
                elif re.search(pattern_estacion_cerradura, cadena):
                    if re.match(pattern_estacion_nombre_contenido, EstacionNombre) and re.match(pattern_estacion_color_contenido, EstacionColor):
                        if re.match(pattern_estacion_estadodis_contenido, EstacionEstado):
                            Estado_Padre = "ninguno"
                            EstacionAux = Estacion(EstacionNombre.lower(), EstacionEstado.lower(), EstacionColor)
                            Lista_Estaciones.append(EstacionAux)
                            cadena = ""
                            EstacionNombre = ""
                            EstacionEstado = ""
                            EstacionColor = ""
                        elif re.match(pattern_estacion_estado_cerrado_contenido, EstacionEstado):
                            Estado_Padre = "ninguno"
                            EstacionAux = Estacion(EstacionNombre.lower(), EstacionEstado.lower(), EstacionColor)
                            Lista_Estaciones.append(EstacionAux)
                            cadena = ""
                            EstacionNombre = ""
                            EstacionEstado = ""
                            EstacionColor = ""
                        else:
                            print("Los Datos dentro de la estacion no poseen el formato adecuado")
                            break
                    else:
                        print("Los Datos dentro de la estacion no poseen el formato adecuado")
                        break

            elif re.search(pattern_nombre_apertura, cadena) and Estado_Padre == "ninguno":
                Estado_Padre = "nombre"
                Numero_Tokens += 1
                Reporte_Tokens.append([Numero_Tokens, cadena[
                    re.search(pattern_nombre_lexema, cadena).start(): re.search(pattern_nombre_lexema, cadena).end()],
                                                 filas, (columnas - len(cadena)), Estado_Padre])
                cadena = ""
            elif Estado_Padre == "nombre":
                if char == "<":
                    NombreMapa = cadena
                    if re.match(pattern_nombre_contenido, NombreMapa):
                        pass
                    else:
                        print("El contenido dentro del nombre del mapa no cumplen con el formato adecuado")
                        break
                    cadena = ""
                elif re.search(pattern_nombre_cerradura, cadena):
                    Estado_Padre = "ninguno"
                    cadena = ""

            if char == "\n" or char == " ":
                pass
            elif Estado_Caracter == "ninguno":
                if char == "<":
                    Estado_Caracter = "apertura"
                    cadena += char
                elif Estado_Padre == "nombre" or Estado_Hijo == "nombre" or Estado_Hijo == "peso" or Estado_Hijo == "inicio" or Estado_Hijo == "fin" or Estado_Hijo == "estado" or Estado_Hijo == "color":
                    cadena += char
                else:
                    Numero_Erores += 1
                    Reporte_Errores.append([Numero_Erores, filas, columnas, char, "Desconocido"])
            elif Estado_Caracter == "apertura":
                if Estado_Padre == "ninguno":
                    if char == "r" or char == "R":
                        Estado_Caracter = "r_ruta"
                        cadena += char
                    elif char == "e" or char == "E":
                        Estado_Caracter = "e_estacion"
                        cadena += char
                    elif char == "n" or char == "N":
                        Estado_Caracter = "n_nombre"
                        cadena += char
                    else:
                        Numero_Erores += 1
                        Reporte_Errores.append([Numero_Erores, filas, columnas, char, "Desconocido"])
                elif Estado_Padre != "ninguno":
                    if char == "/" and Estado_Hijo == "ninguno":
                        Estado_Caracter = "diagonal_cierre"
                        cadena += char
                    elif Estado_Hijo == "ninguno":
                        if char == "n" or char == "N":
                            Estado_Caracter = "n_nombre"
                            cadena+=char
                        elif char == "p" or char == "P":
                            Estado_Caracter = "p_peso"
                            cadena+=char
                        elif char == "i" or char == "I":
                            Estado_Caracter = "i_inicio"
                            cadena+=char
                        elif char == "f" or char == "F":
                            Estado_Caracter = "f_fin"
                            cadena+=char
                        elif char == "e" or char == "E":
                            Estado_Caracter = "e_estado"
                            cadena += char
                        elif char == "c" or char == "C":
                            Estado_Caracter = "c_color"
                            cadena += char
                        else:
                            Numero_Erores += 1
                            Reporte_Errores.append([Numero_Erores, filas, columnas, char, "Descripción"])
                    elif Estado_Hijo != "ninguno":
                        if char == "/":
                            Estado_Caracter = "diagonal_cierre"
                            cadena += char
                    else:
                        Numero_Erores += 1
                        Reporte_Errores.append([Numero_Erores, filas, columnas, char, "Descripción"])
            elif Estado_Caracter == "diagonal_cierre":
                if char == "r" or char == "R":
                    Estado_Caracter = "r_ruta"
                    cadena += char
                elif char == "e" or char == "E":
                    if Estado_Hijo == "estado":
                        Estado_Caracter = "e_estado"
                        cadena += char
                    else:
                        Estado_Caracter = "e_estacion"
                        cadena += char
                elif char == "n" or char == "N":
                    Estado_Caracter = "n_nombre"
                    cadena += char
                elif char == "p" or char == "P":
                    Estado_Caracter = "p_peso"
                    cadena+=char
                elif char == "i" or char == "I":
                    Estado_Caracter = "i_inicio"
                    cadena += char
                elif char == "f" or char == "F":
                    Estado_Caracter = "f_fin"
                    cadena += char
                elif char == "c" or char == "C":
                    Estado_Caracter = "c_color"
                    cadena+=char
                else:
                    Numero_Erores += 1
                    Reporte_Errores.append([Numero_Erores, filas, columnas, char, "Descripción"])
            elif Estado_Caracter == "r_ruta":
                if char == "u" or char == "U":
                    Estado_Caracter = "u_ruta"
                    cadena += char
                else:
                    Numero_Erores += 1
                    Reporte_Errores.append([Numero_Erores, filas, columnas, char, "Descripción"])
            elif Estado_Caracter == "e_estacion":
                if char == "s" or char == "S":
                    Estado_Caracter = "s_estacion"
                    cadena += char
                else:
                    Numero_Erores += 1
                    Reporte_Errores.append([Numero_Erores, filas, columnas, char, "Descripción"])
            elif Estado_Caracter == "n_nombre":
                if char == "o" or char == "O":
                    Estado_Caracter = "o_nombre"
                    cadena += char
                else:
                    Numero_Erores += 1
                    Reporte_Errores.append([Numero_Erores, filas, columnas, char, "Descripción"])
            elif Estado_Caracter == "u_ruta":
                if char == "t" or char == "T":
                    Estado_Caracter = "t_ruta"
                    cadena += char
                else:
                    Numero_Erores += 1
                    Reporte_Errores.append([Numero_Erores, filas, columnas, char, "Descripción"])
            elif Estado_Caracter == "s_estacion":
                if char == "t" or char == "T":
                    Estado_Caracter = "t_estacion"
                    cadena += char
                else:
                    Numero_Erores += 1
                    Reporte_Errores.append([Numero_Erores, filas, columnas, char, "Descripción"])
            elif Estado_Caracter == "o_nombre":
                if char == "m" or char == "M":
                    Estado_Caracter = "m_nombre"
                    cadena += char
                else:
                    Numero_Erores += 1
                    Reporte_Errores.append([Numero_Erores, filas, columnas, char, "Descripción"])
            elif Estado_Caracter == "t_ruta":
                if char == "a" or char == "A":
                    Estado_Caracter = "a_ruta"
                    cadena += char
                else:
                    Numero_Erores += 1
                    Reporte_Errores.append([Numero_Erores, filas, columnas, char, "Descripción"])
            elif Estado_Caracter == "t_estacion":
                if char == "a" or char == "A":
                    Estado_Caracter = "a_estacion"
                    cadena += char
                else:
                    Numero_Erores += 1
                    Reporte_Errores.append([Numero_Erores, filas, columnas, char, "Descripción"])
            elif Estado_Caracter == "m_nombre":
                if char == "b" or char == "B":
                    Estado_Caracter = "b_nombre"
                    cadena += char
                else:
                    Numero_Erores += 1
                    Reporte_Errores.append([Numero_Erores, filas, columnas, char, "Descripción"])
            elif Estado_Caracter == "a_estacion":
                if char == "c" or char == "C":
                    Estado_Caracter = "c_estacion"
                    cadena += char
                else:
                    Numero_Erores += 1
                    Reporte_Errores.append([Numero_Erores, filas, columnas, char, "Descripción"])
            elif Estado_Caracter == "b_nombre":
                if char == "r" or char == "R":
                    Estado_Caracter = "r_nombre"
                    cadena += char
                else:
                    Numero_Erores += 1
                    Reporte_Errores.append([Numero_Erores, filas, columnas, char, "Descripción"])
            elif Estado_Caracter == "c_estacion":
                if char == "i" or char == "I":
                    Estado_Caracter = "i_estacion"
                    cadena += char
                else:
                    Numero_Erores += 1
                    Reporte_Errores.append([Numero_Erores, filas, columnas, char, "Descripción"])
            elif Estado_Caracter == "r_nombre":
                if char == "e" or char == "E":
                    Estado_Caracter = "e_nombre"
                    cadena += char
                else:
                    Numero_Erores += 1
                    Reporte_Errores.append([Numero_Erores, filas, columnas, char, "Descripción"])
            elif Estado_Caracter == "i_estacion":
                if char == "o" or char == "O":
                    Estado_Caracter = "o_estacion"
                    cadena += char
                else:
                    Numero_Erores += 1
                    Reporte_Errores.append([Numero_Erores, filas, columnas, char, "Descripción"])
            elif Estado_Caracter == "o_estacion":
                if char == "n" or char == "N":
                    Estado_Caracter = "n_estacion"
                    cadena += char
                else:
                    Numero_Erores += 1
                    Reporte_Errores.append([Numero_Erores, filas, columnas, char, "Descripción"])
            elif Estado_Caracter == "n_estacion":
                if char == ">":
                    Estado_Caracter = "ninguno"
                    cadena+=char
                else:
                    Numero_Erores += 1
                    Reporte_Errores.append([Numero_Erores, filas, columnas, char, "Descripción"])
            elif Estado_Caracter == "e_nombre":
                if char == ">":
                    Estado_Caracter = "ninguno"
                    cadena+=char
                else:
                    Numero_Erores += 1
                    Reporte_Errores.append([Numero_Erores, filas, columnas, char, "Descripción"])
            elif Estado_Caracter == "a_ruta":
                if char == ">":
                    Estado_Caracter = "ninguno"
                    cadena+=char
                else:
                    Numero_Erores += 1
                    Reporte_Errores.append([Numero_Erores, filas, columnas, char, "Descripción"])
            elif Estado_Caracter == "p_peso":
                if char == "e" or char == "E":
                    Estado_Caracter = "e_peso"
                    cadena+=char
                else:
                    Numero_Erores += 1
                    Reporte_Errores.append([Numero_Erores, filas, columnas, char, "Descripción"])
            elif Estado_Caracter == "e_peso":
                if char == "s" or char == "S":
                    Estado_Caracter = "s_peso"
                    cadena+=char
                else:
                    Numero_Erores += 1
                    Reporte_Errores.append([Numero_Erores, filas, columnas, char, "Descripción"])
            elif Estado_Caracter == "s_peso":
                if char == "o" or char == "O":
                    Estado_Caracter = "o_peso"
                    cadena+=char
                else:
                    Numero_Erores += 1
                    Reporte_Errores.append([Numero_Erores, filas, columnas, char, "Descripción"])
            elif Estado_Caracter == "o_peso":
                if char == ">":
                    Estado_Caracter = "ninguno"
                    cadena+=char
            elif Estado_Caracter == "i_inicio":
                if char == "n" or char == "N":
                    Estado_Caracter = "n_inicio"
                    cadena += char
                else:
                    Numero_Erores += 1
                    Reporte_Errores.append([Numero_Erores, filas, columnas, char, "Descripción"])
            elif Estado_Caracter == "n_inicio":
                if char == "i" or char == "I":
                    Estado_Caracter = "2i_inicio"
                    cadena += char
                else:
                    Numero_Erores += 1
                    Reporte_Errores.append([Numero_Erores, filas, columnas, char, "Descripción"])
            elif Estado_Caracter == "2i_inicio":
                if char == "c" or char == "C":
                    Estado_Caracter = "c_inicio"
                    cadena += char
                else:
                    Numero_Erores += 1
                    Reporte_Errores.append([Numero_Erores, filas, columnas, char, "Descripción"])
            elif Estado_Caracter == "c_inicio":
                if char == "i" or char == "I":
                    Estado_Caracter = "3i_inicio"
                    cadena += char
                else:
                    Numero_Erores += 1
                    Reporte_Errores.append([Numero_Erores, filas, columnas, char, "Descripción"])
            elif Estado_Caracter == "3i_inicio":
                if char == "o" or char == "O":
                    Estado_Caracter = "o_inicio"
                    cadena += char
                else:
                    Numero_Erores += 1
                    Reporte_Errores.append([Numero_Erores, filas, columnas, char, "Descripción"])
            elif Estado_Caracter == "o_inicio":
                if char == ">":
                    Estado_Caracter = "ninguno"
                    cadena += char
                else:
                    Numero_Erores += 1
                    Reporte_Errores.append([Numero_Erores, filas, columnas, char, "Descripción"])
            elif Estado_Caracter == "f_fin":
                if char == "i" or char == "I":
                    Estado_Caracter = "i_fin"
                    cadena += char
                else:
                    Numero_Erores += 1
                    Reporte_Errores.append([Numero_Erores, filas, columnas, char, "Descripción"])
            elif Estado_Caracter == "i_fin":
                if char == "n" or char == "N":
                    Estado_Caracter = "n_fin"
                    cadena += char
                else:
                    Numero_Erores += 1
                    Reporte_Errores.append([Numero_Erores, filas, columnas, char, "Descripción"])
            elif Estado_Caracter == "n_fin":
                if char == ">":
                    Estado_Caracter = "ninguno"
                    cadena+=char
                else:
                    Numero_Erores += 1
                    Reporte_Errores.append([Numero_Erores, filas, columnas, char, "Descripción"])
            elif Estado_Caracter == "e_estado":
                if char == "s" or char == "S":
                    Estado_Caracter = "s_estado"
                    cadena += char
                else:
                    Numero_Erores += 1
                    Reporte_Errores.append([Numero_Erores, filas, columnas, char, "Descripción"])
            elif Estado_Caracter == "s_estado":
                if char == "t" or char == "T":
                    Estado_Caracter = "t_estado"
                    cadena += char
                else:
                    Numero_Erores += 1
                    Reporte_Errores.append([Numero_Erores, filas, columnas, char, "Descripción"])
            elif Estado_Caracter == "t_estado":
                if char == "a" or char == "A":
                    Estado_Caracter = "a_estado"
                    cadena += char
                else:
                    Numero_Erores += 1
                    Reporte_Errores.append([Numero_Erores, filas, columnas, char, "Descripción"])
            elif Estado_Caracter == "a_estado":
                if char == "d" or char == "D":
                    Estado_Caracter = "d_estado"
                    cadena += char
                else:
                    Numero_Erores += 1
                    Reporte_Errores.append([Numero_Erores, filas, columnas, char, "Descripción"])
            elif Estado_Caracter == "d_estado":
                if char == "o" or char == "O":
                    Estado_Caracter = "o_estado"
                    cadena += char
                else:
                    Numero_Erores += 1
                    Reporte_Errores.append([Numero_Erores, filas, columnas, char, "Descripción"])
            elif Estado_Caracter == "o_estado":
                if char == ">":
                    Estado_Caracter = "ninguno"
                    cadena += char
                else:
                    Numero_Erores += 1
                    Reporte_Errores.append([Numero_Erores, filas, columnas, char, "Descripción"])
            elif Estado_Caracter == "c_color":
                if char == "o" or char == "O":
                    Estado_Caracter = "o_color"
                    cadena += char
                else:
                    Numero_Erores += 1
                    Reporte_Errores.append([Numero_Erores, filas, columnas, char, "Descripción"])
            elif Estado_Caracter == "o_color":
                if char == "l" or char == "L":
                    Estado_Caracter = "l_color"
                    cadena += char
                else:
                    Numero_Erores += 1
                    Reporte_Errores.append([Numero_Erores, filas, columnas, char, "Descripción"])
            elif Estado_Caracter == "l_color":
                if char == "o" or char == "O":
                    Estado_Caracter = "2o_Color"
                    cadena += char
                else:
                    Numero_Erores += 1
                    Reporte_Errores.append([Numero_Erores, filas, columnas, char, "Descripción"])
            elif Estado_Caracter == "2o_Color":
                if char == "r" or char == "R":
                    Estado_Caracter = "r_color"
                    cadena += char
                else:
                    Numero_Erores += 1
                    Reporte_Errores.append([Numero_Erores, filas, columnas, char, "Descripción"])
            elif Estado_Caracter == "r_color":
                if char == ">":
                    Estado_Caracter = "ninguno"
                    cadena += char
                else:
                    Numero_Erores += 1
                    Reporte_Errores.append([Numero_Erores, filas, columnas, char, "Descripción"])
            else:
                cadena += char

    Graficar_Reporte_Tokens_Y_Reporte_Errores(Reporte_Tokens, Reporte_Errores)
    return Lista_Rutas, Lista_Estaciones

