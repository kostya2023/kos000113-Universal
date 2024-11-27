from setuptools import setup, find_packages

setup(
    name='universal',  # Имя вашей библиотеки
    version='0.1.0',  # Версия вашей библиотеки
    packages=find_packages(),  # Автоматическое нахождение всех пакетов
    install_requires=["pyOpenssl", "tgcrypto", ],  # Укажите зависимости, если они есть
    author='Kostya',  # Ваше имя
    author_email='kostya_gorshkov_06@vk.com',  # Ваш email
    description='Universal lib for me))',
    long_description=open('readme.md').read(),  # Длинное описание
    long_description_content_type='text/markdown',  # Формат длинного описания
    url='https://github.com/ваш_репозиторий',  # Ссылка на репозиторий
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Укажите лицензию
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Минимальная версия Python
)
