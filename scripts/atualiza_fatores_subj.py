def getVetScore(aval):
	vet_score = [0, 0, 0, 0, 0, 0]

	if aval.q1_perdeu_peso == 1 and aval.q1_perdeu_peso_kg >= 4.5:
		vet_score[0] = 1

	if aval.q2_ativ_fisica == 1:
		vet_score[1] = 1

	if aval.q3_red_forca == 1:
		vet_score[2] = 1

	if aval.q4_red_caminhada == 1:
		vet_score[3] = 1

	if aval.q5_fadiga in (4, 3):
		vet_score[4] = 1

	if aval.q6_desanimo in (4, 3):
		vet_score[5] = 1		

	return vet_score

def getFragilidade_VetScore(aval):
	vet_score = getVetScore(aval)
	score = sum(vet_score)

	# questão 5 e 6 juntas podem pontuar no máximo 1
	if vet_score[4] == 1 and vet_score[5] == 1:
		score -= 1

	# Não frágil
	if score == 0:
		return 'N', vet_score
	# Pré-Frágil
	elif score < 3:
		return 'P', vet_score
	# Frágil
	else:
		return 'F', vet_score		


import django
django.setup()

from ppsus_app.models import Subjetiva
from ppsus_app.src.functions import getFatores

subjetivas = Subjetiva.objects.all()

for sub in subjetivas:
	# atualiza subjetiva
	fragilidade, vet_score = getFragilidade_VetScore(sub)
	sub.fatores = getFatores('subjetiva', fragilidade, vet_score)
	sub.save()