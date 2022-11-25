#DÉBUT

# admettre que l'exécution de la fonction [choice] retourne un élément aléatoire d'une liste donnée en paramètre.
# admettre que l'exécution de la fonction [randrange] retourne un entier aléatoire compris dans un encadrement d'entiers donnée en paramètre.
# 
# définir la fonction [consoleDisplay], qui prend en paramètre un le plateau (board) sous forme d'un tableau  et écrit dans la console ce tableau adapté pour le joueur.
#     initialiser un nouveau tableau 3x3 vide (displayBoard) pour l'affichage
#     pour chaque index de (ligne)s de 0 à 3
#           pour chaque index de (colonne)s de 0 à 3
#               si la case du tableau (board) de la (colonne) active et de la (ligne) active est égale à 1 
#                   alors assigner "x" à la case du tableau (displayBoard) de la (colone) active et de la (ligne) active 
#               sinon si la case du tableau (board) de la (colonne) active et de la (ligne) active est égale à -1
#                   alors assigner "o" à la case du tableau (displayBoard) de la (colone) active et de la (ligne) active 
#      écrire chaque case du tableau (dislpayBoard) en séparant chaque case par "|" et chaque ligne par "-|-|-" et en effectuant des retours à la ligne entre chaque ligne. 
# 
# définir la fonction [getPlayableSpots] qui reçoit en paramètre un plateau (board) sous forme d'un tableau et renvoit une liste de coordonnées ((ligne),(colonne)) représentant les cases égales à 0 du tableau (board)
#     initialiser (spots) comme une liste vide pour accueillir les listes de coordonnées à retourner.
#     pour chaque index de (ligne)s de 0 à 3
#           pour chaque index de (colonne)s de 0 à 3
#               si la case du tableau (board) de la (colonne) active et de la (ligne) active est égale à 0 
#                   ajouter l'élément liste ((ligne),(colonne)) comme nouvel élément de la liste (spots)  
#               retourner la liste (spots). 
# 
# définir la fonction [getCorners] qui prend en paramètre une liste (spots) et retourne les listes de coordonnées qui correspondent à des coins
#     initialiser (cornersList) comme une liste vide
#     pour chaque élément (spot) de la liste (spots).    
#         si l'élément (spot) actif est présent dans la liste de listes (0,0),(2,0),(2,2),(0,2) qui correspondent aux coordonnées de coins d'un tableau 3x3.
#             ajouter la liste (spot) active comme nouvel élément de la liste (cornersList)       
#     retourner la liste (cornersList) qui est la liste des coins présents dans (spots) initialement.  
# 
# définir la fonction [getOppositCorner] qui prend une liste de coordonnées de deux éléments (corner) en paramètre et retourne une liste de coordonnées du coins opposé à celui donné en paramètre
#     initialiser la liste (newCorner) comme une liste de deux éléments NULL.
#     pour chaque entier (i) de 0 à la longueur de la liste (corner).
#         si l'item d'index (i) de la liste (corner) est égal à 2.
#             alors mettre l'item d'index (i) de la liste (newCorner) à 0
#         sinon  
#             alors mettre l'item d'index (i) de la liste (newCorner) à 1  
#     retourner une liste de l'item d'index (0) de la liste (newCorner) puis de l'item d'index (1) de la liste (newCorner)
# 
# définir la fonction [linesSum] prenant en pramètres une liste de (condition)s et un tableau (board) et retourne une ligne, colonne ou diagonale si la somme des éléments de celle-ci est présente dans la liste des (condition)s
#     initialiser (lDiagSum) qui soit égale à la somme de la case en haut à gauche du tableau (board), de la case au centre du tableau (board) et de la case en bas à droite du tableau (board)
#     initialiser (lDiagSum) qui soit égale à la somme de la case en haut à droite du tableau (board), de la case au centre du tableau (board) et de la case en bas à gauche du tableau (board)  
#     si la somme d'éléments (lDiagSum) est égale à l'un des éléments de la liste (condition)
#         alors retourner une liste avec pour éléments "diag" et 0   
#     sinon si la somme d'éléments (rDiagSum) est égale à l'un des éléments de la liste (condition)
#         alors retourner une liste avec pour éléments "diag" et 2
#     sinon
#         alors pour chaque entier (i) de 0 à 3
#             assigner à une variable (rowSum) la somme des colonnes d'index 0,1 et 2 de la ligne d'index i du tableau  
#             assigner à une variable (colSum) la somme des lignes d'index 0,1 et 2 de la colonne d'index i du tableau  
#         si la somme (rowSum) est égale à l'un des éléments de la liste (condition)
#             alors retourner une liste avec pour éléments "row" et l'index i
#         sinon si la somme (colSum) est égale à l'un des éléments de la liste (condition)
#             alors retourner une liste avec pour éléments "col" et l'index i
#      retourner NULL #commentaire : la fonction retourne NULL lorsqu'elle n'a rien renvoyé avant
#
# définir la fonction [chooseSpot] qui prend en paramètres une liste de caractères (player), un tableau (board), un entier égal à 0 ou 1 (pTurn), un entier (turn) et une liste de deux listes (spotsLog) et retourne une liste couple de coordonées qui représentent la case du plateau tableau (board) qu'un joueur essaye de jouer.
#     si la liste de caractères (player) est égale à "CPU"
#         alors initialiser la liste de listes couples (spots) en lui assignant le retour de l'exécution de la fonction [getPlayableSpots] en lui donnant en paramètre le tableau (board) qui retourne une liste de coordonnées représentant chaque case du tableau (board) égale à 0
#         initialiser l'entier (pos) en lui assignant le résultat de 1 + (pTurn) * (-2) qui est égale à soit 1 soit -1 dépendamment de l'entier (pTurn)
#         initialiser la liste (conditions) avec deux éléments, le résultat de  2 * (1 + (pTurn) * (-2)) et le résultat de 2*(1 + (pTurnSwitch(pTurn) * -2)) qui ne sont égale qu'à soit 2 soit -2 dépendamment de l'entier (pTurn)
#         pour chaque élément (condition) dans la liste (conditions)
#             assigner à une variable (line) le retour de l'exécution de la fonction [linesSum] en lui donnant en paramètres l'élément (condition) actif et le tableau (board)  
#             si la variable (line) est différentes de NULL #commentaire : n'est pas égale# 
#                 alors si l'item d'index 0 de la liste couple (line) est égal à "row"
#                     alors pour chaque entier (i) de 0 à 3
#                         si l'item d'index (i) de l'item liste d'index égal à l'item d'index 1 de la liste (line) du tableau (board) est égal à 0 #commentaire : si la case (i) de la ligne donnée par la liste (line) du tableau est égal à 0 
#                             alors retourner une liste comprenant (i) et l'item d'index 1 de la liste (line)  
#                         sinon si l'item d'index égal à l'item d'index 1 de l'item liste d'index (i) de la liste (line) du tableau (board) est égal à 0 #commentaire : si la case (i) de la colonne donnée par la liste (line) du tableau est égal à 0
#                             alors retourner une liste comprenant l'item d'index 1 de la liste (line) et (i) 
#                         sinon
#                             alors pour chaque entier (i) de 0 à 3
#                                 si l'item d'index 1 de la liste (line) est égal à 0
#                                     alors si l'item d'indice (i) de la liste d'indice (i) du tableau (board) #commentaire : une case de coordonnées i i dans le tableau
#                                         retourner une liste avec (i) et (i)
#                                 sinon si l'item d'index 1 de la liste (line) est égal à 0
#                                     alors si l'item d'indice (2-i) de la liste d'indice (i) du tableau (board) #commentaire : une case de coordonnées 2-i i dans le tableau
#                                         retourner une liste avec (2-i) et (i) 
#         initialiser la liste (corners) avec le retour de l'exécution de la fonction [getCorners] avec pour paramètres (spots) #commentaire: liste des coins libres dans le tableau (board)
#         si l'entier (turn) est égal à 1 
#             alors retourner le résultat de l'exécution de la fonction [choice] prenant en paramètre (corners)
#         sinon si l'entier (turn) est égal à 3
#             alors si la longueur de la liste (corners) est égale à 2 #commentaire : donc deux coins sont déjà pris
#                 alors retourner le résultat de l'exécution de la fonction [choice] prenant en paramètre (corners)   
#             sinon si l'item d'index 1 de l'item d'index 1 du tableau (board) est différent de 0 #commentaires : que le centre est pris
#                 si l'item d'index 0 de l'item d'index 0 de l'item d'index (pTurn) du tableau (spotsLog) #commentaires : retourne le x des coordonnées du premier coup/coup 0 du joueur actuel/CPU 
#                     alors retourner (0,1) #commentaire : extrémité de la croix centrale sur la colonne adjacente au coin selectionné précédemment 0 du tableau (board) 
#                 sinon
#                     alors retourner (2,1) #commentaire : extrémité de la croix centrale sur la colonne adjacente au coin selectionné précédemment du tableau (board) 
# #commentaire :stopped l99 
# FIN
# 
# 
# 
# 
# #
