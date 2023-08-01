import json
import io
# create 'let_statement'
def generate_let_statement(datasourceName, tableName, source_value):
    tableName = tableName.replace(" ", "")
    if 'type' in source_value and source_value['type'] == 'query':
        source_value['type'] = 'm'
    if 'query' in source_value:
        expression = ' '.join(source_value['query']).replace('\\"', "'")
        let_statement = 'let\n    Source = {},\n    vw_{} = Value.NativeQuery(Source, "{}")\n\nin\n    vw_{}'.format(datasourceName, tableName, expression, tableName)
        source_value['expression'] = let_statement
        del source_value['query']  # Remove the old 'query' key
    if 'dataSource' in source_value:
        del source_value['dataSource']  # Remove the 'dataSource' key
    return source_value

def remove_key_recursive(obj, key):
    if isinstance(obj, dict):
        for k, v in list(obj.items()):
            if k == key:
                del obj[k]
            elif isinstance(v, (dict, list)):
                remove_key_recursive(v, key)
    elif isinstance(obj, list):
        for item in obj:
            remove_key_recursive(item, key)

# Open and parse the Bim file
file = <Bim FIle Path>
datasourceName = <Give your datasource Name which will be used in the Let - in expression>

with io.open(file, mode='r', encoding='utf-8', errors='replace') as json_file:
    data = json.load(json_file)
remove_key_recursive(data, 'defaultPowerBIDataSourceVersion')
data['compatibilityLevel'] = 1500


# Modify the required keys in the JSON data
for key, value in data.items():
    if key == 'model':
        for key, value in value.items():
            if key == 'tables':
                for table in value:
                    if 'name' in table:
                        tableName = table['name']
                    if 'partitions' in table:
                        partitions_list = table['partitions']
                        for partition in partitions_list:
                            if 'source' in partition:
                                partition['source'] = generate_let_statement(datasourceName, tableName, partition['source'])

# Save the modified data back to the file
with open(file, 'w') as json_file:
    json.dump(data, json_file, indent=4)
