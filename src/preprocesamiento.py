# implementar aqui el preprocesamiento!!
#from MyPlotandNetworkFunctions import *
from itertools import islice
from networkx import *
import networkx as nx
# -----------------------------------------------------------------
# -----------      DICCIONARIOS DE SALIDA  ------------------------
# -----------------------------------------------------------------


dicc_parOD_listaPaths = {}#diccionario tipo; parOD: lista cuyos eltos son listas con los nodos de cada path
dicc_parOD_listaNodosPaths = {}#diccionario tipo; parOD: lista con todos los nodos implicados en todos los paths
dicc_parOD_listaArcosPaths = {}#diccionario tipo; parOD: lista con todos los arcos implicados en todos los paths

# -----------------------------------------------------------------
# -----------      MÉTODOS PRINCIPALES    ------------------------
# -----------------------------------------------------------------
"""
Devuelve un diccionario tipo; {parOD: lista cuyos elementos son listas con todos los k-shortest paths}
"""
def CreaDiccionario_KshortestPaths(Lista_nodos,Lista_arcos_distancias_bus, Lista_OD):
    G = DiGraph()
    G.add_nodes_from(Lista_nodos)
    G.add_weighted_edges_from(Lista_arcos_distancias_bus)#el argumento de entrada es lista con arcos y distancias
    for lista_par in Lista_OD:
        Code_par = lista_par[0]
        origen=lista_par[1]
        destino=lista_par[2]
        dicc_parOD_listaPaths[(origen, destino)] = k2_shortest_paths(G, origen, destino, 2)#diccionario tipo; parOD: lista cuyos elementos son listas de nodos de cada path
    #print("CreaDiccionario_KshortestPaths: dicc_parOD_listaPaths", dicc_parOD_listaPaths)
    return dicc_parOD_listaPaths
"""
Devuelve un diccionario tipo; {parOD: lista con todos los nodos que aparecen en los k-shortest paths}
"""
def CreaDiccionario_listaNodos_KshortestPaths(dicc_parOD_listaPaths):

    for (origen,destino) in dicc_parOD_listaPaths:
        dicc_parOD_listaNodosPaths[(origen, destino)] = []
        #---Se crea diccionario con todos los nodos del path, tipo; parOD: nodos implicados en los shortest paths
        for listaNodospath in range(len(dicc_parOD_listaPaths[(origen, destino)])):
             for nodo in dicc_parOD_listaPaths[(origen, destino)][listaNodospath]:#coge el nodo de  la lista de nodos de unos de los shortest path
                 if nodo not in dicc_parOD_listaNodosPaths[(origen, destino)]:
                    dicc_parOD_listaNodosPaths[(origen, destino)].append(nodo)#diccionario tipo; parOD:lista nodos de todos los paths
                    #print(((i, j), DParesListNod[(i, j)]))
        #print("CreaDiccionario_listaNodos_KshortestPaths:dicc_parOD_listaNodosPaths",[(origen, destino)], dicc_parOD_listaNodosPaths[(origen, destino)])
    return dicc_parOD_listaNodosPaths
"""
Devuelve un diccionario tipo; {parOD: lista con todos los arcos que aparecen en los k-shortest paths}
"""
def CreaDiccionario_listaArcos_KshortestPaths(dicc_parOD_listaPaths):
    for (origen, destino) in dicc_parOD_listaPaths:  # Aqui hay una lista de nodos
        Aux2 = []
        for k in range(len(dicc_parOD_listaPaths[(origen, destino)])):
            Aux = construye_listaArcos(dicc_parOD_listaPaths[(origen, destino)][k])
            Aux2 = Anade_elemensts(Aux2, Aux)
        dicc_parOD_listaArcosPaths[(origen, destino)] = Aux2
    return dicc_parOD_listaArcosPaths
# -----------------------------------------------------------------
# -----------      MÉTODOS AUXILIARES    ------------------------
# -----------------------------------------------------------------

"""
Devuelve los k-caminos más cortos!
"""
def k2_shortest_paths(G, source, target, k, weight=None):
    return list(islice(nx.shortest_simple_paths(G, source, target, weight=weight), k))

def k2b_shortest_paths(G, source, target, k, weight=None):
    return list(islice(nx.shortest_simple_paths(G, source, target, weight=weight), k)), shortest_path_length(G, source, target, weight=weight, method='dijkstra')
"""
Lista; lista con los nodos que definen los paths
return; lista con los arcos del path
"""
def construye_listaArcos(Lista):
    Aux = []
    for o in range(len(Lista) - 1):
        a = Lista[o]
        b = Lista[o + 1]
        Aux.append((a, b))
    return Aux
"""
lista1; lista sobre la que se añaden los elementos
lista2; lista que queremos añadir a lista1
return; lista1 con los datos de lista2, sin repetir elementos
"""
def Anade_elemensts(Lista1, Lista2):
    for k in Lista2:
        if k not in Lista1:
            Lista1.append(k)
    return Lista1

