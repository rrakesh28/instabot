from tkinter import *
from tkinter.ttk import Progressbar

import threading

import xlsxwriter

from plyer import notification

from instabot import Bot
import os 
import glob
window = Tk()
window.title("Instagram Bot")
window.geometry("1366x700")
window.configure(bg = "#ffffff")
window.resizable(False, False)

bot = Bot()

username_variable = StringVar()
password_variable = StringVar()

username_for_list_variable = StringVar()
followers_checkbox = IntVar()
following_checkbox = IntVar()
path_for_users_save_variable = StringVar()

path_to_save_usernames_variable = StringVar()
path_to_save_non_followers = StringVar()

dont_repeat_variable = IntVar()
delay_time_variable = StringVar()

likers_checkbox = IntVar()
commenters_checkbox = IntVar()
path_to_save_likers_commenters_variable = StringVar()

logo = PhotoImage(file='logo.gif')
window.tk.call('wm', 'iconphoto', window._w, logo)

class accountPanel:
    def pack(self,username):
        self.canvas = Canvas(
            window,
            bg = "#CACACA",
            height = 700,
            width = 1366,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.canvas.place(x = 0, y = 0)


        self.canvas.create_text(
            91.5, 54.0,
            text = username,
            fill = "#000000",
            tags = "username",
            font = ("None", int(16.0)))

        #Get users
        self.canvas.create_text(
            56.5, 114.5,
            text = "Get Users",
            fill = "#000000",
            font = ("Roboto-Bold", int(13.0)))

        self.canvas.create_text(
            60.5, 143.5,
            text = "Username",
            fill = "#000000",
            font = ("None", int(12.0)))

        #username entry
        self.entry0_img = PhotoImage(file = f"img_textBox0.png")
        self.entry0_bg = self.canvas.create_image(
            121.0, 177.5,
            image = self.entry0_img)

        self.entry0 = Entry(
            bd = 0,
            bg = "#ffffff",
            textvariable = username_for_list_variable,
            highlightthickness = 0)

        self.entry0.place(
            x = 40.0, y = 165,
            width = 162.0,
            height = 27)

        #path to save user_id's entry
        self.entry1_img = PhotoImage(file = f"img_textBox1.png")
        self.entry1_bg = self.canvas.create_image(
            143.5, 265.5,
            image = self.entry1_img)

        self.entry1 = Entry(
            bd = 0,
            bg = "#ffffff",
            textvariable = path_for_users_save_variable,
            highlightthickness = 0)

        self.entry1.place(
            x = 79.0, y = 253,
            width = 129.0,
            height = 27)

        #followers check box
        self.checkbox0 = Checkbutton(
            text = "Followers", 
            bg = '#CACACA',
            variable = followers_checkbox,
            onvalue = 1, 
            offvalue = 0, 
            height=1, 
            width = 20)
        self.checkbox0.place(
            x = 40, y = 206)

        #following checkbox
        self.checkbox1 = Checkbutton(
            text = "Following", 
            bg = '#CACACA',
            variable = following_checkbox,
            onvalue = 1, 
            offvalue = 0, 
            height=1, 
            width = 20)
        self.checkbox1.place(
            x = 40, y = 229)

        #Get users followers and following btn
        self.img0 = PhotoImage(file = f"img0.png")
        self.b0 = Button(
            image = self.img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = get_list_thread,
            relief = "flat")

        self.b0.place(
            x = 75, y = 292,
            width = 83,
            height = 26)


        #Usernames from userid's
        self.canvas.create_text(
            72.0, 340.5,
            text = "Get Usernames",
            fill = "#000000",
            font = ("None", int(13.0)))

        self.canvas.create_text(
            45.5, 363.5,
            text = "User id’s",
            fill = "#000000",
            font = ("None", int(13.0)))

        #entry for userid's
        self.entry6_img = PhotoImage(file = f"img_textBox6.png")
        self.entry6_bg = self.canvas.create_image(
            102.0, 484.5,
            image = self.entry6_img)

        self.entry6 = Text(
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0)

        self.entry6.place(
            x = 37.0, y = 385,
            width = 130.0,
            height = 201)

        #path to save usernames entry
        self.entry2_img = PhotoImage(file = f"img_textBox2.png")
        self.entry2_bg = self.canvas.create_image(
            143.5, 623.5,
            image = self.entry2_img)

        self.entry2 = Entry(
            bd = 0,
            bg = "#ffffff",
            textvariable = path_to_save_usernames_variable,
            highlightthickness = 0)

        self.entry2.place(
            x = 79.0, y = 611,
            width = 129.0,
            height = 27)

        #btn for usernames
        self.img2 = PhotoImage(file = f"img2.png")
        self.b2 = Button(
            image = self.img2,
            borderwidth = 0,
            highlightthickness = 0,
            command = get_usernames_thread,
            relief = "flat")

        self.b2.place(
            x = 43, y = 661,
            width = 140,
            height = 26)

        self.canvas.create_text(
            294.0, 42.5,
            text = "Auto Dm",
            fill = "#000000",
            font = ("Roboto-Bold", int(15.0)))

        #check for dont' repeat
        self.checkbox2 = Checkbutton(
            text = "Don't repeat", 
            bg = '#CACACA',
            variable = dont_repeat_variable,
            onvalue = 1, 
            offvalue = 0, 
            height=1, 
            width = 20)
        self.checkbox2.place(
            x = 290, y = 74)

        self.canvas.create_text(
            338.5, 125.5,
            text = "Delay Time(sec):",
            fill = "#000000",
            font = ("None", int(13.0)))

        #entry for delay time
        self.entry10_img = PhotoImage(file = f"img_textBox10.png")
        self.entry10_bg = self.canvas.create_image(
            426.5, 124.5,
            image = self.entry10_img)

        self.entry10 = Entry(
            bd = 0,
            bg = "#fefefe",
            textvariable = delay_time_variable,
            highlightthickness = 0)

        self.entry10.place(
            x = 418, y = 118,
            width = 19,
            height = 15)
        self.canvas.create_text(
            404.0, 196.5,
            text = "Message",
            fill = "#000000",
            font = ("None", int(16.0)))

        self.entry11_img = PhotoImage(file = f"img_textBox11.png")
        self.entry11_bg = self.canvas.create_image(
            407.0, 371.0,
            image = self.entry11_img)

        #entry for message
        self.entry11 = Text(
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0)

        self.entry11.place(
            x = 280.0, y = 214,
            width = 254.0,
            height = 314)

        #usernames entry to send messages
        self.entry12_img = PhotoImage(file = f"img_textBox12.png")
        self.entry12_bg = self.canvas.create_image(
            684.0, 356.0,
            image = self.entry12_img)

        self.entry12 = Text(
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0)

        self.entry12.place(
            x = 581.0, y = 63,
            width = 206.0,
            height = 584)

        #btn for send message
        self.img3 = PhotoImage(file = f"img3.png")
        self.b3 = Button(
            image = self.img3,
            borderwidth = 0,
            highlightthickness = 0,
            command = send_thread,
            relief = "flat")

        self.b3.place(
            x = 370, y = 541,
            width = 79,
            height = 30)

        self.canvas.create_text(
            612.5, 42.5,
            text = "Usernames",
            fill = "#000000",
            font = ("None", int(15.0)))

        self.canvas.create_text(
            45.0, 265.5,
            text = "Path:",
            fill = "#000000",
            font = ("None", int(13.0)))

        self.canvas.create_text(
            45.0, 623.5,
            text = "Path:",
            fill = "#000000",
            font = ("None", int(13.0)))

        self.canvas.create_text(
            1104.0, 236.5,
            text = "Path:",
            fill = "#000000",
            font = ("None", int(13.0)))

        #Unfollow users
        self.canvas.create_text(
            928.0, 42.0,
            text = "Unfollow",
            fill = "#000000",
            font = ("Roboto-Bold", int(16.0)))

        self.canvas.create_text(
            926.0, 95.5,
            text = "Usernames to unfollow",
            fill = "#000000",
            font = ("None", int(13.0)))

        #Usernames entry to unfollow
        self.entry13_img = PhotoImage(file = f"img_textBox13.png")
        self.entry13_bg = self.canvas.create_image(
            934.0, 255.5,
            image = self.entry13_img)

        self.entry13 = Text(
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0)

        self.entry13.place(
            x = 849, y = 116,
            width = 170,
            height = 281)

        #btn to unfollow users
        self.img4 = PhotoImage(file = f"img4.png")
        self.b4 = Button(
            image = self.img4,
            borderwidth = 0,
            highlightthickness = 0,
            command = unfollow_users_thread,
            relief = "flat")

        self.b4.place(
            x = 886, y = 408,
            width = 79,
            height = 30)

        #unfollow non-followers
        self.canvas.create_text(
            915.0, 479.5,
            text = "Unfollow non-followers",
            fill = "#000000",
            font = ("None", int(12.0)))

        #btn to unfollow non-followers
        self.img6 = PhotoImage(file = f"img6.png")
        self.b6 = Button(
            image = self.img6,
            borderwidth = 0,
            highlightthickness = 0,
            command = unfollow_non_followers_thread,
            relief = "flat")

        self.b6.place(
            x = 886, y = 517,
            width = 79,
            height = 30)

        #Get non-followers
        self.canvas.create_text(
            886.0, 570.5,
            text = "Get Non-followers",
            fill = "#000000",
            font = ("Roboto-Bold", int(11.0)))

        #path to save non followers
        self.canvas.create_text(
            886.0, 600.5,
            text = "Path:",
            fill = "#000000",
            font = ("None", int(10.0)))

        self.entry16_img = PhotoImage(file = f"img_textBox3.png")
        self.entry16_bg = self.canvas.create_image(
            1000.0, 600.5,
            image = self.entry16_img)

        self.entry16 = Entry(
            bd = 0,
            bg = "#ffffff",
            textvariable = path_to_save_non_followers,
            highlightthickness = 0)

        self.entry16.place(
            x = 930.0, y = 588,
            width = 136.0,
            height = 27)

        #btn to get non followers
        self.img10 = PhotoImage(file = f"img6.png")
        self.b10 = Button(
            image = self.img10,
            borderwidth = 0,
            highlightthickness = 0,
            command = get_non_followers_thread,
            relief = "flat")

        self.b10.place(
            x = 886, y = 630,
            width = 79,
            height = 30)


        #Get likers and commenters
        self.canvas.create_text(
            1177.0, 44.5,
            text = "Get Users",
            fill = "#000000",
            font = ("Roboto-Bold", int(16.0)))

        self.canvas.create_text(
            1119.0, 92.0,
            text = "Post Link",
            fill = "#000000",
            font = ("None", int(12.0)))

        #post link entry
        self.entry14_img = PhotoImage(file = f"img_textBox14.png")
        self.entry14_bg = canvas.create_image(
            1196.0, 136.5,
            image = self.entry14_img)

        self.entry14 = Entry(
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0)

        self.entry14.place(
            x = 1105.0, y = 128,
            width = 182.0,
            height = 19)
        #checkbox for likers
        self.checkbox3 = Checkbutton(
            text = "likers", 
            bg = '#CACACA',
            onvalue = 1, 
            offvalue = 0, 
            height=1, 
            width = 20)
        self.checkbox3.place(
            x = 1120, y = 172)


        #checkbox for commenters
        self.checkbox4 = Checkbutton(
            text = "commenters_checkbox", 
            bg = '#CACACA',
            onvalue = 1, 
            offvalue = 0, 
            height=1, 
            width = 20)
        self.checkbox4.place(
            x = 1119, y = 193)


        #entry for path to save likers and commenters
        self.entry3_img = PhotoImage(file = f"img_textBox3.png")
        self.entry3_bg = self.canvas.create_image(
            1225.0, 234.5,
            image = self.entry3_img)

        self.entry3 = Entry(
            bd = 0,
            bg = "#ffffff",
            textvariable = path_to_save_likers_commenters_variable,
            highlightthickness = 0)

        self.entry3.place(
            x = 1157.0, y = 222,
            width = 136.0,
            height = 27)

        #btn to get likers and commenters
        self.img1 = PhotoImage(file = f"img1.png")
        self.b1 = Button(
            image = self.img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = get_likers_commenters_thread,
            relief = "flat")

        self.b1.place(
            x = 1147, y = 275,
            width = 83,
            height = 26)


    def message_progess(self,i,total):
        self.canvas.create_text(
            348.5, 604.5,
            text = "Message Sent to:",
            fill = "#000000",
            font = ("None", int(11.0)))

        self.canvas.create_text(
            425.0, 605.5,
            text = i,
            fill = "#000000",
            font = ("None", int(11.0)))

        self.canvas.create_text(
            440.0, 605.5,
            text = "/",
            fill = "#000000",
            font = ("None", int(11.0)))

        self.canvas.create_text(
            455.0, 605.5,
            text = total,
            fill = "#000000",
            font = ("None", int(11.0)))

        window.resizable(False, False)

acc = accountPanel()

def login_thread():
    threading.Thread(target=login).start()

def get_list_thread():
    threading.Thread(target=get_list).start()

def get_usernames_thread():
    threading.Thread(target=get_usernames).start()

def send_thread():
    threading.Thread(target=send).start()

def unfollow_users_thread():
    threading.Thread(target=unfollow_users).start()

def unfollow_non_followers_thread():
    threading.Thread(target=unfollow_non_followers).start()

def get_non_followers_thread():
    threading.Thread(target=get_non_followers).start()

def get_likers_commenters_thread():
    threading.Thread(target=get_likers_commenters).start()

def get_list():
    pb = account_progess()
    pb.start()
    username = username_for_list_variable.get()
    followers_checkbox_value = followers_checkbox.get()
    following_checkbox_value = following_checkbox.get()
    file_path_to_save = path_for_users_save_variable.get()

    if file_path_to_save == '':
        file_path_followers = 'followers.xlsx'
        file_path_following = 'following.xlsx'
    else:
        if not os.path.exists(file_path_to_save):
            os.makedirs(file_path_to_save)
        file_path_followers = os.path.join(file_path_to_save,"followers.xlsx")
        file_path_following = os.path.join(file_path_to_save,"following.xlsx")

    if followers_checkbox_value == 1:
        followers_list = bot.get_user_followers(username)

        followers_workbook = xlsxwriter.Workbook(file_path_followers)
        followers_worksheet = followers_workbook.add_worksheet()

        row = 0
        for i in followers_list:
            followers_worksheet.write(row,0,i)
            row = row+1
        followers_workbook.close()

        notification.notify(title="Instagram Bot",message="Followers list downloaded!",timeout=20,app_icon='logo.ico')

    if following_checkbox_value == 1:
        following_list = bot.get_user_following(username)
        
        following_workbook = xlsxwriter.Workbook(file_path_following)
        following_worksheet = following_workbook.add_worksheet()
        
        row = 0
        for i in following_list:
            following_worksheet.write(row,0,i)
            row = row+1
        following_workbook.close()

    pb.stop()
    pb.unpack()
    notification.notify(title="Instagram Bot",message="Following list downloaded!",timeout=20,app_icon='logo.ico')

def get_usernames():
    pb = account_progess()
    pb.start()
    path = path_to_save_usernames_variable.get()
    user_ids = entry6.get('1.0',END)
    usernames_list = []

    if path == '':
        path = 'usernames.xlsx'
    else:
        if not os.path.exists(path):
            os.makedirs(path)
        file_path = os.path.join(path,"usernames.xlsx")

    for user_id in user_ids.strip('\n'):
        try:
            usernames_list.append(bot.get_username_from_user_id(user_id))
        except:
            pass

    usernames_workbook = xlsxwriter.Workbook(file_path)
    usernames_worksheet = followers_workbook.add_worksheet()

    row = 0
    for i in usernames_list:
        usernames_worksheet.write(row,0,i)
        row = row+1
    usernames_workbook.close()

    notification.notify(title='Instagram Bot',message='Usernames Downloaded Sucessfully!',app_icon=logo.ico,timeout=20)

def send():
    checkbox_value = dont_repeat_variable.get()
    message_delay = delay_time_variable.get()
    message = acc.entry11.get('1.0',END)
    usernames = acc.entry12.get('1.0',END)
    sent_users = {}
    usernamesList = []

    for username in usernames.split('\n'):
        usernamesList.append(username)
        try:
            usernamesList.remove('')
        except:
            pass 

    if len(message) > 1000:
        messagebox.showinfo("Sucess",'Length of message is {}, max limit is 1000 characters'.foramt(len(message)))

    else:
        if(checkbox_value == 1):
            if os.path.isfile('temp_msg.txt'):
                with open('temp_msg.txt','r') as f:
                    sent_users.extend(json.loads(f.read()))

                    for i in sent_users:
                        for j in usernamesList:
                            if i == j:
                                usernamesList.remove(i)

        for username in usernamesList:
            try:
                bot.send_message(message,username)
                send_users.append(username)
            except:
                pass 

        with open('temp_msg.txt','w') as f:
            f.write(json.dumps(send_users))
            
    print(checkbox_value,message,delay_time,usernames)

def unfollow_users():
    pb = account_progess()
    pb.start()
    users = entry13.get('1.0',END)
    user_id = []

    for user in users.strip('\n'):
        user_id.append(user)
        try:
            user_id.remove('')
        except:
            pass

    try:
        bot.unfollow_users(user_id)
    except:
        pass 

    pb.stop()
    pb.unpack()
    notification.notify(title="Instagram Bot",message="Unfollowed users!",app_icon=logo.ico,timeout=20)

def unfollow_non_followers():
    pb = account_progess()
    pb.start()
    try:
        bot.unfollow_non_followers()
    except:
        pass
    pb.stop()
    pb.unpack()
    notification.notify(title="Instagram Bot",message="Unfollowed Non-followers",app_icon=logo.ico,timeout=20)

def get_non_followers():
    pb = account_progess()
    pb.start()
    path = path_to_save_non_followers.get()
    non_followers = {}

    followers = bot.get_user_followers(bot.username)
    following = bot.get_user_following(bot.username)

    for i in following:
        for j in followers:
            if i != j:
                non_followers.append(i)

    if path == '':
        path = 'non-followers.xlsx'
    else:
        if not os.path.exists(path):
            os.makedirs(path)
        file_path = os.path.join(path,'non-followers.xlsx')

    non_followers_workbook = xlsxwriter.Workbook(file_path)
    non_followers_worksheet = non_followers_workbook.add_worksheet()

    row = 0
    for i in non_followers:
        non_followers_worksheet.write(row,0,i)
        row = row+1
    non_followers_workbook.close()

    pb.stop()
    pb.unpack()
    notification.notify(title="Instagram Bot",message="Non followers List downloaded!",app_icon=logo.ico,timeout=20)


def get_likers_commenters():
    pb = account_progess()
    pb.start()
    link = entry14.get()
    path   = entry3.get()
    likers_bool = likers_checkbox.get()
    commenters_bool = commenters_checkbox.get()

    if path == '':
        likers_path = 'likers.xlsx'
        commenters_path = 'commenters.xlsx'
    else:
        if not os.path.exists(path):
            os.makedirs(path)
        likers_path = os.path.join(path,'likers.xlsx')
        commenters_path = os.path.join(path,'commenters.xlsx')

        if link == '':
            notification.notify(title="Instagram Bot",message='Provide a link',app_icon=logo.ico,timeout=20)

        else:

            id = bot.get_media_id_from_link(link)

            if likers_bool == 1:
                likers = bot.get_media_likers(id)

                likers_workbook = xlsxwriter.Workbook(likers_path)
                likers_worksheet = likers_workbook.add_worksheet()

                row = 0
                for i in likers:
                    likers_worksheet.write(row,0,i)
                    row = row+1
                likers_workbook.close()

            if commenters_bool == 1:

                commenters = bot.get_media_commenters(id)

                commenters_workbook = xlsxwriter.Workbook(commenters_path)                
                commenters_worksheet = commenters_workbook.add_worksheet()

                row = 0
                for i in commenters:
                    commenters_worksheet.write(row,0,i)
                    row = row+1
                commenters_workbook.close()

    pb.stop()
    pb.unpack()

class login_progess:
    def __init__(self):
        self.progress = Progressbar(window,
            orient =  HORIZONTAL,
            length = 300,
            mode = 'indeterminate')
        self.progress.place(
             x = 900.5, y = 600.0
            )
    def start(self):
        self.progress.start()
    def stop(self):
        self.progress.stop()
    def unpack(self):
        self.progress.place_forget()

class account_progess:
    def __init__(self):
        self.progress = Progressbar(window,
            orient =  HORIZONTAL,
            length = 100,
            mode = 'indeterminate')
        self.progress.place(
             x = 348, y = 650.0
            )
    def start(self):
        self.progress.start()
    def stop(self):
        self.progress.stop()
    def unpack(self):
        self.progress.place_forget()

def unpack_login_panel():
    canvas.delete('all')
    entry0.place_forget()
    entry1.place_forget()
    b0.place_forget()

def login():
    pb = login_progess()
    pb.start()
    username = username_variable.get()
    password = password_variable.get()

    try:
        canvas.delete('usernameTag')
        canvas.delete('passwordTag')
        canvas.delete('invalidLoginTag')
    except:
        pass

    cookie_del = glob.glob("config/*cookie.json")
    try:
        os.remove(cookie_del[0])
    except Exception:
        pass

    if username == '':
        username_error()
        pb.stop()
        pb.unpack()
        
    elif password == '':
        password_error()
        pb.stop()
        pb.unpack()
        
    else:
        try:
            bot.login(username=username,password=password,is_threaded=True)
            pb.stop()
            pb.unpack()
            unpack_login_panel()
            acc.pack(username)
        except Exception as e:
            print(e)
            invalid_login()
            pb.stop()
            pb.unpack()



def username_error():
    canvas.create_text(
        1043.5, 538.0,
        text = "Username required*",
        fill = "#ff0101",
        tags = 'usernameTag',
        font = ("None", int(12.0)))

def password_error():
    canvas.create_text(
        1043.5, 538.0,
        text = "Password required*",
        fill = "#ff0000",
        tags = 'passwordTag',
        font = ("None", int(12.0)))

def invalid_login():
    canvas.create_text(
        1000.5, 538.0,
        text = "Invalid credentials or else check your internet connection",
        fill = "#ff0000",
        tags = 'invalidLoginTag',
        font = ("None", int(12.0)))

canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 700,
    width = 1366,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"main_background.png")
