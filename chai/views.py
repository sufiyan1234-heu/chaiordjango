from django.shortcuts import redirect, render
from .models import ChaiVarity,Store
from django.shortcuts import get_list_or_404
from .forms import ChaiVarityForm

# Create your views here.
def all_chai(request):
    chais = ChaiVarity.objects.all()
    print('hhh',chais)
    return render(request, 'chai/all_chai.html',{"chais":chais})



def chaiDetail(request,chai_id):
    chai = get_list_or_404(ChaiVarity,pk=chai_id)
    print(chai,chai_id)
    return render(request, 'chai/chai_detail.html',{"chai":chai})
    

def chaiStoreView(request):
    print("request method",request)
    stores = None
    if request.method == 'POST':
        form = ChaiVarityForm(request.POST)
        if form.is_valid():
            chair_variety = form.cleaned_data['chai_varity']
            stores = Store.objects.filter(chai_varieties=chair_variety)
    else:
        form = ChaiVarityForm()       
            
    return render(request, 'chai/chai_stores.html',{'stores':stores,'form':form})