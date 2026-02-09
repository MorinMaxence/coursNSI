# Graphes

## 1 - Origine 

Le concept de graphe a été introduit par le mathématicien Leonhard Euler en 1735 pour résoudre le problème des ponts de Königsberg. Les habitants se demandaient s’il existait ou non une promenade dans les rues de Königsberg permettant, à partir d’un point de départ au choix, de passer une et une seule fois par chaque pont et de revenir à son point de départ, étant entendu qu’on ne pouvait traverser la Pregel qu’en passant par les ponts.

![Les ponts de Königsberg](./source/eduscolPlan.png)

Depuis, les graphes sont des structures de données essentielles en informatique, permettant de modéliser des relations entre des éléments. Que ce soit pour représenter un réseau routier, un réseau électrique, Internet, des relations sociales, etc.

## 2 - Vocabulaire général


> ![Représentation d’un graphe](./source/graphe.png)
>
> **Figure 1** : exemple de représentation d’un graphe d’amis, d’ordre 5 (un sommet = une personne) et les arêtes qui représentent les amitiés.

* Un **graphe** est composé d’un ensemble de **sommets** et d’un ensemble d’**arêtes** (ou d'**arcs**). Il s’agit d’une représentation d’un ensemble de relations entre des entités. On le note G = (S, A), où S est un ensemble fini de sommets et A un ensemble fini d’arêtes représentées par des couples de sommets. Par exemple, dans la figure 1, le graphe G = (S, A) avec S = {Alice, Bob, Charlie, Diana, Eve} et A = {(Alice, Bob), (Alice, Charlie), (Bob, Diana), (Charlie, Diana), (Diana, Eve), (Bob, Eve)}.
* Un **sommet** représente une entité, souvent désignée par un cercle dans les représentations graphiques.
* Une **arête** ou un **arc** représente la relation entre deux sommets, souvent désignée par une ligne ou une flèche reliant deux cercles.
* **L'ordre** du graphe est le nombre de sommets qu'il contient.

> **Remarque** : un graphe peut contenir des **arêtes multiples** et des **boucles**. Une arête multiple est une arête qui relie les mêmes sommets que d’autres arêtes. Une boucle est une arête qui relie un sommet à lui-même. S’il n’y a aucun de ces deux cas, on dit que le graphe est **simple**. Nous travaillerons uniquement avec des graphes simples.

Il existe deux types de graphes : les graphes orientés et les graphes non orientés.

## 3 - Graphes non orientés

Un graphe non orienté est un graphe dans lequel les arêtes n’ont pas de direction. Par exemple, dans la figure 1, les arêtes représentent des relations d’amitié réciproques : si Alice est amie avec Bob, alors Bob est également ami avec Alice.

* Deux sommets sont dits **adjacents** s’ils sont reliés par une arête.
Par exemple, Alice et Bob sont adjacents.
* Les **voisins** d’un sommet sont les sommets qui lui sont adjacents.
Par exemple, les voisins de Bob sont Alice, Charlie et Diana.
* Le **degré** d’un sommet est son nombre de voisins.
Par exemple, le degré de Bob est 3.

> ![Exo1](./source/grapheExo1.png)
>
> **Figure 2**: Graphe non orientés

Question : 
* Pour chaque graphe, donner son ordre.
* Est-ce que les couples de sommets suivants sont adjacents ? :
  * Graphe 1 : (A, B), (A, D), (C, E)
  * Graphe 2 : (A, C), (B, D), (C, D)
* Recopier et compléter le tableau des degrés des sommets pour chaque graphe:

| Sommet | Degré Graphe 1 | Degré Graphe 2 |
| :----: | :------------: | :------------: |
|   A    |                |                |
|   B    |                |                |
|   C    |                |                |
|   D    |                |                |
|   E    |                |Pas de sommet E |

* Une **chaîne** est une suite de sommets tels que chaque sommet est adjacent au suivant. Par exemple, le graphe 1 de la figure 2, une chaîne possible est A - E - D - B - C ou encore C - A - B.
* Un **cycle** est une chaîne qui commence et se termine au même sommet.
* La **distance** entre deux sommets est la chaîne la plus courte qui les relie.

Question : 
* Donner une chaîne de longueur 4 dans chacun des graphes.
* Donner un cycle qui passe par tous les sommets dans chacun des graphes.
* Quelle est la distance entre les sommets D et C dans chacun des graphes ?


## 4 - Graphes orientés

Les graphes orientés ont un fonctionnement différent : ce sont des graphes dans lequel les arêtes ont une direction et sont appelées **arcs**. Reprenons notre 1er graphe, mais cette fois-ci en représentant des relations de type "suivre" sur un réseau social. Si Bob suit Alice, cela ne signifie pas nécessairement que Alice suit Bob.

Plusieurs notions changent dans le vocabulaire des graphes orientés :

* On ne parle plus de sommets adjacents, mais de **successeurs** et de **prédécesseurs**. Pour un graphe orienté, un couple de sommets (u, v) est un **arc allant de u vers v**, v est donc un successeur de u et que u est un prédécesseur de v. Un sommet peut être à la fois prédécesseur et successeur d’un autre sommet. Dans notre exemple, 
Bob est un prédécesseur **ET** un successeur d’Alice.
* On ne parle plus de chaîne, mais de **chemin** dans un graphe orienté et la **distance** entre deux sommets devient donc le chemin le plus court qui les relie. Egalement, un cycle dans un graphe orienté est appelé un **circuit** et correspond à un chemin qui commence et se termine au même sommet.

> **Remarque** : On peut également définir le **degré entrant** (nombre de prédécesseurs) et le **degré sortant** (nombre de successeurs) d’un sommet. Le **degré** d'un sommet dans un graphe orienté est la somme de son degré entrant et de son degré sortant.

> ![Représentation d’un graphe orientés](./source/grapheO.png)
>
> **Figure 3**: Graphe de suivi dans un réseau social.

Question :
* Dans notre réseau social, qui sont les personnes suivies par Bob ? Que sont ces personnes pour Bob ?
* Qui sont les personnes qui suivent Alice ? Que sont ces personnes pour Alice ?
* Qui sont les personnes les plus suivies ?
* Quelle est la distance entre Eve et Alice ? 
* Existe-t-il un chemin de Alice vers Eve ? 
* Existe-t-il un circuit dans ce graphe ?
* Recopiez et complétez le tableau des degrés entrants et sortants des sommets :

| Sommet | Degré entrant | Degré sortant | Degré |
| :----: | :------------: | :------------: | :----: |
|   Alice   |                |                |        |
|   Bob    |                |                |        |
|   Charlie    |                |                |        |
|   Diana    |                |                |        |
|   Eve    |                |                |        |
## 5 - Implémentations

Maintenant nous savons ce qu'est un graphe et le vocabulaire associé, voyons comment le représenter en Python. Il existe deux principales façons de représenter un graphe : la matrice d’adjacence et les listes d’adjacence.

### Matrice d'adjacence

On peut représenter un graphe par une matrice carrée appelée **matrice d'adjacence**. Si le graphe possède n sommets, on construit une matrice de taille $n×n$ (une liste de listes en Python), qui contient des 0 et des 1. S'il existe une arête ou un arc du sommet i vers le sommet j, on met un 1 à la position (i, j) de la matrice, sinon on met un 0.

Pour notre graphe de suivi (figure 3), On peut commencer par construire un tableau :

|   |      Alice     |  Bob | Charlie | Eve | Diana |
| :---------------:|:---------------:|:-----:|:-----:|:-----:|:-----:|
| **Alice**  |   0        |  0 | 0 | 0 | 0 |
|**Bob**| 1             |   0 | 1 | 0 | 1 |
| **Charlie**  | 1         |    0 | 0 | 1 | 0 |
| **Eve**  | 0          |    0 | 1 | 0 | 0 |
| **Diana**  | 0          |    0 | 0 | 1 | 0 |

On obtient donc la matrice d'adjacence suivante :

```python
matrice_adjacence = [
    [0, 0, 0, 0, 0],  # Alice
    [1, 0, 1, 0, 1],  # Bob
    [1, 0, 0, 1, 0],  # Charlie
    [0, 0, 1, 0, 0],  # Eve
    [0, 0, 0, 1, 0]   # Diana
]
```

Question :
* A quoi correspond la valeur de la case matrice_adjacence[1][2] ?
* Redessinez le graphe avec les modifications suivantes :
    * matrice_adjacence[1][3] = 1
    * matrice_adjacence[2][0] = 0
    * matrice_adjacence[0][2] = 1
    * matrice_adjacence[1][0] = 0
* Pourquoi la diagonale de la matrice est-elle composée uniquement de 0 ?

> ![GrapheExemple](./source/grapheMatriceAdj.png)
>
> **Figure 4**: Graphe non orienté.

Question :
* Construire la matrice d'adjacence du graphe non orienté.
* La matrice d'adjacence d'un graphe non orienté possède une propriété intéressante : regardez votre matrice sous et au dessus de la diagonale (de la case en haut à gauche à la case en bas à droite). Que remarquez-vous ? Pourquoi ?

> * Implémenter une fonction **verifier_oriente(matrice)** qui prend une matrice d'adjacence d'un graphe et qui renvoie True si le graphe est orienté et False sinon.
>```python
> def verif_oriente(matrice):
>     """Verifie si un graphe est orienté à partir de sa matrice d'adjacence.
>        Param:
>           matrice : list(list(int)) -> Une liste de liste de taille même longueur et largeur 
>           contenant des 0 (pas d'arc) ou des 1 (présence d'arc)
>     """
>     # Votre code ici
> ```

* Dessinez le graphe correspondant à la matrice d'adjacence suivante, Les sommets sont numérotés de 1 à 5:
```python
matrice_adjacence = [
    [0, 1, 0, 1, 0],  
    [1, 0, 0, 0, 1],  
    [1, 0, 0, 1, 0],  
    [0, 0, 1, 0, 0],  
    [1, 1, 1, 1, 0]   
]
```

### Liste d'adjacence

Une autre façon de représenter un graphe est d'utiliser des listes d'adjacence. 
Pour chaque sommet, on crée une liste qui contient tous ses successeurs.
Cette représentation peut paraître plus clair car on peut directement voir les relations entre les sommets et leurs noms. 
Pour cela on peut utiliser un dictionnaire qui va associer un sommet (clé) à sa liste de successeurs (valeur) en python.

```python
graphe = {
    "Alice": [],
    "Bob": ["Alice", "Charlie", "Diana"],
    "Charlie": ["Alice", "Eve"],
    "Eve": ["Charlie"],
    "Diana": ["Eve"]
}
```

Question :
* Que représente la liste associée à la clé "Bob" dans le dictionnaire ?
* Construire la liste d'adjacence du graphe non orienté de la figure 4.
* Dessinez le graphe correspondant à la liste d'adjacence du graphe orienté suivant:
```python
graphe = {
    "A": ["B", "C", "E"],
    "B": ["A", "D", "E"],
    "C": ["A", "D"],
    "D": ["C"],
    "E": ["A", "B", "C", "D"]
}
```


> * Implémenter une fonction **matrice_vers_liste(matrice)** qui prend une matrice d'adjacence d'un graphe et qui renvoie une liste d'adjacence sous forme de dictionnaire. Le nom des sommets sera leur indice dans la matrice (0, 1, 2, ...).
>```python
> def matrice_vers_liste(matrice):
>     """Transforme une matrice d'adjacence en liste d'adjacence.
>        Param:
>           matrice : list(list(int)) -> Une liste de liste de taille même longueur et largeur 
>           contenant des 0 (pas d'arc) ou des 1 (présence d'arc)
>     """
>     liste_adjacence = {}
>     # Votre code ici
>     return liste_adjacence
> ```



