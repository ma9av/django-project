# crm/views.py
from django.shortcuts import render, get_object_or_404
from django.forms import modelform_factory
from django.http import HttpResponse
from django.urls import path

class CRUDViewSet:
    model = None
    fields = "__all__"
    template_base = "crm/crud"

    def get_form_class(self):
        return modelform_factory(self.model, fields=self.fields)

    def get_queryset(self):
        return self.model.objects.all()

    def get_fields(self):
        return [f.name for f in self.model._meta.fields if f.name != "id"]

    # ----- Views -----
    def list_view(self, request):
        objs = self.get_queryset()
        return render(request, f"{self.template_base}/list.html", {
            "objects": objs,
            "fields": self.get_fields(),
            "model_name": self.model.__name__.lower(),
        })

    def form_view(self, request, pk=None):
        instance = get_object_or_404(self.model, pk=pk) if pk else None
        Form = self.get_form_class()
        form = Form(request.POST or None, instance=instance)
        if request.method == "POST" and form.is_valid():
            obj = form.save()
            return render(request, f"{self.template_base}/row.html", {
                "obj": obj,
                "fields": self.get_fields(),
            })
        return render(request, f"{self.template_base}/form.html", {
            "form": form,
            "title": f"{'Edit' if pk else 'Add'} {self.model._meta.verbose_name.title()}"
        })

    def delete_view(self, request, pk):
        obj = get_object_or_404(self.model, pk=pk)
        if request.method == "DELETE":
            obj.delete()
            return HttpResponse("")
        return render(request, f"{self.template_base}/delete_confirm.html", {"obj": obj})

    # ----- URL patterns -----
    def get_urls(self):
        model_name = self.model.__name__.lower()
        return [
            path("", self.list_view, name=f"{model_name}-list"),
            path("create/", self.form_view, name=f"{model_name}-create"),
            path("<int:pk>/update/", self.form_view, name=f"{model_name}-update"),
            path("<int:pk>/delete/", self.delete_view, name=f"{model_name}-delete"),
        ]
