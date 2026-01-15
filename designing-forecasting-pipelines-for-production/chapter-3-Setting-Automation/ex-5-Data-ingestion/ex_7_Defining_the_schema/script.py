# Import the required library
# Start by importing pointblank.
import pointblank as pb

# Define the schema and set columns
# Set the 
# respondent column to object type and 
# value column to float64 type.

table_schema =  pb.Schema(
    columns=[
        ("period", "datetime64[ns]"),   
        ("respondent", "object"),
        ("respondent-name", "object"),
        ("type", "object"),
        ("type-name", "object"),
        ("value", "float64"),
        ("value-units", "object")])

print(table_schema)