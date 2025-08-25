import INIAD_discomfort_checker as IDC
import os

ID = os.getenv("ID")
PS = os.getenv("Password")

data = IDC.get_info(ID, PS, 2313)
IDC.display_result(data)
