---
# Front matter
lang: ru-RU
title: "Лабораторная работа 5"
subtitle: "Вероятностные алгоритмы проверки чисел на простоту" 
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

- Ознакомиться с определением простых чисел 

- Изучить свойства простых чисел и подходы к их обнаружению

- Реализовать вероятностные алгоритмы проверки чисел на простоту

# Описание 

## Простое число 

Пусть а - целое число. Числа ±1, ±а называются тривиальными делителями числа а.

Целое число р называется простым, если оно не является делителем единицы и не имеет других делителей, кроме тривиальных. 

В противном случае число р называется составным. 

Например, числа ±2, ±3, ±5, ±7,±11,±13,±17,±19,±23,±29 являются простыми.

## Проверка на простоту 

Проверка чисел на простоту является составной частью алгоритмов генерации простых чисел, применяемых в криптографии с открытым ключом.

Алгоритмы проверки на простоту можно разделить на вероятностные и детерминированные.

## Типы алгоритмов

Детерминированный алгоритм всегда действует по одной и той же схеме и гарантированно решает поставленную задачу (или не дает никакого ответа). 

Вероятностный алгоритм использует генератор случайных чисел и дает не гарантированно точный ответ. 

## Вероятностные алгоритмы

Вероятностные алгоритмы в общем случае не менее эффективны, чем детерминированные (если используемый генератор случайных чисел всегда дает набор одних и тех же чисел, зависящих от входных данных, то вероятностный алгоритм становится детерминированным).

Для проверки на простоту числа n вероятностным алгоритмом выбирают случайное число а (1 < a < n) и проверяют условия алгоритма. 

Если число n не проходит тест по основанию а, то алгоритм выдает результат «Число n составное», и число n действительно является составным.

## Количество тестов

Если же n проходит тест по основанию а, ничего нельзя сказать о том, действительно ли число n является простым. 

Последовательно проведя ряд проверок таким тестом для разных а и получив для каждого из них ответ «Число n, вероятно, простое», можно утверждать, что число n является простым с вероятностью, близкой к 1.

Рассмотрим такие вероятностные алгоритмы как тест Ферма (рис. -@fig:001), Соловэя-Штрассена (рис. -@fig:003) (а также алгоритм вычисления символа Якоби (рис. -@fig:002)), Миллера-Рабина (рис. -@fig:004), и выполним с их помощью проверки (рис. -@fig:005).

# Алгоритмы

## Тест Ферма

![Тест Ферма](image/image1.png){ #fig:001 width=100% }

## Вычисление символа Якоби

![Вычисление символа Якоби](image/image2.png){ #fig:002 width=100% }

## Тест Соловэя-Штрассена

![Тест Соловэя-Штрассена](image/image3.png){ #fig:003 width=100% }

## Тест Миллера-Рабина

![Тест Миллера-Рабина](image/image4.png){ #fig:004 width=55% }

# Результаты

![Результаты](image/image5.png){ #fig:005 width=75% }

# Выводы

- Ознакомились с определением простых чисел 

- Изучили свойства простых чисел и подходы к их обнаружению

- Реализовали вероятностные алгоритмы проверки чисел на простоту