### A. Количество равных максимальному

| Ограничение времени |             1 секунда              |
|:--------------------|:----------------------------------:|
| Ограничение памяти  |                64Mb                |
| Ввод                |  стандартный ввод или `input.txt`  |
| Вывод               | стандартный вывод или `output.txt` |`

Последовательность состоит из натуральных чисел и завершается числом `0`. Всего вводится не более `10000` чисел
(не считая завершающего числа `0`). Определите, сколько элементов этой последовательности равны ее наибольшему элементу.

_Числа, следующие за числом `0`, считывать не нужно._

**Формат ввода**

* Вводится последовательность целых чисел, оканчивающаяся числом `0` (само число `0` в последовательность не входит).

**Формат вывода**

* Выведите ответ на задачу.

_Пример 1_

| Ввод | Вывод |
|------|-------|
| 1    | 1     |
| 7    |       |
| 9    |       |
| 0    |       |

_Пример 2_

| Ввод | Вывод |
|------|-------|
| 1    | 2     |
| 3    |       |
| 3    |       |
| 1    |       |
| 0    |       |

#### [Решение A](task_A.py)

---

### B. Дома и магазины

| Ограничение времени |             1 секунда              |
|:--------------------|:----------------------------------:|
| Ограничение памяти  |                64Mb                |
| Ввод                |  стандартный ввод или `input.txt`  |
| Вывод               | стандартный вывод или `output.txt` |`

На Новом проспекте построили подряд `10` зданий.
Каждое здание может быть либо _жилым домом_, либо _магазином_, либо _офисным зданием_.

Но оказалось, что жителям некоторых домов на Новом проспекте слишком далеко приходится идти до ближайшего _магазина_.
Для разработки плана развития общественного транспорта на Новом проспекте мэр города попросил вас выяснить, какое же
наибольшее расстояние приходится преодолевать жителям Нового проспекта, чтобы дойти от своего _дома_ до ближайшего
_магазина_.

**Формат ввода**

* Программа получает на вход десять чисел, разделенных пробелами.
  Каждое число задает тип здания на Новом проспекте: число `1` обозначает _жилой дом_, число `2` обозначает _магазин_,
  число `0` обозначает _офисное здание_. Гарантируется, что на Новом проспекте есть хотя бы один жилой дом и хотя бы
  один магазин.

**Формат вывода**

* Выведите одно целое число: наибольшее расстояние от дома до ближайшего к нему магазина. Расстояние между двумя
  соседними домами считается равным `1` (то есть если два дома стоят рядом, то между ними расстояние `1`,
  если между двумя домами есть еще один дом, то расстояние между ними равно `2` и т.д.)

_Пример_

| Ввод                | Вывод |
|---------------------|-------|
| 2 0 1 1 0 1 0 2 1 2 | 3     |

**Примечания**

* В примере из условия дальше всего идти до ближайшего магазина жителям четвертого дома: ближайший к их дому магазин
  находится в первом доме, и им нужно пройти три дома до него. Жителям других домов придется пройти меньшее расстояние
  до ближайшего магазина, поэтому ответ `3`.

#### [Решение B](task_B.py)

---

### C. Изготовление палиндромов

| Ограничение времени |             2 секунды              |
|:--------------------|:----------------------------------:|
| Ограничение памяти  |               512Mb                |
| Ввод                |  стандартный ввод или `input.txt`  |
| Вывод               | стандартный вывод или `output.txt` |`

В строкоремонтную мастерскую принесли строку, состоящую из строчных латинских букв. Заказчик хочет сделать из неё
палиндром. В мастерской могут за `1` байтландский тугрик заменить произвольную букву в строке любой выбранной заказчиком
буквой.

Какую минимальную сумму придётся заплатить заказчику за ремонт строки?

_Напомним, что палиндромом называется строка, которая равна самой себе, прочитанной в обратном направлении._

**Формат ввода**

* Входные данные содержат непустую строку, состоящую из строчных латинских букв, которую принёс заказчик. Длина строки
  не превосходит `10^4`

**Формат вывода**

* Выведите одно целое число - минимальную сумму, которую заказчику придётся заплатить за превращение принесённой
  заказчиком строки в палиндром.

_Пример 1_

| Ввод | Вывод |
|------|-------|
| a    | 0     |

_Пример 2_

| Ввод | Вывод |
|------|-------|
| ab   | 1     |

_Пример 3_

| Ввод | Вывод |
|-----|-------|
| cognitive    | 4     |

#### [Решение C](task_C.py)
