# Joyeuse configuration tool

## Usage

For installing the dependencies, it is advised to use a venv, for example:

```sh
python -m venv ../venv
. ../venv/bin/activate
pip install --upgrade pip
pip install --requirement requirements.txt
```

From the cloned repository, one can then execute the program with either:

```sh
python3 -m joyeuse
```

or

```sh
./scripts/joyeuse.py
```

## Testing

It is possible to test how the program works by using the **example/copie**
instead of the path to a real joyeuse.
For example:

```sh
./scripts/joyeuse.py examples/copie
```

It is also possible to simulate the removal / insertion by moving the
**SETTINGS.txt** file, for example:

Removal:

```sh
mv examples/copie/Secrets/SETTINGS.txt{,.bak}
```

Insertion:

```sh
mv examples/copie/Secrets/SETTINGS.txt{.bak,}
```

## Generating redistributables

### pip

```sh
make pip
```

The resulting package will be in **dist/**.

### Generate a debian package

```sh
make debian
```

The generated packages is in the parent folder.

### Windows

```sh
make windows
```

Having a working environment 
