import dagster as dg
import polars as pl


@dg.asset(
    name="asset_1",
    group_name="portfolio_management",
    description="This is the first asset in the portfolio management pipeline. It serves as a placeholder for future data processing.",
    owners=[
        dg.Owner(
            name="MD",
            email="derstine.michael@gmail.com"
        ),
    ],
    kinds=["polars"]
)
def asset_1() -> pl.DataFrame:
    """
    This function generates a simple DataFrame with a single column 'a' containing values from 1 to 10.
    It serves as a placeholder for future data processing in the portfolio management pipeline.
    """
    return pl.DataFrame({"a": range(1, 11)})