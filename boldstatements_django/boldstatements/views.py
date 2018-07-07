from django.shortcuts import render, redirect
from .models import Statement
from .forms import MakeAStatement

# Create your views here.
def statement_feed(request):
    statements = Statement.objects.all()
    return render(request, 'boldstatements/statement_feed.html', {'statements': statements})

def statement_detail(request, pk):
    statement = Statement.objects.get(id=pk)
    return render(request, 'boldstatements/statement_detail.html', {'statement': statement})

def make_a_statement(request):
    if request.method == 'POST':
        form = MakeAStatement(request.POST, request.FILES)
        if form.is_valid():
            statement = form.save()
            return redirect('statement_detail', pk=statement.pk)
    else:
        form = MakeAStatement()
    return render(request, 'boldstatements/new_statement.html', {'form': form})
