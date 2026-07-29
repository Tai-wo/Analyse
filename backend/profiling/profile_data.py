def profile_dataset(df):

    return {

        "rows": len(df),

        "columns": len(df.columns),

        "column_names":
        list(df.columns),

        "missing_values":
        int(df.isnull().sum().sum()),

        "duplicates":
        int(df.duplicated().sum())
    }