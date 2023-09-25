class EventAggregator:
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, subscriber):
        event_type_name = subscriber.event_type.__name__

        if not self.is_subscribed(event_type_name):
            self.subscribers[event_type_name] = []

        self.subscribers[event_type_name].append(subscriber)

    def publish(self, event):
        event_type_name = event.__class__.__name__

        if not self.is_subscribed(event_type_name):
            return

        for subscriber in self.subscribers[event_type_name]:
            subscriber.consume()

    def is_subscribed(self, event_type_name):
        return event_type_name in self.subscribers
