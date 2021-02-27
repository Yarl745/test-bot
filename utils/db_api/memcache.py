import logging


class ActivitySaver:
    _hour_clicks_counter = {}
    _day_clicks_counter = {}


    def save_click(self, user_id: int):
        # logging.info(f"User {user_id} clicks btn")
        self.update_hour_clicks_counter(user_id)
        self.update_day_clicks_counter(user_id)


    def update_hour_clicks_counter(self, user_id: int):
        key_user_id = str(user_id)
        is_user_has_hour_click = self._hour_clicks_counter.get(key_user_id, False)

        if not is_user_has_hour_click:
            self._hour_clicks_counter.update({key_user_id: True})


    def update_day_clicks_counter(self, user_id: int):
        key_user_id = str(user_id)
        is_user_has_day_click = self._day_clicks_counter.get(key_user_id, False)

        if not is_user_has_day_click:
            self._day_clicks_counter.update({key_user_id: True})


    def clear_day_clicks_counter(self):
        logging.info("Clear day_clicks_counter")
        self._day_clicks_counter.clear()


    def clear_hour_clicks_counter(self):
        logging.info("Clear hour_clicks_counter")
        self._hour_clicks_counter.clear()


    def get_count_hour_clicks(self) -> int:
        count_hour_clicks = len(self._hour_clicks_counter)
        logging.info(f"Get count_hour_clicks = {count_hour_clicks}")
        return len(self._hour_clicks_counter)


    def get_count_day_clicks(self) -> int:
        count_day_clicks = len(self._day_clicks_counter)
        logging.info(f"Get count_day_clicks = {count_day_clicks}")
        return len(self._day_clicks_counter)
