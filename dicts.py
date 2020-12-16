employee = {"name":           "John Doe",
            "year_of_birth":  2000,
            "color_of_eye":   "green",
            "position":       "boss",
            "skills":          ['Java', 'JavaScript', 'C#', 'Python'],
            "address"           :{
                "city": "Budapest",
                "street": "Andrassy"
            }}



print(employee['name'])
print(employee['year_of_birth'])

another_employee = ('John Doe', 2000, 'boss')

print(employee['skills'][1])

print(employee['address']['street'])

employees = ({"name": "John Doe", "year": 2000}, {"name": "Jack Doe", "year": 2001})
print(employees[1]['year'])

g = {
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
}

print(g['glossary']['GlossDiv']['GlossList']['GlossEntry']['Acronym'])


