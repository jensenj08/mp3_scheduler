from bin.json_config import JsonConfig 
from bin.json_config import JsonDirectoryConfig

test = JsonDirectoryConfig('', 'podcast');

#test.config = {"test":"value"}

test.save()