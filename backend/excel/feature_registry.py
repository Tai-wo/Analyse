"""
Excel Feature Registry

Single source of truth for every Excel capability.
"""

EXCEL_CATEGORIES = [
    "Cleaning",
    "Formulas",
    "Lookup",
    "Pivot Tables",
    "Charts",
    "Dashboards",
    "Statistics",
    "Reports",
    "Formatting",
    "Forecasting",
    "Finance",
    "Sales",
    "Inventory",
    "HR",
    "AI"
]

EXCEL_FEATURES = [

    {
        "id": "remove_duplicates",
        "name": "Remove Duplicates",
        "category": "Cleaning",
        "description": "Remove duplicate rows.",
        "icon": "Trash2",
        "keywords": [
            "duplicate",
            "duplicates",
            "repeat"
        ],
        "premium": False,
        "ai_supported": True
    },

    {
        "id": "fill_missing",
        "name": "Fill Missing Values",
        "category": "Cleaning",
        "description": "Automatically fill missing values.",
        "icon": "Database",
        "keywords": [
            "missing",
            "null",
            "blank"
        ],
        "premium": False,
        "ai_supported": True
    },

    {
        "id": "remove_blank_rows",
        "name": "Remove Blank Rows",
        "category": "Cleaning",
        "description": "Delete empty rows.",
        "icon": "Rows3",
        "keywords": [
            "blank",
            "rows"
        ],
        "premium": False,
        "ai_supported": True
    },

    {
        "id": "trim_spaces",
        "name": "Trim Spaces",
        "category": "Cleaning",
        "description": "Remove extra spaces.",
        "icon": "Scissors",
        "keywords": [
            "spaces",
            "trim"
        ],
        "premium": False,
        "ai_supported": True
    },

    {
        "id": "standardize_dates",
        "name": "Standardize Dates",
        "category": "Cleaning",
        "description": "Convert dates into a consistent format.",
        "icon": "Calendar",
        "keywords": [
            "dates",
            "format"
        ],
        "premium": False,
        "ai_supported": True
    }

]