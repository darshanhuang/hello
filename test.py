import unittest

class Enemy(object):
    def __init__(self,name,hp):
        self.name=name
        self.hp=hp

    def die(self):
        self.hp=0
        print '%s died' % self.name
        #del self

class Test1(unittest.TestCase):
    def test_func1(self):
        enemy1 = Enemy('test',20)
        print enemy1.hp

        enemy1.die()
        self.assertEqual(enemy1.hp,0)

if __name__=='__main__':
    unittest.main()
	
