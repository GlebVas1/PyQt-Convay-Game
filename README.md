Первичная попытка освоить qt заради попытки в дизайн. В качестве тестового приложения была выбрана convey game

По сути свой просто "тыкалка" красящая определенные клетки. Возможно выбирать готовые шаблоны объектов на поле, состояние клеток через палитру, использовать кисть с настраиваемым размером и.т.д.

![alt text](https://github.com/GlebVas1/py-test/blob/main/images/1.jpg?raw=true)
![alt text](https://github.com/GlebVas1/py-test/blob/main/images/2.jpg?raw=true)
![alt text](https://github.com/GlebVas1/py-test/blob/main/images/3.jpg?raw=true)
![alt text](https://github.com/GlebVas1/py-test/blob/main/images/4.jpg?raw=true)
![alt text](https://github.com/GlebVas1/py-test/blob/main/images/10.jpg?raw=true)
![alt text](https://github.com/GlebVas1/py-test/blob/main/images/9.jpg?raw=true)


Также имеется сравнительно богатый набор настроек


![alt text](https://github.com/GlebVas1/py-test/blob/main/images/6.jpg?raw=true)


Кроме того, с целью опробовать интерактивный реалтайм дашборд, был встроен динамический настраиваемыйграфик количества клеток различных типов


![alt text](https://github.com/GlebVas1/py-test/blob/main/images/5.jpg?raw=true)
![alt text](https://github.com/GlebVas1/py-test/blob/main/images/11.jpg?raw=true)

Все элементы интерфейса были переделаны через QSS и отдельные иконки-ресурсы




# Known issues:
    1) Изредка может зависнуть в мертвую, при этом не выходя за рамки памяти и.т.д. на больших фпс
    1) Может падать главный график отображения при смене правил



# Todo:
    1) Добавить загрузку сохранение объектов из файлов
    2) Аналогично с палитрами
    3) Рефакторинг
    4) Добавить опций для окна
