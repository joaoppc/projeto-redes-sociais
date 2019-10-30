from unidecode import unidecode
import os
import pandas as pd
from statistics import mean


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
	return media

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
	shots = sheetX['Shots / on target']
	passes = sheetX['Passes / accurate']



	
	if competition[3] == 'Brazil. Serie A':
		if '3' in filename:
			fn = open('result_teams_brA2019.gml','w+')
			print(filename)
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
		'''
		shots_team=[]
		pass_team=[]
		
		for idg, p in enumerate(passes):
			if str(p) == 'nan':
				pass
			else:
				if idg%2 == 0:
					pass_team.append(p)
		media = mean(pass_team)
		passes_mediaA2019[filename]=media

		for idxz, i in enumerate(shots):
			if str(i) == 'nan':
				pass
			else:
				if idxz%2==0:
					shots_team.append(i)
		media = mean(shots_team)
'''
		shots_mediaA2019[filename]=get_media(shots)
		for idx, y in enumerate(teamsA2019):
			dicA2019[unidecode(str(y))]=idx
			fn.write('\tnode [\n')
			fn.write('\t\tid '+str(idx)+'\n')
			fn.write('\t\tlabel '+'\"'+unidecode(str(y))+'\"'+'\n')
			for key in shots_mediaA2019:
				if y in key:
					fn.write('\t\tmedia '+'\"'+unidecode(str(shots_mediaA2019[key]))+'\"'+'\n')
			fn.write('\t]\n')
	elif competition[3] == 'Brazil. Serie A' and '2' in filename:
		'''
		shots_team=[]
		for idxz, i in enumerate(shots):
			if str(i) == 'nan':
				pass
			else:
				if idxz%2==0:
					shots_team.append(i)
		media = mean(shots_team)
		'''
		shots_mediaA2018[filename]=get_media(shots)
		for idx, y in enumerate(teamsA2018):
			dicA2018[unidecode(str(y))]=idx
			fn.write('\tnode [\n')
			fn.write('\t\tid '+str(idx)+'\n')
			for key in shots_mediaA2018:
				if y in key:
					fn.write('\t\tmedia '+'\"'+unidecode(str(shots_mediaA2018[key]))+'\"'+'\n')
			fn.write('\t\tlabel '+'\"'+unidecode(str(y))+'\"'+'\n')
			fn.write('\t]\n')
	elif competition[3] == 'Brazil. Serie A' and '1' in filename:
		'''
		shots_team=[]
		for idxz, i in enumerate(shots):
			if str(i) == 'nan':
				pass
			else:
				if idxz%2==0:
					shots_team.append(i)
		media = mean(shots_team)
		'''
		shots_mediaA2017[filename]=get_media(shots)
		for idx, y in enumerate(teamsA2017):
			dicA2017[unidecode(str(y))]=idx
			fn.write('\tnode [\n')
			fn.write('\t\tid '+str(idx)+'\n')
			for key in shots_mediaA2017:
				if y in key:
					fn.write('\t\tmedia '+'\"'+unidecode(str(shots_mediaA2017[key]))+'\"'+'\n')
			fn.write('\t\tlabel '+'\"'+unidecode(str(y))+'\"'+'\n')
			fn.write('\t]\n')
	elif competition[3] == 'Brazil. Serie A' and '3' not in filename and '2'not in filename and '1'not in filename:
		'''
		shots_team=[]
		for idxz, i in enumerate(shots):
			if str(i) == 'nan':
				pass
			else:
				if idxz%2==0:
					shots_team.append(i)
		media = mean(shots_team)
		'''
		shots_mediaA2016[filename]=get_media(shots)
		for idx, y in enumerate(teamsA2016):
			dicA2016[unidecode(str(y))]=idx
			fn.write('\tnode [\n')
			fn.write('\t\tid '+str(idx)+'\n')
			for key in shots_mediaA2016:
				if y in key:
					fn.write('\t\tmedia '+'\"'+unidecode(str(shots_mediaA2016[key]))+'\"'+'\n')
			fn.write('\t\tlabel '+'\"'+unidecode(str(y))+'\"'+'\n')
			fn.write('\t]\n')

	elif competition[3] == 'Brazil. Serie B' and '3' in filename:
		'''
		shots_team=[]
		for idxz, i in enumerate(shots):
			if str(i) == 'nan':
				pass
			else:
				if idxz%2==0:
					shots_team.append(i)
		media = mean(shots_team)
		'''
		shots_mediaB2019[filename]=get_media(shots)
		for idx, y in enumerate(teamsB2019):
			dicB2019[unidecode(str(y))]=idx
			fn.write('\tnode [\n')
			fn.write('\t\tid '+str(idx)+'\n')
			for key in shots_mediaB2019:
				if y in key:
					fn.write('\t\tmedia '+'\"'+unidecode(str(shots_mediaB2019[key]))+'\"'+'\n')
			fn.write('\t\tlabel '+'\"'+unidecode(str(y))+'\"'+'\n')
			fn.write('\t]\n')	
		#print('2019b')
	elif competition[3] == 'Brazil. Serie B' and '2' in filename:
		'''
		shots_team=[]
		for idxz, i in enumerate(shots):
			if str(i) == 'nan':
				pass
			else:
				if idxz%2==0:
					shots_team.append(i)
		media = mean(shots_team)
		'''
		shots_mediaB2018[filename]=get_media(shots)
		for idx, y in enumerate(teamsB2018):
			dicB2018[unidecode(str(y))]=idx
			fn.write('\tnode [\n')
			fn.write('\t\tid '+str(idx)+'\n')
			for key in shots_mediaB2018:
				if y in key:
					fn.write('\t\tmedia '+'\"'+unidecode(str(shots_mediaB2018[key]))+'\"'+'\n')
			fn.write('\t\tlabel '+'\"'+unidecode(str(y))+'\"'+'\n')
			fn.write('\t]\n')
	elif competition[3] == 'Brazil. Serie B' and '1' in filename:
		shots_team=[]
		for idxz, i in enumerate(shots):
			if str(i) == 'nan':
				pass
			else:
				if idxz%2==0:
					shots_team.append(i)
		media = mean(shots_team)
		shots_mediaB2017[filename]=media
		for idx, y in enumerate(teamsB2017):
			dicB2017[unidecode(str(y))]=idx
			fn.write('\tnode [\n')
			fn.write('\t\tid '+str(idx)+'\n')
			for key in shots_mediaB2017:
				if y in key:
					fn.write('\t\tmedia '+'\"'+unidecode(str(shots_mediaB2017[key]))+'\"'+'\n')
			fn.write('\t\tlabel '+'\"'+unidecode(str(y))+'\"'+'\n')
			fn.write('\t]\n')
	elif competition[3] == 'Brazil. Serie B' and '3' not in filename and '2'not in filename and '1'not in filename:
		'''
		shots_team=[]
		for idxz, i in enumerate(shots):
			if str(i) == 'nan':
				pass
			else:
				if idxz%2==0:
					shots_team.append(i)
		media = mean(shots_team)
		'''
		shots_mediaB2016[filename]=get_media(shots)
		for idx, y in enumerate(teamsB2016):
			dicB2016[unidecode(str(y))]=idx
			fn.write('\tnode [\n')
			fn.write('\t\tid '+str(idx)+'\n')
			for key in shots_mediaB2016:
				if y in key:
					fn.write('\t\tmedia '+'\"'+unidecode(str(shots_mediaB2016[key]))+'\"'+'\n')
			fn.write('\t\tlabel '+'\"'+unidecode(str(y))+'\"'+'\n')
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
									for key in dicA2018:
										if time_casa == key:
											fn1.write('\tedge [\n')
											fn1.write('\t\tsource '+str(dicA2018[key]) +'\n')
											fn1.write('\t\ttarget '+str(dicA2018[time_fora]) +'\n')
											fn1.write('\t\tgols_casa '+str(gols_casa) +'\n')
											fn1.write('\t\tgols_fora '+str(gols_fora) +'\n')
											fn1.write('\t\tshots '+str(shots[2:7]) +'\n')
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