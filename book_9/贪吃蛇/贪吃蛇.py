import random
import turtle as t
 	
t.bgcolor('yellow')
caterpillar=t.Turtle()
caterpillar.shape('square')
caterpillar.color('red')
caterpillar.speed(0)
caterpillar.penup()
caterpillar.hideturtle()


leaf = t.Turtle()
leaf_shape=((0,0),(14,2),(18,6),(20,20),(6,18),(2,14))
t.register_shape = ('leaf',leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.hideturtle()
leaf.speed(0)

game_started = False
text_turtle = t.Turtle()













 	'''
 	class ClassName(object):
 		"""docstring for ClassName"""
 		def __init__(self, arg):
 			super(ClassName, self).__init__()
 			self.arg = arg
 			
 	'''







 '''
 except Exception as e:
 	raise
 else:
 	pass
 finally:
 	pass
 	'''