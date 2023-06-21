# fr - Outil de configuration de la conteuse Joyeuse

Cet outil permet de modifier les paramètres de la conteuse Joyeuse
(fichier **Secrets/SETTINGS.txt**).

Son état actuel est très basique et il manque encore cruellement de
fonctionnalités.

## Utilisation

Brancher la conteuse, puis :

```sh
python3 -m joyeuse /chemin/vers/la/conteuse
```

Il est possible de tester son fonctionnement en utilisant le dossier
**example/copie** au lieu du chemin vers la conteuse.

## Générer un package pip

```sh
make pip
```

Le package généré se trouve dans **dist/**.

## Compatibilité

Pour l'instant, le logiciel n'a été testé que sous Linux (Debian 10).

## License

Ce logiciel est sous GPLv3, ou (en fonction de votre choix), n'importe quelle
version future.

Les personnes qui envoient des contributions, sous quelque forme que ce soit,
patch, pull request, conseil... Acceptent en le faisant, que leur propriété me
soit transférée à moi, **Nicolas Carrier**.

## Autres

**Note** : Je n'ai aucun lien avec la société JOYEUSE qui fabrique cette
conteuse.

Pour plus d'information sur Joyeuse, rendez vous sur son
[site web](https://www.joyeuse.io/).

# en - Joyeuse configuration tool

This tool is meant to configure the parameters of the Joyeuse
(**Secrets/SETTINGS.txt**).

Its current state is very basic and it's still severely lacking features.

## Usage

Plug the Joyeuse, then:

```sh
python3 -m joyeuse /path/to/the/joyeuse
```

It is possible to test how it works by using the **example/copie** instead of
the path to the joyeuse.

## Generate a pip package

```sh
make pip
```

The resulting package will be in **dist/**.

## Compatibility

For now, this software was only tested on Linux (Debian 10).

## License

This software is placed under the GPLv3, or (at your option) any later version.

People sending contributions under any form, patch, pull request, advice...
Accept by doing so, that their ownership gets transferred to me,
**Nicolas Carrier**.

## Others

**Note**: I am not related with the JOYEUSE company which builds the Joyeuse
storyteller.

For more information on Joyeuse, go to its [web site](https://www.joyeuse.io/).

## TODO

Here is my tentative TODO list, sorted by order of priorities (most priority
first):

 * Debian packaging
 * Windows packaging
 * Input parameters validation
 * Auto-detect of the device
 * Publication of 1.0.0
 * Implement a Tutorial tab, allowing to play the videos inside the
   'Tutos vidéo' folder
 * Implement the Sound library, allowing to manage the sounds which can be
   uploaded to the Joyeuse
 * Implement the Music / Stories tab, allowing to add / remove sounds to the
   cube faces
 * Internationalization
 * Implement a studio tab, allowing to record sound files

 * man page? cli? completion?
