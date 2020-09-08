from selenium.webdriver import *
import selenium as sl
class xpaths:
    messaging_box_xpath = ""
    search_box_xpath = "/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]"
    contact_name_xpath = "_2EXPL"
    text_box_xpath = "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]"

class whatsapp_bot(xpaths):
    
    
    
    chat_status = False
    def open_url(self):
        self.driver.get("web.whatsapp.com")

    def __init__():
        driver = Chrome()
        self.contact_name = ''
        self.open_url()

    def return_element(self,standard=xpath,locator=''):
        if standard !=xpath:
            return self.driver.find_element_by_class_name(locator)

        else:
            return self.driver.find_element_by_xpath(locator)

    def open_chat(self,name):
        try:
            search_box = self.return_element(locator=self.search_box_xpath)
            search_box.click()
            search_box.send_keys(name)
            target = self.return_element(standard='class',locator=self.contact_name_xpath)
            target.click()
            self.chat_status = True
            self.contact_name = name
        except:
            print("Error please choose another contact or try again")

    def messaging(self,message):
        textbox = self.return_element(locator=self.messaging_box_xpath)
        text_box.send_keys(message + Keys.ENTER)


