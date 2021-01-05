from mycroft import MycroftSkill, intent_file_handler


class Rgblisten(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('rgblisten.intent')
    def handle_rgblisten(self, message):
        self.speak_dialog('rgblisten')


def create_skill():
    return Rgblisten()

