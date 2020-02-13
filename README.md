# Моковый сервер для проекта Омега Банк

Базовый URL
```
https://omegabank.mock-object.redmadserver.com/api/v1
```

## Авторизация

Механизм аутентификации - Bearer. <br>
В авторизованной зоне, в каждый запрос необходимо добавить http заголовок с токеном, полученный в запросе `/auth/sms/check-code`.
```
Authorization: Bearer <access_token>
```


### Запросить смс-код по номеру телефона
```
POST /auth/sms/send-code
```
<details>
<summary>Подробнее...</summary>
Запрос:
```json
{
    "phone_number": "79991112233"
}
```
Ответ:
```json
{
    "data": {
        "retry_interval": 60
     }
}
```
</details>  

### Проверить код 
```
POST /auth/sms/check-code
```
<details>
<summary>Подробнее...</summary>
Запрос:
```json
{
    "phone_number": "79991112233",
    "code": "1234"
}
```
Ответ:
```json
{
    "data": {
        "access_token": "406A143A-A460-4A05-BF26-C28D7D04F129",
        "refresh_token": "921F7D7A-CB3A-4681-9B93-5A2FD4B46553",
        "expires_in": 86400
     }
}
```
</details>  


### Получить профиль пользователя
```
GET /auth/profile
```
<details>
<summary>Подробнее...</summary>
Ответ:
```json
{
    "data": {
        "user": {
            "user_id": 9703,
            "full_name": "Тестовый Тест Тестович",
            "phone": "79991112233",
            "email": "testdev@redmadrobot.com"
        }
    }
}
```
</details>  

## Точки пополнения банковского счета

### Получить список точек
```
GET /deposition-points
```
<details>
<summary>Подробнее...</summary>
Ответ:
```json
{
    "data": {
        "points": [
            {
                "externalId": "17971",
                "partnerName": "MTSBank",
                "location": {
                    "latitude": 55.7570521,
                    "longitude": 37.61711
                },
                "workHours": "ПН-ВС 08:00-22:00",
                "phones": "+7(495)921-28-00",
                "fullAddress": "г Москва, ул Охотный Ряд, д 2"
            },
        ]
    }
}
```
</details>  

### Получить информацию о партнерах
```
GET /deposition-partners
```
<details>
<summary>Подробнее...</summary>
Ответ:
```json
{
    "data": {
        "partners": [
            {
                "id": "MKB",
                "name": "МКБ",
                "picture": "",
                "url": "",
                "hasLocations": true,
                "isMomentary": false,
                "depositionDuration": "",
                "limitations": "",
                "pointType": "",
                "externalPartnerId": "220",
                "description": "",
                "moneyMin": 10,
                "moneyMax": 300000,
                "hasPreferentialDeposition": false,
                "limits": [
                    {
                        "currency": {
                            "code": 643,
                            "name": "RUB",
                            "strCode": "643"
                        },
                        "min": 10,
                        "max": 300000
                    }
                ],
                "dailyLimits": [
                    {
                        "currency": {
                            "code": 643,
                            "name": "RUB",
                            "strCode": "643"
                        },
                        "amount": 300000
                    }
                ]
            }
        ]
    }
}
```
</details>  