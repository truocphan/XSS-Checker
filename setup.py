import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

with open('requirements.txt') as f:
	requirements = f.readlines()

setuptools.setup(
	name = "XSS-Checker",  
	version = "22.7.2",
	author = "Truoc Phan",
	license = "MIT",
	author_email = "truocphan112017@gmail.com",
	description = "XSS-Checker is a tool used to Check / Validate for XSS vulnerabilities",
	long_description = long_description,
	long_description_content_type = "text/markdown",
	install_requires = requirements,
	url = "https://github.com/truocphan/XSS-Checker",
	packages = setuptools.find_packages(),
	classifiers = [
		"Programming Language :: Python :: 3"
	],
	entry_points = {
		"console_scripts": [
			"XSS-Checker = XSS_Checker:vFaT3_jrF1FN30CA_o46KQ432mUyxGsUjjQqkXNFQzO0iHoX"
		]
	},
)
