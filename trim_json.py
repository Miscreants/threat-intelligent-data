import json

# Keep all APTs with description, attribution, link
result = []
with open('data.json', 'r') as input_file:
    json_object = json.load(input_file)
    print("Number of APTs before trim: " + str(len(json_object)))
    for apt in json_object:
        if not ('value' in apt and 'description' in apt and 'attribution' in apt and 'link' in apt):
            continue
        else:
            apt['name'] = apt.pop('value', None)
            result.append(apt)
    print("Number of APTs after trim: " + str(len(result)))

with open('tmp.json', 'w') as output_file:
    output = json.dump(result, output_file)
