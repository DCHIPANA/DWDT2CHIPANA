from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import infoTienda, infoProducto

# Create your views here.
def productos(request):
    if request.method == 'POST':
        codProducto = request.POST.get('cod_producto')
        desProducto = request.POST.get('des_producto')
        preProducto = request.POST.get('pre_producto')
        cantProducto = request.POST.get('cant_producto')
        selProducto = request.POST.get('sel_producto')
        infoProducto.objects.create(
            Codigo = codProducto,
            Descripcion = desProducto,
            Precio_venta = preProducto,
            Cantidad = cantProducto)
        return HttpResponseRedirect(reverse('gestionTienda:productos'))
    return render(request, 'gestionProductos.html', {
        'listaProductos': infoProducto.objects.all().order_by('id'),
        'listarTiendas': infoTienda.objects.all().order_by('id')
    })
def detalleTienda(request, idTienda):
    tienda = infoTienda.objects.get(id = idTienda)
    if request.method == 'POST':
        idProducto = request.POST.get('sel_Producto')
        infoProducto.objects.filter(id = idProducto).update(Tienda_relacionada = tienda.id)
    listaProductos = infoProducto.objects.all().order_by('id')
    productosTienda = infoProducto.objects.filter(Tienda_relacionada = tienda.id)
    return render(request, 'detalleTienda.html', {
        'listaProductosTienda': productosTienda.order_by('id'),
        'tienda': tienda,
        'listaProductos': listaProductos
    })

def tiendas(request):
    if request.method == 'POST':
        dirTienda = request.POST.get('dir_Tienda')
        proTienda = request.POST.get('pro_Tienda')
        regTienda = request.POST.get('reg_Tienda')
        fecCreaTienda = request.POST.get('fec_Tienda')
        telTienda = request.POST.get('tel_Tienda')
        infoTienda.objects.create(
            Direccion = dirTienda,
            Provincia = proTienda,
            Region = regTienda,
            Fecha_creacion = fecCreaTienda,
            Telefono_contacto = telTienda)
        return HttpResponseRedirect(reverse('gestionTienda:tiendas'))
    return render(request, 'gestionTiendas.html', {
        'listaTiendas': infoTienda.objects.all().order_by('id')
    })
def eliminarTienda(request, idTienda):
    tiendaEliminar = infoTienda.objects.get(id = idTienda)
    tiendaEliminar.delete()
    return render(request, 'gestionTiendas.html', {
        'listarTiendas': infoTienda.objects.all().order_by('id')
    })

def eliminarProducto(request, idProducto):
    productoEliminar = infoProducto.objects.get(id = idProducto)
    productoEliminar.delete()
    return render(request, 'gestionProductos.html', {
        'listaProductos': infoProducto.objects.all().order_by('id'),
        'listarTiendas': infoTienda.objects.all().order_by('id')
    })

def eliminarProductoTienda(request, idProducto, idTienda):
    productoQuitar = infoProducto.objects.get(id = idProducto)
    tienda = infoTienda.objects.get(id = idTienda)
    productoQuitar.Tienda_relacionada = None
    productoQuitar.save()
    listaProductos = infoProducto.objects.all().order_by('id')
    productosTienda = infoProducto.objects.filter(Tienda_relacionada = tienda.id)
    return render(request, 'detalleTienda.html', {
        'listaProductosTienda': productosTienda.order_by('id'),
        'tienda': tienda,
        'listaProductos': listaProductos
    })