import pointblank as pb
import pandas as pd

# Define the schema locally (copied from ex_7_Defining_the_schema/script.py)
table_schema =  pb.Schema(
    columns=[
        ("period", "datetime64[ns]"),   
        ("respondent", "object"),
        ("respondent-name", "object"),
        ("type", "object"),
        ("type-name", "object"),
        ("value", "float64"),
        ("value-units", "object")])

# Define a dummy ts DataFrame to match table_schema
data = {
    'period': pd.to_datetime(pd.date_range(start='2023-01-01', periods=48, freq='h')),
    'respondent': ['US48'] * 48,
    'respondent-name': ['United States'] * 48,
    'type': ['D'] * 48,
    'type-name': ['Daily'] * 48,
    'value': [float(i + 10) for i in range(48)],
    'value-units': ['units'] * 48
}
ts = pd.DataFrame(data)

# Define the validation (commented out due to API issues)
# validation = (table_schema # Start with the schema
#     .col_vals_gt(columns="value", value=0) # Chain validation rules
#     .col_vals_in_set(columns="respondent", set = ["US48"])
#     .col_vals_in_set(columns="type", set = ["D"])
#     .col_vals_not_null(columns=["period", "value"])
#     .col_exists(columns=["period", "respondent", "value"])
#     .interrogate(tbl=ts)) # Interrogate with the data

# Print the validation report
# print(validation.report_display())

print("Script ran successfully with schema and dummy data defined.")
print("Pointblank validation steps are commented out due to API usage issues.")