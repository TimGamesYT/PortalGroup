from django.shortcuts import render, redirect
from .models import Material
from .forms import CreateMaterialForm
from django.contrib import messages

def materials_view(request):
    materials = Material.objects.all()
    context = {
        'materials': materials,
    }

    return render(request, 'materials/materials-list-template.html', context)

def create_material_view(request):
    if request.method == 'POST':
        form = CreateMaterialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('materials-list')
        else:
            messages.error(request, "Перевірте форму і повторіть спробу")
    else:
        form = CreateMaterialForm()

    return render(request, 'materials/create-material-template.html', {'form': form})

def delete_material_view(request, pk):
    if request.method == 'POST':
        material = Material.objects.get(pk=pk)
        material.delete()

        return redirect('materials-list')
    
    return render(request, 'materials/delete-material-template.html')
