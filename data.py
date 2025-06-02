class DataUser:
    my_login = 'bogdanev'
    my_courier_data = {'login': 'bogdanevt', 'password': '123qwerty', 'firstName': 'Bogdan'}
    my_courier_with_wrong_password = {'login': 'bogdanevt', 'password': 'qwerty123'}


class OrderData:
    order_data_with_grey_color = {
        'firstName': 'Матвей',
        'lastName': 'Иронов',
        'address': 'Ленина, 23',
        'metroStation': 2,
        'phone': '+79825465566',
        'rentTime': 2,
        'deliveryDate': '2025-05-31',
        'comment': 'Без комментариев',
        'color': [
            'GREY'
        ]
    }

    order_data_with_black_color = {
        'firstName': 'Ирон',
        'lastName': 'Матвеев',
        'address': 'Омская 54',
        'metroStation': 4,
        'phone': '+79827779988',
        'rentTime': 5,
        'deliveryDate': '2025-05-31',
        'comment': 'Комментарий',
        'color': [
            'BLACK'
        ]
    }

    order_data_with_two_colors = {
        'firstName': 'Олег',
        'lastName': 'Иванов',
        'address': 'Полевая 12',
        'metroStation': 8,
        'phone': '+79821112211',
        'rentTime': 2,
        'deliveryDate': '2025-05-31',
        'comment': 'Да, чёрный и серый',
        'color': [
            'BLACK', 'GREY'
        ]
    }

    order_data_without_colors = {
        'firstName': 'Иван',
        'lastName': 'Олегов',
        'address': 'Городская 13',
        'metroStation': 5,
        'phone': '+79825461122',
        'rentTime': 9,
        'deliveryDate': '2025-05-31',
        'comment': 'Без самокатов в этот раз',
        'color': []
    }

class Answers:
    asnw404 = {
        'code': 404,
        'message': 'Учетная запись не найдена'
    }

    answ409 = {
        'code': 409,
        'message': 'Этот логин уже используется. Попробуйте другой.'
    }

    answ400 = {
        'code': 400,
        'message': 'Недостаточно данных для входа'
    }

    answ201 = {
        'ok': True
    }

    answ400empty = {
        'code': 400,
        'message': 'Недостаточно данных для создания учетной записи'
    }