from django.contrib import admin

# Register your models here.
from .models import Persona
admin.site.register(Persona)

from .models import Usuario
admin.site.register(Usuario)

from .models import Autor
admin.site.register(Autor)

from .models import Estado
admin.site.register(Estado)

from .models import Categoria
admin.site.register(Categoria)

from .models import Editorial
admin.site.register(Editorial)

from .models import Libro
admin.site.register(Libro)

from .models import Prestamos
admin.site.register(Prestamos)





