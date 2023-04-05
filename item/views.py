from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required

from .models import Item

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(Category=item.Category, is_donated=False).exclude(pk=pk)[0:3]

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items
    })

@login_required
def delete(request, pk):
    item= get_object_or_404(Item, pk=pk)
    item.delete()

    return redirect('dashboard:index')