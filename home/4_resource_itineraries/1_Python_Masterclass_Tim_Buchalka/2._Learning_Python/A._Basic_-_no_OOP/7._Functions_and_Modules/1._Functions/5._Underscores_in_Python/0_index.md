# 5. Underscores in Python
Created Friday 22 May 2020


* We have observed that many object names starts with a single, double, or double-start-end is fairly common.
* They have special meaning, according to code-styles, but don't affect the code in any way. Except **Mangling**.

	personal_details = ('Sanjar', 22, 'India')
	print(personal_details)
	name, _, country = personal_details # age is useless
	print(name, country)


