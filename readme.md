# kos000113-universal Library

kos000113-universal — это библиотека Python, предоставляющая различные функции для работы с данными, шифрованием и управлением JSON-файлами. Она включает в себя утилиты для создания ключей, работы с базами данных и генерации сертификатов.

## Установка

Вы можете установить библиотеку с помощью `pip`. Просто выполните следующую команду:

```bash
pip install kos000113-universal
```

## Использование

### Импортирование библиотеки

Чтобы использовать библиотеку, вы можете импортировать необходимые классы и методы следующим образом:

```python
import kos000113-universal
```

### Примеры использования

#### Работа с шифрованием

Key - Должен быть 32 байта и зашифрован в base64
Iv - Init Vector должен быть 32 байта и зашифрован в base64

```python
# Пример использования функций шифрования
crypter = kos000113-universal.crypter()
data_to_encrypt = "Секретные данные"
encrypted_data = crypter.crypt_data(data_to_encrypt, key, Iv)
decrypted_data = crypter.decrypt_data(encrypted_data, key, Iv)
print(decrypted_data)  # Вывод: Секретные данные
```

#### Работа с базой данных

db_name (str): Имя базы данных, к которой нужно подключиться.
SQL_request (str): SQL-запрос для выполнения на базе данных.
params (Tuple[Any]): Параметры для SQL-запроса. По умолчанию пустой кортеж.
formatted (bool): Нужно ли возвращать данные в "красивом" формате. 
                Пример: [(1,), (2,), (3,)] - без форматирования. 
                [1, 2, 3] - с форматированием.
method (str): Метод получения данных; может быть 'fetchone', 'fetchall' или 'fetchmany'.
size (int): Количество записей для метода 'fetchmany'.

```python
# Пример использования функций работы с базой данных
db = kos000113-universal.Database()
db.create_db("my_database.db", SQL_request, params)
data = db.get_data("my_database.db", SQL_request, params, formatted, method, size)
print(data)
```

#### Генерация ключей

```python
# Пример генерации ключей
key_gen = kos000113-universal.GenerateKey()
keys = key_gen.create_keys()
print(keys) # вывод список с 2 элементами

random_key = key_gen.generate_random_key(128)
print(random_key) # чисто строка
```

#### Работа с JSON-файлами

```python
# Пример работы с JSON-файлами
json_handler = kos000113-universal.JsonHandler()
result = json_handler.update_data("data.json", "ключ", "значение")
print(result) # Вывод словаря

data = json_handler.get_data("data.json")
print(data) # Вывод словаря
```

#### Генерация сертификатов

```python
# Пример генерации сертификатов
cer_gen = kos000113-universal.GenerateCustomCer()
cer = cer_gen.generate_cer_SDTP("example.com")
print(cer) # Нужен для моего будущего проекта
```

## Документация функций

### 1. Шифрование (crypter.py)

- **crypt_data(data: str) -> str**
  - Шифрует данные.
  - **Параметры:**
    - `data`: строка, которую нужно зашифровать.
  - **Возвращает:** Зашифрованную строку.

- **decrypt_data(encrypted_data: str) -> str**
  - Дешифрует данные.
  - **Параметры:**
    - `encrypted_data`: строка, которую нужно расшифровать.
  - **Возвращает:** Расшифрованную строку.

### 2. Работа с базой данных (database.py)

- **create_db(db_name: str) -> None**
  - Создает новую базу данных.
  - **Параметры:**
    - `db_name`: имя базы данных.

- **get_data(db_name: str) -> Union[Dict[str, Any], str]**
  - Получает данные из базы данных.
  - **Параметры:**
    - `db_name`: имя базы данных.
  - **Возвращает:** Словарь с данными или сообщение об ошибке.

- **execute_query(query: str) -> Union[str, None]**
  - Выполняет SQL-запрос.
  - **Параметры:**
    - `query`: SQL-запрос для выполнения.
  - **Возвращает:** Результат выполнения запроса или сообщение об ошибке.

### 3. Генерация ключей (generate_key.py)

- **create_keys() -> Tuple[str, str]**
  - Генерирует пару ключей.
  - **Возвращает:** Ключи в виде кортежа.

- **generate_random_key(length: int) -> str**
  - Генерирует случайный ключ заданной длины.
  - **Параметры:**
    - `length`: длина ключа.
  - **Возвращает:** Случайный ключ.

### 4. Работа с JSON-файлами (json_mananger.py)

- *update_data(file_path: str, what_data: str, sama_data: Any) -> Union[str, None]*
  - Обновляет данные в указанном JSON-файле.
  - *Параметры:*
    - `file_path`: путь к JSON-файлу.
    - `what_data`: ключ, который нужно обновить.
    - `sama_data`: новое значение для ключа.
  - *Возвращает:* Сообщение об успешном обновлении или сообщение об ошибке.

- *get_data(file_path: str) -> Union[Dict[str, Any], str]*
  - Получает данные из указанного JSON-файла.
  - *Параметры:*
    - `file_path`: путь к JSON-файлу.
  - *Возвращает:* Словарь с данными или сообщение об ошибке.

### 5. Генерация сертификатов (generate_custom_cer.py)

- *generate_cer_SDTP(domain: str) -> str*
  - Генерирует сертификат для указанного домена.
  - *Параметры:*
    - `domain`: доменное имя.
  - *Возвращает:* Сгенерированный сертификат.

## Лицензия

Этот проект лицензирован под MIT License - подробности можно найти в файле [LICENSE](LICENSE).

## Контрибьюция

Если вы хотите внести свой вклад в проект, пожалуйста, создайте форк репозитория, внесите изменения и создайте Pull Request.

## Автор

Ваше имя - [Konstantin Gorshkov](mailto:kostya_gorshkov_06@vk.com)

## Благодарности

Спасибо за использование библиотеки kos000113-universal!
