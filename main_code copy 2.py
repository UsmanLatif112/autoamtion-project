import requests
from lib.start_profile import *
from lib.resources import Login,Code
from lib.function import *
from lib.data import *
username = "usmanlatif0309@gmail.com"
password = "DSJoker@@03360325@.okay"
comment = "CFBR"
REPLY = "Thanks for connecting with me"
"""=================================================="""
driver= start_profile()
driver.maximize_window()
time.sleep(0.5)
driver.get("https://www.linkedin.com/login/")
time.sleep(0.5)
driver.get("https://www.linkedin.com/mynetwork/invitation-manager/")
time.sleep(5)
actions = ActionChains(driver)
try:
    con_acc_btnn = HomePage(driver)
    con_acc_btnn.wait_ten(Code.con_acc_btn)
    if con_acc_btnn:
        try:
            try:
                time.sleep(1)
                time.sleep(0.5)
                message_container = HomePage(driver)
                message_container.wait_ten(Code.message_container)
                message_container.click_btn(Code.message_container)
                time.sleep(1)
                message_container_cross_s = HomePage(driver)
                message_container_cross_s.click_btn(Code.message_container_cross)
                time.sleep(0.5)
                try:
                    discard_btn_n = HomePage(driver)
                    discard_btn_n.click_btn(Code.discard_btn)
                except:
                    print("No discard button")
            except:
                print("No message modal found")
            try:
                invitation_section = driver.find_elements(By.XPATH, '//li[@data-view-name="pending-invitation"]')
                invitation_sectionn = len(invitation_section)
                if invitation_section:
                    for i in range(invitation_sectionn):
                        try:
                            try:
                                con_acc_reply_btn = WebDriverWait(driver, 5).until(
                                    EC.presence_of_element_located((By.XPATH, f'(//li[@data-view-name="pending-invitation"][{i}]//*[@class="invitation-card__custom-message-container"]//button)[2]')))
                                time.sleep(0.5)
                                con_acc_reply_btn.click()
                                time.sleep(0.5)
                                message_container = HomePage(driver)
                                message_container.wait_five(Code.message_container)
                                time.sleep(0.5)
                                message_container.click_btn(Code.message_container)
                                time.sleep(0.5)
                                print("found reply")
                                for char in REPLY:
                                    actions.send_keys(f"{char}").perform()
                                    time.sleep(0.1)
                                time.sleep(0.5)
                                message_send_btn = HomePage(driver)
                                message_send_btn.wait_five(Code.message_send_btn)
                                time.sleep(1)
                                message_send_btn.click_btn(Code.message_send_btn)
                                time.sleep(1)
                                message_container_cross_s = HomePage(driver)
                                message_container_cross_s.click_btn(Code.message_container_cross)
                                time.sleep(0.5)
                                try:
                                    discard_btn_n = HomePage(driver)
                                    discard_btn_n.click_btn(Code.discard_btn)
                                except:
                                    print("No discard button")
                                time.sleep(0.5)
                            except:
                                print("Connect message not found")

                            try:
                                time.sleep(1)
                                con_acc_btnn = WebDriverWait(driver, 5).until(
                                    EC.presence_of_element_located((By.XPATH, '//button[contains(normalize-space(), "Accept")]'))
                                )
                                time.sleep(0.5)
                                if con_acc_btnn:
                                    print("connect accepted")
                                con_acc_btnn.click()
                                time.sleep(3)

                            except:
                                print("No accept button found")

                        except:
                            print("Error in accepting connection")

            except:
                print("not found on connection page")
        except:
            print("Accept button not found on connection page")
except:
    print("No connection found")
time.sleep(2)
stop_profile()
           