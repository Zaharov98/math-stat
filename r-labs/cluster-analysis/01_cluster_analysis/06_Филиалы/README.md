Классификация филиалов сети магазинов
=====================================
Описание данных
---------------
Руководство сети магазинов желает разделить филиалы на группы с тем, чтобы затем сравнить продажи в разных группах. Данный анализ может помочь в выборе направления развития и оптимизации сети.

Часть переменных представлена в текстовом виде. Эти текстовые переменные перекодированы; отсюда повторение переменных.

Описание переменных
--------------------

* название	Условный код филиала
* площадь	Площадь торгового зала, кв.м.
* проходим	Проходимость, ср. кол-во входящих в магазин  за 10 минут 
			(с 14-00 до 18-00)
* ассортим	Ассортимент (текстовая переменная!)
* конкурен	Как выглядит филиал по совокупности показателей по отношению 
			к ближайшему конкуренту (текстовая переменная!)
* метро		За сколько минут можно дойти до ближайшей станции метро
* консульт	Наличие в торговом зале консультантов (текстовая переменная!)
* дизайн	Наличие или отсутствие следующих компонентов: вывеска, 
			витрина, световая вывеска (текстовая переменная!)
* цены		Индекс цен по отношению к базовым.
* продажи	Совокупные продажи за 2 последних месяца
* ассорт2	Ассортимент (числовая переменная после перекодировки!)
* конкур2	Как выглядит филиал по совокупности показателей по отношению 
			к ближайшему конкуренту (числовая переменная после 
			перекодировки!)
* консул2	Наличие в торговом зале консультантов (числовая переменная 
			после перекодировки!)
* дизайн2	Наличие или отсутствие следующих компонентов: вывеска, 
			витрина, световая вывеска (числовая переменная после 
			перекодировки!)
	
**Комментарий.** Дополнительно к задаче, было бы неплохо добавить новую переменную 'вывеска+витрина'.

**Задача.**	Пользуясь кластерным анализом разделить магазины на группы. Сравнить полученные группы по уровню продаж – это означает, что при классификации надо исключить переменную 'продажи' из списка переменных, используемых при анализе.

Сравнить кластеры по уровню продаж.
