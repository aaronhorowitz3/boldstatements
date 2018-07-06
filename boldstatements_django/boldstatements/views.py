from django.shortcuts import render, redirect
from .models import Statement
from .forms import MakeAStatement

# Create your views here.
def statement_feed(request):
    statements = Statement.object.all()
    return render(request, 'boldstatements/statement_feed.html', {'statements': statements})

def statement_detail(request):
    statement = Statement.object.get(id=pk)
    return render(request, 'boldstatements/statement_detail.html', {'statement': statement})

def make_a_statement(request):
    if request.method == 'POST':
        form = MakeAStatement(request.POST)
        if form.is_valid():
            statement = form.save()
            return redirect('statement_detail', pk=statement.pk)
    else:
        form = MakeAStatement()
    return render(request, 'boldstatements/new_statement', {'form': form})
