from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from mainPage.models import drug


# Create your views here.
@login_required(login_url='/login/')
def adminHome(request):
    return render(request, 'adminHome.html')


@login_required(login_url='/login/')
def addDrug(request):
    return render(request, 'addForm.html')


def logout_view(request):
    logout(request)
    return redirect('page-home')


@login_required(login_url='/login/')
def addNewDrug(request):
    drug_name = request.POST.get('drug_name')
    drug_form = request.POST.get('drug_form')
    drug_class = request.POST.get('drug_class')
    drug_indication = request.POST.get('drug_indication')
    drug_contraindication = request.POST.get('drug_contraindication')
    drug_careful = request.POST.get('drug_careful')
    drug_side_effect = request.POST.get('drug_side_effect')
    drug_dosage = request.POST.get('drug_dosage')
    drug_attention = request.POST.get('drug_attention')
    drug_reference = request.POST.get('drug_reference')
    drug_status = request.POST.get('drug_status')

    drugNew = drug(drug_name=drug_name,
                   drug_form=drug_form,
                   drug_class=drug_class,
                   drug_indication=drug_indication,
                   drug_contraindication=drug_contraindication,
                   drug_careful=drug_careful,
                   drug_side_effect=drug_side_effect,
                   drug_dosage=drug_dosage,
                   drug_attention=drug_attention,
                   drug_reference=drug_reference,
                   drug_status=drug_status)
    drugNew.save()
    return render(request, 'addSuccess.html')


@login_required(login_url='/login/')
def editDrugSuccess(request, pk):
    drugEdit = drug.objects.get(id=pk)

    drug_name = request.POST.get('drug_name')
    drug_form = request.POST.get('drug_form')
    drug_class = request.POST.get('drug_class')
    drug_indication = request.POST.get('drug_indication')
    drug_contraindication = request.POST.get('drug_contraindication')
    drug_careful = request.POST.get('drug_careful')
    drug_side_effect = request.POST.get('drug_side_effect')
    drug_dosage = request.POST.get('drug_dosage')
    drug_attention = request.POST.get('drug_attention')
    drug_reference = request.POST.get('drug_reference')
    drug_status = request.POST.get('drug_status')

    drugEdit.drug_name = drug_name
    drugEdit.drug_form = drug_form
    drugEdit.drug_class = drug_class
    drugEdit.drug_indication = drug_indication
    drugEdit.drug_contraindication = drug_contraindication
    drugEdit.drug_careful = drug_careful
    drugEdit.drug_side_effect = drug_side_effect
    drugEdit.drug_dosage = drug_dosage
    drugEdit.drug_attention = drug_attention
    drugEdit.drug_reference = drug_reference
    drugEdit.drug_status = drug_status

    drugEdit.save()
    return render(request, 'editSuccess.html')


@login_required(login_url='/login/')
def search(request):
    query = request.GET.get('q')
    if query is None:
        query = ''
    results = drug.objects.filter(Q(drug_name__icontains=query)).order_by('drug_name')
    if not results:
        results = None
    return render(request, 'adminSearch.html', {'results': results})


@login_required(login_url='/login/')
def editDrug(request, pk):
    this_drug = drug.objects.get(id=pk)
    return render(request, 'editForm.html', {'this_drug': this_drug})


@login_required(login_url='/login/')
def deleteDrug(request, pk):
    this_drug = drug.objects.get(id=pk)
    return render(request, 'deleteConfirm.html', {'this_drug': this_drug})


@login_required(login_url='/login/')
def deleteDrugSuccess(request, pk):
    delete_drug = drug.objects.get(id=pk)
    delete_drug.delete()
    return render(request, 'deleteSuccess.html')
