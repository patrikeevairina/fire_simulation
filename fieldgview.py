from PySide6.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsPixmapItem
from PySide6.QtGui import QPixmap
from cell import CellGItem
from math import sqrt

class FieldGView(QGraphicsView):
   def __init__(self, parent=None):
      QGraphicsView.__init__(self, parent)
      scene = QGraphicsScene()
      self.setGeometry(0, 0, 2000, 2000)
      self.setScene(scene)
      self.setMouseTracking(True)
      # self.setCacheMode(QGraphicsView.CacheBackground)
      # self.setViewportUpdateMode(QGraphicsView.MinimalViewportUpdate)
      # scene.setItemIndexMethod(QGraphicsScene.NoIndex)
      # self.setOptimizationFlag(QGraphicsView.DontSavePainterState)
      self.cells = list()
      self.columns = 0
      self.rows = 0
      self.forest_fraction = 0.0
      

   # заполнить площадь деревьями с плотностью деревьев == forest_fraction
   def fill(self, cell_width=50, width=30, height=15, forest_fraction=0.8):
      self.forest_fraction = forest_fraction
      scene = self.scene()
      scene.clear()
      self.cells.clear()
      # cell_width = 50
      width = (width*cell_width)
      height = (height*cell_width)
      for i in range(0, height, (int)(cell_width)):
         for j in range(0, width, (int)(cell_width)):
            r = cell_width / 2.0
            magic_coef = r/10.0
            base_x_offset =  (-j / cell_width) * (r - r * sqrt(3.0) / 2.0) 
            base_y_offset = 2 * (-i / cell_width) * (r + magic_coef - r * sqrt(3.0) / 2.0) 
            x_offset = r - magic_coef + base_x_offset * 3.0 / 2.0  if (i / cell_width) % 2 == 0 else base_x_offset * 3.0 / 2.0
            newItem = CellGItem(j, i, cell_width, forest_fraction, x_offset, base_y_offset, (j / cell_width), (i / cell_width))
            newItem.setZValue(-1.0)
            scene.addItem(newItem)
            self.cells.append(newItem)
      self.columns = width / cell_width
      self.rows = height / cell_width
      # self.addDecoration()
      scene.update()

   def addDecoration(self):
      compass = QGraphicsPixmapItem(QPixmap("res/compass.png"))
      compass.setPos(-20, -20)
      compass.setScale(0.1)
      compass.setZValue(0.0)
      self.scene().addItem(compass)
            

   def cellStateList(self):
      states = list()
      for cell in self.cells:
         states.append(cell.type())
      return states
   

   def columnCount(self):
      return self.columns


   def rowCount(self):
      return self.rows
   
   
   def updateCells(self, new_states : list):
      for i in range(0, len(new_states)):
         if self.cells[i].type() == new_states[i]:
            continue
         self.cells[i].update_type(new_states[i])
      

        
