import selenium, pandas, time, requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import requests
from lxml import html



driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
action = ActionChains(driver)




driver.get("https://www.lguplus.com/")
driver.implicitly_wait(5)
time.sleep(1)
driver.maximize_window()
time.sleep(1)
print(driver.title)
# WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#_uid_3") )).get_attribute("title")





if driver.find_element(By.CSS_SELECTOR, f'#_uid_3').get_attribute("title") != "선택됨" :
    print("개인 선택되어 있지 않음")
    driver.get("https://www.lguplus.com/")
    driver.implicitly_wait(5)
    time.sleep(1)

# print(len(driver.find_elements(By.CSS_SELECTOR, "[data-gtm-click-location='네비게이터 영역']")))


def Count() :
        for i in range(1,100) :
            try :
                gnbname = driver.find_element(By.XPATH, f'//*[@id="__layout"]/div/div[3]/header/div[2]/div[1]/nav/ul/li[{i}]')
                if gnbname.text != "" :
                    print(gnbname.text)
            except :
                break



# for sub_menu_item in sub_menu_items :
#
#     sub_menu_items = sub_menu_item.find_elements(By.XPATH, './ul/li')
#
#
#     action.move_to_element(driver.find_element(By.XPATH, f'//div[@class="header"]/div[2]/div[1]/nav/ul/li[{a}]/a/span')).perform()
#     time.sleep(1)
#     for i in range(1,11) :
#         for p in range(1,11):
#             if driver.find_elements(By.XPATH, f'//div[@class="header"]/div[2]/div[1]/nav/ul/li[{a}]/div/ul/li[{i}]/ul/li[{p}]/a') is None :
#                 break
#             else :
#                 driver.find_element(By.XPATH, f'//div[@class="header"]/div[2]/div[1]/nav/ul/li[{a}]/div/ul/li[{i}]/ul/li[{p}]/a')




def slide_Control() :
    try :
        slide = f'//*[@id="cSection"]/div[1]/div[2]/div[1]/div/div[1]/div/div[2]/div/button'
        slide_count = len(driver.find_elements(By.XPATH, slide))
        playbutton = driver.find_element(By.XPATH, f'//*[@id="cSection"]/div[1]/div[2]/div[1]/div/div[1]/div/div[2]/button')
        if playbutton.get_attribute("aria-label") == "슬라이드 일시정지" :
            playbutton.click()

        for i in range(1, slide_count+1) :
            try :
                driver.find_element(By.XPATH, f'//*[@id="cSection"]/div[1]/div[2]/div[1]/div/div[1]/div/div[2]/div/button[{i}]').click()
                time.sleep(2)
                driver.find_element(By.XPATH, f'//*[@id="cSection"]/div[1]/div[2]/div[1]/div/div[1]/div/div[1]/div[{i}]/div/div[2]/img')
                if driver.find_element(By.XPATH, f'//*[@id="cSection"]/div[1]/div[2]/div[1]/div/div[1]/div/div[1]/div[{i}]').get_attribute("aria-hidden") != "false" :
                    print(f'{i}+"번째 이미지 미노출"')
                else : pass
            except Exception as E1 : print(E1)
        play = driver.find_element(By.XPATH, f'//*[@id="cSection"]/div[1]/div[2]/div[1]/div/div[1]/div/div[2]/button')
        name_play = play.get_attribute("aria-label")
        driver.find_element(By.XPATH,
                            f'//*[@id="cSection"]/div[1]/div[2]/div[1]/div/div[1]/div/div[2]/div/button[1]').click()
        play.click()
        for a in range(1,slide_count+1) :
            time.sleep(10)
            if driver.find_element(By.XPATH, f'//*[@id="cSection"]/div[1]/div[2]/div[1]/div/div[1]/div/div[1]/div[{a}]').get_attribute("aria-hidden") != "false" :
                print(f"슬라이드 미동작")
    except Exception as E :
        print(E)
 