background = canvas.create_image(
    350.0, 350.0,
    image=background_img)

canvas.create_text(
    301.5, 99.5,
    text = "Instagram Bot",
    fill = "#ffffff",
    font = ("Roboto-Bold", int(25.0)))

canvas.create_text(
    800.5, 128.5,
    text = "Login",
    fill = "#000000",
    font = ("Roboto-Bold", int(25.0)))

canvas.create_text(
    796.5, 221.5,
    text = "Username",
    fill = "#000000",
    font = ("None", int(16.0)))

canvas.create_text(
    795.5, 340.5,
    text = "Password",
    fill = "#000000",
    font = ("None", int(16.0)))

entry0_img = PhotoImage(file = f"main_img_textBox0.png")
entry0_bg = canvas.create_image(
    1035.0, 271.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#ffffff",
    textvariable = username_variable,
    highlightthickness = 0)

entry0.place(
    x = 773.0, y = 251,
    width = 524.0,
    height = 37)

entry1_img = PhotoImage(file = f"main_img_textBox1.png")
entry1_bg = canvas.create_image(
    1035.0, 394.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#ffffff",
    textvariable =password_variable,
    highlightthickness = 0)

entry1.place(
    x = 773.0, y = 374,
    width = 524.0,
    height = 40)

img0 = PhotoImage(file = f"main_img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = login_thread,
    relief = "flat")

b0.place(
    x = 760, y = 453,
    width = 550,
    height = 43)

canvas.create_text(
    301.5, 321.5,
    text = "Make your life easier",
    fill = "#ffffff",
    font = ("None", int(16.0)))


window.mainloop()
