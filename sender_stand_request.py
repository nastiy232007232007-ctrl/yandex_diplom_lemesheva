import requests
import configuration
import data

# создаем заказ
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)

# получаем заказ по треку
def get_order_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH,
                        params={"t": track})
