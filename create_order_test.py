import sender_stand_request
import data

def test_create_order_and_get_by_track():
    # Шаг 1: Выполнить запрос на создание заказа
    order_response = sender_stand_request.post_new_order(data.order_body)
    
    # Проверяем, что заказ создан успешно
    assert order_response.status_code == 201, "Ошибка создания заказа: " + str(order_response.status_code)
    
    # Шаг 2: Сохранить номер трека заказа
    track_number = order_response.json()["track"]
    print("Трек номер заказа: " + str(track_number))
    
    # Шаг 3: Выполнить запрос на получение заказа по треку заказа
    order_by_track_response = sender_stand_request.get_order_by_track(track_number)
    
    # Шаг 4: Проверить, что код ответа равен 200
    assert order_by_track_response.status_code == 200, "Ошибка получения заказа: " + str(order_by_track_response.status_code)
    
    # Дополнительная проверка: убедимся, что получили корректные данные
    order_data = order_by_track_response.json()
    assert "order" in order_data, "В ответе отсутствует объект заказа"
    assert order_data["order"]["track"] == track_number, "Трек номер в ответе не совпадает"
    
    print("Тест пройден успешно! Заказ создан и получен по треку.")