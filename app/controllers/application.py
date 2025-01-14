from bottle import template


class Application():

    def __init__(self):
        self.pages = {
            'pagina': self.pagina
        }


    def render(self,page):
       content = self.pages.get(page, self.helper)
       return content()


    def helper(self):
        return template('app/views/html/helper')
    
    
    def pagina(self):
        usuario = 'Davi'
        if usuario == 'Davi':
            return template('app/views/html/pagina',user=usuario)
        else:
            return template('app/views/html/pagina',user='Visitante')
