
import cx_Oracle
import os
import sys

try:
    if sys.platform.startswith("darwin"):
        lib_dir = os.path.join(os.environ.get("HOME"), "Downloads",
                               "instantclient_19_8")
        cx_Oracle.init_oracle_client(lib_dir=lib_dir)
    elif sys.platform.startswith("win32"):
        lib_dir="C:\\oracle\\instantclient_19_8"
        cx_Oracle.init_oracle_client(lib_dir=lib_dir)
except Exception as err:
    print("Whoops!")
    print(err)
    sys.exit(1)

def conexionBD():
    dsn = cx_Oracle.makedsn(host='localhost', port=1521, sid='xe')
    return cx_Oracle.connect(
        user="ambientePrueba",
        password="tkoxmtiymtk",
        dsn=dsn
    )