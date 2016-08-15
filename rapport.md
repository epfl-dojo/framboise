# Rapport de projet

## Introduction
Ce projet a pour but de faire un timer de 5 minutes pour le dojo. Le dojo est une séance de programmation en communauté où chacun code par tour de 5 minutes sur un projet commun hébergé sur un laptop qui se passe de personne en personne. Cet appareil doit être fait à partir d'un raspberry pi et fonctionner grâce à une batterie.

L'objectif est d'avoir un timer *portable* de 5 minutes dont la majorité des fonctions sont couvertes par un seul bouton (le fameux buzzer). Ces fonctions sont le démarrage, la pause et la réinitialisation. Un deuxième bouton de type on/off se charge d'allumer et éteindre l'appareil simplement en enclanchant ou en coupant l'alimentation. Le temps restant s'affiche sur un écran tft C-Berry. Au terme des 5 minutes une alarme s'enclenche. Une fois l'alarme enclenchée une pression de réinitialisation (pression longue) le remet à 5 minutes.

Nous utilisons raspian comme système d'exploitation car c'est un système léger tournant avec un noyau linux qui contient des outils nécessaires au développement en python et à la compatibilité raspberry pi. Nous avons programmé dans le langage python car c'est un langage qui fonctionne facilement sur un raspberry pi. De plus ce langage nécessite une utilisation rigoureuse des retour à la ligne et des tabulation ce qui rend le code plus lisible. Nous avons également fait un script bash qui permet de transformer n'importe quel raspberry pi connecté au matériel nécessaire en timer.

## Journal


## Matériel utilisé
- *Raspberry pi 3 de modèle B*  Nous avons choisi d'utiliser un raspberry pi pour ce projet car il allie compacité, performance et facilité d'utilisation et personnalisation.

- *Ecran TFT C-Berry* Nous avons choisi cet écran car c'est le moins cher des écrans pour raspberry pi et c'est suffisant. Petit bémol: se programme en C.

- *Carte SD 8 Gb* C'est la carte recommandée avec un raspberry pi qui a déjà raspian pré-installé. Les 8 Gb sont suffisants mais ne laissent pas beaucoup de marge de maneuvre.

- *Speaker*

- *Câble jack*

- *Batterie externe*

- *Bouton buzzer*

- *Bouton on/off*

- *Boîtier en aluminium* C'est un boîtier fait sur mesure grâce à la coopération avec un polymécanicien.

## Documentation

## Synthèse
