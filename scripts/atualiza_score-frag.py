def getScore(aval, tipo):
	score = 0

	# avaliação subjetiva
	if tipo == 's':
		if aval.q1_perdeu_peso == 1 and aval.q1_perdeu_peso_kg >= 4.5:
			score += 1

		if aval.q2_ativ_fisica == 1:
			score += 1

		if aval.q3_red_forca == 1:
			score += 1

		if aval.q4_red_caminhada == 1:
			score += 1

		if aval.q5_fadiga in (4, 3) or aval.q6_desanimo in (4, 3):
			score += 1

	# avaliação edmonton
	else:
		score += aval.q1_cognicao - 1

		score += aval.q2_estado_saude_A - 1

		if aval.q2_estado_saude_B >= 4:
			score += aval.q2_estado_saude_B - 3

		qtd = len(aval.q3_ind_func)
		if qtd >= 5:
			score += 2
		elif qtd >= 2:
			score += 1

		score += aval.q4_sup_social - 1

		if aval.q5_medicamento_A == 1:
			score += 1

		if aval.q5_medicamento_B == 1:
			score += 1

		if aval.q6_nutricao == 1:
			score += 1

		if aval.q7_humor == 1:
			score += 1

		if aval.q8_continencia == 1:
			score += 1

		score += aval.q9_desemp_func - 1

	return score

def getFragilidade(aval, score, tipo):

	# avaliação subjetiva
	if tipo == 's':
		# Não frágil
		if score == 0:
			return 'N'
		# Pré-Frágil
		elif score < 3:
			return 'P'
		# Frágil
		else:
			return 'F'
			
	# avaliação edmonton
	else:
		# Não apresenta fragilidade
		if score <= 4:
			return 'N'
		# Aparentemente vulnerável
		elif score <= 6:
			return 'V'
		# Fragilidade leve
		elif score <= 8:
			return 'L'
		# Fragilidade moderada
		elif score <= 10:
			return 'M'
		# Fragilidade severa
		else:
			return 'S'

import django
django.setup()

from ppsus_app.models import Subjetiva, Edmonton

subjetivas = Subjetiva.objects.all()
edmontons = Edmonton.objects.all()

for sub, edm in zip(subjetivas, edmontons):
	# atualiza subjetiva
	sub.score = getScore(sub, 's')
	sub.fragilidade = getFragilidade(sub, sub.score, 's')
	sub.save()
	# atualiza edmonton
	edm.score = getScore(edm, 'e')
	edm.fragilidade = getFragilidade(edm, edm.score, 'e')
	edm.save()

