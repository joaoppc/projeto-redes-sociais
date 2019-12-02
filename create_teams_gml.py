from unidecode import unidecode
import os
import pandas as pd
from statistics import mean
import collections
import operator



teamsA2016= []
teamsA2017= []
teamsA2018= []
teamsA2019= []
teamsB2016= []
teamsB2017= []
teamsB2018= []
teamsB2019= []
teamsC2016= []
teamsC2017= []
teamsC2018= []
teamsC2019= []
teamsD=[]

matches_resultA2019=[]
matches_resultA2018=[]
matches_resultA2017=[]
matches_resultA2016=[]
matches_resultB2019=[]
matches_resultB2018=[]
matches_resultB2017=[]
matches_resultB2016=[]
matches_resultC2019=[]
matches_resultC2018=[]
matches_resultC2017=[]
matches_resultC2016=[]



dicA2019={}
dicA2018={}
dicA2017={}
dicA2016={}
dicB2019={}
dicB2018={}
dicB2017={}
dicB2016={}
dicC2019={}
dicC2018={}
dicC2017={}
dicC2016={}
shots_mediaA2019={}
shots_mediaA2018={}
shots_mediaA2017={}
shots_mediaA2016={}
shots_mediaB2019={}
shots_mediaB2018={}
shots_mediaB2017={}
shots_mediaB2016={}
shots_acc_mediaA2019={}
shots_acc_mediaA2018={}
shots_acc_mediaA2017={}
shots_acc_mediaA2016={}
shots_acc_mediaB2019={}
shots_acc_mediaB2018={}
shots_acc_mediaB2017={}
shots_acc_mediaB2016={}
shots_acc_porc_mediaA2019={}
shots_acc_porc_mediaA2018={}
shots_acc_porc_mediaA2017={}
shots_acc_porc_mediaA2016={}
shots_acc_porc_mediaB2019={}
shots_acc_porc_mediaB2018={}
shots_acc_porc_mediaB2017={}
shots_acc_porc_mediaB2016={}
passes_mediaA2019={}
passes_mediaA2018={}
passes_mediaA2017={}
passes_mediaA2016={}
passes_mediaB2019={}
passes_mediaB2018={}
passes_mediaB2017={}
passes_mediaB2016={}
passes_acc_mediaA2019={}
passes_acc_mediaA2018={}
passes_acc_mediaA2017={}
passes_acc_mediaA2016={}
passes_acc_mediaB2019={}
passes_acc_mediaB2018={}
passes_acc_mediaB2017={}
passes_acc_mediaB2016={}
passes_acc_porc_mediaA2019={}
passes_acc_porc_mediaA2018={}
passes_acc_porc_mediaA2017={}
passes_acc_porc_mediaA2016={}
passes_acc_porc_mediaB2019={}
passes_acc_porc_mediaB2018={}
passes_acc_porc_mediaB2017={}
passes_acc_porc_mediaB2016={}
possesion_mediaA2019={}
possesion_mediaA2018={}
possesion_mediaA2017={}
possesion_mediaA2016={}
possesion_mediaB2019={}
possesion_mediaB2018={}
possesion_mediaB2017={}
possesion_mediaB2016={}
losses_mediaA2019={}
losses_mediaA2018={}
losses_mediaA2017={}
losses_mediaA2016={}
losses_mediaB2019={}
losses_mediaB2018={}
losses_mediaB2017={}
losses_mediaB2016={}
losses_low_mediaA2019={}
losses_low_mediaA2018={}
losses_low_mediaA2017={}
losses_low_mediaA2016={}
losses_low_mediaB2019={}
losses_low_mediaB2018={}
losses_low_mediaB2017={}
losses_low_mediaB2016={}
losses_medium_mediaA2019={}
losses_medium_mediaA2018={}
losses_medium_mediaA2017={}
losses_medium_mediaA2016={}
losses_medium_mediaB2019={}
losses_medium_mediaB2018={}
losses_medium_mediaB2017={}
losses_medium_mediaB2016={}
losses_high_mediaA2019={}
losses_high_mediaA2018={}
losses_high_mediaA2017={}
losses_high_mediaA2016={}
losses_high_mediaB2019={}
losses_high_mediaB2018={}
losses_high_mediaB2017={}
losses_high_mediaB2016={}
recoveries_mediaA2019={}
recoveries_mediaA2018={}
recoveries_mediaA2017={}
recoveries_mediaA2016={}
recoveries_mediaB2019={}
recoveries_mediaB2018={}
recoveries_mediaB2017={}
recoveries_mediaB2016={}
recoveries_low_mediaA2019={}
recoveries_low_mediaA2018={}
recoveries_low_mediaA2017={}
recoveries_low_mediaA2016={}
recoveries_low_mediaB2019={}
recoveries_low_mediaB2018={}
recoveries_low_mediaB2017={}
recoveries_low_mediaB2016={}
recoveries_medium_mediaA2019={}
recoveries_medium_mediaA2018={}
recoveries_medium_mediaA2017={}
recoveries_medium_mediaA2016={}
recoveries_medium_mediaB2019={}
recoveries_medium_mediaB2018={}
recoveries_medium_mediaB2017={}
recoveries_medium_mediaB2016={}
recoveries_high_mediaA2019={}
recoveries_high_mediaA2018={}
recoveries_high_mediaA2017={}
recoveries_high_mediaA2016={}
recoveries_high_mediaB2019={}
recoveries_high_mediaB2018={}
recoveries_high_mediaB2017={}
recoveries_high_mediaB2016={}
chalenges_mediaA2019={}
chalenges_mediaA2018={}
chalenges_mediaA2017={}
chalenges_mediaA2016={}
chalenges_mediaB2019={}
chalenges_mediaB2018={}
chalenges_mediaB2017={}
chalenges_mediaB2016={}
chalenges_won_mediaA2019={}
chalenges_won_mediaA2018={}
chalenges_won_mediaA2017={}
chalenges_won_mediaA2016={}
chalenges_won_mediaB2019={}
chalenges_won_mediaB2018={}
chalenges_won_mediaB2017={}
chalenges_won_mediaB2016={}
rankingA2019={}
rankingA2018={}
rankingA2017={}
rankingA2016={}
rankingB2019={}
rankingB2018={}
rankingB2017={}
rankingB2016={}

dicD={}



def get_media(column):
	lista=[]
	for indx, x in enumerate(column):
		if str(x) == 'nan':
			pass
		else:
			if indx%2 == 0:
				lista.append(x)
	media = mean(lista)
	return round(media,2)

def write_media(dic,string,file):
	for key in dic:
		if y in key:
			file.write('\t\tmedia_{0} '.format(string)+'\"'+unidecode(str(dic[key]))+'\"'+'\n')
