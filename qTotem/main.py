import sys
from os.path import abspath, dirname, join
from threading import Thread

from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine

from estilo import *
from interface.ponte import ponte
from paciente import paciente
from siteSide.server import app

# Loop em segundo plano para ler os dados da GPIO
def loopGPIO():
    while(True):
        paciente.getDados()


t1 = Thread(target=loopGPIO)
t1.daemon = True
t1.start()

# Servidor
def server():
    app.run(host='0.0.0.0')
t2 = Thread(target=server)
t2.daemon = True
t2.start()


# Código Qt
if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    qmlFile = join(dirname(__file__), 'interface/main.qml')

    # deixa a Classe Bridge disponível para os aquivos .qml
    engine = QQmlApplicationEngine()
    context = engine.rootContext()
    context.setContextProperty("py", ponte)
    engine.load(abspath(qmlFile))

    if not engine.rootObjects():
        sys.exit(-1)
    #initServer()
    sys.exit(app.exec_())