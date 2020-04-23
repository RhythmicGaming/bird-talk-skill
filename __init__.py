from mycroft import MycroftSkill, intent_file_handler


class BirdTalk(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('talk.bird.intent')
    def handle_talk_bird(self, message):
        self.speak_dialog('talk.bird')


def create_skill():
    return BirdTalk()

