import random
def create():
  person = {
    'hp': 200,
    'damage': 30,
    "defend":  3
  }
  
  person['name'] = input('Введите имя персонажа: ')
  cho = int(input("""Выберите класс
  1 -Reaper 
  2-Gorilla
  3-Mage
"""))
  if cho == 1:
    person['hp'] += 50  
    person["damage"] += 13
  elif cho == 2:
    person["hp"] += 2  
    person["damage"] += 27
  else:
    person["hp"] += 25
    person["damage"] += 17
  
  armor = int(input("""Выбирети броню
  1 - spetsnaz
  2 - swat
  3 - military 
""")) 
  if armor == 1:
    person["defend"] += 10
    person["damage"] -=7
  elif armor == 2:  
    person["defend"] += 15
    person["damage"] -= 12
  else: 
    person["defend"] += 18
    person["damage"] -= 15
  
  gune = int(input("""Выберите оружее
  1 - AK-47
  2 - Драгунов
  3 - BBC Винтарез
"""))
  if gune == 1:
    person["damage"] += 13
    person["hp"] -= 20
  elif gune == 2:
    person["damage"] += 18
    person["hp"] -= 40
  else:
    person["damage"] += 23
    person["hp"] -= 60
  
  return person

def fight(damager, defender):
  real_damage = damager['damage'] + random.randint(-damager["damage"],10) - defender["defend"]
  print(damager['name'], 'наносит', real_damage, 'урона', defender['name'])
  if real_damage <=0:
    print(defender["name"],"Забрал hp y", damager["name"])
  defender['hp'] -= real_damage

def health_info(person):
  print('У', person['name'], 'осталось', person['hp'], 'здоровья')

player_1 = create()
player_2 = create()

while True:
  fight(player_1, player_2)
  fight(player_2, player_1)
  health_info(player_1)
  health_info(player_2)

  if player_2['hp'] <= 0:
    print(player_2['name'], 'сдох')
    break

  if player_1['hp'] <= 0:
    print(player_1['name'], 'сдох')
    break
  input()
