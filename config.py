import yaml

config = None
with open("config.yml", 'r') as stream:
	try:
		config = (yaml.safe_load(stream))
	except yaml.YAMLError as exc:
		print(exc)
