#################---//open this app at the exact time of lecture start\\---########################
import os
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.common.keys import Keys
    from selenium.common.exceptions import NoSuchElementException
    import time
    import datetime
    import tkinter as tk
    from tkinter import simpledialog
    import urllib
except:
    os.system('pip install selenium')
    os.system('pip install webdriver-manager')
    os.system('pip install datetime')
    os.system('pip install tk')
    os.system('pip install urllib3')
finally:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.common.keys import Keys
    from selenium.common.exceptions import NoSuchElementException
    import time
    import datetime
    import tkinter as tk
    from tkinter import simpledialog
    import urllib


usrnm=''
pswd=''
captcha=''
clscount=0
root=tk.Tk()
driver = webdriver.Chrome(ChromeDriverManager().install())
def get_time(timest):
    #eg->9:00 AM - 10:00 AM
    timest=timest.split(" -") 
    timest=timest[0]
    if 'AM' in timest:
        print(timest)
        final_time=timest[:-3]+':00'
        print(final_time)
    else:
        final_time=timest[:-3]
        final_time=final_time.split(":")
        temp=final_time[1]
        final_time=final_time[0]
        if not final_time=='12':
            addtwl=str(int(final_time)+12)
            final_time=addtwl+":"+temp+":00"
        else:
            addtwl=str(int(final_time)+0)
            final_time=addtwl+":"+temp+":00"
        print(final_time)
    return final_time

def jot(final_time):
    timestamp = time.strftime('%H:%M')
    print(timestamp)
    ft=final_time[0:5].split(':')
    ct=timestamp.split(':')
    print(ft,ct)
    diffh=-int(ft[0])+int(ct[0])
    diffm=-int(ft[1])+int(ct[1])
    diff=diffh*60+diffm
    print(diff)
    if diff>-1 and diff<=70:
        print("You are late by "+str(diff)+" m.\nLets join...")
        return 1
    elif diff>-1 and diff>70:
        print('Your class finished '+str(diff)+'m ago.')
        return 0
    else:
        print('You have '+str(-diff)+' m to start the class.')
        return diff

def poll():
    try:
        try:
            frame = WebDriverWait(driver,1).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="frame"]')))
            driver.switch_to.frame(frame)
        except Exception as e: 
            print("-",end="")
        time.sleep(1)
        try:
            driver.find_element_by_xpath("//*[@id='app']/main/div[2]/div/div[2]/div[1]/button").click()
        except:
            driver.find_element_by_xpath("//*[@id='app']/main/div[1]/div/div[2]/div[1]/button").click()
        print(" :)Polled!")
    except Exception as e:
        print(".",end="")
        
    # #poll options
    # #     '''//*[@id="app"]/main/div[2]/div/div[2]/div[1]/button'''
    # #1 out of 3optn
    # '''//*[@id="app"]/main/div[2]/div/div[2]/div[1]/button'''
    # #3 out of 3
    # '''//*[@id="app"]/main/div[2]/div/div[2]/div[3]/button'''

def join_audio():
    try:
        frame = WebDriverWait(driver, 300).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="frame"]')))
        driver.switch_to.frame(frame)
        listenMode = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/span/button[2]')))
        listenMode.click()
    except Exception as e:
        print("No Audio Mode")
    print("Audio Mode Selected")

def get_details():
    global usrnm
    global pswd
    global captcha
    root.withdraw()
    if os.path.isfile('login_up.txt'):
        f=open('login_up.txt','r')
        usrnm=f.readline()
        pswd=f.readline()
    else:
        f=open('login_up.txt','w')
        usrnm=simpledialog.askstring(title="Username",prompt="Enter the Username here:")
        f.write("u-"+usrnm+"\n")
        pswd=simpledialog.askstring(title="Password",prompt="Enter the Password here:")
        f.write("p-"+pswd)
        f.close()
        f=open('login_up.txt','r')
        usrnm=f.readline()
        pswd=f.readline()
        f.close()
    captcha=simpledialog.askstring(title="Captcha",prompt="Enter the captcha here:")
    
    usrnm=usrnm[2:10]
    pswd=pswd[2:]
    captcha=captcha
    return usrnm,pswd,captcha


