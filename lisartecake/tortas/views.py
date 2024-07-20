from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from.models import *

from.forms import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



def home(request):
    return render(request, "tortas/index.html")

def acerca(request):
    return render(request, "tortas/acerca.html")

def contacto(request):
    return render(request, "tortas/contacto.html")

def pagar(request):
    return render(request, "tortas/pago.html")

#___ Torta

@login_required
def tortas(request):
    contexto = {"tortas": Torta.objects.all()}
    return render(request, "tortas/tortas.html", contexto)

@login_required
def tortaForm(request):
    if request.method == "POST":
        miForm = TortaForm(request.POST)
        if miForm.is_valid():
            torta_tipo = miForm.cleaned_data.get("tipo")
            torta_cubierta = miForm.cleaned_data.get("cubierta")
            torta_relleno = miForm.cleaned_data.get("relleno")
            torta_cantidad_de_personas = miForm.cleaned_data.get("cantidad_de_personas")
            torta = Torta(tipo=torta_tipo, cubierta=torta_cubierta, relleno=torta_relleno, cantidad_personas=torta_cantidad_de_personas)
            torta.save()
            contexto = {"tortas": Torta.objects.all() }
            return render(request, "tortas/tortas.html", contexto)
    else:
        miForm = TortaForm()

    return render(request, "tortas/tortaForm.html", {"form": miForm})

@login_required
def tortaUpdate(request, id_torta):
    torta = Torta.objects.get(id=id_torta)
    if request.method == "POST":
        miForm = TortaForm(request.POST)
        if miForm.is_valid():
            torta.tipo = miForm.cleaned_data.get("tipo")
            torta.cubierta = miForm.cleaned_data.get("cubierta")
            torta.relleno = miForm.cleaned_data.get("relleno")
            torta.cantidad_personas = miForm.cleaned_data.get("cantidad_de_personas")
            torta.save()
            contexto = {"tortas": Torta.objects.all() }
            return render(request, "tortas/tortas.html", contexto)
    else:
        miForm = TortaForm(initial={"tipo": torta.tipo, "relleno": torta.relleno, "cubierta": torta.cubierta, "cantidad de personas": torta.cantidad_personas})
    return render(request, "tortas/tortaForm.html", {"form": miForm})

@login_required
def tortaDelete(request, id_torta):
    torta = Torta.objects.get(id=id_torta)
    torta.delete()
    contexto = {"tortas": Torta.objects.all() }
    return render(request, "tortas/tortas.html", contexto)

class TortaDeleteView(LoginRequiredMixin,DeleteView):
    model = Torta
    template_name = 'tortas/tortas_confirm_delete.html'  
    success_url = reverse_lazy('tortas')



#___ Tortas Personalizadas

@login_required
def tortasp(request):
    contexto = {"tortasp": TortaP.objects.all()}
    return render(request, "tortas/tortasp.html", contexto)

@login_required
def tortapForm(request):
    if request.method == "POST":
        miForm = TortapForm(request.POST)
        if miForm.is_valid():
            tortap_tipo = miForm.cleaned_data.get("tipo")
            tortap_cubierta = miForm.cleaned_data.get("cubierta")
            tortap_relleno = miForm.cleaned_data.get("relleno")
            tortap_cantidad_de_personas = miForm.cleaned_data.get("cantidad_de_personas")
            tortap_motivo = miForm.cleaned_data.get("motivo")
            tortap_agregados = miForm.cleaned_data.get("agregados")
            tortap = TortaP(tipo=tortap_tipo, cubierta=tortap_cubierta, relleno=tortap_relleno, cantidad_personas=tortap_cantidad_de_personas, motivo=tortap_motivo, agregados=tortap_agregados)
            tortap.save()
            contexto = {"tortasp": TortaP.objects.all() }
            return render(request, "tortas/tortasp.html", contexto)
    else:
        miForm = TortapForm()

    return render(request, "tortas/tortapForm.html", {"form": miForm})


