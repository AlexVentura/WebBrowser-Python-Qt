# -*- coding: utf-8 -*-

import sys, re

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

class Browser(QWidget):

	"""Constructor del Browser"""
	def __init__(self):
		super(Browser, self).__init__()

		# Creamos dos layouts uno Vertical y otro Horizontal
		vbox = QVBoxLayout(self)
		hbox = QHBoxLayout()

		# Creamos los componentes
		self.btnBack = QPushButton(self.style().standardIcon(QStyle.SP_ArrowLeft), "")
		self.btnForward = QPushButton(self.style().standardIcon(QStyle.SP_ArrowRight), "")
		self.btnReload = QPushButton(self.style().standardIcon(QStyle.SP_BrowserReload), "")
		self.btnStop = QPushButton(self.style().standardIcon(QStyle.SP_BrowserStop), "")
		self.url = QLineEdit()
		self.btnOk = QPushButton(self.style().standardIcon(QStyle.SP_DialogOkButton), "")

		# Asociamos los componentes a los layouts
		hbox.addWidget(self.btnBack)
		hbox.addWidget(self.btnForward)
		hbox.addWidget(self.btnReload)
		hbox.addWidget(self.btnStop)
		hbox.addWidget(self.url)
		hbox.addWidget(self.btnOk)

		# Al layout vertical que contiene a la misma ventana le asociamos el horizontal
		vbox.addLayout(hbox)

		# Creamos el componente web
		self.web = QWebView(self)

		# Agregamos el componente web al layout vertical
		vbox.addWidget(self.web)
		
		# Que el componente web cargue google por defecto
		self.web.load(QUrl("http://google.com.mx"))

		# Creamos una barra de estado y una barra de progreso
		self.status = QStatusBar()
		self.bProg = QProgressBar()
		# Añadimos a la barra de estado la barra de progreso
		self.status.addWidget(QLabel("Loading..."))
		self.status.addWidget(self.bProg)
		# Añadimos todo al layout vertical
		vbox.addWidget(self.status)

		# Conectamos las señales # http://zetcode.com/gui/pyqt5/eventssignals/s
		# self.connect(self.btnBack, SIGNAL("clicked()"), self.web.back)
		self.connect(self.btnBack, SIGNAL("clicked()"), self.web.back)
		self.connect(self.btnForward, SIGNAL("clicked()"), self.web.forward)
		self.connect(self.btnReload, SIGNAL("clicked()"), self.web.reload)
		self.connect(self.btnStop, SIGNAL("clicked()"), self.web.stop)
		self.connect(self.web, SIGNAL("loadProgress(int)"), self.bProg.setValue)
		# Ocultar la barra de estado cuando no se estre trabajando
		self.connect(self.web, SIGNAL("loadStarted()"), self.status.show)
		self.connect(self.web, SIGNAL("loadFinished(bool)"), self.load_finished)
		# Ir a la URL con enter en la caja o en el boton ir
		self.connect(self.url, SIGNAL("returnPressed()"), self.do_search)
		self.connect(self.btnOk, SIGNAL("clicked()"), self.do_search)

	def load_finished(self):
		self.status.hide()
		self.url.setText(self.web.url().toString())

	def do_search(self):
		# Obtenemos el texto ingresado
		link = unicode(self.url.text())
		# Creamos un RegExp para evaluar el texto
		pat = re.compile("(.+)\\.(.+)")
		# Si no fue una URL hacemos la busqueda directa en google
		if pat.match(link) and not link.startswith("http://"):
			link = "http://" + link
		elif not pat.match(link):
			link = "http://google.com.mx/?q=%s" % link.replace(' ', '+')

		self.web.load(QUrl(link))


app = QApplication(sys.argv)

w = Browser()
w.setWindowTitle("LMX - WebBrowser")
w.show()

sys.exit(app.exec_())