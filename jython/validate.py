from ch.ehi.basics.settings import Settings
from org.interlis2.validator import Validator

settings = Settings()
settings.setValue(Validator.SETTING_LOGFILE, "validation.log")
settings.setValue(Validator.SETTING_XTFLOG, "validation.log.xtf")

valid = Validator.runValidation(["ch.so.agi.av.inventar_kantonsgrenzzeichen.xtf"], settings)

print valid