def wishTeacher():
    now = datetime.datetime.now()
    if(now.hour<12):
        wish="Good Morning"
    elif(now.hour>=12 and now.hour<=16):
        wish="Good Afternoon"
    else:
        wish="Good Evening"

    try:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div/main/section/div/header/div/div[1]/div[1]/button')))
        time.sleep(7)
        driver.find_element_by_xpath("/html/body/div/main/section/div/header/div/div[1]/div[1]/button").click()
        driver.find_element_by_xpath('//*[@id="chat-toggle-button"]').click()
        chatbox = driver.find_element_by_id("message-input")
        # chatbox.send_keys(wish)
        chatbox.send_keys(wish)
        chatbox.send_keys(Keys.RETURN)
    except Exception as e:
        print("Teacher not wished:(")

def run():
    driver.maximize_window()
    def site_login():
        driver.get("https://myclass.lpu.in/")
        driver.get("https://myclass.lpu.in/")
        try:
            try:
                rcnt = open("D:/captcha/count.txt", "r")
                cnt=int(rcnt.read())
                rcnt.close()
                cnt+=1
                acnt=open("D:/captcha/count.txt", "w")
                acnt.write(str(cnt))
                acnt.close()
                rcnt = open("D:/captcha/count.txt", "r")
                print(rcnt.read())
                rcnt.close()
            except:
                print('count not done')
            capimg=driver.find_element_by_xpath('//*[@id="c_default_maincontent_examplecaptcha_CaptchaImage"]')
            src=capimg.get_attribute('src')
            print(cnt,type(cnt))
            nwcnt=str(cnt)
            urllib.request.urlretrieve(src,"D:/captcha/"+nwcnt+".png")
        except:
            print('cp not saved')
        get_details()
        driver.find_element_by_id("txtUserName").send_keys(usrnm)
        driver.find_element_by_id ("txtPassword").send_keys(pswd)
        driver.find_element_by_id("CaptchaCodeTextBox").send_keys(captcha)
        driver.find_element_by_id("MainContent_btnSubmit").click()
        time.sleep(1)
        driver.find_element_by_link_text("View Classes/Meetings").click()
        time.sleep(1)
        a=[]
        links=[]
        b=[]
        clstime=[]
        count=0
        a=driver.find_elements_by_css_selector(".fc-time-grid-event.fc-event.fc-start.fc-end")
        for i in range (len(a)):
            app=str(i+1)
            b.append(driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a['+app+']/div/div[1]'))
        for i in a:
            links.append(i.get_attribute("href"))
            count+=1
        for i in b:
            print(i.get_attribute("data-full"))
            clstime.append(get_time(i.get_attribute("data-full")))
            # final_time=i.get_attribute("data-full")
            # print(final_time)
            # # final_time=get_time(final_time)
            # clstime.append(i.get_attribute(i.get_attribute("data-full")))
        
        print(a)
        print(links)
        print(clstime)

        wincnt=1



        #time wise attendence
        # for prd in clstime:
        #     if jot(prd)==1:
        #         driver.get(links[clscount])
        #     elif jot(prd)==0:
        #         print('classdone')
        #     else:
        #         time.sleep(jot(-prd*60))
        #     clscount=clscount+1

        for j in links:
            try:
                jot(clstime[wincnt-1])
            except:
                print('jot//no')
            driver.get(j)
            time.sleep(1)
            try:
                driver.find_element_by_css_selector(".btn.btn-primary.btn-block.btn-sm").click()
                flag=True
            except Exception as e:
                print("Join btn not found")
                flag=False
            if flag:
                join_audio()
                wishTeacher()
                time.sleep(5)
                for k in range(11):
                    # try:
                    #     driver.find_element_by_id("message-input").send_keys("Okay")
                    #     driver.find_element_by_id("message-input").send_keys(Keys.RETURN)
                    # except Exception as e:
                    #     print("Msg box and ok btn not found")
                    #     break
                    for l in range(300):
                        time.sleep(1)
                        poll()
                        
            print("\n----------------#---------------------#------------------#-----------------------")  
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[wincnt])
            wincnt+=1
    site_login()
run()
