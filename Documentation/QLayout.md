### QLayout

Параметры который использует виджет **QVBoxLayout**, **QHBoxLayout**

&nbsp;
###### alignment:
[Qt Namespace | Qt Core 5.15.7](https://doc.qt.io/qt-5/qt.html#AlignmentFlag-enum)
Устанавливает выравнивание для виджета, принимает в качестве аргумента строку с параметром:

Пример использования: 
```python
"alignment": "top"
```


Для каждого `QLayout` используются свои параметры

Параметры для `vbox`(`QVBoxLayout`)

параметр | ожидаемая реакция
--- | ---
top | Выравнивание по верху
bottom | Выравнивание по низу
center | Выравнивание по центру
base_line | Выравнивается с базовой линеей

Параметры для `hbox`(`QHBoxLayout`), еще не функционируют