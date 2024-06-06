from PySide6.QtWidgets import QGraphicsItem
from enum_cell_type import CellType
from PySide6.QtGui import QBrush, Qt, QColor, QPainter, QPainterPath, QImage, QPen
from PySide6.QtCore import QRectF, QPointF
import numpy
from math import sin, cos, pi

green_tree_image = QImage("green_tree.jpg")
burn_tree_image = QImage("burn_tree.jpg")

class CellGItem(QGraphicsItem):
    def __init__(self, x, y, len, forest_fraction, x_offset, y_offset, x_coord, y_coord, parent=None):
        QGraphicsItem.__init__(self, parent)
        self.__type = (CellType)(numpy.random.random() < forest_fraction)
        self.setPos(x + x_offset, y + y_offset)
        self.len = len
        self.col = x_coord
        self.row = y_coord
        

        self.path = QPainterPath()
        r = len / 2
        path_center = self.boundingRect().center()
        self.path.moveTo(QPointF(r, 0))
        self.path.lineTo(QPointF(path_center.x() + r * cos(-30 * pi / 180), path_center.y() + r * sin(-30 * pi / 180)))
        self.path.lineTo(QPointF(path_center.x() + r * cos(30 * pi / 180), path_center.y() + r * sin(30 * pi / 180)))
        self.path.lineTo(QPointF(path_center.x() + r * cos(90 * pi / 180), path_center.y() + r * sin(90 * pi / 180)))
        self.path.lineTo(QPointF(path_center.x() + r * cos(150 * pi / 180), path_center.y() + r * sin(150 * pi / 180)))
        self.path.lineTo(QPointF(path_center.x() + r * cos(210 * pi / 180), path_center.y() + r * sin(210 * pi / 180)))
        self.path.lineTo(QPointF(path_center.x() + r * cos(270 * pi / 180), path_center.y() + r * sin(270 * pi / 180)))
        self.path.closeSubpath()


    def update_type(self, new_type):
        if self.__type != new_type:
            self.__type = new_type
            self.update()

    def boundingRect(self):
        return QRectF(0, 0, self.len, self.len)

    def paint(self, painter, option, widget=None):
        painter.setBrush(self.get_brush(self.__type))  
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)
        # painter.setPen(painter.brush().color().darker())
        painter.drawPath(self.path)
        # if(self.__type == CellType.empty):
        #     return
        # painter.setBrush(Qt.GlobalColor.black)
        # painter.drawText(self.boundingRect(), "{} {}".format((int)(self.row), (int)(self.col)), Qt.AlignmentFlag.AlignCenter)

    def type(self):
        return self.__type

    def get_brush(self, type):
        match type:
            case CellType.empty:
                return QBrush(Qt.GlobalColor.transparent)
            case CellType.tree:
                return QBrush(green_tree_image.scaledToWidth(self.len))
            case CellType.fire:
                return QBrush(burn_tree_image.scaledToWidth(self.len))
            case _:
                raise NameError("no such type of cell")


    
