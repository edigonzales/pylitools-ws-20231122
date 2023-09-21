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

## Virtualenv erstellen und aktivieren

Ins _pylitools/jython_-Verzeichnis wechseln.

```
cd pylitools/jython
```

Virtualenv erstellen und weitere Abhängigkeiten herunterladen:
```
jython -m virtualenv --no-pip --no-wheel .jenv
.jenv/bin/easy_install pip==19.1.1
.jenv/bin/pip install -U setuptools==44.1.1
```

Die Versionen müssen kompatibel mit der von Jython implementierten Python-Version sein.

Virtualenv aktivieren:
```
source .jenv/bin/activate
```

In der Konsole (Multipass-Ubuntu) erkennt mit die Virtualenv:

```
(.jenv) ubuntu@pylitools:~/pylitools/jython$
```

Und `which jython` zeigt den korrekten Pfad:

```
/home/ubuntu/pylitools/jython/.jenv/bin/jython
```

## Einfaches Python-Skript ausführen

```
jython hello.py
```

Weil immer eine JVM gestartet werden muss, dauert das Ausführen des Skriptes länger.

## Java-Klassen in Python-Skript verwenden

```
jython hello_java.py
```

## Ilivalidator in Python-Skript verwenden

```
jython validate.py
```

Die ilivalidator-Bibliothek(en) werden nicht gefunden:

```
Traceback (most recent call last):
  File "validate.py", line 1, in <module>
    from ch.ehi.basics.settings import Settings
ImportError: No module named ch
```

Jip (pip für Java-Dependencies) installieren:

```
pip install jip
```

Es muss eine Konfigurationsdatei _.jip_config_ für _jib_ im Verzeichnis _$VIRTUAL_ENV_ (_.jenv/_) erstellt werden und folgender Inhalt reinkopiert werden:

```
[repos:ilitools]
uri=https://jars.interlis.ch
type=remote

[repos:central]
uri=https://repo1.maven.org/maven2/
type=remote

[repos:local]
uri=~/.m2/repository/
type=local
```

Anschliessend kann die "top level"-Java-Bibliothek installiert werden:

```
jip install ch.interlis:ilivalidator:1.13.3
```

Die Jar-Dateien werden heruntergeladen. Ganz zum Schluss erscheint eine Fehlermeldung, die aber nicht relevant ist:

```
jip [Finished] dependencies resolved
Error in atexit._run_exitfuncs:
Traceback (most recent call last):
  File "/home/ubuntu/apps/jython/Lib/atexit.py", line 24, in _run_exitfuncs
    func(*targs, **kargs)
  File "/home/ubuntu/apps/jython/Lib/site-packages/urllib3/packages/backports/weakref_finalize.py", line 133, in _exitfunc
    gc.disable()
NotImplementedError: can't disable Java GC
Error in sys.exitfunc:
Traceback (most recent call last):
  File "/home/ubuntu/apps/jython/Lib/atexit.py", line 24, in _run_exitfuncs
    func(*targs, **kargs)
  File "/home/ubuntu/apps/jython/Lib/site-packages/urllib3/packages/backports/weakref_finalize.py", line 133, in _exitfunc
    gc.disable()
NotImplementedError: can't disable Java GC
```

Überprüfen, ob alle Jars vorhanden sind:
```
ls -la .jenv/javalib
```

Das ilivalidator-Python-Skript nochmals ausführen:
```
jython validate.py
```

Man muss den CLASSPATH mit den soeben heruntergeladenen Java-Klassen ergänzen. Das kann ein Shell-Skript übernehmen:

```
#! /bin/bash

JYTHON_CMD="jython"
JAVA_LIBS="$VIRTUAL_ENV/javalib/*.jar"
PYTHON_PATH=""

for lib in $JAVA_LIBS
do PYTHON_PATH="$PYTHON_PATH:$lib"
   CLASSPATH="$CLASSPATH:$lib"
done

export CLASSPATH

$JYTHON_CMD -Dpython.path=$PYTHON_PATH "$@"
```

Mit `jip` wurde dieses Skript installiert (_jython_all_) installiert, muss aber noch ausführbar gemacht werden.
```
chmod +rx .jenv/bin/jython-all
```

```
jython-all validate.py
```

Und es funktioniert.

## Minimaler Validator-Webservice mit Flask

Flask installieren:
```
pip install Flask
```

Webservice starten:
```
jython-all webservice.py
```

Falls in einer VM gearbeitet wird, muss diese ggf so konfiguriert werden, dass man via Browser auf sie zugreifen kann. Die IP mit Multipass kann man wie folgt herausfinden:
```
multipass list
```

Anschliessend z.B. `http://192.168.64.2:5001/`. Falls alles lokal ausgeführt wird, reicht `http://0.0.0.0:5001/`.