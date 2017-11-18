from django.shortcuts import render, redirect
#hay que importar el formulario
from apps.expediente.models import CatalogoAlergia
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from apps.expediente.requests.AlergiaRequest import AlergiaForm



class AlergiaList(ListView):
    model = CatalogoAlergia
    template_name = 'expediente/alergias/alergia_list.html'

class AlergiaCreate(CreateView):
    model = CatalogoAlergia
    form_class = AlergiaForm
    template_name = 'expediente/alergias/alergia_form.html'
    success_url = reverse_lazy('expediente:alergia_listar')

class AlergiaUpdate(UpdateView):
    model = CatalogoAlergia
    form_class = AlergiaForm
    template_name = 'expediente/alergias/alergia_form.html'
    success_url = reverse_lazy('expediente:alergia_listar')


#metodo delete no implementado debido a conflicto con llave foranea en modelo expediente
#class AlergiaDelete(DeleteView):
 #   model = CatalogoAlergia
  #  template_name = 'expediente/alergias/alergia_delete.html'
   # success_url = reverse_lazy('expediente:alergia_listar')


def alergia_delete(request, id_alergia):
	alergia = CatalogoAlergia.objects.get(id=id_alergia)
	if request.method == 'POST':
		alergia.delete()
		return redirect('expediente:alergia_listar')
	return render(request, 'expediente/alergias/alergia_delete.html', {'expediente':alergia})


