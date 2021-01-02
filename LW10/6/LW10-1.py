import io

with io.open('input.txt','r', encoding='utf-8') as inp:
    inp = inp.read().splitlines()

with open('output.txt', 'w') as out:
    schedule = { 'Математика лекция': 0,
              'Математика практика': 0,
              'АлоВТ лабораторная': 0,
              'Английский лекция': 0,
              'Лекция ОАиП': 0,
              'Лаборатория ОАиП': 0,
              'Лекция ИПО': 0,
              'Практика ИПО': 0,
              'Математика лекция': 0,
              'ММ лабораторная': 0,
              'Практика ИПО': 0,
              'ММ лекция': 0,
              'Лекция ИПО': 0,
              'Лекция ТРПО': 0,
              'Практика ИПО': 0,
	    }
    for i in inp:
        for j in i.split():
            if j == 'лекция':
                schedule[i] += 1
            if j == 'практика':
                schedule[i] += 1
            if j == 'лабораторная':
                schedule[i] += 1
    for i in schedule:
        print(i,': ',schedule[i],end ='\n', file=out)