def slide_arrow() :
    slide = f'//*[@id="cSection"]/div[1]/div[2]/div[1]/div/div[1]/div/div[2]/div/button'
    slide_count = len(driver.find_elements(By.XPATH, slide))
    playbutton = driver.find_element(By.XPATH, f'//*[@id="cSection"]/div[1]/div[2]/div[1]/div/div[1]/div/div[2]/button')
    if playbutton.get_attribute("aria-label") == "슬라이드 일시정지":
        playbutton.click()
    for b in range(1,slide_count) :
        try :
            driver.find_element(By.XPATH, f'//*[@id="cSection"]/div[1]/div[2]/div[1]/div/div[1]/div/button[2]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, f'//*[@id="cSection"]/div[1]/div[2]/div[1]/div/div[1]/div/div[1]/div[{b+1}]/div/div[2]/img')
        except Exception as E1 :
            print(E1)






# def benefit() :
#     try :
#         action.move_to_element(driver.find_element(By.CLASS_NAME, "benefits-section")).perform()
#         time.sleep(2)
#         if driver.find_element(By.XPATH, f'//*[@id="cSection"]/div[1]/div[2]/div[2]/div/div/div[1]/p').text != "유플러스 이벤트를 만나보세요" :
#             print("베네핏 타이틀 에러")
#         else : pass
#         benefit_frame = driver.find_elements(By.XPATH, '//*[@id="cSection"]/div[1]/div[2]/div[2]/div/div/div[2]')
#         for a in len(benefit_content) :
#             benefit_content = benefit_frame.find_elements(By.XPATH, '/div[@Class="item-box type-long')
#             print(len(benefit_content))
#
#
#     except Exception as E : print(E)

def benefit():
    try:
        action.move_to_element(driver.find_element(By.CLASS_NAME, "benefits-section")).perform()
        time.sleep(2)
        if driver.find_element(By.XPATH, f'//*[@id="cSection"]/div[1]/div[2]/div[2]/div/div/div[1]/p').text != "유플러스 이벤트를 만나보세요":
            print("베네핏 타이틀 에러")
        else:
            benefit_frame = driver.find_element(By.XPATH, '//*[@id="cSection"]/div[1]/div[2]/div[2]/div/div/div[2]')
            benefit_content = benefit_frame.find_elements(By.XPATH, './/div[@class="item-box type-long"]/a')



            # print(len(benefit_content))
            a = 1
            for i in benefit_content :
                benefit_title = i.get_attribute("data-gtm-click-text")
                print(a,":",benefit_title)
                a += 1

    except Exception as E:
        print(E)

def paymentsection() :
    action.move_to_element(driver.find_element(By.CLASS_NAME, f'payment-section')).perform()
    time.sleep(2)
    # try :
    #     print(driver.find_element(By.XPATH, f'//*[@id="cSection"]/div[1]/div[2]/div[3]/div/div/div[1]/p').text)
    # except Exception as E :
    #     pritn(E)
    try :
        common_xpath = '//*[@id="cSection"]/div[1]/div[2]/div[3]/div/div/div[2]/'

        # Get the number of elements at the second depth
        num_elements = len(driver.find_elements(By.XPATH, common_xpath + 'div'))
        driver.find_elements(By.XPATH, common_xpath + 'div')
        # Iterate over the elements at the second depth
        # for i in range(1, num_elements + 1):
        #     # Construct the XPath for each element at the second depth
        #     xpath = common_xpath + f'div[{i}]'
        #
        #     # Wait for the element to be visible and fully loaded
        #     element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        #
        #     # Get the 'src' attribute of the element
        #     src_attribute = element.get_attribute('src')
        #
        #     # Print the 'src' attribute
        #     print(f"src Attribute for element {i}: {src_attribute}")
    except : print("N")

def blurbTest() :
    action.move_to_element(driver.find_element(By.CLASS_NAME, 'blurb-area')).perform()
    time.sleep(2)
    blurb_Title = driver.find_elements(By.XPATH, '//*[@id="cSection"]/div[1]/div[2]/div[4]/div/div[1]/div[1]/p')

    for i in blurb_Title :
        if i.text == "" :
            print("blurb 영역 타이틀 미노출")
            break

    if driver.find_elements(By.XPATH, '//*[@id="cSection"]/div[1]/div[2]/div[4]/div/div[2]/img') is None :
        print("Blurb img Error")
    if driver.find_elements(By.XPATH, '//*[@id="cSection"]/div[1]/div[2]/div[4]/div/div[2]/img') is None :
        print("Blurb bg img Error")

def promotion_section() :
    promotion_section_title = driver.find_element(By.XPATH, '//*[@id="cSection"]/div[1]/div[2]/div[5]/div/div[1]')
    action.move_to_element(promotion_section_title).perform()
    time.sleep(2)
    title_text = promotion_section_title.find_elements(By.CLASS_NAME, 'h1')
    for i in title_text :
        if i.text == "" :
            print("프로모션 타이틀 에러")
            break

    Content_Total_Count = driver.find_elements(By.XPATH, '//*[@id="cSection"]/div[1]/div[2]/div[5]/div/div[2]/ul/li')
    # print(len(Content_Total_Count))
    for i in (1,len(Content_Total_Count)) :
        try : driver.find_element(By.XPATH, f'//*[@id="cSection"]/div[1]/div[2]/div[5]/div/div[2]/ul/li[{i}]/a/img')
        except : print(i,"번째 이미지 없음")
    # for i in Content :
    #     print(i)

def Device_recommend() :
    title = driver.find_element(By.XPATH, '//*[@id="cSection"]/div[1]/div[2]/div[6]/div/div/div[1]')
    action.move_to_element(title).perform()
    time.sleep(2)
    title_Text = title.find_elements(By.XPATH, './/p')
    for i in title_Text :
        if i.text == "" :
            print("Error")
            break

    tablist = driver.find_element(By.XPATH, '//*[@id="cSection"]/div[1]/div[2]/div[6]/div/div/div[2]')
    tablist_Count = tablist.find_elements(By.XPATH, './/li')
    for i in range(1,len(tablist_Count)+1) :
        try :
            driver.find_element(By.XPATH, f'//*[@id="cSection"]/div[1]/div[2]/div[6]/div/div/div[2]/ul/li[{i}]/a').text
            driver.find_element(By.XPATH, f'//*[@id="cSection"]/div[1]/div[2]/div[6]/div/div/div[2]/ul/li[{i}]/a').click()
            time.sleep(1)
            driver.find_element(By.XPATH, f'//*[@id="recomm-tabcon-0{i}"]/ul')
            tablist_Content = driver.find_elements(By.XPATH, f'//*[@id="recomm-tabcon-0{i}"]/ul/li')
            for b in range(1,len(tablist_Content)+1) :
                tablist_Content_detail = driver.find_element(By.XPATH, f'//*[@id="recomm-tabcon-0{i}"]/ul/li[{b}]')
                if tablist_Content_detail.get_attribute("href") == "" :
                    print("연결된 페이지 없음")








        except Exception as E :
            print(E)

def HlepDesk() :
    HelpDesk_title = f'//*[@id="CUST"]/div[1]/p'
    action.move_to_element(driver.find_element(By.XPATH, HelpDesk_title)).perform()
    time.sleep(1)
    try :
        HelpDesk_Content = f'//*[@id="CUST"]/div[2]/div'
        for i in range(1, len(driver.find_elements(By.XPATH, HelpDesk_Content))+1) :
            driver.find_element(By.XPATH, HelpDesk_Content+f'[{i}]'+'/i/img')


    except Exception as E :
        print(E)

if __name__ == '__main__' :
    Count()
    slide_Control()
    slide_arrow()
    benefit()
    paymentsection()
    blurbTest()
    promotion_section()
    Device_recommend()
    HlepDesk()


