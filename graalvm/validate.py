import java
import os

files = os.listdir(os.path.join(".venv", "javalib"))
for file in files:
    if file.endswith("jar"):
        #print(os.path.join(".venv", "javalib", file))
        java.add_to_classpath(os.path.join(".venv", "javalib", file))

Settings = java.type("ch.ehi.basics.settings.Settings")
Validator = java.type("org.interlis2.validator.Validator")

settings = Settings()
settings.setValue(Validator.SETTING_LOGFILE, "validation.log")
settings.setValue(Validator.SETTING_XTFLOG, "validation.log.xtf")

valid = Validator.runValidation(["ch.so.agi.av.inventar_kantonsgrenzzeichen.xtf"], settings)

print(valid)