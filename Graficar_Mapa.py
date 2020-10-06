from graphviz import Digraph
def Grafica_Mapa(Rutas, Estaciones, NombreMapa):
    f = Digraph(format="png", name="Mapa")
    f.attr(rankdir="TD", size="8")
    f.attr("node")
    for i in Estaciones:
        f.node(i.nombre, shape = "", label= i.nombre+"\n"+i.estado, fillcolor = i.color, style="filled")
    for i in Rutas:
        f.edge(i.inicio, i.fin, label=i.nombre + "\n" + str(i.peso))
    f.attr(label=NombreMapa)
    f.view()