# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define p1 = Character('Haru', color="#ebf2f3")
define p2 = Character('Egor4k', color="#ebf2f3")
define p3 = Character('Учитель истории', color="#ffffff")
define p4 = Character('Shizuku', color="#ffffff")
define p5 = Character('Учитель алгебры', color="#ebf2f3")
define p6 = Character('Nami', color="#ffffff")
# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

#Музыка и звуки:
define audio.musdef = "audio/def.mp3"
define audio.musend = "audio/end.mp3"
define audio.soundf = "audio/soundf.mp3"
define audio.spat = "audio/spat.mp3"
define audio.dosd = "audio/dosd.mp3"
define audio.nosh = "audio/nosh.mp3"
define audio.shagi = "audio/shagi.mp3"
define audio.pad = "audio/pad.mp3"
define audio.spat1 = "audio/spat1.mp3"
define audio.zev = "audio/zev.mp3"
define audio.shizsn = "audio/shizsn.mp3"
define audio.bore = "audio/bore.mp3"




   
# Игра начинается здесь:
label start:
    play music dosd
    scene start with fade
    "{cps=30}Серые стены школы равнодушно отражали тусклый свет пасмурного осеннего дня."
    "{cps=30}Капли дождя барабанили по подоконникам, создавая монотонный ритм, который эхом разносился по пустым коридорам."
    "{cps=30}Ещё пять минут до начала первого урока, но даже эти мгновения тишины казались бесконечными."
    "{cps=30}Школьные годы – странное время. Время, когда каждый день наполнен одновременно рутиной и открытиями, когда кажется, что весь мир лежит у твоих ног, но при этом ты не знаешь, куда сделать следующий шаг."
    "{cps=30}Время, когда дружба проверяется на прочность, а первая любовь может перевернуть всю жизнь с ног на голову."
    stop music fadeout 3
    scene black with fade 
    play music shagi
    p1 "{cps=30} Надо бы поторопиться...."
    

    
   
   
   
    


    define points = 0

    scene main with fade
    stop music fadeout 2
    play music musdef

    p1 "{cps=30}Как я устал от этой учебы!"
    show haru at left
    with dissolve
    p1 "{cps=30}Надеюсь день пройдет быстро!"
    show ego at right
    with dissolve
    p2 "{cps=30}Здорово чувак, как дела?" 
    p1 "{cps=30}О, привет, я думал ты не прийдешь."
    p2 "{cps=30}Я патался отсидется дома, но в этот раз не получилось, мать с утра была не в настроении и заставила идти на учебу."
    p1 "{cps=30}Лан, как думаешь сегодня сможем до 7 урока досидеть?"
    p2 "{cps=30}Что-то я не уверен, смотрел расписание? Я бы после 4-того ушел"
    p1 "{cps=30} Да уж... Я вчера пришел домой и уснул, учебники не менял со вчерашнего дня. "
    p1 "{cps=30}Ох, первая история? Я ничего не учил еще и оценок нет."
    p2 "{cps=30}Крепись..."
    p2 "{cps=30}Лан, пошли уже."

    

    
    scene class history with fade
    play music soundf
    "{cps=30}Начался урок истории"
    "{cps=30}Вам очень страшно, надеятесь, что сможете просто просидеть урок."
    stop music
    play music musdef
    show haru at left
    p1 "{cps=30}Вот бы не спросила"
    hide haru
    show techer hist 
    p3 "{cps=30}Отвечает..."
    hide techer hist
    show haru at left
    p1 "{cps=30}Может быть попытать удачу? Вопрос вроде не сложный. Если отвечу хотя бы на 4 то балл не упадет и аттестация будет"
    menu:
        "{cps=30}Ответить или Затерпеть"
        "{cps=30}Затерпеть":
            jump zaterpet
        "{cps=30}Ответить":
            "{cps=30}Вы перенервничали, забыли все, что хотели сказать и просто промычали"
            hide haru
            show techer hist
            p3 "{cps=30}Два, садись"
            jump otvet
label otvet:
    stop music
    scene black with fade
    "{cps=30}. . . ."
    play music nosh
    scene die with fade
    play music end
    "{cps=30}Вас охватила депрессия и совершили харакири в таулете т.к это оценка повлияла на вашу аттестацию"
    scene lose with fade
    "{cps=30}Конец :("
    stop music
    return
