class EventAggregator:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def publish(self):
        for subscriber in self.subscribers:
            subscriber.consume()
