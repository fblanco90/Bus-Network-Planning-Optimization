import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.patches as mpatches

class GrafoColores:
    def __init__(self, listas):
        self.listas = listas
        self.G = nx.MultiDiGraph(sum(listas, []))  # Concatenar todas las listas en una sola lista de aristas

    def dibujar_grafo(self):
        posiciones_personalizadas = {
            '0': (-3, 2),
            '1': (-2, 1),
            '2': (0, 1),
            '3': (-2, 0),
            '4': (-3, 0),
            '5': (0, 0),
            '6': (2, -1),
            '7': (1, -1),
            '8': (2, 1),
            '9': (1, -2),
            '10': (-1, -2),
            '11': (-2, -1),
            '12': (0, -3),
            '13': (2, -3),
            '14': (2, 0),
        }

        color_mapping = {
            'L1': 'red',
            'L2': 'blue',
            'L3': 'yellow',
            'L4': 'lightgreen',
            'L5': 'purple',
            'L6': 'orange',
            'L7': 'cyan',
            'L8': 'black'
        }

        legend_patches = [mpatches.Patch(color=color_mapping[label], label=label) for label in color_mapping if label[1:].isdigit() and 1 <= int(label[1:]) <= len(self.listas) and any(e[:2] in self.listas[int(label[1]) - 1] for e in self.G.edges)]

        plt.figure()

        nx.draw_networkx_nodes(self.G, posiciones_personalizadas, node_color='skyblue', node_size=200, alpha=1)
        nx.draw_networkx_labels(self.G, posiciones_personalizadas, font_size=10, font_color='black', font_family='sans-serif')

        ax = plt.gca()
        unique_tuple = set()
        contador = 0

        for i, color in color_mapping.items():
            indice_numerico = int(i[1]) - 1
            if 0 <= indice_numerico < len(self.listas):
                lineas = self.listas[indice_numerico]
                aristas_insertadas_linea = set()
                k = 0
                for e in self.G.edges:
                    if e[:2] in lineas and e not in unique_tuple and e[2] <= contador and e[:2] not in aristas_insertadas_linea:
                        unique_tuple.add(e)
                        aristas_insertadas_linea.add(e[:2])
                        ax.annotate("",
                                    xy=posiciones_personalizadas[e[1]], xycoords='data',
                                    xytext=posiciones_personalizadas[e[0]], textcoords='data',
                                    arrowprops=dict(arrowstyle="->", color=color,
                                                    shrinkA=10, shrinkB=10,
                                                    linewidth=2,
                                                    connectionstyle="arc3,rad=rrr".replace('rrr', str(0.15 + 0.15 * e[2])
                                                    ),
                                                    ),
                                    )
                    k += 1
                contador += 1


        plt.legend(handles=legend_patches, loc='upper right', bbox_to_anchor=(1.25, 1))
        plt.axis('off')
        self.image_path = 'grafo_temp.png'
        plt.savefig(self.image_path, format='png', bbox_inches='tight')
        plt.show()
        plt.close()



