import re
from color_string import color_string

FILE_PATH= 'input.py'

COMMENT_REGEX = re.compile(r'#.*\n') # punto significa algo/cualquier cosa
def parse_file(path, print_result = False):
	with open(path, 'r') as f:
		content = f.read()
	
	rules = [
		{
			'pattern': COMMENT_REGEX,
			'action': lamda match: color_string(match, green),
		}
	]

	parsed = content
	for rule in rules:
		parsed = re.sub(rule['pattern'], rule['action'], content)
	
	if print_result:
		print(parsed)