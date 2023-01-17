from authentication.models import User

def update_subscription(subscription_id, is_subscribed):
    try:
        user = User.objects.get(id=subscription_id)
        user.is_subscribed = is_subscribed
        user.save()
        return True
    except:
        return False

class SubscriptionService:
    def subscribe(subscription_id):
        return update_subscription(subscription_id, is_subscribed = True)

    def unsubscribe(subscription_id):
        return update_subscription(subscription_id, is_subscribed = False)
