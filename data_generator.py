import random
import string


def generate_message():
    """Generates a random message from a random user id to a random recipient id"""
    user_ids = [i for i in range(101)]
    recipient_ids = user_ids.copy()

    random_user_id = random.choice(user_ids)

    # User can't send message to himself
    recipient_ids.remove(random_user_id)
    random_recipient_id = random.choice(recipient_ids)

    # Generate a dummy message
    message = "".join(random.choice(string.ascii_letters) for i in range(32))

    return {
        'user_id': random_user_id,
        'recipient_id': random_recipient_id,
        'message': message
    }


if __name__ == '__main__':
    print(generate_message())
