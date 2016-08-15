# Rapport de projet

## Description du projet
Ce projet a pour but de faire un timer de 5 minutes pour le dojo. Le dojo est une séance de programmation en communauté où chacun code par tour de 5 minutes sur un projet commun hébergé sur un laptop qui se passe de personne en personne. Cet appareil doit être fait à partir d'un raspberry pi et fonctionner grâce à une batterie.

L'objectif est d'avoir un timer *portable* de 5 minutes dont la majorité des fonctions sont couvertes par un seul bouton (le fameux buzzer). Ces fonctions sont le démarrage, la pause et la réinitialisation. Un deuxième bouton de type on/off se charge d'allumer et éteindre l'appareil simplement en enclanchant ou en coupant l'alimentation. Le temps restant s'affiche sur un écran tft C-Berry. Au terme des 5 minutes une alarme s'enclenche. Une fois l'alarme enclenchée une pression de réinitialisation (pression longue) le remet à 5 minutes.

Nous utilisons raspian comme système d'exploitation car c'est un système léger tournant avec un noyau linux qui contient des outils nécessaires au développement en python et à la compatibilité raspberry pi. Nous avons programmé dans le langage python car c'est un langage qui fonctionne facilement sur un raspberry pi. De plus ce langage nécessite une utilisation rigoureuse des retour à la ligne et des tabulation ce qui rend le code plus lisible. Nous avons également fait un script bash qui permet de transformer n'importe quel raspberry pi connecté au matériel nécessaire en timer.

## Journal

Le projet s'est déroulé sur une période d'environ 5 mois, nous avons planifié de nous rencontrer 2 fois par semaine (lundi et vendredi), pour une durée de 4 heures (séances de 2 heures chacunes).
Voici le récapitulatif du travail effectué lors des séances:

| Date     |     Travail effectué      |
|----------|:-------------------------:|
| 29.04.16 | Rédaction du cahier des charges |
| 02.05.16 | Rédaction du cahier des charges |
| 13.05.16 | Installation, configuration des outils, Code python permetttant l'interaction entre le bouton et le raspberry)|
| 20.05.16 | Présentation du cahier des charges aux formateurs |
| 27.05.16 | Développement de l'interface du minuteur, essais d'interactions avec le bouton|
| 27.05.16 | Première discussion avec Sylvain, apprenti polymécanicien pour un projet de boitier pour notre minuteur|
| 31.05.16 | Recherche des composant manquant à notre projet |
| 03.06.16 | Tests de la sortie audio du raspberry, test de l'écran (ne fonctionne plus) |
| 07.06.16 | Recherche d'autres petits composant(câbles) et commande de la totalité |
| 13.06.16 | Envoi de plans des pièces à Sylvain |

Durant quelques semaines , (entre le 17.06.16 et le 15.07.16), nous nous sommes principalement concentrés
sur notre code, nous nous sommes vu plus souvent et nous avons réaliser une "semaine dévellopement" où nous
avons travaillé ensemble tous les jours (environ 1h30 - 2h par jour) sur notre code. 
Nous avons ainsi pu terminer le dévellopement
des interactions entre le timer(et son interface) et le bouton.

| Date     |     Travail effectué      |
|----------|:-------------------------:|
| 29.04.16 | Paufinage du code         |
| 15.08.16 | Rédaction du rapport de projet |

A suivre...
=======


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