def write_ranking(dic,file):
	for key in dic:
		if y in key:
			file.write('\t\tposicao'+'\"'+unidecode(str(dic[key]))+'\"'+'\n')

rankingA2016['Palmeiras']=1
rankingA2016['Santos']=2
rankingA2016['Flamengo']=3
rankingA2016['Atlético Mineiro']=4
rankingA2016['Botafogo']=5
rankingA2016['Athletico Paranaense']=6
rankingA2016['Corinthians']=7
rankingA2016['Ponte Preta']=8
rankingA2016['Grêmio']=9
rankingA2016['São Paulo']=10
rankingA2016['Chapecoense']=11
rankingA2016['Cruzeiro']=12
rankingA2016['Fluminense']=13
rankingA2016['Sport Recife']=14
rankingA2016['Coritiba']=15
rankingA2016['Vitória']=16
rankingA2016['Internacional']=17
rankingA2016['Figueirense']=18
rankingA2016['Santa Cruz']=19
rankingA2016['América Mineiro']=20
rankingA2017['Corinthians']=1
rankingA2017['Palmeiras']=2
rankingA2017['Santos']=3
rankingA2017['Grêmio']=4
rankingA2017['Cruzeiro']=5
rankingA2017['Flamengo']=6
rankingA2017['Vasco da Gama']=7
rankingA2017['Chapecoense']=8
rankingA2017['Atlético Mineiro']=9
rankingA2017['Botafogo']=10
rankingA2017['Athletico Paranaense']=11
rankingA2017['Bahia']=12
rankingA2017['São Paulo']=13
rankingA2017['Fluminense']=14
rankingA2017['Sport Recife']=15
rankingA2017['Vitória']=16
rankingA2017['Coritiba']=17
rankingA2017['Avaí']=18
rankingA2017['Ponte Preta']=19
rankingA2017['Atlético GO']=20
rankingA2018['Palmeiras']=1
rankingA2018['Flamengo']=2
rankingA2018['Internacional']=3
rankingA2018['Grêmio']=4
rankingA2018['São Paulo']=5
rankingA2018['Atlético Mineiro']=6
rankingA2018['Athletico Paranaense']=7
rankingA2018['Cruzeiro']=8
rankingA2018['Botafogo']=9
rankingA2018['Santos']=10
rankingA2018['Bahia']=11
rankingA2018['Fluminense']=12
rankingA2018['Corinthians']=13
rankingA2018['Chapecoense']=14
rankingA2018['Ceará']=15
rankingA2018['Vasco da Gama']=16
rankingA2018['Sport Recife']=17
rankingA2018['América Mineiro']=18
rankingA2018['Vitória']=19
rankingA2018['Paraná']=20


