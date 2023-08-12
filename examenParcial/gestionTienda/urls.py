from django.urls import path
from . import views
app_name = 'gestionTienda'

urlpatterns = [
    path('productos', views.productos, name = 'productos'),
    path('tiendas', views.tiendas, name = 'tiendas'),
    path('detalleTienda/<str:idTienda>', views.detalleTienda, name = 'detalleTienda'),
    path('eliminarTienda/<str:idTienda>', views.eliminarTienda, name = 'eliminarTienda'),
    path('eliminarProducto/<str:idProducto>', views.eliminarProducto, name = 'eliminarProducto'),
    path('eliminarProductoTienda/<str:idProducto>/<str:idTienda>', views.eliminarProductoTienda, name = 'eliminarProductoTienda'),

]