label zaterpet: 
    "{cps=30}(спустя 40 минут)"
    p1 "{cps=30}Неужели я смог это пережить."
    scene main with fade
    show haru at left
    p1 "{cps=30}Надеюсь, остальные уроки пройдут так же быстро"
    show ego at right
    p2 "{cps=30}Тебе повезло, сегодня она была без настроения, валила всех доп.вопросами."
    hide ego
    with dissolve
    p1 "{cps=30}Пойду прогуляюсь по школе пока есть время"
    play sound pad
    p4 "{cps=30}АЙ! Смотри куда идешь!"
    show shizuku angre at right
    with dissolve
    show haru sp at left
    p1 "{cps=30}П.. пр. прости, совсем ушел в себя, даже не вижу куда иду :)"
    p4 "{cps=30}Ладно не извиняйся, мне тоже нужно было заметить тебя."
        

    p1 "{cps=30}Ч.. что ты же Shizuku Kamoto"
    p4 "{cps=30}Приятно познакомится, но мне пора идти, скоро начнется урок"
    hide shizuku angre
    with dissolve
    "{cps=30}(Я был в шоке, она же модель, я недавно видел ее в журналах, а теперь она учится вместе с нами!!!!!!)"
    "{cps=30}(Я стоял так еще минут 5, осозновая это, пока не прозвенел звонок на следующий урок.)"
    "{cps=30}Прозвенел звонок и я пошел в класс"
    scene vhod with fade
    show haru at left
    with dissolve
    "{cps=30}Фух, вроде успел к началу."
    hide haru
    scene vhod class with fade
    show techer algebra 
    p5 "{cps=30}Заходи!"
    scene class algebra with fade
    show techer algebra
    p5 "{cps=30}Здравствуйте, сегодня будет подготовка к предстоящему тесту"
    show haru at left
    hide techer algebra
    with dissolve
    show haru sp at left
    "{cps=30}..."
    show shizuku sp at right
    with dissolve
    p4 "{cps=30}Ухты! Приветик, это же ты меня чуть не сбил в коридоре?"
    p1 "{cps=30}Д.. да" 
    hide shizuku sp 
    show shizuku hp at right
    p4 "{cps=30}Нуууу... раз мы в одном классе, то будем знакомы:)"
    hide haru
    show haru sm3 at left
    with dissolve
    p1 "{cps=30}..... ок"
    hide haru sm3
    hide shizuku
    "{cps=30}Урок прошел так же рутинно, как и первый. Но то что Kamoto учиться с вами в одном классе до сих пор удивляет вас."
    "{cps=30}Вы думаете пойти прогулятся по школе или попробовать заговорить с Kamoto"
    jump vibor
        
label vibor:
    menu:
        "{cps=30}Прогуляться или Поговорить с Kamoto"
        "{cps=30}Прогуляться":
            jump koridor
        "{cps=30}Поговорить с Kamoto":
            jump rom
label rom:
    scene class algebra with fade
    show haru at left
    "{cps=30}А почему ты перевелась в нашу школу и зачем вообще? Ты же и так работаешь и получаешь хорошие деньги с журналов."
    show shizuku hp at right
    p4 "{cps=30}Я всегда училась паралельно с хобби, просто в другой школе."
    p1"{cps=30}А как ты начала работать? Если не секрет"
    p4"{cps=30}хммм."
    p4"{cps=30}А давай я отвечу тебе на это когда мы пойдем гулять после уроков"
    p1"{cps=30}...."
    p1"{cps=30}Прости но нет, мне что то плохо я домой лучше прямо сейчас пойду."
    p4"{cps=30}Ну ладно, тогда завтра. Обещаешь мне?"
    p1"{cps=30}Не знаю, пока"
    scene kor 1 with fade
    play music shagi
    '...'
    "{cps=30}По пути я встретил Egor4k и он предложил пойти к нему в гости, т.к он тоже уходил"
    jump gosti