count = 0
os.chdir("teams" )
for filename in os.listdir(os.getcwd()):
	xls = pd.ExcelFile(filename)
	sheetX = xls.parse(0)

	competition = sheetX['Competition']
	team = sheetX['Team']
	date = sheetX['Date']
	goals = sheetX['Goals']
	match = sheetX['Match']
	possesion = sheetX['Possession, %']
	shots = sheetX['Shots / on target']
	shots_target = sheetX['Unnamed: 9']
	shots_target_porc = sheetX['Unnamed: 10']
	passes = sheetX['Passes / accurate']
	passes_acc = sheetX['Unnamed: 12']
	passes_acc_porc = sheetX['Unnamed: 13']
	losses = sheetX['Losses / Low / Medium / High']
	losses_low = sheetX['Unnamed: 16']
	losses_medium = sheetX['Unnamed: 17']
	losses_high = sheetX['Unnamed: 18']
	recoveries = sheetX['Recoveries / Low / Medium / High']
	recoveries_low = sheetX['Unnamed: 20']
	recoveries_medium = sheetX['Unnamed: 21']
	recoveries_high = sheetX['Unnamed: 22']
	chalenges = sheetX['Challenges / won']
	chalenges_won = sheetX['Unnamed: 24']



	
	if competition[3] == 'Brazil. Serie A':
		if '3' in filename:
			fn = open('result_teams_brA2019.gml','w+')
			#print(filename)
			#print(shots[2:7])

		elif '2' in filename:
			fn = open('result_teams_brA2018.gml','w+')
		elif '1' in filename:
			fn = open('result_teams_brA2017.gml','w+')
		elif '3' and '2' and '1'not in filename:
			fn = open('result_teams_brA2016.gml','w+')
	elif competition[3] == 'Brazil. Serie B':
		if '3' in filename:
			fn = open('result_teams_brB2019.gml','w+')
		elif '2' in filename:
			fn = open('result_teams_brB2018.gml','w+')
		elif '1' in filename:
			fn = open('result_teams_brB2017.gml','w+')
		elif '3' and '2' and '1'not in filename:
			fn = open('result_teams_brB2016.gml','w+')
	elif competition[3] == 'Brazil. Serie C':
		if '3' in filename:
			fn = open('result_teams_brC2019.gml','w+')
		elif '2' in filename:
			fn = open('result_teams_brC2018.gml','w+')
		elif '1' in filename:
			fn = open('result_teams_brC2017.gml','w+')
		elif '3' and '2' and '1'not in filename:
			fn = open('result_teams_brC2016.gml','w+')
	else: 
		if '3' in filename:

			fn = open('result_teams_bretc2019.gml','w+')
		elif '2' in filename:
			fn = open('result_teams_bretc2018.gml','w+')
		elif '1' in filename:
			fn = open('result_teams_bretc2017.gml','w+')
		elif '3' not in filename and '2'not in filename and '1'not in filename:
			fn = open('result_teams_bretc2016.gml','w+')

	fn.write('graph [\n')
	fn.write('\tdirected 1\n')

	for  x in team:
		if str(x) == 'nan':
			pass
		else:
			if competition[3] == 'Brazil. Serie A':
				if '3' in filename:
					if x == 'Atletico PR':
						x = 'Athletico Paranaense'
					elif x not in teamsA2019 :
						teamsA2019.append(x)
				elif '2' in filename:
					if x == 'Atletico PR':
						x = 'Athletico Paranaense'
					elif x not in teamsA2018 :
						teamsA2018.append(x)
				elif '1' in filename:
					if x == 'Atletico PR':
						x = 'Athletico Paranaense'
					elif x not in teamsA2017 :
						teamsA2017.append(x)
				elif '3' not in filename and '2'not in filename and '1'not in filename:
					if x == 'Atletico PR':
						x = 'Athletico Paranaense'
					elif x not in teamsA2016 :
						teamsA2016.append(x)
			elif competition[3] == 'Brazil. Serie B':
				if '3' in filename:
					if x not in teamsB2019 :
						teamsB2019.append(x)
				elif '2' in filename:
					if x not in teamsB2018 :
						teamsB2018.append(x)
				elif '1' in filename:
					if x not in teamsB2017 :
						teamsB2017.append(x)
				elif '3' not in filename and '2'not in filename and '1'not in filename:
					if x not in teamsB2016 :
						teamsB2016.append(x)
			elif competition[3] == 'Brazil. Serie C':
				if '3' in filename:
					if x not in teamsC2019 :
						teamsC2019.append(x)
				elif '2' in filename:
					if x not in teamsC2018 :
						teamsC2018.append(x)
				elif '1' in filename:
					if x not in teamsC2017 :
						teamsC2017.append(x)
				elif '3' not in filename and '2'not in filename and '1'not in filename:
					if x not in teamsC2016 :
						teamsC2016.append(x)
			else: 
				if x not in teamsD :
					teamsD.append(x)

	

	if competition[3] == 'Brazil. Serie A' and '3' in filename:
		

		shots_mediaA2019[filename]=get_media(shots)
		passes_mediaA2019[filename]=get_media(passes)
		shots_acc_mediaA2019[filename]=get_media(shots_target)
		passes_acc_mediaA2019[filename]=get_media(passes_acc)
		shots_acc_porc_mediaA2019[filename]=get_media(shots_target_porc)
		passes_acc_porc_mediaA2019[filename]=get_media(passes_acc_porc)
		possesion_mediaA2019[filename]=get_media(possesion)
		losses_mediaA2019[filename]=get_media(losses)
		losses_low_mediaA2019[filename]=get_media(losses_low)
		losses_medium_mediaA2019[filename]=get_media(losses_medium)
		losses_high_mediaA2019[filename]=get_media(losses_high)
		recoveries_mediaA2019[filename]=get_media(recoveries)
		recoveries_low_mediaA2019[filename]=get_media(recoveries_low)
		recoveries_medium_mediaA2019[filename]=get_media(recoveries_medium)
		recoveries_high_mediaA2019[filename]=get_media(recoveries_high)
		chalenges_mediaA2019[filename]=get_media(chalenges)
		chalenges_won_mediaA2019[filename]=get_media(chalenges_won)

		
		#print(collections.OrderedDict(sorted_x))


		for idx, y in enumerate(teamsA2019):

			dicA2019[unidecode(str(y))]=idx

			fn.write('\tnode [\n')
			fn.write('\t\tid '+str(idx)+'\n')
			fn.write('\t\tlabel '+'\"'+unidecode(str(y))+'\"'+'\n')
			write_media(shots_mediaA2019,'shots',fn)
			write_media(passes_mediaA2019,'passes',fn)
			write_media(shots_acc_mediaA2019,'shots_target',fn)
			write_media(passes_acc_mediaA2019,'passes_acc',fn)
			write_media(shots_acc_porc_mediaA2019,'shots_target_porc',fn)
			write_media(passes_acc_porc_mediaA2019,'passes_acc_porc',fn)
			write_media(possesion_mediaA2019,'possesion',fn)
			write_media(losses_mediaA2019,'losses',fn)
			write_media(losses_low_mediaA2019,'losses_low',fn)
			write_media(losses_medium_mediaA2019,'losses_medium',fn)
			write_media(losses_high_mediaA2019,'losses_high',fn)
			write_media(recoveries_mediaA2019,'recoveries',fn)
			write_media(recoveries_low_mediaA2019,'recoveries_low',fn)
			write_media(recoveries_medium_mediaA2019,'recoveries_medium',fn)
			write_media(recoveries_high_mediaA2019,'recoveries_high',fn)
			write_media(chalenges_mediaA2019,'chalenges',fn)
			write_media(chalenges_won_mediaA2019,'chalenges_won',fn)
			fn.write('\t]\n')

	elif competition[3] == 'Brazil. Serie A' and '2' in filename:

		shots_mediaA2018[filename]=get_media(shots)
		passes_mediaA2018[filename]=get_media(passes)
		shots_acc_mediaA2018[filename]=get_media(shots_target)
		passes_acc_mediaA2018[filename]=get_media(passes_acc)
		shots_acc_porc_mediaA2018[filename]=get_media(shots_target_porc)
		passes_acc_porc_mediaA2018[filename]=get_media(passes_acc_porc)
		possesion_mediaA2018[filename]=get_media(possesion)
		losses_mediaA2018[filename]=get_media(losses)
		losses_low_mediaA2018[filename]=get_media(losses_low)
		losses_medium_mediaA2018[filename]=get_media(losses_medium)
		losses_high_mediaA2018[filename]=get_media(losses_high)
		recoveries_mediaA2018[filename]=get_media(recoveries)
		recoveries_low_mediaA2018[filename]=get_media(recoveries_low)
		recoveries_medium_mediaA2018[filename]=get_media(recoveries_medium)
		recoveries_high_mediaA2018[filename]=get_media(recoveries_high)
		chalenges_mediaA2018[filename]=get_media(chalenges)
		chalenges_won_mediaA2018[filename]=get_media(chalenges_won)

		

		for idx, y in enumerate(teamsA2018):

			dicA2018[unidecode(str(y))]=idx

			fn.write('\tnode [\n')
			fn.write('\t\tid '+str(idx)+'\n')
			fn.write('\t\tlabel '+'\"'+unidecode(str(y))+'\"'+'\n')
			write_media(shots_mediaA2018,'shots',fn)
			write_media(passes_mediaA2018,'passes',fn)
			write_media(shots_acc_mediaA2018,'shots_target',fn)
			write_media(passes_acc_mediaA2018,'passes_acc',fn)
			write_media(shots_acc_porc_mediaA2018,'shots_target_porc',fn)
			write_media(passes_acc_porc_mediaA2018,'passes_acc_porc',fn)
			write_media(possesion_mediaA2018,'possesion',fn)
			write_media(losses_mediaA2018,'losses',fn)
			write_media(losses_low_mediaA2018,'losses_low',fn)
			write_media(losses_medium_mediaA2018,'losses_medium',fn)
			write_media(losses_high_mediaA2018,'losses_high',fn)
			write_media(recoveries_mediaA2018,'recoveries',fn)
			write_media(recoveries_low_mediaA2018,'recoveries_low',fn)
			write_media(recoveries_medium_mediaA2018,'recoveries_medium',fn)
			write_media(recoveries_high_mediaA2018,'recoveries_high',fn)
			write_media(chalenges_mediaA2018,'chalenges',fn)
			write_media(chalenges_won_mediaA2018,'chalenges_won',fn)
			fn.write('\t\tposition '+'\"'+unidecode(str(rankingA2018[y]))+'\"'+'\n')
			fn.write('\t]\n')

	elif competition[3] == 'Brazil. Serie A' and '1' in filename:

		shots_mediaA2017[filename]=get_media(shots)
		passes_mediaA2017[filename]=get_media(passes)
		shots_acc_mediaA2017[filename]=get_media(shots_target)
		passes_acc_mediaA2017[filename]=get_media(passes_acc)
		shots_acc_porc_mediaA2017[filename]=get_media(shots_target_porc)
		passes_acc_porc_mediaA2017[filename]=get_media(passes_acc_porc)
		possesion_mediaA2017[filename]=get_media(possesion)
		losses_mediaA2017[filename]=get_media(losses)
		losses_low_mediaA2017[filename]=get_media(losses_low)
		losses_medium_mediaA2017[filename]=get_media(losses_medium)
		losses_high_mediaA2017[filename]=get_media(losses_high)
		recoveries_mediaA2017[filename]=get_media(recoveries)
		recoveries_low_mediaA2017[filename]=get_media(recoveries_low)
		recoveries_medium_mediaA2017[filename]=get_media(recoveries_medium)
		recoveries_high_mediaA2017[filename]=get_media(recoveries_high)
		chalenges_mediaA2017[filename]=get_media(chalenges)
		chalenges_won_mediaA2017[filename]=get_media(chalenges_won)

		for idx, y in enumerate(teamsA2017):

			dicA2017[unidecode(str(y))]=idx

			fn.write('\tnode [\n')
			fn.write('\t\tid '+str(idx)+'\n')
			fn.write('\t\tlabel '+'\"'+unidecode(str(y))+'\"'+'\n')
			write_media(shots_mediaA2017,'shots',fn)
			write_media(passes_mediaA2017,'passes',fn)
			write_media(shots_acc_mediaA2017,'shots_target',fn)
			write_media(passes_acc_mediaA2017,'passes_acc',fn)
			write_media(shots_acc_porc_mediaA2017,'shots_target_porc',fn)
			write_media(passes_acc_porc_mediaA2017,'passes_acc_porc',fn)
			write_media(possesion_mediaA2017,'possesion',fn)
			write_media(losses_mediaA2017,'losses',fn)
			write_media(losses_low_mediaA2017,'losses_low',fn)
			write_media(losses_medium_mediaA2017,'losses_medium',fn)
			write_media(losses_high_mediaA2017,'losses_high',fn)
			write_media(recoveries_mediaA2017,'recoveries',fn)
			write_media(recoveries_low_mediaA2017,'recoveries_low',fn)
			write_media(recoveries_medium_mediaA2017,'recoveries_medium',fn)
			write_media(recoveries_high_mediaA2017,'recoveries_high',fn)
			write_media(chalenges_mediaA2017,'chalenges',fn)
			write_media(chalenges_won_mediaA2017,'chalenges_won',fn)
			fn.write('\t\tposition '+'\"'+unidecode(str(rankingA2017[y]))+'\"'+'\n')
			fn.write('\t]\n')
	elif competition[3] == 'Brazil. Serie A' and '3' not in filename and '2'not in filename and '1'not in filename:

		shots_mediaA2016[filename]=get_media(shots)
		passes_mediaA2016[filename]=get_media(passes)
		shots_acc_mediaA2016[filename]=get_media(shots_target)
		passes_acc_mediaA2016[filename]=get_media(passes_acc)
		shots_acc_porc_mediaA2016[filename]=get_media(shots_target_porc)
		passes_acc_porc_mediaA2016[filename]=get_media(passes_acc_porc)
		possesion_mediaA2016[filename]=get_media(possesion)
		losses_mediaA2016[filename]=get_media(losses)
		losses_low_mediaA2016[filename]=get_media(losses_low)
		losses_medium_mediaA2016[filename]=get_media(losses_medium)
		losses_high_mediaA2016[filename]=get_media(losses_high)
		recoveries_mediaA2016[filename]=get_media(recoveries)
		recoveries_low_mediaA2016[filename]=get_media(recoveries_low)
		recoveries_medium_mediaA2016[filename]=get_media(recoveries_medium)
		recoveries_high_mediaA2016[filename]=get_media(recoveries_high)
		chalenges_mediaA2016[filename]=get_media(chalenges)
		chalenges_won_mediaA2016[filename]=get_media(chalenges_won)

		for idx, y in enumerate(teamsA2016):

			dicA2016[unidecode(str(y))]=idx

			fn.write('\tnode [\n')
			fn.write('\t\tid '+str(idx)+'\n')
			fn.write('\t\tlabel '+'\"'+unidecode(str(y))+'\"'+'\n')
			write_media(shots_mediaA2016,'shots',fn)
			write_media(passes_mediaA2016,'passes',fn)
			write_media(shots_acc_mediaA2016,'shots_target',fn)
			write_media(passes_acc_mediaA2016,'passes_acc',fn)
			write_media(shots_acc_porc_mediaA2016,'shots_target_porc',fn)
			write_media(passes_acc_porc_mediaA2016,'passes_acc_porc',fn)
			write_media(possesion_mediaA2016,'possesion',fn)
			write_media(losses_mediaA2016,'losses',fn)
			write_media(losses_low_mediaA2016,'losses_low',fn)
			write_media(losses_medium_mediaA2016,'losses_medium',fn)
			write_media(losses_high_mediaA2016,'losses_high',fn)
			write_media(recoveries_mediaA2016,'recoveries',fn)
			write_media(recoveries_low_mediaA2016,'recoveries_low',fn)
			write_media(recoveries_medium_mediaA2016,'recoveries_medium',fn)
			write_media(recoveries_high_mediaA2016,'recoveries_high',fn)
			write_media(chalenges_mediaA2016,'chalenges',fn)
			write_media(chalenges_won_mediaA2016,'chalenges_won',fn)
			write_media(chalenges_won_mediaA2016,'chalenges_won',fn)
			fn.write('\t\tposition '+'\"'+unidecode(str(rankingA2016[y]))+'\"'+'\n')
			fn.write('\t]\n')

	elif competition[3] == 'Brazil. Serie B' and '3' in filename:

		shots_mediaB2019[filename]=get_media(shots)
		passes_mediaB2019[filename]=get_media(passes)
		shots_acc_mediaB2019[filename]=get_media(shots_target)
		passes_acc_mediaB2019[filename]=get_media(passes_acc)
		shots_acc_porc_mediaB2019[filename]=get_media(shots_target_porc)
		passes_acc_porc_mediaB2019[filename]=get_media(passes_acc_porc)
		possesion_mediaB2019[filename]=get_media(possesion)
		losses_mediaB2019[filename]=get_media(losses)
		losses_low_mediaB2019[filename]=get_media(losses_low)
		losses_medium_mediaB2019[filename]=get_media(losses_medium)
		losses_high_mediaB2019[filename]=get_media(losses_high)
		recoveries_mediaB2019[filename]=get_media(recoveries)
		recoveries_low_mediaB2019[filename]=get_media(recoveries_low)
		recoveries_medium_mediaB2019[filename]=get_media(recoveries_medium)
		recoveries_high_mediaB2019[filename]=get_media(recoveries_high)
		chalenges_mediaB2019[filename]=get_media(chalenges)
		chalenges_won_mediaB2019[filename]=get_media(chalenges_won)

		for idx, y in enumerate(teamsB2019):

			dicB2019[unidecode(str(y))]=idx

			fn.write('\tnode [\n')
			fn.write('\t\tid '+str(idx)+'\n')
			fn.write('\t\tlabel '+'\"'+unidecode(str(y))+'\"'+'\n')
			write_media(shots_mediaB2019,'shots',fn)
			write_media(passes_mediaB2019,'passes',fn)
			write_media(shots_acc_mediaB2019,'shots_target',fn)
			write_media(passes_acc_mediaB2019,'passes_acc',fn)
			write_media(shots_acc_porc_mediaB2019,'shots_target_porc',fn)
			write_media(passes_acc_porc_mediaB2019,'passes_acc_porc',fn)
			write_media(possesion_mediaB2019,'possesion',fn)
			write_media(losses_mediaB2019,'losses',fn)
			write_media(losses_low_mediaB2019,'losses_low',fn)
			write_media(losses_medium_mediaB2019,'losses_medium',fn)
			write_media(losses_high_mediaB2019,'losses_high',fn)
			write_media(recoveries_mediaB2019,'recoveries',fn)
			write_media(recoveries_low_mediaB2019,'recoveries_low',fn)
			write_media(recoveries_medium_mediaB2019,'recoveries_medium',fn)
			write_media(recoveries_high_mediaB2019,'recoveries_high',fn)
			write_media(chalenges_mediaB2019,'chalenges',fn)
			write_media(chalenges_won_mediaB2019,'chalenges_won',fn)
			fn.write('\t]\n')	
		
	elif competition[3] == 'Brazil. Serie B' and '2' in filename:
	
		shots_mediaB2018[filename]=get_media(shots)
		passes_mediaB2018[filename]=get_media(passes)
		shots_acc_mediaB2018[filename]=get_media(shots_target)
		passes_acc_mediaB2018[filename]=get_media(passes_acc)
		shots_acc_porc_mediaB2018[filename]=get_media(shots_target_porc)
		passes_acc_porc_mediaB2018[filename]=get_media(passes_acc_porc)
		possesion_mediaB2018[filename]=get_media(possesion)
		losses_mediaB2018[filename]=get_media(losses)
		losses_low_mediaB2018[filename]=get_media(losses_low)
		losses_medium_mediaB2018[filename]=get_media(losses_medium)
		losses_high_mediaB2018[filename]=get_media(losses_high)
		recoveries_mediaB2018[filename]=get_media(recoveries)
		recoveries_low_mediaB2018[filename]=get_media(recoveries_low)
		recoveries_medium_mediaB2018[filename]=get_media(recoveries_medium)
		recoveries_high_mediaB2018[filename]=get_media(recoveries_high)
		chalenges_mediaB2018[filename]=get_media(chalenges)
		chalenges_won_mediaB2018[filename]=get_media(chalenges_won)

		for idx, y in enumerate(teamsB2018):

			dicB2018[unidecode(str(y))]=idx

			fn.write('\tnode [\n')
			fn.write('\t\tid '+str(idx)+'\n')
			fn.write('\t\tlabel '+'\"'+unidecode(str(y))+'\"'+'\n')
			write_media(shots_mediaB2018,'shots',fn)
			write_media(passes_mediaB2018,'passes',fn)
			write_media(shots_acc_mediaB2018,'shots_target',fn)
			write_media(passes_acc_mediaB2018,'passes_acc',fn)
			write_media(shots_acc_porc_mediaB2018,'shots_target_porc',fn)
			write_media(passes_acc_porc_mediaB2018,'passes_acc_porc',fn)
			write_media(possesion_mediaB2018,'possesion',fn)
			write_media(losses_mediaB2018,'losses',fn)
			write_media(losses_low_mediaB2018,'losses_low',fn)
			write_media(losses_medium_mediaB2018,'losses_medium',fn)
			write_media(losses_high_mediaB2018,'losses_high',fn)
			write_media(recoveries_mediaB2018,'recoveries',fn)
			write_media(recoveries_low_mediaB2018,'recoveries_low',fn)
			write_media(recoveries_medium_mediaB2018,'recoveries_medium',fn)
			write_media(recoveries_high_mediaB2018,'recoveries_high',fn)
			write_media(chalenges_mediaB2018,'chalenges',fn)
			write_media(chalenges_won_mediaB2018,'chalenges_won',fn)
			fn.write('\t]\n')

	elif competition[3] == 'Brazil. Serie B' and '1' in filename:

		shots_mediaB2017[filename]=get_media(shots)
		passes_mediaB2017[filename]=get_media(passes)
		shots_acc_mediaB2017[filename]=get_media(shots_target)
		passes_acc_mediaB2017[filename]=get_media(passes_acc)
		shots_acc_porc_mediaB2017[filename]=get_media(shots_target_porc)
		passes_acc_porc_mediaB2017[filename]=get_media(passes_acc_porc)
		possesion_mediaB2017[filename]=get_media(possesion)
		losses_mediaB2017[filename]=get_media(losses)
		losses_low_mediaB2017[filename]=get_media(losses_low)
		losses_medium_mediaB2017[filename]=get_media(losses_medium)
		losses_high_mediaB2017[filename]=get_media(losses_high)
		recoveries_mediaB2017[filename]=get_media(recoveries)
		recoveries_low_mediaB2017[filename]=get_media(recoveries_low)
		recoveries_medium_mediaB2017[filename]=get_media(recoveries_medium)
		recoveries_high_mediaB2017[filename]=get_media(recoveries_high)
		chalenges_mediaB2017[filename]=get_media(chalenges)
		chalenges_won_mediaB2017[filename]=get_media(chalenges_won)

		for idx, y in enumerate(teamsB2017):

			dicB2017[unidecode(str(y))]=idx

			fn.write('\tnode [\n')
			fn.write('\t\tid '+str(idx)+'\n')
			fn.write('\t\tlabel '+'\"'+unidecode(str(y))+'\"'+'\n')
			write_media(shots_mediaB2017,'shots',fn)
			write_media(passes_mediaB2017,'passes',fn)
			write_media(shots_acc_mediaB2017,'shots_target',fn)
			write_media(passes_acc_mediaB2017,'passes_acc',fn)
			write_media(shots_acc_porc_mediaB2017,'shots_target_porc',fn)
			write_media(passes_acc_porc_mediaB2017,'passes_acc_porc',fn)
			write_media(possesion_mediaB2017,'possesion',fn)
			write_media(losses_mediaB2017,'losses',fn)
			write_media(losses_low_mediaB2017,'losses_low',fn)
			write_media(losses_medium_mediaB2017,'losses_medium',fn)
			write_media(losses_high_mediaB2017,'losses_high',fn)
			write_media(recoveries_mediaB2017,'recoveries',fn)
			write_media(recoveries_low_mediaB2017,'recoveries_low',fn)
			write_media(recoveries_medium_mediaB2017,'recoveries_medium',fn)
			write_media(recoveries_high_mediaB2017,'recoveries_high',fn)
			write_media(chalenges_mediaB2017,'chalenges',fn)
			write_media(chalenges_won_mediaB2017,'chalenges_won',fn)
			fn.write('\t]\n')

	elif competition[3] == 'Brazil. Serie B' and '3' not in filename and '2'not in filename and '1'not in filename:
	
		shots_mediaB2016[filename]=get_media(shots)
		passes_mediaB2016[filename]=get_media(passes)
		shots_acc_mediaB2016[filename]=get_media(shots_target)
		passes_acc_mediaB2016[filename]=get_media(passes_acc)
		shots_acc_porc_mediaB2016[filename]=get_media(shots_target_porc)
		passes_acc_porc_mediaB2016[filename]=get_media(passes_acc_porc)
		possesion_mediaB2016[filename]=get_media(possesion)
		losses_mediaB2016[filename]=get_media(losses)
		losses_low_mediaB2016[filename]=get_media(losses_low)
		losses_medium_mediaB2016[filename]=get_media(losses_medium)
		losses_high_mediaB2016[filename]=get_media(losses_high)
		recoveries_mediaB2016[filename]=get_media(recoveries)
		recoveries_low_mediaB2016[filename]=get_media(recoveries_low)
		recoveries_medium_mediaB2016[filename]=get_media(recoveries_medium)
		recoveries_high_mediaB2016[filename]=get_media(recoveries_high)
		chalenges_mediaB2016[filename]=get_media(chalenges)
		chalenges_won_mediaB2016[filename]=get_media(chalenges_won)

		for idx, y in enumerate(teamsB2016):

			dicB2016[unidecode(str(y))]=idx

			fn.write('\tnode [\n')
			fn.write('\t\tid '+str(idx)+'\n')
			fn.write('\t\tlabel '+'\"'+unidecode(str(y))+'\"'+'\n')
			write_media(shots_mediaB2016,'shots',fn)
			write_media(passes_mediaB2016,'passes',fn)
			write_media(shots_acc_mediaB2016,'shots_target',fn)
			write_media(passes_acc_mediaB2016,'passes_acc',fn)
			write_media(shots_acc_porc_mediaB2016,'shots_target_porc',fn)
			write_media(passes_acc_porc_mediaB2016,'passes_acc_porc',fn)
			write_media(possesion_mediaB2016,'possesion',fn)
			write_media(losses_mediaB2016,'losses',fn)
			write_media(losses_low_mediaB2016,'losses_low',fn)
			write_media(losses_medium_mediaB2016,'losses_medium',fn)
			write_media(losses_high_mediaB2016,'losses_high',fn)
			write_media(recoveries_mediaB2016,'recoveries',fn)
			write_media(recoveries_low_mediaB2016,'recoveries_low',fn)
			write_media(recoveries_medium_mediaB2016,'recoveries_medium',fn)
			write_media(recoveries_high_mediaB2016,'recoveries_high',fn)
			write_media(chalenges_mediaB2016,'chalenges',fn)
			write_media(chalenges_won_mediaB2016,'chalenges_won',fn)
			fn.write('\t]\n')	

	elif competition[3] == 'Brazil. Serie C' and '3' in filename:
		for idx, y in enumerate(teamsC2019):
			dicC2019[unidecode(str(y))]=idx
			fn.write('\tnode [\n')
			fn.write('\t\tid '+str(idx)+'\n')
			fn.write('\t\tlabel '+'\"'+unidecode(str(y))+'\"'+'\n')
			fn.write('\t]\n')
	elif competition[3] == 'Brazil. Serie C' and '2' in filename:
		for idx, y in enumerate(teamsC2018):
			dicC2018[unidecode(str(y))]=idx
			fn.write('\tnode [\n')
			fn.write('\t\tid '+str(idx)+'\n')
			fn.write('\t\tlabel '+'\"'+unidecode(str(y))+'\"'+'\n')
			fn.write('\t]\n')
	elif competition[3] == 'Brazil. Serie C' and '1' in filename:
		for idx, y in enumerate(teamsC2017):
			dicC2017[unidecode(str(y))]=idx
			fn.write('\tnode [\n')
			fn.write('\t\tid '+str(idx)+'\n')
			fn.write('\t\tlabel '+'\"'+unidecode(str(y))+'\"'+'\n')
			fn.write('\t]\n')
	elif competition[3] == 'Brazil. Serie C' and '3' not in filename and '2'not in filename and '1'not in filename:
		for idx, y in enumerate(teamsC2016):
			dicC2016[unidecode(str(y))]=idx
			fn.write('\tnode [\n')
			fn.write('\t\tid '+str(idx)+'\n')
			fn.write('\t\tlabel '+'\"'+unidecode(str(y))+'\"'+'\n')
			fn.write('\t]\n')		

	else: 

		for idx, y in enumerate(teamsD):
			dicD[unidecode(str(y))]=idx
			fn.write('\tnode [\n')
			fn.write('\t\tid '+str(idx)+'\n')
			fn.write('\t\tlabel '+'\"'+unidecode(str(y))+'\"'+'\n')
			fn.write('\t]\n')
	fn.close()

