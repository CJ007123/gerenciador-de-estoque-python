import unittest

loader = unittest.TestLoader()
tests = loader.discover('Projeto_Estoque/tests')
test_runner = unittest.TextTestRunner()
test_runner.run(tests)