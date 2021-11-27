### QGroupBox

Параметры который использует виджет [**`QGroupBox`**](https://doc.qt.io/qt-5/qgroupbox.html)

Для инициализации используете ключ `group`, в любом из ранее созданных лайоутов
Пример:
```python
self.layouts = {  
     "vbox": [  
		 {"group": {  
			"config": {  
				"title": "wrapper QGroupBox:",  
			},  

			"hbox": [  
				QLabel("Текст внутри wrapper QGroupBox")  
			]  
		}}  
    ]  
}
```

Внутри `group` необходимо создавать layout (`hbox` или `vbox`)

Так же можно указать ключ `config` для указания настроек `box`

&nbsp;
##### Ключи настроек

###### title:
Устанавливается заголовк для виджета `box`