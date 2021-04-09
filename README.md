# fizz-buzz-python
Jeu Fizz Buzz en Python

##Install
```
python setup.py install
```

##Lancer le jeu
run.py prends en entrée un chiffre et un nom de jeu<br/>
exemple
```
run.py 1 Fizz
```

##Règles du jeu
Si le jeu est **Fizz** alors les règles sont les suivantes :<br/>
- Si le chiffre contient un deux ou est un multiple de deux alors le programme doit repondre **Fizz**, sinon il doit repondre le chiffre fourni en entrée.<br/>

Si le jeu est **Buzz** alors les règles sont les suivantes :<br/>
- Si le chiffre contient un cinq ou est un multiple de cinq alors le programme doit repondre **Buzz**, sinon il doit repondre le chiffre fourni en entrée.<br/>

Si le jeu est **FizzBuzz** alors les règles sont les suivantes :<br/>
- Si le chiffre contient un deux et un cinq ou qu'il est multiple de deux et de cinq alors le programme doit repondre **Fizz-Buzz**<br/>
- Si le chiffre contient un deux ou est un multiple de deux alors le programme doit repondre **Fizz**, sinon il doit repondre le chiffre fourni en entrée.<br/>
- Si le chiffre contient un cinq ou est un multiple de cinq alors le programme doit repondre **Buzz**, sinon il doit repondre le chiffre fourni en entrée.<br/>

##Lancer les test
Pour lancer les test il suffit de faire
```
python -m pytest test
```