# Native

Mit Java und GraalVM wird eine shared lib ("dll") aus den ilivalidator-Klassen hergestellt. Ergänzend braucht es Python-Bindings für diese shared lib. Das daraus resultierende Python-Modul kann wie jedes andere Python-Modul verwendet werden. Java wird nicht mehr benötigt. 

- https://github.com/pylitools/ilivalidator
- https://github.com/pylitools/ilivalidator/blob/main/java-lib/src/main/java/ch/so/agi/ilivalidator/libnative/IlivalidatorLib.java
- https://github.com/pylitools/ilivalidator/blob/main/ilivalidator/ilivalidator.py

## Shared lib erzeugen

GraalVM installieren:

```
sdk i java 21-graalce
sdk u java 21-graalce
```

```
git clone https://github.com/pylitools/ilivalidator
```

```
cd ilivalidator/java-lib/
```

Abhängigkeiten installieren:
```
sudo apt-get update 
sudo apt-get install gcc zlib1g-dev build-essential
```

Kompilieren:
```
./gradlew clean test nativeCompile
```

## Python installieren

Ubuntu:
```
sudo apt update
sudo apt install python3-pip
sudo apt install python3.10-venv
```

Im Multipass-Image muss nur `venv` installiert werden:

```
sudo apt install python3.10-venv
```

Oder man kann auch die GraalPy-Implementierung verwenden. 

## Venv erstellen
Falls vorgängig das Jython-Beispiel durchgespielt wurde, muss Jython wieder aus dem PATH entfernt werden (z.B. _.bashrc_).

```
python3 -m venv .venv
```

Und aktivieren:
```
source .venv/bin/activate
```

## ilivalidator Python-Modul installieren
```
pip install ilivalidator==0.0.4
```

Zum Modul gehört die shared library, die ebenfalls heruntergeladen wird.

## Ilivalidator in Python-Skript verwenden
```
python3 validate.py
```

## Minimaler Validator-Webservice mit Flask

Flask installieren:
```
pip install Flask
```

Webservice starten:
```
python3 webservice.py
```

Falls in einer VM gearbeitet wird, muss diese ggf so konfiguriert werden, dass man via Browser auf sie zugreifen kann. Die IP mit Multipass kann man wie folgt herausfinden:
```
multipass list
```

Anschliessend z.B. `http://192.168.64.2:5001/`. Falls alles lokal ausgeführt wird, reicht `http://0.0.0.0:5001/`.