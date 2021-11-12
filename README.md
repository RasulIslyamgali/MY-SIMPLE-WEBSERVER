# MY-SIMPLE-WEBSERVER
Веб сервер с помощью модуля python socket.

Так же особенность этого сайта в том, что данные при вводе сразу же сохраняются в БД.

Т.е. человек ввел ИИН, создается поле для него в БД. Потом он вводит ФИО, дату рождения и т.д.

И каждое следующее введенное поле сразу же сохраняется в БД, и если человек ввел ФИО и покинул сайт, в БД останется информация как минимум об ИИН и ФИО.

Проверку изменения каждого инпут поля сделал с помощью чистого JavaScript, при этом при каждом сохранении данных страница не обнавляется.

Т.е. юзеру это никак не мешает.

Знаю, что никто сейчас сайты не делает. Это тестовый проект, для понимания того, как все работает на низком уровне.


--------------------------------------------------

Web server using python socket module.

Also, the feature of this site is that the data when entered is immediately saved to the database.

Those. the person entered the IIN, a field is created for him in the database. Then he enters full name, date of birth, etc.

And each next entered field is immediately saved in the database, and if a person entered their full name and left the site, the database will contain information about at least IIN and full name.

Checking the change of each input field was done using pure JavaScript, while each time the data is saved, the page is not refreshed.

Those. it does not bother the user in any way.

I know that no one makes websites now. This is a test project to understand how everything works at a low level.

