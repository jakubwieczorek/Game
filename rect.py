# !usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtGui, QtCore

class Rect(QtWidgets.QGraphicsPixmapItem):
    width = 50

    def __init__(self, parent, x = None, y = None):
        """first argument is parent of the object (when object is declared, next four arguments is coordinates"""
        QtWidgets.QGraphicsItem.__init__(self)
        if x == None and y == None:
            self.setPos(parent.geometry().width() / 2, parent.geometry().height() / 2)
        elif x != None and y != None:
            self.setPos(x, y)


        pixmap = QtGui.QPixmap("../Game/rect.png")
        # width of pixmap is 50 pxl, I must fit second coordinate
        self.setPixmap(pixmap.scaled(self.width, self.width * 600 / 247, QtCore.Qt.KeepAspectRatio))

    def getWidth():
        return Rect.width
    getWidth = staticmethod(getWidth)



