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