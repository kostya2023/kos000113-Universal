▎kos000113-universal Library

kos000113-universal is a Python library that provides various functions for data manipulation, encryption, and JSON file management. It includes utilities for key generation, database operations, and certificate generation.

▎Installation

You can install the library using pip. Just run the following command:

pip install kos000113-universal


▎Usage

▎Importing the Library

To use the library, you can import the necessary classes and methods as follows:

import kos000113-universal


▎Usage Examples

▎Working with Encryption

Key - Must be 32 bytes and encoded in base64  
Iv - Initialization Vector must be 32 bytes and encoded in base64

# Example of using encryption functions
crypter = kos000113-universal.crypter()
data_to_encrypt = "Secret data"
encrypted_data = crypter.crypt_data(data_to_encrypt, key, Iv)
decrypted_data = crypter.decrypt_data(encrypted_data, key, Iv)
print(decrypted_data)  # Output: Secret data


▎Working with Database

• db_name (str): The name of the database to connect to.

• SQL_request (str): The SQL query to execute on the database.

• params (Tuple[Any]): Parameters for the SQL query. Defaults to an empty tuple.

• formatted (bool): Whether to return data in a "pretty" format. 
  Example: [(1,), (2,), (3,)] - without formatting. 
  [1, 2, 3] - with formatting.

• method (str): The method for retrieving data; can be 'fetchone', 'fetchall', or 'fetchmany'.

• size (int): The number of records for the 'fetchmany' method.

# Example of using database functions
db = kos000113-universal.Database()
db.create_db("my_database.db", SQL_request, params)
data = db.get_data("my_database.db", SQL_request, params, formatted, method, size)
print(data)


▎Key Generation

# Example of key generation
key_gen = kos000113-universal.GenerateKey()
keys = key_gen.create_keys()
print(keys)  # Output: list with 2 elements

random_key = key_gen.generate_random_key(128)
print(random_key)  # Output: random string


▎Working with JSON Files

# Example of working with JSON files
json_handler = kos000113-universal.JsonHandler()
result = json_handler.update_data("data.json", "key", "value")
print(result)  # Output: dictionary

data = json_handler.get_data("data.json")
print(data)  # Output: dictionary


▎Certificate Generation

# Example of certificate generation
cer_gen = kos000113-universal.GenerateCustomCer()
cer = cer_gen.generate_cer_SDTP("example.com")
print(cer)  # Needed for my future project


▎Function Documentation

▎1. Encryption (crypter.py)

• crypt_data(data: str) -> str

  • Encrypts data.

  • Parameters:

    • data: string to be encrypted.

  • Returns: Encrypted string.

• decrypt_data(encrypted_data: str) -> str

  • Decrypts data.

  • Parameters:

    • encrypted_data: string to be decrypted.

  • Returns: Decrypted string.

▎2. Database Operations (database.py)

• create_db(db_name: str) -> None

  • Creates a new database.

  • Parameters:

    • db_name: name of the database.

• get_data(db_name: str) -> Union[Dict[str, Any], str]

  • Retrieves data from the database.

  • Parameters:

    • db_name: name of the database.

  • Returns: Dictionary with data or an error message.

• execute_query(query: str) -> Union[str, None]

  • Executes anSQL query.

  • Parameters:

    • query: SQL query to execute.

  • Returns: Result of the query execution or an error message.

▎3. Key Generation (generate_key.py)

• create_keys() -> Tuple[str, str]

  • Generates a pair of keys.

  • Returns: Keys as a tuple.

• generate_random_key(length: int) -> str

  • Generates a random key of the specified length.

  • Parameters:

    • length: length of the key.

  • Returns: Random key.

▎4. Working with JSON Files (json_manager.py)

• update_data(file_path: str, what_data: str, sama_data: Any) -> Union[str, None]

  • Updates data in the specified JSON file.

  • Parameters:

    • file_path: path to the JSON file.

    • what_data: key to be updated.

    • sama_data: new value for the key.

  • Returns: Message about successful update or an error message.

• get_data(file_path: str) -> Union[Dict[str, Any], str]

  • Retrieves data from the specified JSON file.

  • Parameters:

    • file_path: path to the JSON file.

  • Returns: Dictionary with data or an error message.

▎5. Certificate Generation (generate_custom_cer.py)

• generate_cer_SDTP(domain: str) -> str

  • Generates a certificate for the specified domain.

  • Parameters:

    • domain: domain name.

  • Returns: Generated certificate.

▎License

This project is licensed under the MIT License - details can be found in the LICENSE file.

▎Contribution

If you would like to contribute to the project, please fork the repository, make your changes, and create a Pull Request.

▎Author

Your name - Konstantin Gorshkov

▎Acknowledgments

Thank you for using the kos000113-universal