# GraalPy

GraalPy ist eine Python-Implementierung. Dank GraalVM lässt sich damit Polyglot programmieren und es lassen sich neben anderen Sprachen Java-Klassen ausführen (ähnlich jython). 

## GraalPy installieren

Siehe https://github.com/oracle/graalpython/releases

```
wget https://github.com/oracle/graalpython/releases/download/graal-23.1.0/graalpy-community-jvm-23.1.0-linux-amd64.tar.gz
```

```
tar -xzf graalpy-community-jvm-23.1.0-linux-amd64.tar.gz -C /home/ubuntu/apps/
```
Es muss die "-jvm"-Version sein. Die non-community-Version dünkt mich broken.

Python im Pfad ergänzen, z.B. _.bashrc_. Falls vorgängig das Jython-Beispiel durchgespielt wurde, muss Jython wieder aus dem PATH entfernt werden:

```
which python
python --version
```

## Venv erstellen

```
python3 -m venv .venv
```

Und aktivieren:
```
source .venv/bin/activate
```

## Einfaches Python-Skript ausführen

```
python3 hello.py
```

Startup-Zeit sehr gut.

## Java-Klassen in Python-Skript verwenden

```
python3 hello_java.py
```

Upsi:
```
Traceback (most recent call last):
  File "/home/ubuntu/pylitools/graalvm/hello_java.py", line 1, in <module>
    import java
ModuleNotFoundError: No module named 'java'
```

```
graalpy hello_java.py
```

Es muss wieder eine JVM gestartet werden. Entsprechend ist die Startup-Zeit nicht mehr super toll.