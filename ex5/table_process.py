import pandas as pd


def clean_columns(columns_list):

    cleaned_columns = []

    for col_name in columns_list:
        cleaned_columns.append(col_name.lstrip('# ').split('#')[0].rstrip())

    return cleaned_columns


def get_filter_rules(filtering_rules):

    rules_dict = {}

    for rule in filtering_rules:
        rules_dict[rule.split(':')[0].strip()] = rule.split(':')[1].strip()

    return rules_dict


if __name__ == '__main__':
    file_name = 'table.xlsx'
    table_filtering_rules_file = 'table_filtering'
    columns_order_file = 'columns_order'

    data = pd.read_excel(file_name)

    with open(columns_order_file) as f:
        columns_order = f.readlines()

    columns_order = clean_columns(columns_order)
    data = data[columns_order]

    with open(table_filtering_rules_file) as f:
        filtering_rules = f.readlines()

    rules_dict = get_filter_rules(filtering_rules)

    writer = pd.ExcelWriter('multisheet.xlsx', engine='xlsxwriter')

    for key, rule in rules_dict.items():
        data_sheet = eval(f"data.query('{rule}')")

        data_sheet.to_excel(writer, sheet_name=key)

    writer.save()
