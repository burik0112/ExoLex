from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from dictionary.models import Term


# Create your views here.

def home(request):
    # base.html emas, home.html bo'lishi shart!
    return render(request, 'home.html')


@login_required
def terms(request):
    search = request.GET.get('search')
    if search:
        terms = Term.objects.filter(name_uz__icontains=search)
    else:
        terms = Term.objects.all()

    return render(request, 'terms.html', {'terms': terms})


def term_detail(request, pk):
    # Agar termin topilmasa, avtomat 404 xatolik beradi
    term = get_object_or_404(Term, pk=pk)
    return render(request, 'term_detail.html', {'term': term})