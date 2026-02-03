# Lee el fichero con los id de stops y devuelve una lista con los id
def Lectura_StopsFile (pathData,stop_file_name):
    Lista_nodos = []  # viene bien que sea lista para hacer las restri
    fichero_stops=open(pathData+stop_file_name, 'r')
    for linea in fichero_stops:
        valor=linea
        Lista_nodos.append(valor.rstrip())#para quitar el salto de línea
    fichero_stops.close()
    return Lista_nodos
# Lee el fichero con los datos de los arcos bus, si Id es cero devuelve tupla con los arcos, si Id es 1, devuelve lista con los
# Id de cada arco, Si Id es 2, devuelve lista con  arco y longitud
def Lectura_ArcsBusFile(pathData, arcBus_file_name, Id):
    Lista_arcos_bus = []  # viene bien que sea lista para hacer las restri
    Lista_arcos_distancias_bus = []  # lista cuyos elementos son tuplas con los arcos y las distancias
    Lista_ID_arcos_bus = []  # viene bien que sea lista para hacer las restri
    fichero_arcs_bus=open(pathData+arcBus_file_name, 'r')
    dicc_arco_distancia={}
    for linea in fichero_arcs_bus:
        aux = []
        aux2 = []
        valor=linea.split(";")
      #  print(valor)
        edge_id=valor[0]
        edge_idq = valor[1]
        edge_dch = valor[2]
        edge_distancia=valor[3]
        aux.append(edge_idq)
        aux.append(edge_dch)
        #aux2.append(edge_idq)
        #aux2.append(edge_dch)
        Lista_arcos_bus.append(tuple(aux))
        Lista_ID_arcos_bus.append(edge_id)
        #aux2.append(edge_distancia.rstrip())
        #Lista_arcos_distancias_bus.append(aux2)
        aux.append(edge_distancia.rstrip())#rstrip() para quitar el salto de línea
        Lista_arcos_distancias_bus.append(aux)
        dicc_arco_distancia[(edge_idq,edge_dch)] = edge_distancia.rstrip()
    fichero_arcs_bus.close()
    if Id == 0: #devuelve tupla con los arcos
        return Lista_arcos_bus
    elif Id == 1:#devuelve lista con los Id de cada arco
        return Lista_ID_arcos_bus
    elif Id == 2:#devuelve lista con  arco y longitud
       # print(Lista_arcos_distancias_bus)
        return Lista_arcos_distancias_bus
    elif Id == 3:#devuelve diccionario tipo arco: distancia
        return dicc_arco_distancia
    else:
        print("Id incorrecto")

# Lee el fichero con los datos de los aristas PED, si Id es cero devuelve tupla con las aristas, si Id es 1, devuelve lista con los
# Id de cada arista, Si Id es 2, devuelve lista con  arista y longitud
def Lectura_ArcsPEDFile(pathData, arcPED_file_name, Id):
    Lista_aristas_distancias_PED = []  # lista cuyos elementos son tuplas con los arcos y las distancias
    Lista_ID_aristas_PED = []
    Lista_aristas_PED = []  # viene bien que sea lista para hacer las restri
    dicc_arco_distancia_PED={}
    fichero_arcs_PED=open(pathData+arcPED_file_name, 'r')
    for linea in fichero_arcs_PED:
        aux = []
        aux2 = []
        valor=linea.split(";")
      #  print(valor)
        edge_id=valor[0]
        edge_idq = valor[1]
        edge_dch = valor[2]
        edge_distancia=valor[3]
        aux.append(edge_idq)
        aux.append(edge_dch)
        #aux2.append(edge_idq)
        #aux2.append(edge_dch)
        Lista_aristas_PED.append(tuple(aux))
        Lista_ID_aristas_PED.append(edge_id)
        #aux2.append(edge_distancia.rstrip())
        #Lista_arcos_distancias_bus.append(aux2)
        aux.append(edge_distancia.rstrip())#rstrip() para quitar el salto de línea
        Lista_aristas_distancias_PED.append(aux)
        dicc_arco_distancia_PED[(edge_idq, edge_dch)] = edge_distancia.rstrip()
    fichero_arcs_PED.close()
    if Id == 0:#devuelve tupla con los arcos
        return Lista_aristas_PED
    elif Id == 1:#devuelve lista con los Id de cada arco
        return Lista_ID_aristas_PED
    elif Id == 2:#devuelve lista con  arco y longitud
       # print(Lista_aristas_distancias_PED)
        return Lista_aristas_distancias_PED
    elif Id == 3:  # devuelve diccionario tipo arco: distancia
        return dicc_arco_distancia_PED
    else:
        print("Id incorrecto")

# Devuelve tupla con el id, origen, destino y demanda
def Lectura_ODFile(pathData, OD_name, Id):
    Lista_OD = []
    dicc_OD_demanda={}
    fichero_OD = open(pathData + OD_name, 'r')
    for linea in fichero_OD:
        aux = []
        valor = linea.split(";")
        id = valor[0]
        origen = valor[1]
        destino = valor[2]
        demanda= valor[3]
        aux.append(id)
        aux.append(origen)
        aux.append(destino)
        aux.append(demanda.rstrip())
        Lista_OD.append(tuple(aux))
        dicc_OD_demanda[(origen,destino)]=demanda.rstrip()
    fichero_OD.close()
   # print(Lista_OD)

    if Id == 0:  # devuelve tupla con los  Id, OD, demanda
        return Lista_OD
    elif Id == 1:  # devuelve diccionario tipo; OD:demanda
        return dicc_OD_demanda
    else:
        print("Id incorrecto")

    print("Lista_OD"+Lista_OD)
    return Lista_OD
# Devuelve tupla con las coordenadas X e Y de cada nodo (por si es necesario este método...)
def Lectura_CoordenadaFile(pathData,coordenadas_name):
    Lista_coordenadas = []  # para calcular las distancias
    fichero_coordendas=open(pathData+coordenadas_name, 'r')
    for linea in fichero_coordendas:
        coordenadas=[]
        valor=linea.split(";")
        coordenadaX=valor[0]
        coordenadaY= valor[1]
        coordenadas.append(coordenadaX)
        coordenadas.append(coordenadaY.rstrip())
        Lista_coordenadas.append(tuple(coordenadas))
    fichero_coordendas.close()
    return Lista_coordenadas

# -----------------------------------------------------------------
# -----------      MÉTODOS SIN PREPROCESO  ------------------------
# -----------------------------------------------------------------
def CreaDiccionario_listaNodos(Lista_nodos, Lista_OD):
    dicc_listaNodos={}
    for parOD in Lista_OD:
        origen=parOD[1]
        destino=parOD[2]
        dicc_listaNodos[(origen,destino)]=Lista_nodos
    return dicc_listaNodos

def CreaDiccionario_listaArcos(Lista_arcos_bus, Lista_OD):
    dicc_listaArcos={}
    for parOD in Lista_OD:
        origen=parOD[1]
        destino=parOD[2]
        dicc_listaArcos[(origen,destino)]=Lista_arcos_bus
    return dicc_listaArcos