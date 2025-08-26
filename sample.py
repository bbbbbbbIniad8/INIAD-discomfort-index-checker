import INIAD_discomfort_checker as IDC
import os
from dotenv import load_dotenv

load_dotenv('.env')

ID = os.getenv("ID")
PS = os.getenv("Password")

data = IDC.get_info(ID, PS, 2313)
IDC.display_result(data)
