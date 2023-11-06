-----------
чтобы запустить тесты на функцию encoder из файла morse.py
можно перейти в файл test_morse_encode.py и запустить его
или сделать это с помощью команд python -m doctest -v morse.py
-----------
чтобы запустить фикстуру с pytest на функцию decode 
pytest test_morse_decode.py
-----------
чтобы запустить unittest на функцию fit_transform
можно запуститьфайл test_fit_transform.py
или python test_fit_transform.py  
----------
чтобы запустить pytest на функцию fit_transform
pytest test_fit_transform2.py
----------

Есть файл result.txt - там результаты запусков тестов
В каждой папке сформирован html отчет о покрытии кода тестами