import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="XSS-Checker",  
	version="22.6.28",
	author="Truoc Phan",
	scripts=["XSS-Checker.py"],
	license="MIT",
	author_email="truocphan112017@gmail.com",
	description="XSS-Checker is a tool used to Check / Validate for XSS vulnerabilities.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	install_requires=[
		"colored",
		"requests",
		"selenium",
		"webdriver_manager"
	],
	url="https://github.com/truocphan/XSS-Checker",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3"
	],
)
