# Universal Library

Universal — это библиотека Python, предоставляющая различные функции для работы с данными, шифрованием и управлением JSON-файлами. Она включает в себя утилиты для создания ключей, работы с базами данных и генерации сертификатов.

## Установка

Вы можете установить библиотеку с помощью `pip`. Просто выполните следующую команду:

```bash
pip install universal
```

## Использование

### Импортирование библиотеки

Чтобы использовать библиотеку, вы можете импортировать необходимые классы и методы следующим образом:

```python
import universal
```

### Примеры использования

#### Работа с шифрованием

```python
# Пример использования функций шифрования
crypter = universal.Crypter()
data_to_encrypt = "Секретные данные"
encrypted_data = crypter.crypt_data(data_to_encrypt)
decrypted_data = crypter.decrypt_data(encrypted_data)
print(decrypted_data)  # Вывод: Секретные данные
```

#### Работа с базой данных

```python
# Пример использования функций работы с базой данных
db = universal.Database()
db.create_db("my_database.db")
data = db.get_data("my_database.db")
print(data)
```

#### Генерация ключей

```python
# Пример генерации ключей
key_gen = universal.GenerateKey()
keys = key_gen.create_keys()
print(keys)

random_key = key_gen.generate_random_key(128)
print(random_key)
```

#### Работа с JSON-файлами

```python
# Пример работы с JSON-файлами
json_handler = universal.JsonHandler()
result = json_handler.update_data("data.json", "ключ", "значение")
print(result)

data = json_handler.get_data("data.json")
print(data)
```

#### Генерация сертификатов

```python
# Пример генерации сертификатов
cer_gen = universal.GenerateCustomCer()
cer = cer_gen.generate_cer_SDTP("example.com")
print(cer)
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

Спасибо за использование библиотеки Universal!