for filename in os.listdir(os.getcwd()):
	if 'gml' in filename:
		pass
	else:
		xls = pd.ExcelFile(filename)
		sheetX = xls.parse(0)

		competition = sheetX['Competition']
		team = sheetX['Team']
		date = sheetX['Date']
		goals = sheetX['Goals']
		match = sheetX['Match']
		shots = sheetX['Shots / on target']

		for  idx1, z in enumerate(match):
			if str(z) == 'nan':
				pass
			else:
				if idx1%2 == 0:
					if competition[3] == 'Brazil. Serie A':
						if '3' in filename:
							
							fn1 = open('result_teams_brA2019.gml','a+')
							ano = '2019'
							time_casa = unidecode(str(z.split('-')[0])).strip(' ')
							time_fora = unidecode(str(z.split('-')[1])).strip(' ')[:-4]
							gols_casa =int(z.split(' ')[-1].split(':')[0])
							gols_fora = int(z.split(' ')[-1].split(':')[1])
							if time_casa == 'Atletico PR':
								time_casa = 'Athletico Paranaense' 
							if time_fora == 'Atletico PR':
								time_fora = 'Athletico Paranaense'
							if gols_casa > gols_fora:
								matches_game = time_casa + '-' + time_fora + str(gols_casa) + '>' + str(gols_fora)
								if matches_game not in matches_resultA2019:
									matches_resultA2019.append(matches_game)
									for key in dicA2019:
										if time_casa == key:
											fn1.write('\tedge [\n')
											fn1.write('\t\tsource '+str(dicA2019[key]) +'\n')
											fn1.write('\t\ttarget '+str(dicA2019[time_fora]) +'\n')
											fn1.write('\t\tgols_casa '+str(gols_casa) +'\n')
											fn1.write('\t\tgols_fora '+str(gols_fora) +'\n')
											fn1.write('\t]\n')
										


						elif '2' in filename:
							fn1 = open('result_teams_brA2018.gml','a+')
							ano = '2018'
							time_casa = unidecode(str(z.split('-')[0])).strip(' ')
							time_fora = unidecode(str(z.split('-')[1])).strip(' ')[:-4]
							gols_casa =int(z.split(' ')[-1].split(':')[0])
							gols_fora = int(z.split(' ')[-1].split(':')[1])
							if time_casa == 'Atletico PR':
								time_casa = 'Athletico Paranaense' 
							if time_fora == 'Atletico PR':
								time_fora = 'Athletico Paranaense'
							if gols_casa > gols_fora:
								matches_game = time_casa + '-' + time_fora + str(gols_casa) + '>' + str(gols_fora)
								if matches_game not in matches_resultA2018:
									matches_resultA2018.append(matches_game)
									if gols_casa > gols_fora:
										for key in dicA2018:
											if time_casa == key:
												fn1.write('\tedge [\n')
												fn1.write('\t\tsource '+str(dicA2018[time_casa]) +'\n')
												fn1.write('\t\ttarget '+str(dicA2018[time_fora]) +'\n')
												fn1.write('\t\tgols_casa '+str(gols_casa) +'\n')
												fn1.write('\t\tgols_fora '+str(gols_fora) +'\n')
												fn1.write('\t]\n')
									elif gols_fora > gols_casa:
										for key in dicA2018:
											if time_casa == key:
												fn1.write('\tedge [\n')
												fn1.write('\t\tsource '+str(dicA2018[time_fora]) +'\n')
												fn1.write('\t\ttarget '+str(dicA2018[time_casa]) +'\n')
												fn1.write('\t\tgols_casa '+str(gols_casa) +'\n')
												fn1.write('\t\tgols_fora '+str(gols_fora) +'\n')
												fn1.write('\t]\n')

						elif '1' in filename:
							fn1 = open('result_teams_brA2017.gml','a+')
							ano = '2017'
							time_casa = unidecode(str(z.split('-')[0])).strip(' ')
							time_fora = unidecode(str(z.split('-')[1])).strip(' ')[:-4]
							gols_casa =int(z.split(' ')[-1].split(':')[0])
							gols_fora = int(z.split(' ')[-1].split(':')[1])
							if time_casa == 'Atletico PR':
								time_casa = 'Athletico Paranaense' 
							if time_fora == 'Atletico PR':
								time_fora = 'Athletico Paranaense'
							if gols_casa > gols_fora:
								matches_game = time_casa + '-' + time_fora + str(gols_casa) + '>' + str(gols_fora)
								if matches_game not in matches_resultA2017:
									matches_resultA2017.append(matches_game)
									for key in dicA2017:
										if time_casa == key:
											fn1.write('\tedge [\n')
											fn1.write('\t\tsource '+str(dicA2017[key]) +'\n')
											fn1.write('\t\ttarget '+str(dicA2017[time_fora]) +'\n')
											fn1.write('\t\tgols_casa '+str(gols_casa) +'\n')
											fn1.write('\t\tgols_fora '+str(gols_fora) +'\n')
											fn1.write('\t]\n')

						elif '3' not in filename and '2'not in filename and '1'not in filename:
							fn1 = open('result_teams_brA2016.gml','a+')
							ano = '2016'
							time_casa = unidecode(str(z.split('-')[0])).strip(' ')
							time_fora = unidecode(str(z.split('-')[1])).strip(' ')[:-4]
							gols_casa =int(z.split(' ')[-1].split(':')[0])
							gols_fora = int(z.split(' ')[-1].split(':')[1])
							if time_casa == 'Atletico PR':
								time_casa = 'Athletico Paranaense' 
							if time_fora == 'Atletico PR':
								time_fora = 'Athletico Paranaense'
							if gols_casa > gols_fora:
								matches_game = time_casa + '-' + time_fora + str(gols_casa) + '>' + str(gols_fora)
								if matches_game not in matches_resultA2016:
									matches_resultA2016.append(matches_game)
									for key in dicA2016:
										if time_casa == key:
											fn1.write('\tedge [\n')
											fn1.write('\t\tsource '+str(dicA2016[key]) +'\n')
											fn1.write('\t\ttarget '+str(dicA2016[time_fora]) +'\n')
											fn1.write('\t\tgols_casa '+str(gols_casa) +'\n')
											fn1.write('\t\tgols_fora '+str(gols_fora) +'\n')
											fn1.write('\t]\n')


				elif competition[3] == 'Brazil. Serie B':
						if '3' in filename:
							
							fn1 = open('result_teams_brB2019.gml','a+')
							ano = '2019'
							time_casa = unidecode(str(z.split('-')[0])).strip(' ')
							time_fora = unidecode(str(z.split('-')[1])).strip(' ')[:-4]
							gols_casa =int(z.split(' ')[-1].split(':')[0])
							gols_fora = int(z.split(' ')[-1].split(':')[1])
							if gols_casa > gols_fora:
								matches_game = time_casa + '-' + time_fora + str(gols_casa) + '>' + str(gols_fora)
								if matches_game not in matches_resultB2019:
									matches_resultB2019.append(matches_game)
									for key in dicB2019:
										if time_casa == key:
											fn1.write('\tedge [\n')
											fn1.write('\t\tsource '+str(dicB2019[key]) +'\n')
											fn1.write('\t\ttarget '+str(dicB2019[time_fora]) +'\n')
											fn1.write('\t\tgols_casa '+str(gols_casa) +'\n')
											fn1.write('\t\tgols_fora '+str(gols_fora) +'\n')
											fn1.write('\t]\n')
							
						elif '2' in filename:
							fn1 = open('result_teams_brB2018.gml','a+')
							ano = '2018'
							time_casa = unidecode(str(z.split('-')[0])).strip(' ')
							time_fora = unidecode(str(z.split('-')[1])).strip(' ')[:-4]
							gols_casa =int(z.split(' ')[-1].split(':')[0])
							gols_fora = int(z.split(' ')[-1].split(':')[1])
							if gols_casa > gols_fora:
								matches_game = time_casa + '-' + time_fora + str(gols_casa) + '>' + str(gols_fora)
								if matches_game not in matches_resultB2018:
									matches_resultB2018.append(matches_game)
									for key in dicB2018:
										if time_casa == key:
											fn1.write('\tedge [\n')
											fn1.write('\t\tsource '+str(dicB2018[key]) +'\n')
											fn1.write('\t\ttarget '+str(dicB2018[time_fora]) +'\n')
											fn1.write('\t\tgols_casa '+str(gols_casa) +'\n')
											fn1.write('\t\tgols_fora '+str(gols_fora) +'\n')
											fn1.write('\t]\n')

						elif '1' in filename:
							fn1 = open('result_teams_brB2017.gml','a+')
							ano = '2017'
							time_casa = unidecode(str(z.split('-')[0])).strip(' ')
							time_fora = unidecode(str(z.split('-')[1])).strip(' ')[:-4]
							gols_casa =int(z.split(' ')[-1].split(':')[0])
							gols_fora = int(z.split(' ')[-1].split(':')[1])
							if gols_casa > gols_fora:
								matches_game = time_casa + '-' + time_fora + str(gols_casa) + '>' + str(gols_fora)
								if matches_game not in matches_resultB2017:
									matches_resultB2017.append(matches_game)
									for key in dicB2017:
										if time_casa == key:
											fn1.write('\tedge [\n')
											fn1.write('\t\tsource '+str(dicB2017[key]) +'\n')
											fn1.write('\t\ttarget '+str(dicB2017[time_fora]) +'\n')
											fn1.write('\t\tgols_casa '+str(gols_casa) +'\n')
											fn1.write('\t\tgols_fora '+str(gols_fora) +'\n')
											fn1.write('\t]\n')

						elif '3' not in filename and '2'not in filename and '1'not in filename:

							fn1 = open('result_teams_brB2016.gml','a+')
							ano = '2016'
							time_casa = unidecode(str(z.split('-')[0])).strip(' ')
							time_fora = unidecode(str(z.split('-')[1])).strip(' ')[:-4]
							gols_casa =int(z.split(' ')[-1].split(':')[0])
							gols_fora = int(z.split(' ')[-1].split(':')[1])
							if gols_casa > gols_fora:
								matches_game = time_casa + '-' + time_fora + str(gols_casa) + '>' + str(gols_fora)
								if matches_game not in matches_resultB2016:
									matches_resultB2016.append(matches_game)
									for key in dicB2016:
										if time_casa == key:
											fn1.write('\tedge [\n')
											fn1.write('\t\tsource '+str(dicB2016[key]) +'\n')
											fn1.write('\t\ttarget '+str(dicB2016[time_fora]) +'\n')
											fn1.write('\t\tgols_casa '+str(gols_casa) +'\n')
											fn1.write('\t\tgols_fora '+str(gols_fora) +'\n')
											fn1.write('\t]\n')


				elif competition[3] == 'Brazil. Serie C':
						if '3' in filename:
							
							fn1 = open('result_teams_brC2019.gml','a+')
							ano = '2019'
							time_casa = unidecode(str(z.split('-')[0])).strip(' ')
							time_fora = unidecode(str(z.split('-')[1])).strip(' ')[:-4]
							gols_casa =int(z.split(' ')[-1].split(':')[0])
							gols_fora = int(z.split(' ')[-1].split(':')[1])
							if time_casa == 'Atlético PR':
								time_casa = 'Athletico Paranaense' 
							if time_fora == 'Atlético PR':
								time_fora = 'Athletico Paranaense'
							if gols_casa > gols_fora:
								matches_game = time_casa + '-' + time_fora + str(gols_casa) + '>' + str(gols_fora)
								if matches_game not in matches_resultC2019:
									matches_resultC2019.append(matches_game)
									for key in dicC2019:
										if time_casa == key:
											fn1.write('\tedge [\n')
											fn1.write('\t\tsource '+str(dicC2019[key]) +'\n')
											fn1.write('\t\ttarget '+str(dicC2019[time_fora]) +'\n')
											fn1.write('\t\tgols_casa '+str(gols_casa) +'\n')
											fn1.write('\t\tgols_fora '+str(gols_fora) +'\n')
											fn1.write('\t]\n')

				#IMPLEMENTAR APÓS DOWNLOAD JOGOS SERIE C


