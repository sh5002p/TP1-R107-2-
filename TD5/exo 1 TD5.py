Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> nom = "Soul"
>>> prenom = "of cinder"
>>> math = 15
>>> anglais = 17
>>> info = 13
>>> promotion = 2024
>>> type(nom)
<class 'str'>
>>> KeyboardInterrupt
>>> type(nom, prenom, math, anglais, info, promotion)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    type(nom, prenom, math, anglais, info, promotion)
TypeError: type() takes 1 or 3 arguments
>>> type(prenom)
<class 'str'>
>>> moy = (math + anglais + info)/3
>>> print("L'étudiant {} {} de la promotion {} a une moyenne de {}".format(nom, prenom, promotion, moy))
L'étudiant Soul of cinder de la promotion 2024 a une moyenne de 15.0
