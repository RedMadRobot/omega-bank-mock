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

## Получение списков банковских продуктов

### Получить информацию о картах
```
GET /cards
```
<details>
<summary>Подробнее...</summary>

Ответ:
```json
{
    "data": {
        "cards": [
            {
                "id": 1,
                "name": "Visa Classic",
                "number": "NDSL RA01 203 4455 12",
                "value": 1233
            },
            {
                "id": 2,
                "name": "Visa Classic",
                "number": "NDSL RA01 203 4455 13",
                "value": 5234
            },
            {
                "id": 3,
                "name": "Visa Gold",
                "number": "NDSL RA01 203 4455 14",
                "value": 6225
            },
            {
                "id": 4,
                "name": "Visa Platinum",
                "number": "NDSL RA01 203 4455 15",
                "value": 8885
            }
        ]
    }
}
```

Curl пример:
```
curl http://127.0.0.1:5000/api/v1/cards
```
</details>

### Получить информацию о счетах
```
GET /deposits
```
<details>
<summary>Подробнее...</summary>

Ответ:
```json
{
    "data": {
        "deposits": [
            {
                "id": 5,
                "name": "Platinum",
                "number": "NDSL RA01 203 4455 01",
                "value": 30234
            },
            {
                "id": 6,
                "name": "Package",
                "number": "NDSL RA01 203 4455 02",
                "value": 12976
            },
            {
                "id": 7,
                "name": "Elite",
                "number": "NDSL RA01 203 4455 03",
                "value": 51234
            },
            {
                "id": 8,
                "name": "Platinum",
                "number": "NDSL RA01 203 4455 04",
                "value": 73417
            }
        ]
    }
}
```

Curl пример:
```
curl http://127.0.0.1:5000/api/v1/deposits
```
</details>

## Регистрация новых банковских продуктов
### Зарегистрировать новую карту
```
POST /cards
```
<details>
<summary>Подробнее...</summary>

Получить список всех типов карт можно [тут](#получение-списка-всех-типов-карт)

Запрос:
```json
{
    "type": "classic"
}
```

Ответ:
```json
{
    "data": {
        "card": {
            "id": 5,
            "name": "Visa Gold",
            "number": "NDSL RA01 203 4455 16",
            "value": 1117
        }
    }
}
```

Curl пример:
```
curl -d '{"type":"classic"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/api/v1/cards
```
</details>

### Получение списка всех типов карт
```
POST /card-types
```
<details>
<summary>Подробнее...</summary>

Ответ:
```json
{
    "data": {
        "types": [
            "classic",
            "gold",
            "platinum"
        ]
    }
}
```

Curl пример:
```
curl http://127.0.0.1:5000/api/v1/card-types
```
</details>

### Открыть новый счет
```
POST /deposits
```
<details>
<summary>Подробнее...</summary>

Получить список всех типов счетов можно [тут](#получение-списка-всех-типов-счетов)

Запрос:
```json
{
    "type": "package"
}
```

Ответ:
```json
{
    "data": {
        "deposit": {
            "id": 9,
            "name": "Platinum",
            "number": "NDSL RA01 203 4455 05",
            "value": 11117
        }
    }
}
```

Curl пример:
```
curl -d '{"type":"package"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/api/v1/deposits
```
</details>

### Получение списка всех типов счетов
```
POST /deposit-types
```
<details>
<summary>Подробнее...</summary>

Ответ:
```json
{
    "data": {
        "types": [
            "package",
            "platinum",
            "elite"
        ]
    }
}
```

Curl пример:
```
curl http://127.0.0.1:5000/api/v1/deposit-types
```
</details>