return       
label koridor:
    "{cps=30}Вы идете в коридор"
    scene black with fade
    play music shagi
    "{cps=30}Пойду прогуляюсь"
    stop music fadeout 2
    play music musdef
    scene vhod with fade
    show haru at left
    with dissolve
    play sound pad
    p1 "{cps=30}ААА"
    show nami sp at right
    with dissolve
    p6 " {cps=30}О п.. привет Haru. Прости, что испугала."
    p6 "{cps=30}Слушай а ты.."
    p1 "{cps=30}Да, новенькая - Shizuku Kamoto, ты же в курсе кто она?"
    p6 "{cps=30} ... да."
    p6 "{cps=30}А ты...."
    p1 "{cps=30}Ладно извини, мне пора."
    hide nami sad
    show nami sp at right
    with dissolve
    p6 "{cps=30} н ну.. да, конечно, извини."
    hide nami sad
    scene kor 1 with fade
    p1 "{cps=30}Странный сегодня день, что-то не так как обычно в школе. День какой-то насыщенный."
    show ego at right
    p2 "{cps=30}О Haru, я как раз тебя искал!"
    show haru at left
    with dissolve
    p1 "{cps=30}Привет!"
    p2 "{cps=30} Как тебе новенькая?"
    p1 "{cps=30}Нууу как тебе сказать, неожидал честно говоря. Мы еще и познакомились, когда я ее чуть не сбил в коридоре."
    p1 "{cps=30}Однако, она решила подружиться в первую очередь со мной. Странно это все."
    p2 "{cps=30}Хммммм, ну согласен. А как она с тобой общается? "
    p1 "{cps=30}Да не понимаю я, заигрывает что ли со мной. Она слишком активная, предпологаю ей нравятся клубы, пьянки ну и т.д"
    p2 "{cps=30}Ты уверен? Она же знаменитость, по крайней мере в нашем городе."
    p1 "{cps=30}Не знаю я ничего! Говорю же просто странная она. Это лишь мои догадки."
    p2 "{cps=30}Да ладно тебе не кипишуй. Ладно, скоро перерыв закончится. Пошли в класс."
    p2 "{cps=30}Не хочешь после этого уйти? И ко мне сразу в гости тогда."
    p1 "{cps=30}Давай да, а то день не такой рутинный как обычно, не хочу чтобы он продолжался тут."
    p2 "{cps=30}После этого урока на 1 этаже, выйдем через спортзал."
    p1 "{cps=30}Хорошо"
    stop music fadeout 2
    play music soundf
    scene class 3 with fade
    "{cps=30}Поскорей бы это все закончилось."
    stop music fadeout 2
    "{cps=30}...."
    scene black with fade
    play music spat1
    p1 "{cps=30}Z... z... z.."
    stop music fadeout 2
    scene class 3 with fade
    play sound zev
    stop music fadeout 2
    p1 "{cps=30}Пора уходить"
    play music shagi
    scene kor 1 with fade
    '...'
    play music musdef
    scene stairs with fade
    "{cps=30}Псс"
    "{cps=30}Haru иди сюда"
    "{cps=30}Я обернулся и увидел Shizuku"
    show shizuku hp at right
    with dissolve
    p4"{cps=30}Слушай Haru, не хочешь прогуляться сейчас?"
    show haru sp s at left
    with dissolve
    "{cps=30}Я был в ступоре, мне никогда не паредлагали погулять вместе, даже знакомые,  а это Shizuku"
    stop music fadeout 2
label zanovo:
    play music musdef
    show shizuku hp at right
    show haru sp s at left
    p4"{cps=30}Ну так что?"
    menu:
        "{cps=30}Пойти с Egor4k или Пойти с Shizuku"
        "{cps=30}Пойти с Egor4k":
            jump kent
        "{cps=30}Пойти с Shizuku":
            jump genshina
label kent:
    show haru at left
    with dissolve
    play sound shizsn
    show shizuku angre at right
    p1 "{cps=30}Извини, но я обещал встретиться со своим другом"
    p4 "{cps=30}Ладно, я поняла"
    p1 "{cps=30}Завтра встретимся, пока!"
    p4 "{cps=30}Угу..."
    hide shizuku angre
    stop music fadeout 2
    scene skol with fade
    play music shagi
    '...'
    stop music fadeout 2
    play music musdef
    show ego at right
    with dissolve
    p2 "{cps=30}Ну наконец-то, почему так долго?"
    show haru at left
    with dissolve
    p1"{cps=30}Сорян, нужно было задержаться, проверял тест"
    p2"{cps=30}Ладно пошли"
    stop music fadeout 2
    play music shagi
    scene black with fade
    '...'
    jump gosti
