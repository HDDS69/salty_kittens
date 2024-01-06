from random import * 
plaer = int(input("первоначальные настройки \nсколько игроков будут играть?"))
coli = int(input("сколько соли надо получить"))
listforgamer = []
#оснойной класс игрока
class player:  
     
     def __init__(self,name):
         self.__имя = name
         self.стамина = 10
         self.соль = 0
         self.xp = 3 
         self.ключи = 0

# проверки
     def __xpbar__(self):
         if self.xp <= 0 :
             print("игрок",self.имя," умер")
             return 2
         elif self.соль == coli and self.xp > 0:
             print("игрок",self.имя,"победил")
             return 1
         else:
             return 0
             return self.xp
             return self.соль
     def __solebar__(self):
         if self.соль <= 0 :
             print("у игрока",self.имя," 0 соли")
             play.соль = 0
             return 0
         else:
             return 1
             return self.xp
     def minusbar(self,стамина,other):
         if self.стамина < other :
             print("у игрока",self.имя," не достаточно стамины")
             return self.стамина
             return 0
         elif self.стамина <= 0:
             print("у игрока",self.имя," 0 стамины")
             play.стамина = 0
             return 0
         else:
             return 1
             return self.стамина
     def __keybar__(self,ключи,other):
             if self.ключи <= 0:
                 print("у игрока",self.имя," 0 ключей")
                 play.ключи = 0
                 return 0
             else:
                 return 1
                 return self.ключи
         
     
# класс мобов
class mob():
    def __init__(self):
        nama = ["Бомжик аид","Ишак","Лох чилийский"," Пипохуй","Рыглан","Теребло","Сотрудник ашана","Рыгозавр","Членосос","Гравий","Зум дар дар","Мусье еблан","Чубрик"," Пвгуд","Пубертатная язва","Пузатый челек"," Ренат Гослибенков","Фейхуя"]
        i = len(nama) - 1
        xp = randint(1,3)
        nam = randint(0,i)
        self.имя = nama[nam]
        self.xp = xp
        print("перед вами враг: ",nama[nam], xp,"хп")
    def __urone__(self,xp):
        urone = randint(1,2)
        otvet = randint(1, 6)
        game = int(input("ваше действие\n1 - ударить \n2 - уйти"))
        if game == 1 and play.minusbar(play.стамина,self.xp)==1:
            if otvet == 1 :
             print("по вам попали и нанесли урон в 1 хп \nвы убили врага")
             play.соль =play.соль+1
             play.xp =-urone
             play.стамина =play.стамина-self.xp
             self.xp = 0
             if otvet == 3:
              print("вы получили 1 соль и 1 ключ")
              play.ключи =play.ключи+1
              return self.xp
             else:
              print("вы получили одну соль")
              play.соль =+1
              return self.xp
            else:
             print("по вам промахнулись \nвы убили врага")
             play.соль = play.соль+1
             play.стамина = play.стамина- self.xp
             self.xp = 0
             if otvet == 3:
              print("вы получили 1 соль и 1 ключ")
              play.ключи =+1
              return self.xp
             else:
               print("вы получили одну соль")
               return self.xp
        else:
            if otvet == 1 or 2 or 3:
             print("по вам попали -1 хп ")
             play.xp = play.xp-urone
            else:
                print("по вам промохнулись")
                
#класс обьектов                
class objekt():
     def __obj__(self):
         name = ["коробка","дерево","гора","пустырь","пустой дом","сундук","мошеник","ловушка"]
         x = len(name) - 1
         i = randint(0, x)
         self.name = name[i]
         if self.name == "коробка":
             print("вы нашли коробку \nваша стамина востоновленна")
             play.стамина = 10
             print(play.__dict__)
         elif self.name == "сундук":
             vibor = int(input("ты нашёл сундук \n1 - открыть(1ключ) \n2 - пройти мимо"))
             if vibor == 1 and play.__keybar__(play.ключи,1)==1:
              print("вы нашли 1 соль")
              play.ключи =play.ключи-1
              play.соль =play.соль+1
             else:
              print("ну ладно")
         elif self.name == "мошеник":
             x = randint(1,2)
             if x == 1 and play.__solebar__()==1:
                 print("вас обокрал мошеник он украл 1 соль")
                 play.соль =play.соль-1
             elif x == 2 and play.__keybar__(play.ключи,1) == 1:
                 print("вас обокрал мошеник он украл 1 ключ")
                 play.ключи =play.ключи-1
             else:
                 print("мошеник - ты настолько беден что у тебя нечего красть")
         elif self.name == "ловушка":
              print("вы попали в ловушку \n-1 хп ")
              play.xp = play.xp-1
         elif self.name == "гора" :
              vibor = int(input("ты нашёл гору \n1 - забраться(2стамины) \n2 - пройти мимо"))
              if vibor == 1 and play.minusbar(play.стамина,2) == 1:
               print("вы нашли 1 соль")
               play.стамина = play.стамина-2
               play.соль =play.соль +1
              else:
               print("ну ладно")
         elif self.name == "дерево":
             print("дерево(пустая клетка)")
         elif self.name == "пустой дом":
             print("пустой дом(пустая клетка)")
         elif self.name == "пустырь":
             print("пустырь(пустая клетка)")
         else:
             print("кажеться вы в пустоте")
          
def xod():
    x = randint(1,5)
    if x == 2:
        c = mob()
        c.__urone__(c.xp)
    else:
        v = objekt()
        v.__obj__()
def namestart():   
 for i in range(plaer):
  name = input("введите имя котика")
  play = player(name)
  listforgamer.append(play)

namestart()
while True:
  a = 1
  for i in range(len(listforgamer)):
     play = listforgamer[i]
     s = listforgamer[i]
     print("ход игрока =",play.__dict__)
     if play.__xpbar__() == 0:
       viber = int(input("ваше действие : \n1 - вынюхать соль(востоновить здоровье)(потратить 1 соль) \n2 - пойти вперёд"))
       if viber == 1 :
           if play.__solebar__() == 1 :
             print("ваше хп востоновленна")
             play.соль =play.соль -1
             play.xp = 3
             xod()
           else:
             print("возрощайся когда будет больше 0 соли")
             xod()
       else:
           xod()
     elif play.__xpbar__() == 2:
          print("пропуск хода")
     else:
        a = 2
        break
  
  if a == 2:
   break 
  else:
   print(" ")