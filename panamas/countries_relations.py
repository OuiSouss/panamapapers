from neo4j.v1 import GraphDatabase, basic_auth

import os


driver = GraphDatabase.driver("bolt://localhost", auth=basic_auth("neo4j", "neo"))
session = driver.session()

countries = ['South Africa', 'Liechtenstein', 'Monaco', 'Belgium', 'Lebanon', 'Switzerland', 'Malaysia', 'Spain', 'United Kingdom', 'Jersey', 'France', 'Luxembourg', 'Taiwan', 'Estonia', 'Mexico', 'Argentina', 'Guernsey', 'United States', 'Venezuela', 'Hong Kong', 'Panama', 'Saudi Arabia', 'Germany', 'Kuwait', 'Poland', 'Brazil', 'Turkey', 'Egypt', 'Canada', 'Portugal', 'Russia', 'Isle of Man', 'Malta', 'Hungary', 'Israel', 'Greece', 'Philippines', 'Italy', 'China', 'Gibraltar', 'Bahamas', 'Honduras', 'Australia', 'Austria', 'Sweden', 'Slovenia', 'Uruguay', 'Thailand', 'Ecuador', 'Colombia', 'United Arab Emirates', 'Peru', 'Czech Republic']
#, 'South Korea', 'Costa Rica', 'Andorra', 'Cyprus', 'Cayman Islands', 'Latvia', 'Antigua and Barbuda', 'Guatemala', 'Ukraine', 'New Zealand', 'Chile', 'El Salvador', 'Seychelles', 'Uganda', 'Iceland', 'Bolivia', 'Netherlands', 'Niue', 'Montenegro', 'Serbia', 'Norway', 'Macao', 'Kenya', 'Syria', 'Viet Nam', 'Turks and Caicos Islands', 'Bermuda', 'Barbados', 'Denmark', 'Mauritius', 'Mozambique', 'Japan', 'Finland', 'Iran', 'Singapore', 'Bahrain', 'Saint Kitts and Nevis', 'Nigeria', 'Dominican Republic', 'British Virgin Islands', 'Tunisia', 'Belarus', 'India', 'Indonesia', 'Ireland', 'Vanuatu', 'Paraguay', 'Nicaragua', 'Aruba'], 'Sri Lanka', 'Puerto Rico', 'Qatar', 'Lesotho', 'Cuba', "Côte d Ivoire", 'Tanzania', 'Romania', 'Jordan', 'Macedonia', 'Zimbabwe', 'Bulgaria', 'Djibouti', 'Moldova', 'Ghana', 'Senegal', 'Belize', 'Curaçao', 'Lithuania', 'Croatia', 'Trinidad and Tobago', 'Bangladesh', 'Angola', 'Saint Vincent and the Grenadines', 'Sudan', 'Oman', 'Morocco', 'Kazakhstan', 'Saint Lucia', 'Malawi', 'Georgia', 'Libya', 'U.S. Virgin Islands', 'Liberia', 'Pakistan', 'Zambia', 'Dominica', 'Botswana', 'Sint Maarten (Dutch part)', 'Brunei', 'Not identified', 'French Polynesia', 'Cook Islands', 'Norfolk Island', 'Samoa', 'Papua New Guinea', 'Nepal', 'Fiji', 'Anguilla', 'Grenada', 'Myanmar', 'Azerbaijan', 'Laos', 'Maldives', 'Northern Mariana Islands', 'Slovakia', 'American Samoa', 'Haiti', 'Cambodia', 'Mongolia', 'Central African Republic', 'Burkina Faso', 'Yemen', 'Cape Verde', 'Madagascar', 'Uzbekistan', 'DR Congo', 'Jamaica', 'Sierra Leone', 'Chad', 'Iraq', 'Cameroon', 'Mali', 'Algeria', 'Namibia', 'Rwanda', 'Turkmenistan', 'Martinique', 'Swaziland', 'Armenia', 'Somalia', 'Albania', 'Guam', 'Tajikistan', 'Saint Martin (French part)', 'Gabon', 'North Korea', 'Gambia', 'Marshall Islands', 'Nauru', 'Guinea', 'Benin', 'Togo', 'Suriname', 'Bosnia and Herzegovina', 'Palestine', 'Guinea-Bissau', 'Solomon Islands', 'Niger', 'Ethiopia', 'Guyana', 'Equatorial Guinea', 'Réunion', 'San Marino', 'Kyrgyzstan', 'Tonga', 'Bhutan']

# for i in countries:
# 	print(i)
# 	for j in countries:
# 		if (i==j):
# 			continue
# 		else:
# 			l_relations = []
# 			result = session.run("MATCH (n:Global)-[r]->(m:Global) WHERE (n.countries = '"+i+"' AND m.countries = '"+j+"') RETURN type(r) AS types")
# 			for t in result:
# 				h = t["types"]
# 				c = h.split(";")
# 				for s in c:
# 					if s not in l_relations:
# 						l_relations.append(s)
# 			if (len(l_relations)>=1):
# 				print("From: " + i + " To: " + j + ": ")
# 				print(l_relations)
# 				tmp = str(len(l_relations))
# 				# session.run("MATCH (n:Country{country:'"+i+"'}), (m:Country{country:'"+j+"'}) CREATE(n)-[: RelationTo]->(m)")
# 				for z in l_relations:
# 					session.run("MATCH (n:Country{country:'"+ i +"'}), (m:Country{country:'"+ j + "'}) CREATE UNIQUE (n)-[:interactions{cpt_interaction:"+ tmp +"}]->(m)")
# 			else :
# 				print("From: " + i + " To: " + j + ": None")
# session.close()

cpt =0
for i in countries:
	cpt += 1
	print(cpt)
	print(i)
	index_i = countries.index(i)
	for x in range (index_i+1, len(countries)):
		j = countries[x]
		print(j)
		result_a = session.run("MATCH (n)-[r]->(m) WHERE (n.countries = '"+i+"' AND m.countries = '"+j+"') RETURN COUNT(r) as count")
		for r in result_a:
			h = r["count"]
			if (h>=1):
				session.run("MATCH (n:Country{country:'"+ i +"'}), (m:Country{country:'"+ j + "'}) CREATE UNIQUE (n)-[:interactions{cpt_interaction:"+ str(h)+"}]->(m)")
		result_b = session.run("MATCH (n)-[r]->(m) WHERE (n.countries = '"+j+"' AND m.countries = '"+i+"') RETURN COUNT(r) as count")
		for r in result_b:
			h=r["count"]
			if (h>=1):
				session.run("MATCH (n:Country{country:'"+ j +"'}), (m:Country{country:'"+ i + "'}) CREATE UNIQUE (n)-[:interactions{cpt_interaction:"+ str(h) +"}]->(m)")
session.close()