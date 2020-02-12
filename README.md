# Моковый сервер для проекта Омега Банк

Базовый URL
```
https://omegabank.mock-object.redmadserver.com/api/v1
```

## Авторизация

### Запросить смс-код по номеру телефона
```
POST /auth/sms/send-code

Body:
{
    "phone_number": "79991112233"
}
```

### Проверить код 
```
POST /auth/sms/check-code

Body:
{
    "phone_number": "79991112233",
    "code": "1234"
}
```

### Получить профиль пользователя
```
GET /auth/profile
```

## Точки пополнения банковского счета

### Получить список точек
```
GET /deposition-points
```

### Получить информацию о партнерах
```
GET /deposition-partners
```