df=spark.table("metadata")
df.display


raw_df={}

for row in df.collect() :
    raw_table=row['RawTableName']
    raw_col= f"{row['RawTableColumn']}{row['DataType']}"
    if raw_table in raw_df :
        raw_df[raw_table].append(raw_col)
    else :
            raw_df[raw_table]=[raw_col]



curated_df={}

for row in df.collect() :
    curated_table=row['CuratedTableName']
    curated_col= f"{row['CuratedTableColumn']}{row['CuratedTableDataType']}"
    if curated_table in curated_df :
        curated_df[curated_table].append(curated_col)
    else :
            curated_df[curated_table]=[curated_col]



presentation_df={}

for row in df.collect() :
    presentation_table=row['PresentationTableName']
    presentation_col= f"{row['PresentationTableColumn']}{row['PresetationTableDataType']}"
    if presentation_table in presentation_df :
        raw_df[presentation_table].append(presentation_col)
    else :
            presentation_df[presentation_table]=[presentation_col]


def create_tablel(layer_dict):
    for table_name,columns in layer_dict.items():
        column_list=",".join(columns)
        spark.sql(f"CREATE TABLE IF NOT EXISTS {table_name} ({column_list})")
        print(f"Table created:{table_name}")
create_tablel(raw_df)
create_tables(curated_df)
create_tables(presentation_df)            