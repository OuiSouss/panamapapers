#!/usr/bin/python

import csv

dict_type ={
    '':[''],
    '1st vice president and director':['1st v.p. / director'],
    '2nd vice president':['2nd vice president','second vice president'],
    '3rd vice president':['3rd vice president'],
    'accountant':['accountant'],
    'advisor to the board':['advisor to the board'],
    'alternate director':['alt director', 'alt. dir to ian fair','alternate director', 'alternate director of'],
    'anderson':['anderson'],
    'appointor of':['appointor of'],
    'assistant secretary and assistant treasurer':['as. sec. / as. treas.'],
    'assistant controler':['assistant controller','asst. controller'],
    'assistant director':['assistant director'],
    'assistant secretary':['assistant secretary','assistant secretary of','asst. secretary'],
    'assistant treasurer':['assistant treasurer','asst. treasurer'],
    'assistant treasurer and director':['asst treas / director','dir / asst treasurer'],
    'attorney at law':['attorney at law'],
    'attorney in fact':['attorney in fact'],
    'auditor of':['auditor of'],
    'auth. representative of':['auth. representative of'],
    'authorized signatory of':['authorised person / signatory of','authorized', 'authorized signatory','authorized signatory of'],
    'bank signatory of':['bank signatory of'],
    'banker':['banker'],
    'beneficial owner of':['beneficial owner of'],
    'beneficiary of':['beneficiary of'],
    'beneficiary and shareholder and director':['beneficiary, shareholder and director of'],
    'board representative of':['board representative of'],
    'bruno a. roberts':['bruno a. roberts'],
    'business people':['businessman', 'businesswoman'],
    'chief executive officer and secretary':['c.e.o. / secretary'],
    'chief financial officer':['c.f.o.','chief fin. officer','chief financial off','director / c.f.o.'],
    'president':['chairman','chairman & president','chairman / director','chairman / pres / dir','chairman / president','chairman of','company / director','director / c.o.o.','president - director of','president and director of','president director','president / diector','pres. / chairman','president','president of'],
    'president and chief executive officer':['chairman / board / c.e.o','c.e.o. / pres. / dir.','president / c.e.o / director','pres. / ch.exec. / dir.','president / c.e.o'],
    'chief executive officer':['c.e.o','chief exec. officer','chief executive off'],
    'chartered accountant':['chartered accountant'],
    'class a director':['class a director'],
    'class b director':['class b director'],
    'clementi limited':['clementi limited'],
    'co-trustee of trust of':['co-trustee of trust of'],
    'company':['co.','company'],
    'company executive':['company executive'],
    'company secretary':['company secretary'],
    'connected of':['connected of'],
    'controller':['controller'],
    'corporate director':['corp. director','corporate director'],
    'corporate secretary':['corporate secretary'],
    'corporation':['corporation'],
    'correspondent address of':['correspondent addr. of'],
    'cramlington':['cramlington'],
    'custodian of':['custodian of'],
    'deputee chairman and treasurer and director':['dep.chairman / tr. dir'],
    'dipl. ing.':['dipl. ing.'],
    'director and assistant secretary':['dir / asst secretary','director / ass. sec.','director / assist sec','director / asst. sec','director, assistant secretary'],
    ' president and director and secretary and treasurer':['dir / pres / sec / tre','dir / pres / treas / sec','pres / dir. / sec. / tres.'],
    'president and director and secretary':['dir / pres / secretary','director / pres / secretary','director / pres. / secr.','director, secretary, president','pres / sec / director','pres. / dir. / sec.','president / dir / secret'],
    'president and treasurer and director':['dir / pres / treas','director - p / t','director / pres / treas','presid / treas / dir'],
    'director and vice president and president and treasurer and secretary':['dir / pres / vp / trea / sec'],
    'director and vice president':['dir / vice president / cof','director / v.p.','director, vice president','vice president / director','v-president / director','vice president / c.f.o.','deputy ch. / c.e.o','vp / c.e.o.'],
    'director and vice president and treasurer':['dir / vice president / treas','dir. v. pres. / tre','director - vp / t','v.p. / treas. / director','vp / treasurer / directo'],
    'director and vice president and assistant secretary':['dir. / chrm. / vp / a.s.','dir. / v. p. / a.s.'],
    'director and treasurer and secretary':['dir. / sec. / treasure','direc / secr. / treas.','director / treas / sec','director / treasurer / s'],
    'vice president and secretary and director':['dir. / vp / sec','director - v / s','director / v.pres. / sec','director / vp / secretar','director, secretary, vice president','vice president / sec. / dir.'],
    'director and secretary':['dir. and sec.','director / sec','director / secretary','director, secretary','director/secretary'],
    'director':['director','director (rami makhlouf) of','director of','diretor'],
    'director and beneficial owner of':['director / beneficial owner of'],
    'director and chief executive officer':['director / c.e.o','director / c.e.o / pres.','director / chief investment officer','director / cob'],
    'director and manager':['director / manager','director / mgn. dir.'],
    'director and officer':['director / officer'],
    'director and president and 01':['director / pres / 01'],
    'director and president':['director / president','director, president','director/president','pres / ch.invest.of / di'],
    'director and shareholder and beneficial owner of':['director / shareholder / beneficial owner of'],
    'director and shareholder':['director / shareholder of','director and shareholder of'],
    'director and treasurer':['director / treasurer','director/treasurer','treas. / director'],
    'director and officer and president':['director/officer president'],
    'dr. norbert marxer':['dr. norbert marxer'],
    'entity similar to':['entity similar to'],
    'executive vice president':['ex vice president','exec. vice president'],
    'executive':['executive'],
    'executive director':['executive director'],
    'executive officer':['executive officer'],
    'financial controller':['financial controller'],
    '1st beneficiary of':['first beneficiary of'],
    '1st director':['first director'],
    '1st vice president':['first vice president'],
    'foundation council':['foundation council'],
    'general accountant of':['general accountant of'],
    'general counsel':['general counsel'],
    'general manager':['general manager'],
    'gfs':['gfs'],
    'grantee of a mortagage of':['grantee of a mortgage of'],
    'ibc':['ibc'],
    'independant non executive director':['ind. non-exec. dir.'],
    'independent director':['independent director'],
    'intermediary of':['intermediary of'],
    'investment advisor of':['investment advisor','investment advisor of'],
    'joint settlor of ':['joint settlor of'],
    'legal advisor of':['legal advisor of'],
    'manager corporate':['manager-corporate'],
    'managing director':['managing director','mng. director / china'],
    'member':['member','mr /'],
    'member and shareholder':['member / shareholder of'],
    'member of foundation council of':['member of foundation council of'],
    'nominated person of':['nominated person of'],
    'nominee beneficial owner of':['nominee beneficial owner of'],
    'nominee beneficiary of':['nominee beneficiary of'],
    'nominee director of':['nominee director of'],
    'nominee investment advisor of':['nominee investment advisor of'],
    'nominee name of':['nominee name of'],
    'nominee protector of':['nominee protector of'],
    'nominee secretary of':['nominee secretary of'],
    'nominee shareholder of':['nominee shareholder of'],
    'nominee trust settlor of':['nominee trust settlor of'],
    'non executive director':['non','non executive direct'],
    'officer of':['officer','officer of'],
    'ordinary director':['ordinary director'],
    'owner of':['owner of'],
    'owner and director and shareholder':['owner, director and shareholder of'],
    'partner of':['partner of'],
    'permanent director':['permanent director'],
    'personal directorship of':['personal directorship of'],
    'power of attorney and shareholder of':['power of attorney / shareholder of'],
    'power of attorney':['power of attorney of'],
    'president and vice president':['pres / v.p.'],
    'president and secretary':['pres. / secretary','president / secretary'],
    'president and treasurer':['president / treas.','president / treasurer'],
    'principal beneficiary of':['principal beneficiary of'],
    'probably same officer as':['probably same officer as'],
    'protector of':['protector of'],
    'records and registers of':['records & registers of'],
    'register of director':['register of director of'],
    'register of shareholder':['register of shareholder of'],
    'registered address':['registered address'],
    'registered agent':['registered agent'],
    'registered office':['registered office'],
    'related entity':['related entity'],
    'reserve director':['reserve director of'],
    'resident director':['resident director of'],
    'resigned':['resigned'],
    'safekeeping':['safekeeping of'],
    'same address as':['same address as'],
    'same company as':['same company as'],
    'same intermediary as':['same intermediary as'],
    'same name and registration date as':['same name and registration date as'],
    'same name as':['same name as'],
    'secretary and treasurer':['sec / treas','secretary / treasurer'],
    'secretary':['secretary','secretary of','sec'],
    'shareholder':['shareholder','shareholder (through julex foundation) of','shareholder of'],
    'signatory':['signatory of'],
    'similar name and address as':['similar name and address as'],
    'sole director and president and secretary and treasurer':['sol director/president/secretary/treasurer','sole director/president/secretary/treasurer'],
    'sole director':['sole director'],
    'sole director and secretary':['sole director / sec.'],
    'sole shareholder':['sole shareholder of'],
    'sole signatory and beneficial owner of':['sole signatory / beneficial owner of'],
    'sole signatory of':['sole signatory of'],
    'special director':['special director'],
    'stockbroker of':['stockbroker of'],
    'subscriber':['subscriber'],
    'successor protector of':['successor protector of'],
    't.c.':['t.c.'],
    'tax advisor of':['tax advisor of'],
    'to gary lane':['to gary lane'],
    'treasurer':['treasurer','treasurer of'],
    'treasurer and assistant secretary':['treasurer / asst. sec.'],
    'trust settlor of':['trust settlor of'],
    'trustee of trust of':['trustee of trust of'],
    'tur limited':['tur limited'],
    'unit trust register of':['unit trust register of'],
    'vice president and senior trader':['v.p / / senior trader'],
    'vice president':['vice president','vice president and','vice president of'],
    'vice president and general manager':['vice president / g.m.'],
    'vice president and general counsel':['vice president / gen coun /'],
    'vice president and secretary':['vice president / sec.','vice president / secretary','vice president/secretary'],
    'vice president and treasurer and secretary':['vice president / sec. / trea','vice president / treas / sec'],
    'vice president and treasurer':['vice president / treasurer','vp / treasurer'],
    'vice president-finance':['vice president-finance'],
    'vice-chairman':['vice-chairman'],
    'vice president and treasurer and assistant secretary':['vp / treas. asst sec'],
}


"""

s = "vice president"
k = "vice president / secretary"
#print dict_type.keys()
#print dict_type.values()
if s in dict_type.keys():
    for i in dict_type[s]:
        print i
for key,val in dict_type.items():
    if k in val:
        print key
"""


global row_header
global name_type_act
global new_row1_change
global liste

liste = []

with open("all_edges.csv", "r+") as edges_reader:
    reader = csv.reader(edges_reader, delimiter=',', lineterminator='\n')
    for row in reader:
        if reader.line_num == 1:
            row_header = row
            continue
        else :
            name_type_act = row[1].lower()
            for key,vals in dict_type.items():
                if name_type_act in vals:
                    new_row1_change = key
            row[1] = new_row1_change
            
            outfilename = "edges_{}.csv".format(row[1])
            with open(outfilename, "a") as outfile:
                writer = csv.writer(outfile, delimiter=',', lineterminator='\n')
                if not row[1] in liste:
                    liste.append(row[1])
                    writer.writerow(row_header)
                writer.writerow(row)
                outfile.close()
            
edges_reader.close()

print (len(dict_type))
