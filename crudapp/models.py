from django.db import models

class Contact(models.Model):
    firstName = models.CharField("Nome", max_length=255, blank = True, null = True)
    lastName = models.CharField("Sobrenome", max_length=255, blank = True, null = True)
    email = models.EmailField()
    phone = models.CharField("Telefone",max_length=20, blank = True, null = True)
    address = models.TextField("Endereço",blank=True, null=True)
    description = models.TextField("Descrição",blank=True, null=True)
    createdAt = models.DateTimeField("Criado em", auto_now_add=True)

    def __str__(self):
        return self.firstName
    
