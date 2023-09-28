from django.db import models

class ProducyManager(models.Manager):
    
    def prodoctos_por_user(self, usuario):
        return self.filter(
            user_created = usuario
        )
        
    def prodoctos_con_stok(self):
        return self.filter(
            stok__gt=0,
        ).order_by('-num_sales')
        
    def prodoctos_genero(self, genero):
        
        if genero == 'm':
            mujer = True
            varon = False
        elif  genero == 'v':
            mujer = False
            varon = True
        else:
            mujer = True
            varon = True
            
        return self.filter(
            woman = mujer,
            man = varon
        ).order_by('created')
        
    def filtrar_productos(self, **filtros):
        return self.filter(
            man = filtros['man'],
            woman = filtros['woman'],
            name__icontains = filtros['name']
        )