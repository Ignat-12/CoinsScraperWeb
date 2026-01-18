from portfolio.models import Portfolio, Asset
from django.core.management.base import BaseCommand
from django.utils.timezone import now
from pandas import read_excel


class Command(BaseCommand):
    help = "Import data of portfolio from excel file."

    def add_arguments(self, parser):
        parser.add_argument(
            "file_path",
            type=str,
            help="Path to excel file"
        )

    def handle(self, *args, **options):
        file_path = options["file_path"]

        sheets = read_excel(
            file_path,
            sheet_name=None,
            engine="openpyxl"
        )

        for sheet_name, df in sheets.items():
            portfolio = Portfolio.objects.create(
                name=sheet_name,
                own_wallet=True,
            )
            for row in df.to_dict(orient="records"):
                Asset.objects.create(
                    portfolio=portfolio,
                    cryptocurrency_id=row["Cryptocurrency ID"],
                    name=row["Asset Name"],
                    symbol=row["Symbol"],
                    amount=row["Amount"],
                    current_price=row["Current Price"],
                    holdings_value=row["Holdings Value"],
                    pl_value=row["PL Value"],
                    pl_percent_value=row["PL %"],
                    last_updated=now(),
                )

        self.stdout.write(self.style.SUCCESS("Portfolio seeded"))
