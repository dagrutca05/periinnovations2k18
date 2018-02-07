# Игра в кости: 
# 1. Играют два человека
# 2. У каждого есть запас денег
# 3. В начале игры каждый игрок делает ставку
# 4. Затем побрасываются кубики
# 5. Тот, у кого очков больше, забирает ставку
# 6. Игра идет до тех пор, пока один из игроков
# не обанкротится
import random

player_one = {'счет': 1000}
player_two = {'счет': 1000}
player_three = {'счет': 1000}

player_one['имя'] = input('Имя первого игрока: ')
player_two['имя'] = input('Имя второго игрока: ')
player_three['имя'] = input('Имя третьего игрока: ')

while True:
  player_one['ставка'] = int(input("Первый игрок ставит: "))
  player_two['ставка'] = int(input("Второй игрок ставит: "))
  player_three['ставка'] = int(input("Третий игрок ставит: "))

  player_one['бросок'] = random.randint(2, 12)
  player_two['бросок'] = random.randint(2, 12)
  player_three['бросок'] = random.randint(2, 12) 

  print('У первого игрока выпало ', player_one['бросок'], 'очков')
  print('У второго игрока выпало ', player_two['бросок'], 'очков')
  print('У третьего игрока выпало ', player_two['бросок'], 'очков')

  if player_one['бросок'] > player_two['бросок']:
    print("Первый игрок выиграл ставку")
    player_one['счет'] += player_two['ставка'] and layer_two['счет'] += player_two['ставка'] and player_three['счет'] += player_two and player_one['ставка']
     player_one['счет'] -= player_two['ставка'] and layer_two['счет'] -= player_two['ставка'] and player_three['счет'] -= player_two and player_one['ставка']
  elif player_one['бросок'] < player_two['бросок']:
    print("Второй игрок выиграл ставку")
    player_two['счет'] -= player_one['ставка'] and player_one['счет'] += player_one['ставка'] and player_three['бросок'] += player_two['бросок']
    player_two['счет'] -= player_one['ставка'] and player_one['счет'] -= player_one['ставка'] and player_three['бросок'] -= player_two['бросок']
  elif player_one['бросок'] < player_two['бросок']
    print("Третий игрок выиграл ставку")
    player_two['счет'] += player_one['ставка'] and player_one['счет'] += player_one['ставка'] and player_three['бросок'] += player_two['бросок']
    player_two['счет'] -= player_one['ставка'] and player_one['счет'] -= player_one['ставка'] and player_three['бросок'] -= player_two['бросок']
  else:
    print("Ничья")

  print("У первого игрока на счету ", player_one['счет'])
  print("У второго игрока на счету ", player_two['счет'])
  print("У третьего игрока на счету ", player_two['счет'])
  if player_one['счет'] <= 0:
    print('Первый игрок обанкротился. Второй игрок выиграл')
    break
  if player_two['счет'] <= 0:
    print('Второй игрок обанкротился. Первый игрок выиграл')
    break
  if player_two['счет'] <= 0:
    print('Третий игрок обанкротился. Первый игрок выиграл')
    break