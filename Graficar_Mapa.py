from graphviz import Digraph
def Grafica_Mapa(Rutas, Estaciones):
    f = Digraph(format="png", name="prueba")
    f.attr(rankdir="TD", size="8")
    f.attr("node")
    # f.edge("0", "0", label="x")
    # f.edge("0", "1", label="x")
    # f.edge("1", "0", label="y")
    # f.edge("1", "2", label="y")
    # f.edge("2", "0", label="x")
    # f.edge("2", "3", label="x")
    # f.edge("3", "0", label="y")
    # f.edge("3", "2", label="y")
    for i in Estaciones:
        f.node(i.nombre, shape = "", label= i.nombre+"\n"+i.estado, fillcolor = i.color, style="filled")
    for i in Rutas:
        f.edge(i.inicio, i.fin, label=i.nombre + "\n" + str(i.peso))
    f.view()