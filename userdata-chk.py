import yaml

with open("seed/user-data", 'r') as strm:
    try:
        print(yaml.safe_load(strm))
    except yaml.YAMLError as ex:
        print(ex)
