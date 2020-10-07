from graphviz import Digraph
def Filtro_Rutas(Estacion_Inicio, Estacion_Fin, Lista_Estaciones, Lista_Rutas):
    g = Digraph(format="png", name="Ruta")
    g.attr(rankdir="LR", size="8")
    g.attr("node")
    Ruta_Final = []
    Lista_Rutas_Totales = []
    Listado_de_Rutas_Inicio = []
    Peso_Aux1 = 0
    Peso_Aux2 = 0
    #Aqui se guardan todas las rutas que inician en la estación en la que el usuario comienza su recorrido
    for i in Lista_Rutas:
        if i.inicio == Estacion_Inicio.lower():
            Listado_de_Rutas_Inicio.append(i)
    #Aqui se valida que existan rutas que inicien en esta estación
    if Listado_de_Rutas_Inicio != []:
        for e in Listado_de_Rutas_Inicio:
            """Si inicialmente se registra una ruta que inicie y termine en las estaciones que el usuario ingresa
            Esta es guardada en una lista para luego compararla con las demás"""
            if e.fin == Estacion_Fin.lower():
                Lista_Rutas_Totales.append([e])
            else:
                for w in Lista_Rutas:
                    if e.fin == w.inicio and w.fin == Estacion_Fin.lower():
                        Lista_Rutas_Totales.append([e, w])
    else:
        print("Por el momento ninguna ruta inicia en su destino")
    for i in Lista_Rutas_Totales:
        for j in i:
            Peso_Aux1 += float(j.peso)
        Peso_Aux1 = Peso_Aux1/len(i)
        if Peso_Aux2 == 0 or Peso_Aux1 < Peso_Aux2:
            Peso_Aux2 = Peso_Aux1
            Ruta_Final = i
        elif Peso_Aux1 > Peso_Aux2:
            Lista_Rutas_Totales.remove(i)
    # for i in Lista_Rutas_Totales:
    #     for e in i:
    #         for j in Lista_Estaciones:
    #             if j.nombre == e.inicio or j.nombre == Estacion_Fin.lower():
    #                 g.node(j.nombre, shape="", label=j.nombre + "\n" + j.estado, fillcolor=j.color, style="filled")
    #         g.edge(e.inicio, e.fin, label=e.nombre + "\n" + str(e.peso))
    for k in Ruta_Final:
        for j in Lista_Estaciones:
            if j.nombre == k.inicio or j.nombre == Estacion_Fin.lower():
                g.node(j.nombre, shape="", label=j.nombre + "\n" + j.estado, fillcolor=j.color, style="filled")
        g.edge(k.inicio, k.fin, label=k.nombre + "\n" + str(k.peso))

    g.view()