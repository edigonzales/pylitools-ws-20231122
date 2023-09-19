# pylitools-ws-20231122

## Vorbereitung

### Multipass
Mit [Multipass](https://multipass.run/install) können einfach und schnell Linux-VM erstellt werden.

VM (Ubuntu 22.04) erstellen und starten:
```
multipass launch jammy --cpus 4 --disk 20G --memory 8G --name pylitools
```

Verzeichnis mounten:
```
multipass mount $PWD pylitools:/home/ubuntu/pylitools
```

In VM einloggen:
```
multipass shell pylitools
```

VM stoppen:
```
multipass stop pylitools
```

VM definitiv löschen:
```
multipass delete --purge pylitools
```



- Multipass... oder auch nicht -> GraalVM geht ja ohne. Trotzdem als Backup-Lösung für Windows.
- Port forwarding muss gehen.