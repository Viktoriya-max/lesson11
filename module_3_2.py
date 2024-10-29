def send_email(message, recipient, sender = 'university.help@gmail.com'):
    #Если строки recipient и sender не содержит "@" или не оканчивается на ".com"/".ru"/".net"
    if '@' not in recipient or not recipient.endswith(('.com', '.ru', '.net'))\
            or '@' not in sender or not sender.endswith(('.com', '.ru', '.net')):
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
    #Если же sender и recipient совпадают
    elif sender == recipient:
        print('нельзя отправить письмо самому себе!')
    #Если отправитель по умолчанию - university.help@gmail.com
    elif sender == 'university.help@gmail.com':
        print('письмо успешно отправлено с адреса', sender, 'на адрес', recipient)
    #В противном случае
    elif sender != 'university.help@gmail.com':
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', sender, 'на адрес', recipient )

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender = 'urbaninfo@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')