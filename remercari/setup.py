setup(
	name = 'remercari',
	version = '1.0',
	packages = find_packages(),
	package_data = {
		'remercari':['dataset/*.csv']
	},
	entry_points = {
		'scrapy':['settings=remercari.settings']
	},
	zip_safe = False,
)