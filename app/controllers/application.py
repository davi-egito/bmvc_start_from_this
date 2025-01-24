from bottle import template


class Application():

    def __init__(self):
        self.pages = {
            'pagina': self.pagina
        }
        self.model= DataRecord()

    def render(self,page):
       content = self.pages.get(page, self.helper)
       if not parameter:
           return content()
       else:
           return content(parameter)       

    def helper(self): #controle da pagina helper
        return template('app/views/html/helper')
    
    def pagina(self, parameter=None): #controle da pagina pagina
        if not parameter:
            return template('app/views/html/pagina')
        else:
            user = self.models.work_with_parameter(parametro)
            if not user:
                return redirect('/pagina')
