
{
    "name": "Stock Card Report",
    "summary": "Add stock card report on Inventory Reporting.",
    "version": "16.0.1.0.0",
    "category": "Warehouse",
    "website": "https://tintonajisadewo.github.io/",
    "author": "Tinton Aji Sadewo",
    "license": "AGPL-3",
    "depends": ["stock", "date_range", "report_xlsx_helper"],
    "data": [
        "security/ir.model.access.csv",
        "data/paper_format.xml",
        "data/report_data.xml",
        "reports/stock_card_report.xml",
        "wizard/stock_card_report_wizard_view.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "stock_card_report/static/src/css/**/*",
            "stock_card_report/static/src/js/**/*",
        ]
    },
    "installable": True,
}
