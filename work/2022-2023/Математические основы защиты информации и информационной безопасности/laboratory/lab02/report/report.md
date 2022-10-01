---
# Front matter
lang: ru-RU
title: "Лабораторная работа 2"
subtitle: "Шифры перестановки" 
author: "Греков Максим Сергеевич"

# Formatting
toc-title: "Содержание"
toc: true # Table of contents
toc_depth: 2
lof: true # List of figures
lot: false # List of tables
fontsize: 12pt
linestretch: 1.5
papersize: a4paper
documentclass: scrreprt
polyglossia-lang: russian
polyglossia-otherlangs: english
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Serif
monofont: PT Serif
mainfontoptions: Ligatures=TeX
romanfontoptions: Ligatures=TeX
sansfontoptions: Ligatures=TeX,Scale=MatchLowercase
monofontoptions: Scale=MatchLowercase
indent: true
pdf-engine: lualatex
header-includes:
  - \linepenalty=10 # the penalty added to the badness of each line within a paragraph (no associated penalty node) Increasing the value makes tex try to have fewer lines in the paragraph.
  - \interlinepenalty=0 # value of the penalty (node) added after each line of a paragraph.
  - \hyphenpenalty=50 # the penalty for line breaking at an automatically inserted hyphen
  - \exhyphenpenalty=50 # the penalty for line breaking at an explicit hyphen
  - \binoppenalty=700 # the penalty for breaking a line at a binary operator
  - \relpenalty=500 # the penalty for breaking a line at a relation
  - \clubpenalty=150 # extra penalty for breaking after first line of a paragraph
  - \widowpenalty=150 # extra penalty for breaking before last line of a paragraph
  - \displaywidowpenalty=50 # extra penalty for breaking before last line before a display math
  - \brokenpenalty=100 # extra penalty for page breaking after a hyphenated line
  - \predisplaypenalty=10000 # penalty for breaking before a display
  - \postdisplaypenalty=0 # penalty for breaking after a display
  - \floatingpenalty = 20000 # penalty for splitting an insertion (can only be split footnote in standard LaTeX)
  - \raggedbottom # or \flushbottom
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

# Цель работы 

- Ознакомиться с шифрами перестановки.

- Реализовать маршрутное шифрование.

- Реализовать шифрование с помощью решеток.

- Реализовать шифрование Таблица Виженера.

# Описание методов

Шифры перестановки преобразуют открытый текст в криптограмму путем перестановки его символов. 

Способ, каким при шифровании переставляются буквы открытого текста, и является ключом шифра. 

Важным требованием евс является равенство длин ключа и исходного текста.

# Маршрутное шифрование

## Описание 

Простейшим примеров перестановочного шифра являются так называемые «маршрутные перестановки», использующие некоторую геометрическую фигуру (плоскую или объемную). 

Шифрование заключается в том, что текст записывается в такую фигуру по некоторой траектории, а выписывается по другой траектории. (рис. -@fig:001)

## Реализация 

![Маршрутное шифрование](image/image1.png){ #fig:001 width=100% }

Результат: **ЕЕНПНЗОАТАЬОВОКННЕЬВЛДИРИЯЦТИА**

# Шифрование с помощью решеток

## Описание 

Выбирается число _k_. Строим квадрат со стороной длины k и заполняем его клетки числами от _1_ до _k^2_.

Поворачиваем квадрат на _90_ градусов по часовой стрелке и приписываем справа от исходного квадрата.

Поворачивая на _90_ градусов по часовой стрелки и добавляя полученный квадрат сначала снизу, а затем слева от предыдущего, получим квадрат со стороной _2k_.

В этом квадрате закрасим произвольным образом все цифры, причем каждая цифра может быть закрашена только один раз.

Это и будет решёткой для шифрования. 

Код для шифрования представляет последовательность _k_ цифр от _1_ до _4_, _i_-тая цифра обозначает в каком подквадрате (нумеруются в порядке создания) закрашивать число _i_.

Открытый текст разбивается на блоки длины _4k^2_. 

Каждый блок разбивается на подстроки длины _k^2_. 

Решетка накладывается на пустой лист бумаги, закрашиваемые клетки вырезаются. 

Для первой подстроки ее _i_-ый символ записывается в вырезанное _i_-ое число решетки. 

Повторяем процесс еще _3_ раза, поворачивая перед этим решетку на _90_ градусов по часовой стрелке. 

В результате получаем таблицу, составляющую из символов открытого текста. 

Криптограмма из этой таблицы получается путем построчного выписывания символов или применения приемов маршрутного шифрования. (рис. -@fig:002)

## Реализация 

![Шифрование с помощью решеток](image/image2.png){ #fig:002 width=100% }

Результат 1: **ДПОРДАГВЛИИОСПОО**

Результат 2: **ЕФОСЕИШАТТРСОПНЛАНВЫНМНИТЯОСТПТЯКЕНЕ**

# Таблица Виженера

## Описание 

Шифр Виженера состоит из последовательности нескольких шифров Цезаря с различными значениями сдвига. (рис. -@fig:003)

Для зашифровывания может использоваться таблица алфавитов, называемая _tabula recta_ или квадрат (таблица) Виженера. 

Применительно к русскому алфавиту таблица Виженера составляется из строк по _33_ символов, причём каждая следующая строка сдвигается на несколько позиций. 

Таким образом, в таблице получается _33_ различных шифров Цезаря. 

На каждом этапе шифрования используются различные алфавиты, выбираемые в зависимости от символа ключевого слова. 

## Реализация 

![Таблица Виженера](image/image3.png){ #fig:003 width=100% }

Результат: **ЦРЪФЮОХШКФФЯГКЬЬЧПЧАЛНТШЦА**

# Вывод

- Ознакомились с шифрами перестановки.

- Реализовали маршрутное шифрование.

- Реализовали шифрование с помощью решеток.

- Реализовали шифрование Таблица Виженера.
