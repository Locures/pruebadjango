from django.urls import path
from inicio.views import inicio, mostrar_horario, saludo, crear_auto, autos, ver_auto, eliminar_auto, editar_auto

urlpatterns = [
    
    path('', inicio, name='inicio'),
    path('mostrar-horario/', mostrar_horario, name = 'mostrar_horario'),
    path('saludo/<str:nombre>/<str:apellido>/', saludo, name = 'saludo'),
    path('autos/', autos, name = 'autos'),
    path('autos/nuevo/', crear_auto, name = 'crear_auto'),
    path('autos/<int:id_auto>/', ver_auto, name = 'ver_auto'),
    path('autos/<int:id_auto>/eliminar/', eliminar_auto, name = 'eliminar_auto'),
    path('autos/<int:id_auto>/editar/', editar_auto, name = 'editar_auto')
    # path('alumnos/nuevo/<str:nombre>/<str:apellido>/<int:edad>', crear_alumno, name = 'crear_alumno'),
]