![continuous integration](https://github.com/ncarrier/joyeuse/actions/workflows/continuous_integration.yml/badge.svg?branch=master)

# fr - Outil de configuration de la conteuse Joyeuse

Cet outil permet de modifier les paramètres de la conteuse Joyeuse
(fichier **Secrets/SETTINGS.txt**).

## Installation

### Windows

Télécharger la [dernière version pour Windows][windows].

### Linux

### Ubuntu

Télécharger la dernière version pour Ubuntu 22.04 :

```sh
wget https://github.com/ncarrier/joyeuse/releases/latest/download/joyeuse-ubuntu-22.04.tar.gz
```

L'extraire :

```sh
tar xf joyeuse-ubuntu-22.04.tar.gz
```

L'installer :

```sh
sudo apt install ./joyeuse_*.deb
```

Une version pour Ubuntu 20.04 est également disponible, remplacer dans les
instructions précédentes, 22 par 20.

## Tous systèmes Windows ou Linux

Pour les utilisateurs ayant python installé, avec pip :

```sh
pip install joyeuse
```

## Utilisation

Lancer l'application en double-cliquant sur le fichier .exe sous Windows, ou en
entrant la commande :

```sh
joyeuse
```

sous Linux.

Puis brancher la conteuse, qui affichera les paramètres de configuration de la
conteuse.

## Compatibilité

Pour l'instant, le logiciel a été testé sous :

 * Windows
     * version 10
 * Linux
     * Debian 10 et 11 (via pip)
     * Ubuntu 20.04 et 22.04

## License

Ce logiciel est sous GPLv3, ou (en fonction de votre choix), n'importe quelle
version future.

Les personnes qui envoient des contributions, sous quelque forme que ce soit,
patch, pull request, conseil... Acceptent en le faisant, que leur propriété me
soit transférée à moi, **Nicolas Carrier**.
Ceci au moyen de l'ajout d'un sign-off aux commits.

## Autres

**Note** : Je n'ai aucun lien avec la société JOYEUSE qui fabrique cette
conteuse.

Pour plus d'information sur Joyeuse, rendez vous sur son
[site web][joyeuse].

# en - Joyeuse configuration tool

This tool is meant to configure the parameters of the Joyeuse
(**Secrets/SETTINGS.txt**).

## Installation

### Windows

Download [the latest Windows version][windows].

### Linux

### Ubuntu

Download the latest Ubuntu 22.04 version:

```sh
wget https://github.com/ncarrier/joyeuse/releases/latest/download/joyeuse-ubuntu-22.04.tar.gz
```

Extract it:

```sh
tar xf joyeuse-ubuntu-22.04.tar.gz
```

Install it:

```sh
sudo apt install ./joyeuse_*.deb
```

An Ubuntu 20.04 version is availe too, remplace 22 with 20 in the instructions
above.

## All Windows or Linux systems

For the users having python installed, with pip :

```sh
pip install joyeuse
```

## Utilisation

Launch the application with a double-click on the .exe, for Windows, or by
running:

```sh
joyeuse
```

under Linux.

Then plug the Joyeuse in, which will make its configuration parameters appear.

## Compatibility

For now, the software has been tested for:

 * Windows
     * version 10
 * Linux
     * Debian 10 and 11 (via pip)
     * Ubuntu 20.04 and 22.04

## License

This software is placed under the GPLv3, or (at your option) any later version.

People sending contributions under any form, patch, pull request, advice...
Accept by doing so, that their ownership gets transferred to me,
**Nicolas Carrier**.

## Others

**Note**: I am not related with the JOYEUSE company which builds the Joyeuse
storyteller.

For more information on Joyeuse, go to its [web site][joyeuse].

## What's next

Here is my tentative roadmap:

 * Version 1.0.0
     * Support of parameters control
 * Version 1.1.0
     * Implement a Tutorial tab, allowing to play the videos inside the
   'Tutos vidéo' folder
     * Internationalization
 * Version 1.2.0
     * Implement the Sound library, allowing to manage the sounds which can be
     uploaded to the Joyeuse
     * Implement the Music / Stories tab, allowing to add / remove sounds to the
     cube faces
 * Version 1.3.0
     * Implement a studio tab, allowing to record sound files

[joyeuse]: https://www.joyeuse.io/
[windows]: https://github.com/ncarrier/joyeuse/releases/latest/download/joyeuse.exe