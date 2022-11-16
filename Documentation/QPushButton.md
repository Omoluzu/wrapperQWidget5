### QPushButton

Параметры который использует виджет **QPushButton**

**Оглавление:**
- [пример](#Пример)
- [action](#action)
- [flat](#flat)
- [icon](#icon)
- [size](#size)
- [tooltip](#tooltip)


###### Пример: 
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
            },
            'tooltip': "Этло выплывающая подсказка"
        }
```


&nbsp;
###### action:
Активация нажатия на кнопку. В качестве арумента принимает экземпляр функции.
Пример:
```python
class WrapperButton(QPushButton):  
    @wrapper_widget  
    def __init__(self):  
        super().__init__()  
        self.config = {  
            'action': self.action_cliked,  
        }
	
	def action_cliked(self):  
    	print("Click WrapperButton")
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
Является инструкцией для установки иконки.  
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

###### tooltip
Высплывающая подсказка для кнопки. Принимает в себя строковое значение.
**Пример:**
```python
"tooltip": "Это всплывающая подсказка"
```