@login_required
def tortapUpdate(request, id_tortap):
    tortap = TortaP.objects.get(id=id_tortap)
    if request.method == "POST":
        miForm = TortapForm(request.POST)
        if miForm.is_valid():
            tortap.tipo = miForm.cleaned_data.get("tipo")
            tortap.cubierta = miForm.cleaned_data.get("cubierta")
            tortap.relleno = miForm.cleaned_data.get("relleno")
            tortap.cantidad_personas = miForm.cleaned_data.get("cantidad_de_personas")
            tortap.motivo = miForm.cleaned_data.get("motivo")
            tortap.agregados = miForm.cleaned_data.get("agregados")
            tortap.save()
            contexto = {"tortasp": TortaP.objects.all() }
            return render(request, "tortas/tortasp.html", contexto)
    else:
        miForm = TortapForm(initial={"tipo": tortap.tipo, "relleno": tortap.relleno, "cubierta": tortap.cubierta, "cantidad de personas": tortap.cantidad_personas, "motivo": tortap.motivo, "agregados": tortap.agregados})
    return render(request, "tortas/tortapForm.html", {"form": miForm})


@login_required
def tortapDelete(request, id_tortap):
    tortap = TortaP.objects.get(id=id_tortap)
    tortap.delete()
    contexto = {"tortasp": TortaP.objects.all() }
    return render(request, "tortas/tortasp.html", contexto)




#___ Modelados

@login_required
def modelados(request):
    contexto = {"modelados": Modelado.objects.all()}
    return render(request, "tortas/modelados.html", contexto)

@login_required
def modeladoForm(request):
    if request.method == "POST":
        miForm = ModeladoForm(request.POST)
        if miForm.is_valid():
            modelo_descripcion = miForm.cleaned_data.get("descripcion")
            modelo_dimensiones = miForm.cleaned_data.get("dimensiones")
            modelo_miscelaneos = miForm.cleaned_data.get("misc")
            modelo = Modelado(descripcion=modelo_descripcion, dimensiones=modelo_dimensiones, misc=modelo_miscelaneos)
            modelo.save()
            contexto = {"modelados": Modelado.objects.all() }
            return render(request, "tortas/modelados.html", contexto)
    else:
        miForm = ModeladoForm()

    return render(request, "tortas/modeladoForm.html", {"form": miForm})


@login_required
def modeladoUpdate(request, id_modelado):
    modelado = Modelado.objects.get(id=id_modelado)
    if request.method == "POST":
        miForm = ModeladoForm(request.POST)
        if miForm.is_valid():
            modelado.descripcion = miForm.cleaned_data.get("descripcion")
            modelado.dimensiones = miForm.cleaned_data.get("dimensiones")
            modelado.misc = miForm.cleaned_data.get("misc")
            modelado.save()
            contexto = {"modelados": Modelado.objects.all() }
            return render(request, "tortas/modelados.html", contexto)
    else:
        miForm = ModeladoForm(initial={"descripcion": modelado.descripcion, "dimensiones": modelado.dimensiones, "misc": modelado.misc})
    return render(request, "tortas/modeladoForm.html", {"form": miForm})


@login_required
def modeladoDelete(request, id_modelado):
    modelado = Modelado.objects.get(id=id_modelado)
    modelado.delete()
    contexto = {"modelados": Modelado.objects.all()}
    return render(request, "tortas/modelados.html", contexto)



#__Cupcakes


class CupcakeList(LoginRequiredMixin,ListView):
    model = Cupcake

class CupcakeCreate(LoginRequiredMixin,CreateView):
    model = Cupcake
    fields = ["tipo", "cubierta", "relleno", "docenas"]
    success_url = reverse_lazy("cupcakes")

class CupcakeUpdate(LoginRequiredMixin,UpdateView):
    model = Cupcake
    fields = ["tipo", "cubierta", "relleno", "docenas"]
    success_url = reverse_lazy("cupcakes")

class CupcakeDelete(LoginRequiredMixin,DeleteView):
    model = Cupcake
    success_url = reverse_lazy("cupcakes")

class CupcakeDeleteView(LoginRequiredMixin,DeleteView):
    model = Cupcake
    template_name = 'tortas/cupcake_confirm_delete.html'  
    success_url = reverse_lazy('cupcakes')




#__ Buscar

def buscarTorta(request):
    return render(request, "tortas/buscarTorta.html")

def encontrarTorta(request):
    if request.GET["Buscar"]:
        patron = request.GET["Buscar"]
        torta = Torta.objects.filter(tipo__icontains=patron)
        contexto = {'tortas': torta}
    else:
        contexto = {"tortas": Torta.objects.all()} 

    return render(request, "tortas/tortas.html", contexto)