label gosti:
    play music musdef
    scene komnata with fade
    show ego at right
    with dissolve
    p2"{cps=30}Ну че рассказывай, че там с Shizuku"
    show haru at left
    p1"{cps=30}Нуу, просто поговорил с ней"
    p2"{cps=30}Просто не бывает, что дальше!"
    p1"{cps=30}Ну предложила прогулятся"
    p1"{cps=30}Я был растерян, отказал вообщем"
    p2"{cps=30}Но в любом случае ты же понимаешь, что она не просто так общается именно с тобой."
    p1"{cps=30}Ну да.."
    p2"{cps=30}А ты замечашь, что не только Shizuku хочет с тобой познакомиться."
    p1"{cps=30}Нет, у меня даже в мыслях не было."
    p2"{cps=30}Ты очень сильно нравишься Nami"
    p2"{cps=30}Она такая скромная и стеснительная, как и ты"
    p1"{cps=30}Правда?"
    p2"{cps=30}Подумай об этом, но честный от меня совет, лучше не связывайся с Shizuku"
    p1"{cps=30}Да не с кем не собираюсь я общаться, мне и так проблем своих хватает"
    p2"{cps=30}Ладно давай увидимся завтра"
    p2"{cps=30}Скоро мать прийдет, да и дел куча"
    p1"{cps=30}Давай"
    scene black with fade
    stop music fadeout 2
    play music shagi
    '...'
    stop music fadeout 2
    scene noch with fade
    "{cps=30}Я лежал и думал, почему я? Что я сделал такого необычного чтобы заслужить внимания модели"
    "{cps=30}Обдумывал слова ego, почему еще Nami, сегодня она вроде хотела что-то сказать, но в итоге ушел."
    p1"{cps=30}Все хватит, я так не усну."
    scene black with fade
    play sound zev
    stop music fadeout 2
    "{cps=30}Опять рутинный день"
    play music musdef
    "{cps=30}(спустя 1 ч я пришел в школу)"
    scene skol with fade
    p1"{cps=30}Что же сказать им"
    stop music fadeout 2
    menu:
        "{cps=30}Выбрать Shizuku или Nami"
        "{cps=30}Пойти к Shizuku":
            jump shizuka
        "{cps=30}Пойти с Nami":
            jump nami
label shizuka:
    play music musdef
    scene skol with fade
    show haru sp at left
    p1"{cps=30}Слушай Shizuku, я обдумал твое предложение, давай сходим прогуляемся"
    show shizuku sp at right
    with dissolve
    p4"{cps=30}О супер, тогда после уроков :)"
    hide shizuku sp
    show shizuku hp at right
    with dissolve
    scene black with fade
    "{cps=30}Школьный день прошел очень быстро, мысли только были о прогулке"
    scene skol with fade
    show shizuku hp at right
    with dissolve
    show haru sp at left
    with dissolve
    p1"{cps=30}Ну что пойдем?"
    p4"{cps=30}Конечно"
    scene doroga with fade
    show shizuku ni
    with dissolve
    stop music fadeout 2
    p4"{cps=30}Слушай Haru..."
    p1"{cps=30}Да"
    p4"{cps=30}Я"
    play sound zbil
    scene black with fade
    "{cps=30}...................."
    return

label nami:
    play music bore
    scene skol with fade
    show haru at left
    with dissolve
    p1"{cps=30}Nami ты вчера хотела мне что-то сказать, я хочу выслушать тебе"
    show nami ang at right
    with dissolve
    p6"{cps=30}Неважно"
    p1"{cps=30}Нет правда, я хочу выслушать тебя"
    p6"{cps=30}..."
    p1"{cps=30}Ну пожалуйста"
    p6"{cps=30}Правда интересно?"
    p1"{cps=30}Да"
    hide nami ang
    show nami sad at right
    p6"{cps=30}т..ты.."
    p1"{cps=30}Я понал, давай прогуляеся вместе после школы"
    p6"{cps=30}Да"
    scene black with fade
    "{cps=30}Я не знаю, что на меня нашло тогда, я почувствовал себя уверенно рядом с ней, осознал, что именно она нужна мне"
    "{cps=30}Школьный день прошел очень быстро, мысли только были о прогулке"
    scene naberesh with fade
    show nami lov 
    with dissolve
    p6"{cps=30}Haru я хотела сказать тебе, что мне нравишься"
    p1"..."
    p6"{cps=30}Это взаимно?"
    p6"{cps=30}П...прости я много лишнего наговорила"
    p6"{cps=30}Мне так стыдно.."
    p1"{cps=30}Ну успакойся, все хорошо. Ты тоже мне нравишься."
    p6"{cps=30}Правда?"
    p1"{cps=30}Да"
    stop music fadeout 2
    p6"<3❤️"


return






    






        




    






    









label genshina:
    hide haru sp
    hide shizuku hp
    "ЗАПОМНИ КЕНТОВ НА ЖЕНЩИН НЕ МЕНЯЮТ!!!!!!!!!!"
    jump zanovo


    














    










     











                
            
        
        


        







        
        






        





        




        

    








    



    return
