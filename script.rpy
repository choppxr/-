define a = Character('Алина', color="#553f63")
define n = Character('Настя', color="#553f63")

define audio.baby = 'audio/lana.mp3'
define audio.mitsk = 'audio/mitski.mp3'
transform lefter:
    xalign 0.7
label start:
    play music baby
    scene main
    with Fade(0.5, 0.0, 0.5, color = '#bea7c9')

    show al 1 with dissolve
    pause 3
    show al 3 with dissolve
    pause 1
    show al 2 with dissolve
    pause 3
#    hide al 2 with dissolve
    
    scene nas 1
    with Fade(0.5, 0.0, 0.5, color = '#4d4153')
    pause
    
    
    scene main
    with Fade(0.5, 0.0, 0.5, color = '#4d4153')
    show alin with dissolve
    a '(Только вышли из засады, организованной конкурирующей группировкой. Перестрелка была жестокой и короткой.)' with dissolve
    a '(Я потеряла большую часть своих товарищей во время этого события.)'
    a '(Все выжившие разминулись по разным сторонам и потеряли друг друга из вида.)'
    a '(Хоть жертвы масштабные, долг был выполнен не полностью – часть награбленного осталась у противников, – но выжить удалось.)'
    a '(Теперь моя цель – добраться до безопасного места, расположенного на другом конце города, до того, как меня обнаружат.)'
    a '(Преследователи могут быть где угодно, выжидая удобного момента для удара. {w}Нужно как можно скорее..)'
    hide alin
    show al 8 at zoomin with vpunch
    a '...' with dissolve
   # hide al 8 with dissolve
    show alin1 at lefter
    hide al 8
    a '(Рана в плече хоть и лёгкая, но ноет ужасно.)' with dissolve
    a '(Времени в обрез. Нужно выбираться отсюда.)'
    
    scene main 1 with Fade(1, 0.0, 1, color = '#4d4153')
    show nas 2 with dissolve
    show al 13 with dissolve   
    show al 14 with dissolve
    pause 3
    
    scene arm with Fade(2, 1, 2, color = '#4d4153')
    pause 1
    scene arm 1
    pause 1
    scene arm
    pause 1
    scene arm 1
    pause 1
    scene arm
    pause 1
    scene arm 1
    pause 1
    
   
    
    scene main with Fade(3, 1, 3, color = '#4d4153')
    show alin2 with dissolve
    pause
    show alin3
    pause 3
    scene main 2 with Fade(3, 2, 1, color = '#4d4153')
    show us 1 with dissolve
    pause
    scene main 2
    show nast
    n '(Че с ней?)' with dissolve
    scene pis 
    pause
    scene main with Fade(1, 1, 1, color = '#4d4153')
    show alin3 with dissolve
    pause 3
    show al 3 with vpunch
    n 'Эй' with dissolve
    scene main 1 with Fade(2, 1, 1, color = '#4d4153')
    show one with dissolve
    show nast1 with dissolve
    show alina with dissolve
    pause
    show nast2
    n 'С тобой нормально всё? Помочь? У меня бинты все дела.' with dissolve
    hide nast2
    show nast1
    show alin 4
    show alin 5
    pause 2
    show alin 4
    show nast2 
    n 'И чего молчишь? У тебя кровь течёт, ты о чём думаешь-то?' with dissolve
    hide nast2
    show nast1
    show alin 4
    show alin 5
    pause 2
    show alin 4
    show alin 6
    a 'Не твоё дело.'
    show alin 7
    a 'Я не собираюсь получать помощь от тех, кто убивает моих людей.'
    a 'Из-за вашего главаря и всей группировки мои товарищи мертвы напрасно, ваша подлость и чревоугодие затмили всё живое.'
    a 'И какой смысл мне доверять тебе?'
    show alin 8
    show alin 9
    pause 1
    show alin 3
    window hide
    pause 10
    show nas 9
    n 'Нет, ну если ты желаешь умереть от потери крови или упасть в обморок, после чего попасть в плен, то ладно. {w}Делай, как знаешь.'
    hide nast2
    hide nast1
    hide nas 9 with moveoutleft
    show alin 9
    pause
    scene main 3 with Fade(2, 1, 1, color = '#4d4153')
    pause
    a 'Ладно, погоди...' with dissolve
    window hide 
    pause
    scene maim 4 with dissolve
    n 'Так, всё. Я обработала тебе рану.' with dissolve
    n 'Бинт наложила, заживёт.'
    window hide
    pause
    a 'Спасибо.' with dissolve
    window hide
    pause
    scene main 5 with Fade(3, 2, 1, color = '#4d4153')
    play music mitsk
    show uss with dissolve
    pause
    show us 4
    a 'Зачем вы всё это делаете? Занимаетесь нарокоторговлей в подполье, занимаетесь чёрным бизнесом по-полному.'
    a 'В битвах играете по-грязному, даже не знаю, есть ли у тебя и у твоих понятие морали и нравственных ценностей.'
    show us 5
    pause
    show us 6
    n 'Ваша команда все наши биткоины в 2007 украла. {w}Мы мстим.'
    show uss1
    pause
    hide uss1
    show us 9
    a 'Понятно.'
    show us 7
    pause 3
    show us 6
    n 'С днём рождения!'
    show us 7
    pause
    show us 9
    a 'Спасибо.'
    show us 7
    pause
    scene main 3 with Fade(2, 1, 1, color = '#4d4153')
    pause
    return 

image alin:
    "al 4"
    choice:
        pause 2
    choice:
        pause 4
    "al 5"
    pause 0.25
    repeat
   
image alin1:
    "al 11"
    choice:
        pause 2
    choice:
        pause 4
    "al 12"
    pause 0.25
    repeat
  
image alin2:
    "al 19"
    choice:
        pause 2
    choice:
        pause 1
    "al 20"
    pause 3
    repeat  

image alin3:
    "al 21"
    choice:
        pause 2
    choice:
        pause 1
    "al 22"
    pause 3
    repeat  
image nast:
    "nas 3"
    choice:
        pause 2
    choice:
        pause 1
    "nas 4"
    pause 0.5
    repeat 

image nast1:
    "nas 5"
    choice:
        pause 2
    choice:
        pause 1
    "nas 6"
    pause 0.5
    repeat     
image nast2:
    "nas 7"
    choice:
        pause 2
    choice:
        pause 1
    "nas 8"
    pause 0.5
    repeat 
image alina:
    "alin 1"
    choice:
        pause 2
    choice:
        pause 1
    "alin 2"
    pause 0.5
    repeat  
    
image uss:
    "us 2"
    choice:
        pause 2
    choice:
        pause 1
    "us 3 al"
    pause 0.5
    "us 3 nas"
    pause 0.5
    repeat  
image uss1:
    "us 7"
    choice:
        pause 2
    choice:
        pause 1
    "us 8"
    pause 0.5
    repeat      
    
transform zoomin:
    zoom 1.2 xpos 990 ypos 540 anchor(0.5, 0.5,)
    linear 3 zoom 1
   