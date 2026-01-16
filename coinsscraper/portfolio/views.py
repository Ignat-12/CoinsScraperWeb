from django.shortcuts import render

from .models import Portfolio


def portfolio_list(request):
    portfolios = Portfolio.objects.prefetch_related("assets")
    return render(
        request,
        "portfolio/portfolio_list.html",
        {"portfolios": portfolios},
    )
