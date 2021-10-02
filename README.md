
### ***WrapperWidget***:
Декоратор, являющийся оберткой  [`PyQt.QWidget`](https://doc.qt.io/qt-5/qwidget.html)  необходимый для удобного позиционирования виджетов.
Обязательным атрибутом который необходимо создать в декорированном классе является словарь `self.layouts`. В котором описывается инструкция для создания layout и виджетов. 

Примеры создания:
```python
from WrapperWidget import wrapper_widget

class NewWidget(QWidget)
	
	@wrapper_widget
	def __init__(self)
		super().__init__()
		
		self.table = TableMappingWidget()
		self.id_widget = JSON.UI.TreeIdElementWidget(dialog=self)
		btn_mapping = QPushButton("ЗАМАПИТЬ")
		
		self.layouts = {
			"vbox": [
				{"hbox": [
					self.table,
		 			self.id_widget
				]},
		 		btn_mapping
			]
		}		
```
Описание примера: 
- Главным ключом атрибута `self.layouts`, указан [`vbox`](#vbox). Это означает что основным начальным layout является [`QVBoxLayout`](https://doc.qt.io/qt-5/qvboxlayout.html).
- Значением данного ключа является список виджетов. Которые будут отрисованне в нашем  [`QVBoxLayout`](https://doc.qt.io/qt-5/qvboxlayout.html).
- Первым параметроя является еще один словарих с ключем [`"hbox"`](#hbox), это означает что внутри [`QVBoxLayout`](https://doc.qt.io/qt-5/qvboxlayout.html) необходимо создать [`QHBoxLayout`](https://doc.qt.io/qt-5/qhboxlayout.html), у которого есть два ранее созданных виджета `self.table` и `self.id_widget` . 
- Второй параметр является виджетом кнопки, которая будет позиционироваться в  [`QVBoxLayout`](https://doc.qt.io/qt-5/qvboxlayout.html).

#### Описание работы self.layouts
**self.layouts** - является инструкцией для создание структуры вилдетов.
При создании атрибута `self.layouts` необходимо указать **только** один ключ со значениями [`"vbox"`](#vbox) или [`"hbox"`](#hbox). Это будет главный основной layout на котором будут все остальные элементы.

#### Ключи атрибута self.layouts

###### config:
```python
"config": {}
```
Является ключем для задания настроек текущего виджета.
Список ключей для конфига описан ниже

Пример:
```python
self.layouts = {
	"vbox": [
		{"config": {
			"margin": [0]
		}}
	]
}
```

Или для основного приложения:

```python
self.config = {
	"title": "App"
}
```

&nbsp;
###### vbox:
```python
"vbox": []
```
Является сигналом на создание  [`QVBoxLayout`](https://doc.qt.io/qt-5/qvboxlayout.html).
Данный параметр является словаряем. 
Значением данного словаря является `list`
В данном списке можно: указывать: 
- созданные экземпляры виджетов,  
- словари с остальными арибутами.

Пример: 
```python
"vbox": [  
	{"hbox": []},  
	btn_mapping  
]
```

&nbsp;
###### hbox:
```python
"hbox": []
```
Работает аналогично атрибуту [`vbox`](#vbox) , только создается[`QHBoxLayout`](https://doc.qt.io/qt-5/qhboxlayout.html).


&nbsp;
#### Список ключей параметра config
###### title:
```python
"title": type(str)
```
**title**  - Устанавливает заголовок виджета. Принимает в себя аргумент строки

&nbsp;
###### margin:
```python
"margin": [left: int, top: int, right: int, button: int]
```
Обвязка для [setContentsMargins](https://doc.qt.io/qt-5/qwidget.html#setContentsMargins)
Задает поля вокрут текущего виджета.
Принимает в себя 4-ре числовые значения для каждой стороны, Или 1 значение для всех сторон.