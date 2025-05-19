import dagster as dg
import polars as pl


@dg.asset(
    name="asset_2",
    group_name="portfolio_management",
    description="This is the second asset in the portfolio management pipeline. It serves as a placeholder for future data processing.",
    owners=[
        dg.Owner(
            name="MD",
            email="derstine.michael@gmail.com"
        )
    ],
    kinds=["polars"],
    ins={
        "asset_1": dg.In(
            asset_key="asset_1",
            description="This is the first asset in the portfolio management pipeline. It serves as a placeholder for future data processing."
        )
    }
)
def asset_2(
    asset_1: pl.DataFrame,  # type: ignore[valid-type, no-untyped-def]
) -> pl.DataFrame:

    asset_2 = (
        asset_1
        .with_columns(
            pl.col("a").mul(2.5).alias("b")
        )
    )

    return asset_2