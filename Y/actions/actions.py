from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

# import hyperlink
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


class ActionSchedule(Action):
    def name(self) -> Text:
        return "action_schedule"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        subjsched = next(tracker.get_latest_entity_values("subj_programm"), None)
        examsched = next(tracker.get_latest_entity_values("exams_programm"), None)

        if subjsched is not None and examsched is not None:
            dispatcher.utter_message(
                text=" Το πρόγραμμα εξεταστικής ΚΑΙ μαθημάτων είναι εδώ: "
            )
        elif subjsched is not None and examsched is None:
            dispatcher.utter_message(text="Το πρόγραμμα μαθημάτων είναι εδώ: ")
        elif subjsched is None and examsched is not None:
            dispatcher.utter_message(text="Το πρόγραμμα εξεταστικής είναι εδώ: ")
        else:
            dispatcher.utter_message(text="???")

        return []


class ActionSecretary(Action):
    def name(self) -> Text:
        return "action_secretary"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        contact_secr = next(tracker.get_latest_entity_values("contact_secr"), None)
        contact_mail_secr = next(
            tracker.get_latest_entity_values("contact_mail_secr"), None
        )
        contact_number_secr = next(
            tracker.get_latest_entity_values("contact_number_secr"), None
        )

        if contact_secr is not None:
            dispatcher.utter_message(
                text="Το τηλ της γραμματειας ειναι: και το μαιλ της αυτο "
            )

        if contact_mail_secr is not None:
            dispatcher.utter_message(text="Το mail της γραμματειας ειναι αυτο: ")

        if contact_number_secr is not None:
            dispatcher.utter_message(text="Το της της γραμματειας ειναι αυτο: ")

        return []


class ActionLocationInfo(Action):
    def name(self) -> Text:
        return "action_location_info"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        txt = "Το κτίριο της σχολής, οι αίθουσες των διαλέξεων καθώς και η γραμματεία βρίσκονται εδώ : https://goo.gl/maps/XWmFzNJLud7PR3wE7"
        dispatcher.utter_message(text=txt)

        return []
