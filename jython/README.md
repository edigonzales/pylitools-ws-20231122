## Jython installieren

```
wget https://repo1.maven.org/maven2/org/python/jython-installer/2.7.3/jython-installer-2.7.3.jar
```

```
java -jar jython-installer-2.7.3.jar
```

Falls Multipass verwendet wird, wird kein GUI angezeigt. Als target-Verzeichnis _/home/ubuntu/apps/jython/_ eintippen.

Das _bin_-Verzeichnis der PATH-Umgebungsvariable hinzufügen (z.B. in _.bashrc_):

```
export PATH=$PATH:/home/ubuntu/apps/jython/bin
```

```
jython --help
```

## Virtualenv installieren

Es muss eine kompatible Version installiert werden:
```
jython -m pip install virtualenv==15.2.0
```

## Virtualenv erstellen

Ins _pylitools/jython_-Verzeichnis wechseln.

```
cd pylitools/jython
```

