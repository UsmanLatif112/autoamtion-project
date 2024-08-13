import requests
from lib.start_profile import *
from lib.resources import Login,Code
from lib.function import *
from lib.data import *
username = "usmanlatif0309@gmail.com"
password = "DSJoker@@03360325@.okay"
comment = "CFBR"
"""=================================================="""
driver= start_profile()
driver.maximize_window()
driver.get("https://www.linkedin.com/login")
time.sleep(2)
actions = ActionChains(driver)
try:
    
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row
        
        for row in csv_reader:
            # Assuming columns are indexed as 0, 1, 2, etc.
            creator_link = row[1]            
            driver.get(f"{creator_link}recent-activity/all/")
            success = 0
            i = 1
            while success < 1:
                try:
                    try:
                        time.sleep(1)
                        block_comment = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@class="comments-disabled-comments-block"][contains(normalize-space(), "Only group members can comment on this post. You can still react or repost it.")]')))
                        if block_comment:
                           i += 1 
                    except:
                        print("no block_comment found")
                    time.sleep(2)
                    post_cmnt = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f'(//*[@id="fie-impression-container"])[{i}]//button[contains(normalize-space(), "Comment")]')))
                    time.sleep(0.5)
                    actions.move_to_element(post_cmnt).perform()
                    time.sleep(1)
                    post_cmnt.click()
                    time.sleep(1)
                    print("Comment button found")
                    if post_cmnt:
                        try:
                            time.sleep(2)
                            like_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f'(//*[@id="fie-impression-container"])[{i}]//button[contains(normalize-space(), "Like")]')))
                            time.sleep(1)
                            like_btn.click()
                        except:
                            print("Like button not found")
                        try:
                            time.sleep(3)
                            cmnt_box_x = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f'(//*[@id="fie-impression-container"])[{i}]//*[@data-placeholder="Add a comment…"]')))
                            cmnt_box_x.click()
                            time.sleep(1)
                            for char in comment:
                                cmnt_box_x.send_keys(char)
                                time.sleep(0.1)
                        except Exception as e:
                            print(e)
                            print("unable to type comment")
                            continue
                        try:
                            time.sleep(0.5)
                            post_btnn = HomePage(driver)
                            post_btnn.wait_five(Code.post_btn)
                            time.sleep(0.5)
                            post_btn_n = HomePage(driver)
                            post_btn_n.click_btn(Code.post_btn)
                            success += 1
                            i += 1
                            print(success)
                            print(i)
                        except:
                            print("post comment buuton not found")
                        try:
                            time.sleep(0.5)
                            cmnt_btnn = HomePage(driver)
                            cmnt_btnn.wait_five(Code.cmnt_btn)
                            time.sleep(0.5)
                            cmnt_btn_n = HomePage(driver)
                            cmnt_btn_n.click_btn(Code.cmnt_btn)
                            success += 1
                            i += 1
                            print(success)
                            print(i)
                        except:
                            print("Comment_comment button not found")
                    else:
                        print("comment button not found")
                        print(e)
                        i += 1
                        continue
                except Exception as e:
                    print("comment button not found")
                    print(e)
                    i += 1
                    continue
                time.sleep(2)
                continue
        stop_profile()
except Exception as e:
    print(e)
    time.sleep(0.5)
    stop_profile()
    # remove_profile(profile_iD)
# Security_Code_Input_email = HomePage(driver)
# Security_Code_Input_email.wait_five(Code.security_code_input_em)
# Security_Code_Input_Email = HomePage(driver)
# Security_Code_Input_Email.click_btn(Code.security_code_input_em)
# time.sleep(0.5)
# Security_Code_Input_Emaill = HomePage(driver)
# Security_Code_Input_Emaill.enter_name_delay(Code.security_code_input_em, "usman")
    