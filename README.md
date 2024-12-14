[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/pBuX0a9_)
# Домашняя работа 5-6 (PRO)

В этом задании необходимо создать API для обучения, загрузки, 
получения предсказания и управления моделью машинного обучения. 

API основан на FastAPI. В качестве модели машинного обучения предлагается использовать простую линейную регрессию из библиотеки scikit-learn. 
В качестве хранилища для моделей можно использовать словарь.


# Требования
- Python 3.10+
- Зависимости описаны в requirements.txt 
- FastAPI и Uvicorn для создания и запуска API
- Описание требуемого API находится в **openapi_pro.yaml**. Для просмотра можно пользоваться Swagger Editor: https://editor.swagger.io
  
# Снижение балла
- Разрешено использование дополнительных зависимостей. В этом случае, при отсутствии этих зависимостей в requirements.txt, работа оценивается в 0 баллов
- За любое несоответвие сигнатур эндпоинтов (методов API) описанным в **openapi_pro.yaml** оценка снижается

# Установка зависимостей 
```pip install -r requirements.txt```

# Запуск API
```python model_trainer/main.py```