fn = open('result_teams_brA2019.gml','a')
fn.write(']\n')
fn.close()
fn = open('result_teams_brB2019.gml','a')
fn.write(']\n')
fn.close()
fn = open('result_teams_brC2019.gml','a')
fn.write(']\n')
fn.close()
fn = open('result_teams_bretc2019.gml','a')
fn.write(']\n')
fn = open('result_teams_brA2018.gml','a')
fn.write(']\n')
fn.close()
fn = open('result_teams_brB2018.gml','a')
fn.write(']\n')
fn.close()
fn = open('result_teams_brC2018.gml','a')
fn.write(']\n')
fn.close()
fn = open('result_teams_bretc2018.gml','a')
fn.write(']\n')
fn.close()
fn = open('result_teams_brA2017.gml','a')
fn.write(']\n')
fn.close()
fn = open('result_teams_brB2017.gml','a')
fn.write(']\n')
fn.close()
fn = open('result_teams_brC2017.gml','a')
fn.write(']\n')
fn.close()
fn = open('result_teams_bretc2017.gml','a')
fn.write(']\n')
fn.close()
fn = open('result_teams_brA2016.gml','a')
fn.write(']\n')
fn.close()
fn = open('result_teams_brB2016.gml','a')
fn.write(']\n')
fn.close()
fn = open('result_teams_brC2016.gml','a')
fn.write(']\n')
fn.close()
fn = open('result_teams_bretc2016.gml','a')
fn.write(']\n')
fn.close()