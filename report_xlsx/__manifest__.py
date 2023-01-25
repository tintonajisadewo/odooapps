{
    "name": "Base report xlsx",
    "summary": "Base module to create xlsx report",
    "author": "Tinton Aji Sadewo",
    "website": "https://tintonajisadewo.github.io/",
    "category": "Reporting",
    "version": "16.0.1.0.1",
    "development_status": "Mature",
    "license": "AGPL-3",
    "external_dependencies": {"python": ["xlsxwriter", "xlrd"]},
    "depends": ["base", "web"],
    "demo": ["demo/report.xml"],
    "installable": True,
    "assets": {
        "web.assets_backend": [
            "report_xlsx/static/src/js/report/action_manager_report.esm.js",
        ],
    },
}
