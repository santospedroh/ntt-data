# Importamos nosso app
from app import app
import unittest

class Test(unittest.TestCase):

    def setUp(self):
        # cria uma instância do unittest, precisa do nome "setUp"
        self.app = app.test_client()
        
        # envia uma requisicao GET para a URL                                                                                                                                                            
        self.result = self.app.get('/hello')   
        
if __name__ == "__main__":                                                                                                                                                                               
    print('INICIANDO OS TESTES')                                                                                                                                                                        
    print('----------------------------------------------------------------------')                                                                                                                      
    unittest.main(verbosity=2)