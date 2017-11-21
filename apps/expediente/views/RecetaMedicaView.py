from django.http import Http404, HttpResponseRedirect
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from apps.expediente.requests.RecetaMedicaRequest import RecetaMedicaForm, RecetaMedicamentoForm
from apps.expediente.models import RecetaMedica, RecetaMedicamento


class ListadoRecetasMedicas(ListView):
    model = RecetaMedica
    template_name = 'expediente/recetas/listado.html'

class AgregarRecetaMedica(CreateView):
    model = RecetaMedica
    template_name = 'expediente/recetas/formulario.html'
    form_class = RecetaMedicamentoForm
    second_form_class = RecetaMedicaForm
    success_url = reverse_lazy('expediente:listado_recetas')

    def get_context_data(self, **kwargs):
        context = super(AgregarRecetaMedica, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        receta_medicamento_form = self.form_class(request.POST)
        receta_medica_form = self.second_form_class(request.POST)
        if receta_medicamento_form.is_valid() and receta_medica_form.is_valid():
            recetamedicamento = receta_medicamento_form.save(commit=False)
            recetamedicamento.RecetaMedica = receta_medica_form.save()
            recetamedicamento.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(
                form=receta_medicamento_form,
                form2=receta_medica_form,
                receta_medicamento_errores=receta_medicamento_form.errors,
                receta_medica_errores=receta_medica_form.errors,
                mensaje_error='No se pudo guardar la receta medica. Por favor revise los datos.'
            ))

class ModificarRecetaMedica(UpdateView):
    model = RecetaMedicamento
    second_model = RecetaMedica
    form_class = RecetaMedicamentoForm
    second_form_class = RecetaMedicaForm
    template_name = 'expediente/recetas/formulario.html'
    success_url = reverse_lazy('expediente:listado_recetas')

    def get_context_data(self, **kwargs):
        context = super(ModificarRecetaMedica, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        receta_medicamento = self.model.objects.get(id=pk)
        receta_medica = self.second_model.objects.get(id=receta_medicamento.RecetaMedica.id)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=receta_medica)
        context['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_receta = kwargs['pk']
        receta_medicamento = self.model.objects.get(id=id_receta)
        receta_medica = self.second_model.objects.get(id=receta_medicamento.RecetaMedica.id)

        receta_medicamento_form = self.form_class(request.POST, instance=receta_medicamento)
        receta_medica_form = self.second_form_class(request.POST, instance=receta_medica)

        if receta_medicamento_form.is_valid() and receta_medica_form.is_valid():
            receta_medicamento_form.save()
            receta_medica_form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())


def eliminarReceta(request, id):
    if not request.is_ajax():
        raise Http404("Error: Solicitud denegada - Esta acción solo se puede ejecutar desde una llamada Ajax.")
    receta = RecetaMedicamento.objects.get(id = id)
    if request.method == 'GET':
        receta.delete()
        return JsonResponse({'error': False, 'mensaje': 'Se eliminó la Receta de la consulta ' + receta.RecetaMedica.Consulta})
    return JsonResponse({'error': True, 'mensaje': 'No se pudo eliminar la Receta de la consulta ' + receta.RecetaMedica.Consulta})
