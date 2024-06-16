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
<img align="left" src="https://github.com/FabLabUtoPi/Souris/blob/main/images/Switch.png" width="1150" height="800" />
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


# Logiciel de Gestion de la souris


# Choix du micrologiciel
Le micro-logiciel installé sur la souris est Circuit Python. Python est le langage de programmation qui connaît la plus forte croissance. Il est enseigné dans les lycées et les universités. C'est un langage de programmation de haut niveau, ce qui signifie qu'il est conçu pour être facile à lire, à écrire et à maintenir. Il prend en charge les modules et les paquets, ce qui signifie qu'il est facile de réutiliser un code existant pour d'autres projets. Il dispose d'un interpréteur intégré, ce qui signifie qu'il n'y a pas d'étapes supplémentaires, comme la compilation, pour faire fonctionner le code qui a été écrit. De plus , Python est un logiciel libre, ce qui signifie que tout le monde peut l'utiliser, le modifier ou l'améliorer
CircuitPython ajoute la prise en charge du matériel à toutes ces caractéristiques du langage Python. Si quelqu’un a déjà des connaissances en Python, il peut facilement les appliquer à l'utilisation de CircuitPython. Si l’utilisateur n'a aucune expérience préalable, il est très simple de commencer avec ce langage ! La version de Circuit Python est adaptée au modèle de carte à programmer. Dans notre cas c’est [la version 8.2.7](https://circuitpython.org/board/raspberry_pi_pico/)  qui était disponible pour le Raspberry Pi PICO au moment de la création du prototype. 
<img align="left" src="https://github.com/FabLabUtoPi/Souris/blob/main/images/circuit_Python.jpg" width="1000" height="700" />
(source [circuitpython.org](https://circuitpython.org/))
## Installation de Circuit Python
A partir de la page ci-dessus, sélectionnez la langue (French), et téléchargez le micrologiciel. Il est disponible au format .uf2. 
Commencez avec le Raspberry Pi PICO débranché. Appuyez sur le bouton BOOTSEL du Raspberry Pi PICO et connectez la prise USB . Maintenez le bouton appuyé jusqu’à ce qu’une fenêtre RPI-RP2 s’ouvre sur le bureau. Relâchez le bouton BOOTSEL. On accède maintenant à la mémoire du Raspberry Pi PICO comme si c’était une clé USB.
**Nota :** Cette opération n’aboutira pas si vous utilisez un câble de charge seule. Vérifiez bien que vous utilisez un câble de données. Si la fenêtre RPI-RP2 n’apparaît pas après un long moment, vérifiez les points indiqués et recommencez l’opération. 
<img align="center" src="https://github.com/FabLabUtoPi/Souris/blob/main/images/circuit_Python_02.jpg" width="800" height="360" />  

Ouvrez une fenêtre sur le dossier où est enregistré Circuit Python et faites le glisser dans la fenêtre RPI-RP2.  

<img align="center" src="https://github.com/FabLabUtoPi/Souris/blob/main/images/circuit_Python_03.jpg" width="800" height="300" />  




