n = float(input('Qundos metros te a sua parede:'))
km = n / 1000
hm = n / 100
dam = n / 10
dm = n * 10
cm = n * 100
mm = n * 1000
print('Em kilometros a sua parede mede {:3f}km \n Em dacametros a sua parede mede {:3f}dam \n Em decimtros a sua parede mede {:3f} \n Em centimetros a sua parede mede {:2}cm \n Em melimetros meede{:2f}mm'.format(km, hm, dam, dm, cm, mm))