#______________________________


def buscarTortap(request):
    return render(request, "tortas/buscarTortap.html")

def encontrarTortap(request):
    if request.GET["Buscar"]:
        patron = request.GET["Buscar"]
        tortap = TortaP.objects.filter(tipo__icontains=patron)
        contexto = {'tortasp': tortap}
    else:
        contexto = {"tortasp": TortaP.objects.all()} 

    return render(request, "tortas/tortasp.html", contexto)

#_______________________________

def buscarModelado(request):
    return render(request, "tortas/buscarModelado.html")

def encontrarModelado(request):
    if request.GET["Buscar"]:
        patron = request.GET["Buscar"]
        modelado = Modelado.objects.filter(descripcion__icontains=patron)
        contexto = {'modelados': modelado}
    else:
        contexto = {"modelados": Modelado.objects.all()} 

    return render(request, "tortas/modelados.html", contexto)

#_______________________________
def buscarCupcake(request):
    return render(request, "tortas/buscarCupcake.html")

def encontrarCupcake(request):
    if request.GET["Buscar"]:
        patron = request.GET["Buscar"]
        cupcake = Cupcake.objects.filter(tipo__icontains=patron)
        contexto = {'cupcake_list': cupcake}
    else:
        contexto = {"cupcake_list": Cupcake.objects.all()} 

    return render(request, "tortas/cupcake_list.html", contexto)

#________________________________


#__ Login / Logout / Registro

def loginRequest(request):
    if request.method == "POST":
        usuario = request.POST["username"]
        clave = request.POST["password"]
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)

            #_____ Buscar Avatar de usuario___________
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar
            #_________________________________________
            return render(request, "tortas/index.html")
        else:
            return redirect(reverse_lazy('login'))
    else:
        miForm = AuthenticationForm()

    return render(request, "tortas/login.html", {"form": miForm})

def registro(request):
    if request.method == "POST":
       miForm = RegistroFrom(request.POST)
       if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home'))
    else:
        miForm = RegistroFrom()
    return render(request, "tortas/registro.html", {"form": miForm})


#__Carrito de compras


@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Torta, id=producto_id)    
    cart_items, created = CartItem.objects.get_or_create(user=request.user, producto=producto)
    
    if created:
        cart_items.cantidad = 1
        messages.success(request, f'{producto.tipo} ha sido agregado al carrito.')
    else:
        cart_items.cantidad += 1
        messages.success(request, f'{producto.tipo} ha sido actualizado en el carrito.')
    
    cart_items.save()
    return redirect('ver_carrito')


@login_required
def ver_carrito(request):
    cart_items = Cart.objects.filter(user=request.user)
    return render(request, 'tortas/carrito.html', {'cart_items': cart_items})



#@login_required
#def carritoDelete(request, id_cartitem):
    cartitem = CartItem.objects.get(id=id_cartitem)
    cartitem.delete()
    contexto = {"cartitem": CartItem.objects.all() }
    return render(request, "tortas/carrito.html", contexto)



#__ Edicion de Perfil / Avatar

@login_required
def editProfile(request):
    usuario = request.user
    if request.method == "POST":
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.email = miForm.cleaned_data.get("first_name")
            user.first_name = miForm.cleaned_data.get("last_name")
            user.last_name = miForm.cleaned_data.get("email")
            user.save()
            return redirect(reverse_lazy("home"))
    else:
        miForm = UserEditForm(instance=usuario)
    return render(request, "tortas/editarPerfil.html", {"form": miForm})


class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "tortas/cambiar_clave.html"
    success_url = reverse_lazy("home")


@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)
        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            imagen = miForm.cleaned_data["imagen"]
            #________Eliminar avatares antiguos______
            oldAvatar = Avatar.objects.filter(user=usuario)
            if len(oldAvatar) > 0:
                for i in range(len(oldAvatar)):
                    oldAvatar[i].delete()
            #________________________________________
            avatar = Avatar(user=usuario, imagen=imagen)
            avatar.save()
            #________Enviar avatar a home____________
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            #________________________________________
            return redirect(reverse_lazy("home"))
    else:
        miForm = AvatarForm()
    return render(request, "tortas/agregarAvatar.html", {"form": miForm})



