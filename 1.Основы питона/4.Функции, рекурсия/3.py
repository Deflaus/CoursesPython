listt = ['2018-01-01', 'yandex', 'cpc', 100]

def rek(listt):
	if len(listt) > 2:
		return {listt[0] : rek(listt[1:])}
	else:
		return {listt[0] : listt[1]}


print(rek(listt))