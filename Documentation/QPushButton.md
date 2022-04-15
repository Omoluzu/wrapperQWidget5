### QPushButton

Параметры который использует виджет **QPushButton**
Пример создания: 
```python
class WrapperButton(QPushButton):  
  
    @wrapper_widget  
    def __init__(self):  
        super().__init__()  
  
        self.config = {  
            'size': 50,  
            'flat': True,  
            'icon': {  
                "icon": "ico/check.png",  
                "size": 50  
            }  
        }
```


&nbsp;
###### flat:
Если стоит флаг `True`, то большинство стилей не будут рисовать фон кнопки. По умолчанию стоит флаг `False`

***Пример использования:***
```python
"flat": True
```

&nbsp;
###### icon:
Является инсрукцией для установки иконки.  
Параметры инструкции смотреть в [`QIcon`](QIcon.md)

***Пример использования: ***
```python
"icon": {
	"icon": "check.png",  
	"resource": True,  
	"size": 50
}
```

&nbsp;
###### size:
Устанавливает ширину и высоту кнопки
Может принимать в себя как `list[x, y]` так и просто `xy`
где `x` - ширина кнопки
где `y` - высота кнопки
где `xy` - ширина и высота кнопки

***Пример использования:***
```python
"size": [x, y]
"size": [xy]
"size": xy
```