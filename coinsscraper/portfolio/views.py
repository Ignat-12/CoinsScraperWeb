from django.shortcuts import render

from coinsscraper.portfolio.models import Portfolio


def portfolio_list(request):
    portfolios = Portfolio.objects.prefetch_related("assets")
    return render(
        request,
        "portfolios/portfolio_list.html",
        {"portfolios": portfolios},
    )
