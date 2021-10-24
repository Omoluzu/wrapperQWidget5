### QIcon

Иструкция для настроек иконок приложения.
Переопределяяет библиотеку [`QIcon`](https://doc.qt.io/qt-5/qicon.html)

**Оглавление:**
- [icon](#icon)
- [resource](#resource)

&nbsp;
###### icon:
Путь до расположения файла с иконкой
**Внимание:** На данный момент работает только с параметром `resource`=`True`

***Пример использования:***
```python
"icon": "check.png"
```

&nbsp;
###### resource:
Флаг указывающий на то откуда брать файл с иконкой  
По умолчанию `False`
Где:
- `True`:  Файл с иконкой расположен в файле ресурсе.
- `False`: По умолчанию. На данный момент недоступно. Файл расположен локально на диске ПК.
- 
- ***Пример использования:***
```python
"resource": True
```