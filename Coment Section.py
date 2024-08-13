import requests
from lib.start_profile import *
from lib.resources import Login,Code
from lib.function import *
from lib.data import *
username = "usmanlatif0309@gmail.com"
password = "DSJoker@@03360325@.okay"
comment = "CFBR"
# comment = "Quality isn't just a step; it's the foundation. Let's build it right the first time!"
"""=================================================="""
driver= start_profile()
driver.maximize_window()
driver.get("https://www.linkedin.com/login")
time.sleep(5)
try:
    try:
        Search_Bar = HomePage(driver)
        Search_Bar.wait_ten(Code.Search_Bar)
        Search_Barr = HomePage(driver)
        Search_Barr.click_btn(Code.Search_Bar) 
        time.sleep(.5)
        Search_Barrr = HomePage(driver)
        Search_Barrr.enter_name_delay(Code.Search_Bar, "my name")
        time.sleep(1)
        actions = ActionChains(driver)
        actions.send_keys(Keys.ENTER).perform()
        try:
            time.sleep(1)
            Post_fill_l = HomePage(driver)
            Post_fill_l.wait_ten(Code.Post_fil)
            time.sleep(0.5)
            Post_fill = HomePage(driver)
            Post_fill.click_btn(Code.Post_fil)
        except Exception as e:
            print(e)
        try:
            time.sleep(1)
            Sort_Byy_y = HomePage(driver)
            Sort_Byy_y.wait_ten(Code.Sort_By)
            time.sleep(0.5)
            Sort_Byy = HomePage(driver)
            Sort_Byy.click_btn(Code.Sort_By)
            time.sleep(0.5)
            Latest_post_t = HomePage(driver)
            Latest_post_t.wait_ten(Code.Latest_post)
            time.sleep(0.5)
            Latest_post_tt = HomePage(driver)
            Latest_post_tt.click_btn(Code.Latest_post)
            time.sleep(0.5)
            Latest_post_btn_n = HomePage(driver)
            Latest_post_btn_n.wait_ten(Code.Latest_post_btn)
            time.sleep(0.5)
            Latest_post_btnn = HomePage(driver)
            Latest_post_btnn.click_btn(Code.Latest_post_btn)
            time.sleep(0.5)
            Date_postedd = HomePage(driver)
            Date_postedd.wait_ten(Code.Date_posted)
            time.sleep(0.5)
            Date_posted_d = HomePage(driver)
            Date_posted_d.click_btn(Code.Date_posted)
            time.sleep(0.5)
            past_24_hourss = HomePage(driver)
            past_24_hourss.wait_ten(Code.past_24_hours)
            time.sleep(0.5)
            past_24_hours_s = HomePage(driver)
            past_24_hours_s.click_btn(Code.past_24_hours)
            time.sleep(0.5)
            past_24_hours_btnn = HomePage(driver)
            past_24_hours_btnn.wait_ten(Code.past_24_hours_btn)
            time.sleep(0.5)
            past_24_hours_btn_s = HomePage(driver)
            past_24_hours_btn_s.click_btn(Code.past_24_hours_btn)
        except Exception as e:
            print(e)
    except Exception as e:
        print(e)
    time.sleep(3)
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row
        
        for row in csv_reader:
            # Assuming columns are indexed as 0, 1, 2, etc.
            creator_link = row[0]
            time.sleep(1)
            Search_Bar = HomePage(driver)
            Search_Bar.wait_ten(Code.Search_Bar)
            Search_Barr = HomePage(driver)
            Search_Barr.click_btn(Code.Search_Bar) 
            time.sleep(.5)
            Search_Barrr = HomePage(driver)
            Search_Barrr.enter_name_delay(Code.Search_Bar, creator_link)
            time.sleep(1)
            time.sleep(1)
            actions = ActionChains(driver)
            actions.send_keys(Keys.ENTER).perform()
            
            success = 0
            i = 1
            while success < 3:
                try:
                    time.sleep(2)
                    post_cmnt = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f'(//*[@id="fie-impression-container"])[{i}]//button[contains(normalize-space(), "Comment")]')))
                    time.sleep(0.5)
                    actions.move_to_element(post_cmnt).perform()
                    time.sleep(0.5)
                    time.sleep(1)
                    post_cmnt.click()
                    time.sleep(1)

                    print("Comment button found")
                    if post_cmnt:
                        # Random decision to click the "Like" button or not
                        if random.choice([True, False]):  # 50% chance to click the "Like" button
                            try:
                                time.sleep(2)
                                like_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f'(//*[@id="fie-impression-container"])[{i}]//button[contains(normalize-space(), "Like")]')))
                                time.sleep(1)
                                like_btn.click()
                                print("Like button clicked")
                            except:
                                print("Like button not found")
                        else:
                            print("Skipping Like button click")
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
                            print("Comment, comment buuton not found")
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
    print("keywords list completed")
    stop_profile()
except Exception as e:
    print(e)
    time.sleep(0.5)
    stop_profile()
    