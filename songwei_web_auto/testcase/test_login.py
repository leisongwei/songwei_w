import unittest


class login(unittest.TestCase):
    """"测试相等"""
    def testlogin(self):
        """测试2=2"""
        self.assertEqual(2, 2)

    def testlogin1(self):
        """测试2=3"""
        self.assertEqual(2, 3)


if __name__ == "__main__":
    unittest.main()

