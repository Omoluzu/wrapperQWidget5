### QTreeWidget

Настройка для виджета [QTreeWidget](https://doc.qt.io/qt-6/qtreewidget.html)

&nbsp;
**Оглавление:**
- [пример](#пример-использования)
- [column](#column)
	- [count](#count)
	- [width](#width)
- [header](#header)
	- [hidden](#hidden)

&nbsp;
###### Пример использования:
```python
class WrapperTreeWidget(QTreeWidget):  
  
    @wrapper_widget  
    def __init__(self):  
        super().__init__()  
  
        self.config = {  
            "header": {  
                "hidden": True  
            },  
  
            "column": {  
                "count": 2,  
                "width": {  
                    0: 280,  
                    1: 5  
                }  
            }  
        }
```


&nbsp;
###### column:
Оргазинует надстройку для колонок виджета
- [count](#count)
- [width](#width)
Пример:
```python
self.config = {
	"column": {  
		"count": 2,  
		"width": {  
			0: 280,  
			1: 5  
		}  
	}  
}
```


&nbsp;
###### count:
Устанавливает кол-во колонок.
По умолчанию `1`
Пример:
```python
"count": 2
```

&nbsp;
###### width:
Установка размера для колонок
Пример:
```python
"width": {  
	0: 280,  
	1: 5  
}
```


&nbsp;
###### header:
Оргазинует надстройку для заголовка виджета
- [hidden](#hidden)

Пример:
```python
self.config = {  
	"header": {  
		"hidden": True  
	},  
```

&nbsp;
###### hidden:
Сокрытие элемента заголовка.
По умолчанию `False`
```pyhon
"hidden": True  
```
