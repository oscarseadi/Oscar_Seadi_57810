from django.urls import path, include
from.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name = "home"),
    path('home/', home, name = "home"),
    path('acerca/', acerca, name = "acerca"),
    path('contacto/', contacto, name = "contacto"),        

    #__ Tortas
    path('tortas/', tortas, name = "tortas"),
    path('tortas_form/', tortaForm, name = "tortaForm"),
    path('torta_update/<id_torta>', tortaUpdate, name= "tortaUpdate"),
    path('torta_delete/<int:pk>', TortaDeleteView.as_view(), name= "tortaDelete"),

    #__ Tortas Personalizadas
    path('tortasp/', tortasp, name = "tortasp"),
    path('tortasp_form/', tortapForm, name = "tortapForm"),
    path('tortap_update/<id_tortap>', tortapUpdate, name= "tortapUpdate"),
    path('tortap_delete/<id_tortap>', tortapDelete, name= "tortapDelete"),

    #__ Modelados
    path('modelados/', modelados, name = "modelados"),
    path('modelados_form/', modeladoForm, name = "modeladoForm"),
    path('modelado_update/<id_modelado>', modeladoUpdate, name= "modeladoUpdate"),
    path('modelado_delete/<id_modelado>', modeladoDelete, name= "modeladoDelete"),
    
    #__ Cupcakes
    path('cupcakes/', CupcakeList.as_view(), name = "cupcakes"),
    path('cupcakeCreate/', CupcakeCreate.as_view(), name = "cupcakeCreate"),
    path('cupcakeUpdate/<int:pk>/', CupcakeUpdate.as_view(), name = "cupcakeUpdate"),
    path('cupcakeDelete/<int:pk>/', CupcakeDelete.as_view(), name = "cupcakeDelete"),
    

    #__ Buscar
    path('buscarTorta/', buscarTorta, name = "buscarTorta"),
    path('encontrarTorta/', encontrarTorta, name = "encontrarTorta"),
    path('buscarTortap/', buscarTortap, name = "buscarTortap"),
    path('encontrarTortap/', encontrarTortap, name = "encontrarTortap"),
    path('buscarModelado/', buscarModelado, name = "buscarModelado"),
    path('encontrarModelado/', encontrarModelado, name = "encontrarModelado"),
    path('buscarCupcake/', buscarCupcake, name = "buscarCupcake"),
    path('encontrarCupcake/', encontrarCupcake, name = "encontrarCupcake"),

    #__ Login / Logout / Registro
    path('login/', loginRequest, name = "login"),
    path('logout/', LogoutView.as_view(template_name="tortas/logout.html"), name = "logout"),
    path('registro/', registro, name = "registro"),


    #__Carrito
    path('carrito/', ver_carrito, name='ver_carrito'),
    path('pagar/', pagar, name='pagar'),
    path('agregar/<int:producto_id>/', agregar_al_carrito, name='agregar_al_carrito'),

    #__Edicion de Perfil / Avatar
    path('perfil/', editProfile, name = "perfil"),
    path('<int:pk>/password/', CambiarClave.as_view(), name = "cambiarClave"),
    path('agregar_avatar/', agregarAvatar, name = "agregar_avatar"),

]