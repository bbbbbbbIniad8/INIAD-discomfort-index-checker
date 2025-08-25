from INIAD_discomfort_checker import DiscomfortIndexInINIAD as DIII
from dotenv import load_dotenv
import os

ID = os.getenv("ID")
PS = os.getenv("Password")

data = DIII.get_info(ID, PS, 2313)
DIII.display_result(data)