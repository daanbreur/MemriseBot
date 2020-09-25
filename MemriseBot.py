#  Copyright (c) 2020.
#  Created By: Daan Breur

from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from utils import Word


class MemriseBot:
    def __init__(self, username, password, course_id, word_list=None):
        if word_list is None:
            word_list = []
        self.username = username
        self.password = password
        self.course_id = course_id
        self.wordList = word_list

        self.qIndex = 0
        self.driver = webdriver.Chrome('./chromedriver.exe')
        print("[Bot] Successfully Initialized")

    def login(self):
        self.driver.get('https://memrise.com/login/')
        sleep(2)

        print(f"[Login] Username: {self.username}")
        print(f"[Login] Password: [censored]")

        try:
            self.driver.find_element_by_xpath(
                '/html/body/div[3]/div[4]/div/div[2]/div/div/div/form/div[3]/input').send_keys(
                self.username)  # Username Field
            self.driver.find_element_by_xpath(
                '/html/body/div[3]/div[4]/div/div[2]/div/div/div/form/div[4]/input'
            ).send_keys(
                self.password)  # Password Field
            self.driver.find_element_by_xpath(
                '/html/body/div[3]/div[4]/div/div[2]/div/div/div/form/input[3]').click()  # Submit Button
            sleep(2)
        except NoSuchElementException:
            print("[Login] Failed... Terminating Application.")
            exit()

        try:
            self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/div/button').click()  # Close AD
            sleep(2)
        except NoSuchElementException:
            print("Close AD Failed... Terminating Application.")

        try:
            self.driver.find_element_by_xpath(
                f'//*[@id="course-{self.course_id}"]/div/div[1]/div[2]/div/div/div[1]/p/a').click()  # Open Course
            sleep(2)
        except NoSuchElementException:
            print("Couldn't open Course... Terminating Application.")
            exit()

        word_list_elmnt = self.driver.find_elements_by_class_name('thing')
        for word_elmnt in word_list_elmnt:
            word_a = word_elmnt.find_element(By.XPATH, './/div[3]/div').text  # Word A
            word_b = word_elmnt.find_element(By.XPATH, './/div[4]/div').text  # Word B
            self.wordList.append(Word(word_a, word_b))

        try:
            self.driver.find_element_by_xpath(
                '//*[@id="content"]/div/div/div[1]/div[1]/div[3]/a[4]').click()  # Start Learn
            sleep(1)
        except NoSuchElementException:
            print("Couldn't start learning... Terminating Application.")
            exit()

        self.start_guessing()

    def start_guessing(self):
        while True:
            sleep(2)
            if self.check_exists_by_xpath('//*[@id="boxes"]/div/button'):
                try:
                    self.driver.find_element_by_xpath('//*[@id="boxes"]/div/button').click()  # Next Button
                    print(f"[Question #{self.qIndex}] Next Button")
                    self.qIndex += 1
                except Exception:
                    print( "An error has occurred at Next Button" )
                    print( Exception )  
            else:
                if self.driver.find_element_by_xpath('/html/body/div[4]/div/p').text == 'Session complete!':
                    try:
                        self.driver.find_element_by_xpath('/html/body/div[5]/div[3]/div/div/div[3]').click()
                        sleep(2)
                        self.driver.find_element_by_xpath('/html/body/div[5]/div[3]/div/div/div[3]/div[2]/div[5]/div/a').click()
                    except Exception:
                        print( "An error has occurred at Session Complete Button" )
                        print( Exception )  
                    
                else:
                    answer = ''
                    question_txt = self.driver.find_element_by_xpath('//*[@id="prompt-row"]/div/div').text
                    for item in self.wordList:
                        if item.english == question_txt:
                            answer = item.dutch
                            self.answer_question(answer, question_txt)
                            self.qIndex += 1
                        elif item.dutch == question_txt:
                            answer = item.english
                            self.answer_question(answer, question_txt)
                            self.qIndex += 1

    def answer_question(self, answer, question_txt):
        if self.check_exists_by_xpath('//*[@id="boxes"]/div/ol/li[1]/span[2]'):
            print(f"[Question #{self.qIndex}] Type: MultipleChoice Question: {question_txt} Answer: {answer}")
            for i in range(1, 10):
                try:
                    button = self.driver.find_element_by_xpath(f'//*[@id="boxes"]/div/ol/li[{i}]/span[2]')
                    button_txt = button.text
                    print(f"[{i}] {button_txt}")
                    if button_txt == answer:
                        button.click()
                        break
                except NoSuchElementException:
                    break
        else:
            print(f"[Question #{self.qIndex}] Type: InputBox Question: {question_txt} Answer: {answer}")
            answer_input = self.driver.find_element_by_xpath('//*[@id="boxes"]/div/div[4]/input')
            answer_input.send_keys(answer)

    def check_exists_by_xpath(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True
