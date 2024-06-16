Souris - Projet Souris - Lauréat ANCT
# Une souris adaptée pour personnes en situation de handicap
![souris_AMI](https://github.com/FabLabUtoPi/Souris/assets/172394416/6b358368-5b6c-40fc-a2e8-d84d5bd7ac80)
## A l’origine du projet 
Un ami aveugle de naissance réalise des podcasts. Il se plaint de l’utilisation d’une souris « classique » car parfois lorsqu’il pense déplacer la souris horizontalement pour sélectionner un mot, il la déplace en diagonale et sélectionne plusieurs mots, plusieurs lignes. Il existe des souris adaptée mais leur prix est hors de sa portée car les aides ne couvrent pas la dépense à engager.
Le projet d’une souris adaptée est proposé au FabLab et accepté.
## L’approche du FabLab UtoPi
### Cahier des charges
#### Généralités
Au sein du **FabLab UtoPi** se crée une équipe qui va se consacrer au développement de la souris adaptée. Au vu des prix pratiqués pour ce genre de matériel (~700 à 800€), le premier élément pris en compte est le coût. Il est décidé de limiter le coût de la souris aux alentours de 50€ maxi pour la mettre à la portée d’un maximum de personnes.

#### Choix du microcontrôleur
Au sein du **FabLab UtoPi** plusieurs possibilités de développement existent. Les microcontrôleurs utilisés sont le STM32, la famille des PIC, Arduino et Raspberry Pi PICO. 
En raison des possibilités de programmation en MicroPython du Raspberry Pi PICO, ce qui le rend accessible à un plus large nombre d’utilisateurs (le langage Python est le langage choisi par l’Éducation Nationale pour les lycées), c’est ce modèle qui a été choisi. Son prix autour de 5€ permet de conserver un prix raisonnable pour les souris produites.

#### Déplacement du curseur
<img align="left" src="https://github.com/FabLabUtoPi/Souris/assets/172394416/01e57f6c-cd12-442f-93f3-072081b24ce8" width="200" height="168" />
Pour limiter les déplacements aux directions HAUT, BAS, DROITE et GAUCHE, le choix s’est porté sur un joystick. Celui-ci permet de plus une adaptation en cas de problème de préhension. Les tests avec un joystick analogique (avec des potentiomètres) et un numérique (avec des switch) ont abouti au choix de la version numérique.
Si l’utilisateur déplace le joystick en diagonale (volontairement ou par inadvertance), il sera averti par un vibreur intégré à la souris, qui fournit un retour haptique.

#### Boutons additionnels
<p align="center"><img align="left" src="https://github.com/FabLabUtoPi/Souris/blob/main/images/snapshot_07.jpg" width="200" height="168" /></p>
Lorsque le joystick sera maintenu en position un certain temps (programmable), le curseur sur l’écran se déplacera automatiquement dans la direction choisie. 
Boutons additionnels
La souris sera dotée de 5 boutons placés devant le joystick. Selon les retours d’expérience, ce nombre pourra être modifié ainsi que les emplacements. Les fonctions retenues pour ces boutons sont : Clic gauche, clic droit, appel d’un logiciel (programmable, par défaut NVDA), roulette UP, roulette DOWN.

#### Le retour haptique
<img align="left" src="https://github.com/FabLabUtoPi/Souris/blob/main/images/vibreur.jpg" width="200" height="168" />
Pour assurer un retour haptique (tactile), la souris sera munie d’un vibreur. C’est un moteur miniature qui entraîne une masselotte excentrée et produit des vibrations. Ce genre de vibreur équipe les tablettes et les smartphones. Le vibreur pourra signaler des actions comme le déplacement en diagonale, confirmer l’activation d’une touche…
Une action lors de la connexion de la souris (appui sur touche ou combinaison de touches) permettra de dévalider l’utilisation du retour haptique.

#### Retour auditif
<img align="left" src="https://github.com/FabLabUtoPi/Souris/blob/main/images/buzzer.jpg" width="150" height="168" />
Un retour auditif (sous forme de clic ou de bip) est envisagé avec la présence d’un buzzer activé par une des sorties du Raspberry Pi PICO. 
Une action lors de la connexion de la souris (appui sur touche ou combinaison de touches) permettra de dévalider l’utilisation du retour auditif.  

#### Sortie du programme
La programmation du Raspberry Pi PICO se fait via la connexion USB. Une combinaison touche/joystick sera prévue pour arrêter le programme et donner accès au microcontrôleur pour pouvoir modifier le programme.
Combinaison prévue : Touche centrale + touche la plus à droite + joystick en BAS. Si cette combinaison est activée en cours de programme, le programme allume les LEDs des 5 touches, envoie sur le port console un message d’avertissement, puis s’arrête. Cela permet au développeur de reprendre la main pour apporter plus facilement des modifications. Sur les modèles définitifs cette fonction pourra être dévalidé.  

## Réalisation technique
### Brochage du Raspberry Pi PICO
<img align="left" src="https://github.com/FabLabUtoPi/Souris/blob/main/images/pinout_PICO.jpg" width="1050" height="560" />  
Le Raspberry Pi PICO expose ses Entrées/Sorties GPIO comme ci-dessus. Le choix a été fait d’utiliser la partie gauche de la carte pour connecter les différents matériels utilisés (switch, LEDs, vibreur et buzzer). Les bornes de masse (GND) intercalées permettent de connecter la masse aux endroits souhaités.
La partie droite comporte une dizaine de GPIO supplémentaires, dont des possibilités d’Entrée Analogique qui pourront éventuellement être utilisées pour des développements futurs.\\\

### Schéma global de la souris adaptée
<img align="left" src="https://github.com/FabLabUtoPi/Souris/blob/main/images/schema_global.jpg" width="1050" height="760" />

Le schéma montre la connexion des LEDs (GP0 à GP4), des 5 boutons poussoirs (GP5 à GP9) et du joystick (GP10 à GP13). 
Le vibreur est connecté à la sortie GP14, et le buzzer à la sortie GP15.
La sortie GP15 active le vibreur. La diode anti retour aux bornes du moteur est nécessaire avec le moteur utilisé.

### Plaque support des boutons poussoirs
<img align="left" src="https://github.com/FabLabUtoPi/Souris/blob/main/images/plaque_8x2cm.jpg" width="670" height="189" />
La plaque support des boutons poussoirs choisie est un modèle de carte prototype double face universel. Pour la version définitive on pourra envisager la fabrication d’un PCB (circuit imprimé) sur mesure et plus adapté. Mais pour le prototype, cette solution était la plus rapidement mise en œuvre.

### Câblage des Boutons poussoirs
<img align="left" src="https://github.com/FabLabUtoPi/Souris/blob/main/images/Switch.png" width="1150" height="700" />
Les boutons poussoirs sont documentés ci-dessus. En position repos, les broches 1 et 3 sont reliées (position NF = Normalement Fermé). Quand on appuie sur le bouton poussoir 1-3 s’ouvre et 1-2 se ferme (NO = Normalement ouvert).
La LED est connectée aux bornes 5 (anode) et 6 (cathode). Il conviendra d’ajouter une résistance en  série avec la LED pour protéger la sortie du Raspberry Pi PICO. Cette résistance vaudra au minimum 220 Ω, une valeur supérieure réduira la luminosité de la LED.
<img align="left" src="https://github.com/FabLabUtoPi/Souris/blob/main/images/connexion_BP.jpg" width="1050" height="450" />

Le câblage des boutons poussoirs et des LEDs est ici représenté vu de dessous. Sur la plaque prototype, des fils ont été soudés et relient les différents éléments (voir photo)

### Câblage du joystick
<img align="center" src="https://github.com/FabLabUtoPi/Souris/blob/main/images/cablage_joystick.jpg" width="820" height="800" />
Nota : En fonction de la position de montage du joystick, il faudra éventuellementadapter le programme.  

Le câblage du joystick ne pose pas de problème particulier. Lorsque l’utilisateur pousse le manche du joystick dans une direction, le switch concerné établit un contact entre les bornes COM et NO.  

### Connexion du vibreur au Raspberry Pi PICO
<img align="center" src="https://github.com/FabLabUtoPi/Souris/blob/main/images/connexion_vibreur.jpg" width="1000" height="390" />  
La sortie GP14 du Raspberry Pi PICO ne peut pas fournir le courant nécessaire pour actionner le moteur du vibreur (~ 200 mA max.). Un transistor 2N222 ou équivalent reçoit le signal et commande le vibreur.

# Modélisation 3D du boîtier de la souris
<img align="center" src="https://github.com/FabLabUtoPi/Souris/blob/main/Mod%C3%A8les_3D/souris_04.jpg" width="1000" height="390" />  

La modélisation a été faite avec Fusion 360. Les fichiers sont disponibles dans le dossier Modèles_3D

# Logiciel de Gestion de la souris
## Choix du micrologiciel
Le micro-logiciel installé sur la souris est Circuit Python. Python est le langage de programmation qui connaît la plus forte croissance. Il est enseigné dans les lycées et les universités. C'est un langage de programmation de haut niveau, ce qui signifie qu'il est conçu pour être facile à lire, à écrire et à maintenir. Il prend en charge les modules et les paquets, ce qui signifie qu'il est facile de réutiliser un code existant pour d'autres projets. Il dispose d'un interpréteur intégré, ce qui signifie qu'il n'y a pas d'étapes supplémentaires, comme la compilation, pour faire fonctionner le code qui a été écrit. De plus , Python est un logiciel libre, ce qui signifie que tout le monde peut l'utiliser, le modifier ou l'améliorer
CircuitPython ajoute la prise en charge du matériel à toutes ces caractéristiques du langage Python. Si quelqu’un a déjà des connaissances en Python, il peut facilement les appliquer à l'utilisation de CircuitPython. Si l’utilisateur n'a aucune expérience préalable, il est très simple de commencer avec ce langage ! La version de Circuit Python est adaptée au modèle de carte à programmer. Dans notre cas c’est [la version 8.2.7](https://circuitpython.org/board/raspberry_pi_pico/)  qui était disponible pour le Raspberry Pi PICO au moment de la création du prototype. 
<img align="left" src="https://github.com/FabLabUtoPi/Souris/blob/main/images/circuit_Python.jpg" width="1000" height="700" />
(source [circuitpython.org](https://circuitpython.org/))
## Installation de Circuit Python
A partir de la page ci-dessus, sélectionnez la langue (French), et téléchargez le micrologiciel. Il est disponible au format .uf2. 
Commencez avec le Raspberry Pi PICO débranché. Appuyez sur le bouton BOOTSEL du Raspberry Pi PICO et connectez la prise USB . Maintenez le bouton appuyé jusqu’à ce qu’une fenêtre RPI-RP2 s’ouvre sur le bureau. Relâchez le bouton BOOTSEL. On accède maintenant à la mémoire du Raspberry Pi PICO comme si c’était une clé USB.  
**Nota :** _Cette opération n’aboutira pas si vous utilisez un câble de charge seule. Vérifiez bien que vous utilisez un câble de données. Si la fenêtre RPI-RP2 n’apparaît pas après un long moment, vérifiez les points indiqués et recommencez l’opération._\
<img align="center" src="https://github.com/FabLabUtoPi/Souris/blob/main/images/circuit_Python_02.jpg" width="900" height="360" />  

Ouvrez une fenêtre sur le dossier où est enregistré Circuit Python et faites le glisser dans la fenêtre RPI-RP2.  

<img align="center" src="https://github.com/FabLabUtoPi/Souris/blob/main/images/circuit_Python_03.jpg" width="850" height="300" />  
Répondez OK à la demande du système.\

<img align="center" src="https://github.com/FabLabUtoPi/Souris/blob/main/images/circuit_Python_04.jpg" width="800" height="380" /> 

Le fichier est copié dans la mémoire du Raspberry Pi PICO. A la fin du transfert, la fenêtre RPI-RP2 disparaît et le Raspberry Pi PICO redémarre en utilisant circuit Python. La LED interne du Raspberry Pi PICO, située près de la prise USB, clignote une fois toutes les 5 secondes environ.  

**Nota :** _Si votre Raspberry Pi PICO se retrouve dans un état vraiment bizarre et ne s'affiche même pas comme un lecteur de disque lors de l'installation de CircuitPython, essayez d'installer le fichier .uf2 "nuke" qui fera un "nettoyage en profondeur" de votre mémoire flash. Vous perdrez tous les fichiers de la carte, mais au moins vous pourrez reprendre la main ! Après le nettoyage, réinstallez CircuitPython._  

Lien vers le fichier de nettoyage [flash_nuke.uf2](https://cdn-learn.adafruit.com/assets/assets/000/099/419/original/flash_nuke.uf2?1613329170).  

# Installation de Mu
Mu est un éditeur Python simple pour les débutants. C’est l’interface préconisé par Adafruit pour travailler avec Circuit Python.
<img align="center" src="https://github.com/FabLabUtoPi/Souris/blob/main/images/circuit_Python_06.jpg" width="900" height="814" /> 
Rendez vous sur [la page de l’éditeur Mu](https://codewith.mu/) et téléchargez (Download) la version correspondant à votre système d’exploitation. Si vous êtes sous Windows, désinstallez les anciennes versions de Mu existant sur votre machine. Installez Mu sur votre machine.
L’installation et le démarrage sont un peu longs, soyez patient.
Au premier démarrage, si la carte Raspberry Pi PICO n’est pas connectée, il faudra choisir le mode de fonctionnement Circuit Python pour Mu.  
Si vous laissez la carte Raspberry Pi PICO, préparée avec Circuit Python, connectée, Mu la détecte et demande si vous voulez passer en mode Circuit Python. Répondez OUI.
<img align="center" src="https://github.com/FabLabUtoPi/Souris/blob/main/images/circuit_Python_07.jpg" width="900" height="520" /> 
Mu est prêt à être utilisé. On peut le tester avec un Hello World :  

Cliquez sur l’icône Serial, dans la console tapez CTRL + B pour passer en mode REPL. Tapez le code   

print(« Hello World ! »)  

Quand vous tapez sur la touche ENTRÉE la commande est exécutée.  
<img align="center" src="https://github.com/FabLabUtoPi/Souris/blob/main/images/circuit_Python_08.jpg" width="900" height="122" />  

Lorsqu’un programme fonctionne dans un boucle infinie, placez vous dans la fenêtre de la console Circuit Python REPL, puis tapez CTRL + C. Un message vous demande de taper sur une touche quelconque pour reprendre la main :  

<img align="center" src="https://github.com/FabLabUtoPi/Souris/blob/main/images/circuit_Python_09.jpg" width="900" height="230" />  

# Cahier des charges logiciel

Le logiciel écrit en Python doit émuler une souris « classique ». Les déplacement privilégiés sont en X et Y, des boutons poussoirs remplacent les boutons Droit et Gauche, ainsi que la roulette. Un bouton programmable permet de déclencher le lancement d’un programme particulier (NVDA, par exemple).
Un retour haptique (vibreur) et sonore (buzzer) permettent de signaler certaine situations à l’utilisateur.  

## Bibliothèque utilisée
La bibliothèque utilisée pour émuler la souris et le clavier est la bibliothèque s’appelle adafruit_hid (HID = Human Interface Device). Téléchargez la bibliothèque sur la page Github [https://github.com/adafruit/Adafruit_CircuitPython_HID](https://github.com/adafruit/Adafruit_CircuitPython_HID), en cliquant sur le bouton vert CODE puis Download ZIP. Dézippez l’archive. Dans le dossier Adafruit_CircuitPython_HID-main créé lors de l’extraction de l’archive, copiez le dossier adafruit_hid qui contient la librairie pour gérer le clavier et la souris. Collez ce dossier dans le dossier lib du Raspberry Pi PICO.  

<img align="center" src="https://github.com/FabLabUtoPi/Souris/blob/main/images/circuit_Python_11.jpg" width="900" height="360" /> 

## Description du logiciel souris_v4.py - Rubrique Programmes
Le logiciel de la souris est fourni sous licence open source MIT. 
Les différentes connexions sont définies ainsi :

La position x=0, y=0 pour la souris est en haut à gauche de l'écran
### Connexion des switchs
|   Action    |      |   GPIO  |  
|---    |---    |---    | 
|   UP    |   Souris vers le haut    |   GP12    |  
|   DOWN    |   Souris vers le bas    |    GP13   |       
|   RIGHT    |   Souris vers la gauche    |   GP10    |      
|   LEFT    |    Souris vers la droite   |  GP11     |      
|   |   |   |                              
| GAUCHE  | Appui bouton gauche  | GP5  |                              
| DROITE  | Appui bouton droit  | GP6  |                              
|   |   |   |                              
| PROG  | Lancement programme  | GP7  |                              
|   |   |   |                              
| Wheel UP  | Roulette vers le haut  | GP8  |                              
| Wheel DOWN  | Roulette vers le bas  | GP9  |  

### Connexion des LEDs
|   LED    |  Bouton    |   GPIO  |  
|---    |---    |---    | 
| DROITE  | Bouton droit  | GP0  |                              
| GAUCHE  | Bouton gauche  | GP1  |                              
| PROG  | Lancement programme  | GP2  |                              
| Wheel UP  | Roulette vers le haut  | GP3  |                              
| Wheel DOWN  | Roulette vers le bas  | GP4  |  

| Action  |   | GPIO  |                              
|---   |---   |---   |
| Vibreur  |   | GP14  |                              
| Buzzer  |   | GP15  |                              
                              
A la mise sous tension les LEDs clignotent pour montrer que le programme démarre. Si l'utilisateur ne peut pas voir cette séquence, elle est utile pour la personne qui monte et teste la souris. De même le vibreur est actionné deux fois rapidement.

Si le joystick est manipulé pour bouger la souris en diagonale, une vibration avertit l'utilisateur.
Les touches peuvent être programmées à la demande de l'utilisateur en fonction des logiciels qu'il utilise.
Par défaut elles sont programmées comme suit, de gauche à droite
- Bouton gauche de la souris (clic gauche)
- Bouton droit de la souris (clic droit)
- Ouverture du menu Windows
- Défilement roulette vers le haut
- Défilement roulette vers le bas

# Choix de la licence du logiciel embarqué
Le Logiciel est publié sous licence MIT : _La licence MIT est une licence de logiciel pour logiciels libres1 et open source2, provenant de l'Institut de technologie du Massachusetts (MIT) à la fin des années 1980. Cette licence de logiciel permissive implique très peu de limitations sur la réutilisation du code et elle est ainsi compatible avec de nombreuses autres licences. 
MIT License_ [(source Wikipedia)](https://fr.wikipedia.org/wiki/Licence_MIT)

Copyright (c) 2024 FabLabUtoPi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:  

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.  

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

# Sécurité du logiciel embarqué
Le logiciel n’ayant pas d’interaction avec les logiciels des autres machines, il n’apparait pas de problème de sécurité spécifique

# Liens vers les composants (valable en septembre 2023)
[Carte 8x2 cm pour le câblage des boutons](https://s.click.aliexpress.com/e/_DdNWyrd)  
[Boutons poussoirs avec LED intégrée](https://s.click.aliexpress.com/e/_DdBT0JN)  
[Vibreur pour le retour haptique](https://s.click.aliexpress.com/e/_DFjq7wf)  
[Joystick à 4 axes numériques (switch) sans bouton poussoir central](https://fr.aliexpress.com/item/1005001832652034.html)  
[Joystick à 4 axes numériques (switch) avec bouton poussoir central](https://s.click.aliexpress.com/e/_Dmqzrnh)  


