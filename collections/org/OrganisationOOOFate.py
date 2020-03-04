import uuid
import random
from typing import Dict

class OrganisationOOOFate:

  @staticmethod
  def people_list() -> Dict: 
    dic = {}

    names = [
      "Denis",
      "John",
      "Lena",
      "Alexandra",
      "Philipp",
      "Lex",
      "Arthur",
      "Stan",
      "Boris",
      "Irina",
      "Volodimir",
      "Josh",
      "Evgeni",
      "Arseni"
    ]

    second_names = [
      "Ivanka",
      "Black",
      "Putin",
      "Britva",
      "Lennon",
      "Fox",
      "Dry",
      "Shadman",
      "Sparkle",
      "Smith",
      "Middle"
    ]

    for i in range(0, 1000):
      dic[str(uuid.uuid4())] = {
        "name": names[int(random.random() * len(names))] + " " + second_names[int(random.random() * len(second_names))],
        "room": int(random.random() * 1000)
      }
    
    return dic
