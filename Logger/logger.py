#Log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL

def log(msg, level):
    """Def logger"""
    print("[", level, "]", msg)

def debug(msg):
    log(msg, "DEBUG")

def info(msg):
    log(msg, "INFO")

def info(msg):
    log(msg, "WARNING")

def info(msg):
    log(msg, "ERROR")

def info(msg):
    log(msg, "CRITICAL")

'''
log("Start script", "INFO")
debug("Mesaj") -> [DEBUG] Mesaj
info("Mesaj") -> [INFO] Mesaj
warining("Mesaj") -> [WARNING] Mesaj
error("Mesaj") -> [ERROR] Mesaj
critical("Mesaj") -> [CRITICAL] Mesaj
'''