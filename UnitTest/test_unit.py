import unittest

class simpleTest2(unittest.TestCase):
   
    def setUp(self):
        self.a = 10
        self.b = 20
        name = self.shortDescription()
        if name == "Add":
            self.a = 10
            self.b = 20
            print(name, self.a, self.b)
        if name == "Sub":
            self.a = 10
            self.b = 20
            print(name, self.a, self.b)
    
    def tearDown(self):
        print ("\n end of test", self.shortDescription())

    def testadd(self):
        
        result = self.a + self.b
        self.assertTrue(result == 30)

    def testsub(self):

        result = self.a - self.b
        self.assertTrue(result == -10)

if __name__ == "__main__":
    unittest.main()

