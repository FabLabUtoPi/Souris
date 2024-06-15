Souris
Projet Souris - Lauréat ANCT
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
<img align="left" src="https://github.com/FabLabUtoPi/Souris/blob/main/images/snapshot_07.jpg" width="200" height="168" />
Lorsque le joystick sera maintenu en position un certain temps (programmable), le curseur sur l’écran se déplacera automatiquement dans la direction choisie. 
Boutons additionnels
La souris sera dotée de 5 boutons placés devant le joystick. Selon les retours d’expérience, ce nombre pourra être modifié ainsi que les emplacements. Les fonctions retenues pour ces boutons sont : Clic gauche, clic droit, appel d’un logiciel (programmable, par défaut NVDA), roulette UP, roulette DOWN.

#### Le retour haptique
<img align="left" src="https://github.com/FabLabUtoPi/Souris/blob/main/images/vibreur.jpg" width="200" height="168" />
Pour assurer un retour haptique (tactile), la souris sera munie d’un vibreur. C’est un moteur miniature qui entraîne une masselotte excentrée et produit des vibrations. Ce genre de vibreur équipe les tablettes et les smartphones. Le vibreur pourra signaler des actions comme le déplacement en diagonale, confirmer l’activation d’une touche…
Une action lors de la connexion de la souris (appui sur touche ou combinaison de touches) permettra de dévalider l’utilisation du retour haptique.

#### Retour auditif
<img align="left" src="https://github.com/FabLabUtoPi/Souris/blob/main/images/buzzer.jpg" width="200" height="168" />
Un retour auditif (sous forme de clic ou de bip) est envisagé avec la présence d’un buzzer activé par une des sorties du Raspberry Pi PICO. 
Une action lors de la connexion de la souris (appui sur touche ou combinaison de touches) permettra de dévalider l’utilisation du retour auditif.
