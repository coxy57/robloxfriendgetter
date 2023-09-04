import requests

# put user id for roblox here
USER_ID = 1

class errors:
    class TargetUserInvalid(Exception):
        pass


class RobloxFriendGrabber:
    def __init__(self, id):
        self.BASE_URL = "https://friends.roblox.com/"
        self.FRIEND_ENDPOINT = "v1/users/%s/friends" % id

    def get_friends(self, check_if_banned: bool = False, save_to_file=False):
        friends = requests.get(self.BASE_URL + self.FRIEND_ENDPOINT)
        if "errors" in friends.text:
            raise errors.TargetUserInvalid("User is not valid.")
        if check_if_banned:
            names = [data['name'] for data in friends.json()['data'] if not data['isBanned']]
        else:
            names = [data['name'] for data in friends.json()['data']]
        if save_to_file:
            with open(save_to_file,'a+') as name_file:
                name_file.writelines(name + '\n' for name in names)
        return names


try:
    r = RobloxFriendGrabber(USER_ID)
    print(r.get_friends(check_if_banned=True, save_to_file=""))
except errors.TargetUserInvalid as e:
    print(e)
